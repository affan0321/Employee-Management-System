import React, { useEffect, useState } from "react";
// import { getEmployees } from "../services/api";  // ✅ Import the API function
import { getEmployees } from "../services/api";
const EmployeeDashboard = () => {
    const [employees, setEmployees] = useState([]);

    useEffect(() => {
        getEmployees().then(data => {
            console.log("Employee Data:", data);
            setEmployees(data);
        });
    }, []);

    return (
        <div className="container mt-4">
            <h2 className="text-center mb-4">Employee Dashboard</h2>
            <table className="table table-striped table-bordered">
                <thead className="table-dark">
                    <tr>
                        <th>ID</th>
                        <th>Name</th>
                        <th>Position</th>
                    </tr>
                </thead>
                <tbody>
                    {employees.length === 0 ? (
                        <tr><td colSpan="3" className="text-center">No employees found.</td></tr>
                    ) : (
                        employees.map(employee => (
                            <tr key={employee.id}>
                                <td>{employee.id}</td>
                                <td>{employee.name}</td>
                                <td>{employee.position}</td>
                            </tr>
                        ))
                    )}
                </tbody>
            </table>
        </div>
    );
};

export default EmployeeDashboard;
