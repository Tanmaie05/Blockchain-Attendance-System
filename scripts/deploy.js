import { ethers } from "ethers";
import fs from "fs";

async function main() {
  // Connect to local Hardhat node
  const provider = new ethers.JsonRpcProvider("http://127.0.0.1:8545");

  // Use first account private key (from your node)
  const wallet = new ethers.Wallet(
    "0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80",
    provider
  );

  // Read compiled contract
  const artifact = JSON.parse(
    fs.readFileSync("./artifacts/contracts/Attendance.sol/Attendance.json")
  );

  const factory = new ethers.ContractFactory(
    artifact.abi,
    artifact.bytecode,
    wallet
  );

  const contract = await factory.deploy();

  await contract.waitForDeployment();

  console.log("Contract deployed to:", contract.target);
}

main();