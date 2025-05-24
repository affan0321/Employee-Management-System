import React, { useEffect, useState } from "react";
import { getEmployees, markAttendance } from "../services/api";

const MarkAttendance = ({ onAttendanceMarked }) => {
    const [employees, setEmployees] = useState([]);

    useEffect(() => {
        getEmployees().then(setEmployees);
    }, []);

    const handleAttendance = async (id) => {
        await markAttendance(id);
        console.log("Attendance marked for employee:", id);
        if (onAttendanceMarked) {
        onAttendanceMarked();  // Call refresh function if available
    }
    };

    return (
        <div>
            <h2>Mark Attendance</h2>
            {employees.length === 0 ? <p>No employees found.</p> : (
                <ul>
                    {employees.map(emp => (
                        <li key={emp.id}>
                            {emp.name} - {emp.position}
                            <button onClick={() => handleAttendance(emp.id)}>Mark Present</button>
                        </li>
                    ))}
                </ul>
            )}
        </div>
    );
};

export default MarkAttendance;
