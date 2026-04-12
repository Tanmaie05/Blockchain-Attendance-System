import streamlit as st
from web3 import Web3
import json

# ---------------- CONNECT TO HARDHAT ----------------
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

if not w3.is_connected():
    st.error("❌ Hardhat node not connected. Start Hardhat first.")
    st.stop()

# ---------------- LOAD CONTRACT ----------------
with open("abi.json") as f:
    abi = json.load(f)

# Replace with the deployed contract address from Hardhat logs
contract_address = Web3.to_checksum_address("0xCf7Ed3AccA5a467e9e704C703E8D87F634fB0Fc9")
contract = w3.eth.contract(address=contract_address, abi=abi)

# ---------------- ACCOUNT ----------------
# Use the first account from Hardhat
account = w3.eth.accounts[0]

# ---------------- UI ----------------
st.title("📌 Blockchain-Based Attendance System")

menu = st.sidebar.selectbox("Menu", ["Mark Attendance", "View Attendance"])

# ---------------- MARK ATTENDANCE ----------------
if menu == "Mark Attendance":
    st.subheader("Mark Attendance")

    student_name = st.text_input("Enter Student Name").strip()
    date = st.text_input("Enter Date (DD-MM-YYYY)").strip()
    status_input = st.selectbox("Status", ["Present", "Absent"])

    if st.button("Submit Attendance"):
        if student_name and date:
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
            st.warning("Please fill all fields")

# ---------------- VIEW ATTENDANCE ----------------
elif menu == "View Attendance":
    st.subheader("📋 Attendance Records")

    try:
        count = contract.functions.getAttendanceCount().call()

        if count == 0:
            st.info("No attendance records found yet.")
        else:
            for i in range(count):
                record = contract.functions.getAttendance(i).call()

                student_name = record[0]
                date = record[1]
                status = "Present" if record[2] else "Absent"

                st.write(f"👤 {student_name} | 📅 {date} | {status}")

    except Exception as e:
        st.error(f"❌ Error loading data: {str(e)}")
