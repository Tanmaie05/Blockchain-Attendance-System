**Ledger-based Attendance Viewer**

A decentralized web application that securely records and manages student attendance using blockchain technology. This system ensures immutability, transparency, and tamper-proof record keeping, solving limitations of traditional attendance systems.

🚀**Project Overview**

This project implements a **blockchain-powered attendance system** where attendance records are stored on a smart contract instead of a centralized database. Once recorded, data cannot be modified, ensuring trust and integrity.
The system provides:
* Faculty login for secure access
* Real-time attendance recording
* Student dashboard with attendance insights
* Automated attendance percentage calculation

🛠️ Tech Stack

*Blockchain*:
Ethereum (Hardhat Local Network),
Solidity (Smart Contracts),
Hardhat (Development & Deployment)

*Backend*:
Python,
Web3.py (Blockchain interaction)

*Frontend*:
Streamlit (Web UI)

*Data Handling*:
Pandas,
CSV (Student data)

⚙️**Features**
* Secure Faculty Login
* Immutable Attendance Records (Blockchain)
* Student Dashboard
* Attendance Percentage Calculation
* Auto Date Detection
* Dropdown Student Selection
* Real-time Data Fetching

📂**Project Structure**

blockchain-attendance-system/

    app.py: Streamlit application

    students.csv: Student list
    
    abi.json: Smart contract ABI

    contracts/: Solidity contract

    scripts/: Deployment scripts

    requirements.txt: Python dependencies

▶️**How to Run Locally**

1.Open Project Folder
cd C:\Users\tanma\OneDrive\Desktop\BLockchain-Project

2.Start Hardhat Blockchain
npx hardhat node
⚠️Keep this terminal running. Do not close it.

3.Open a New Terminal
cd C:\Users\tanma\OneDrive\Desktop\BLockchain-Project

4.Compile Smart Contract
npx hardhat compile

5.Deploy Smart Contract
npx hardhat run scripts/deploy.js --network localhost
After deployment, you will see:
Contract deployed to: 0xABC123...
Copy this contract address and update it in app.py:

6.Install Dependencies
pip install streamlit web3 pandas

7.Run the Application
streamlit run app.py

8.Open in Browser
http://localhost:8501

🌐**Deployment**

The application can be deployed using:
* Streamlit Cloud (UI)
* Ethereum Testnet (Sepolia)
> Note: Local blockchain (Hardhat) is used for development and demonstration.
