// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Attendance {

    struct Record {
        string studentName;
        string date;
        bool isPresent;
    }

    Record[] public records;

    address public teacher;

    constructor() {
        teacher = msg.sender;
    }

    modifier onlyTeacher() {
        require(msg.sender == teacher, "Only teacher allowed");
        _;
    }

    function markAttendance(
        string memory name,
        string memory date,
        bool status
    ) public onlyTeacher {
        records.push(Record(name, date, status));
    }

    function getRecords() public view returns (Record[] memory) {
        return records;
    }

    function getAttendanceCount() public view returns (uint) {
        return records.length;
    }

    function getAttendance(uint index)
        public
        view
        returns (string memory, string memory, bool)
    {
        Record memory r = records[index];
        return (r.studentName, r.date, r.isPresent);
    }
}