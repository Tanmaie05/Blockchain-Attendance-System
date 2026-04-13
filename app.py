import streamlit as st
from web3 import Web3
import json
import pandas as pd
import datetime

# ---------------- CONNECT BLOCKCHAIN ----------------
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

if not w3.is_connected():
    st.error("❌ Blockchain not connected")
    st.stop()

# ---------------- LOAD CONTRACT ----------------
with open("abi.json") as f:
    abi = json.load(f)

contract_address = Web3.to_checksum_address("0xDc64a140Aa3E981100a9becA4E685f962f0cF6C9")
contract = w3.eth.contract(address=contract_address, abi=abi)

account = w3.eth.accounts[0]

# ---------------- LOAD STUDENTS ----------------
try:
    df = pd.read_csv("students.csv")
    students = df["name"].dropna().unique().tolist()
except:
    students = ["Alice", "Bob", "Charlie"]  # fallback

# ---------------- LOGIN SYSTEM ----------------
FACULTY_USERNAME = "admin"
FACULTY_PASSWORD = "1234"

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# ---------------- LOGIN PAGE ----------------
if not st.session_state.logged_in:
    st.title("🔐 Faculty Login")

    username = st.text_input("Username", key="login_username")
    password = st.text_input("Password", type="password", key="login_password")

    if st.button("Login", key="login_button"):
        if username == FACULTY_USERNAME and password == FACULTY_PASSWORD:
            st.session_state.logged_in = True
            st.success("✅ Login successful")
            st.rerun()
        else:
            st.error("❌ Invalid credentials")

# ---------------- MAIN APP ----------------
else:
    st.title("📌 Ledger-based Attendance Viewer")

    if st.button("Logout", key="logout_button"):
        st.session_state.logged_in = False
        st.rerun()

    menu = st.sidebar.selectbox(
        "Menu",
        ["Mark Attendance", "View Attendance", "Student Dashboard"],
        key="menu_select"
    )

    # ---------------- MARK ATTENDANCE ----------------
    if menu == "Mark Attendance":
        st.subheader("Mark Attendance")

        with st.form("attendance_form", clear_on_submit=True):

            # ✅ Dropdown instead of typing
            student_name = st.selectbox("Select Student", students)

            # ✅ Auto date
            date = datetime.date.today().strftime("%Y-%m-%d")
            st.write(f"📅 Date: {date}")

            status_input = st.selectbox("Status", ["Present", "Absent"])

            submitted = st.form_submit_button("Submit Attendance")

            if submitted:
                if student_name:
                    status = True if status_input == "Present" else False
                    try:
                        tx_hash = contract.functions.markAttendance(
                            student_name, date, status
                        ).transact({'from': account})

                        w3.eth.wait_for_transaction_receipt(tx_hash)
                        st.success("✅ Attendance stored on blockchain!")

                    except Exception as e:
                        st.error(f"❌ Error: {str(e)}")
                else:
                    st.warning("⚠️ Please select a student")

    # ---------------- VIEW ATTENDANCE + % ----------------
    elif menu == "View Attendance":
        st.subheader("📋 Attendance Records (Real-Time)")

        try:
            count = contract.functions.getAttendanceCount().call()

            if count == 0:
                st.info("No records yet")
            else:
                all_records = []

                for i in range(count):
                    record = contract.functions.getAttendance(i).call()
                    student_name, date, status_bool = record

                    all_records.append((student_name, date, status_bool))

                    status = "Present" if status_bool else "Absent"
                    st.write(f"👤 {student_name} | 📅 {date} | {status}")

                # -------- ATTENDANCE PERCENTAGE --------
                st.subheader("📊 Calculate Attendance Percentage")

                # ✅ Dropdown instead of typing
                student_query = st.selectbox("Select Student", students, key="percent_student")

                if st.button("Calculate Percentage"):

                    total = 0
                    present = 0

                    for rec in all_records:
                        if rec[0].lower() == student_query.lower():
                            total += 1
                            if rec[2]:
                                present += 1

                    if total > 0:
                        percentage = (present / total) * 100
                        st.success(f"📊 Attendance: {percentage:.2f}%")
                        st.info(f"Present: {present} / Total: {total}")
                    else:
                        st.warning("No records found for this student")

        except Exception as e:
            st.error(f"❌ Error: {str(e)}")

    # ---------------- STUDENT DASHBOARD ----------------
    elif menu == "Student Dashboard":
        st.subheader("🎓 Student Dashboard")

        # ✅ Dropdown instead of typing
        student_name = st.selectbox("Select Your Name", students, key="dashboard_student")

        if st.button("View Dashboard"):

            try:
                count = contract.functions.getAttendanceCount().call()

                total = 0
                present = 0
                records_found = []

                for i in range(count):
                    record = contract.functions.getAttendance(i).call()
                    name, date, status = record

                    if name.lower() == student_name.lower():
                        total += 1
                        if status:
                            present += 1

                        records_found.append((date, status))

                if total == 0:
                    st.warning("No records found for this student")
                else:
                    percentage = (present / total) * 100

                    st.success(f"📊 Attendance: {percentage:.2f}%")
                    st.info(f"✅ Present: {present} | 📚 Total Classes: {total}")

                    st.subheader("📅 Attendance History")

                    for rec in records_found:
                        status_text = "Present" if rec[1] else "Absent"
                        st.write(f"📅 {rec[0]} → {status_text}")

            except Exception as e:
                st.error(f"❌ Error: {str(e)}")