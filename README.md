**Ledger-based Attendance Viewer**:

A decentralized web application that securely records and manages student attendance using blockchain technology. This system ensures immutability, transparency, and tamper-proof record keeping, solving limitations of traditional attendance systems.

🚀 Project Overview
This project implements a **blockchain-powered attendance system** where attendance records are stored on a smart contract instead of a centralized database. Once recorded, data cannot be modified, ensuring trust and integrity.
The system provides:
* Faculty login for secure access
* Real-time attendance recording
* Student dashboard with attendance insights
* Automated attendance percentage calculation

🛠️ Tech Stack
🔗 Blockchain
* Ethereum (Hardhat Local Network)
* Solidity (Smart Contracts)
* Hardhat (Development & Deployment)

💻 Backend
* Python
* Web3.py (Blockchain interaction)

🌐 Frontend
* Streamlit (Web UI)

🗄️ Data Handling
* Pandas
* CSV (Student data)

⚙️ Features
* 🔐 **Secure Faculty Login**
* 🧾 **Immutable Attendance Records (Blockchain)**
* 👨‍🎓 **Student Dashboard**
* 📊 **Attendance Percentage Calculation**
* 📅 **Auto Date Detection**
* 📋 Dropdown Student Selection
* ⚡ Real-time Data Fetching

📂 Project Structure
blockchain-attendance-system/
app.py: Streamlit application
students.csv: Student list
abi.json: Smart contract ABI
contracts/: Solidity contract
scripts/: Deployment scripts
requirements.txt: Python dependencies

▶️ How to Run Locally
1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/blockchain-attendance-system.git
cd blockchain-attendance-system
```

2. Install dependencies
```bash
pip install -r requirements.txt
npm install
```

3. Start blockchain
```bash
npx hardhat node
```

4. Deploy smart contract
```bash
npx hardhat run scripts/deploy.js --network localhost
```

5. Update contract address in `app.py`

6. Run the application
```bash
streamlit run app.py
```

🌐 Deployment
The application can be deployed using:

* Streamlit Cloud (UI)
* Ethereum Testnet (Sepolia)
> Note: Local blockchain (Hardhat) is used for development and demonstration.
