import React, { useEffect, useState } from "react";
import { getEmployeePerformance } from "../services/api";

const PerformanceDashboard = () => {
    const [performance, setPerformance] = useState([]);

    useEffect(() => {
        getEmployeePerformance().then(setPerformance);
    }, []);

    return (
        <div className="container mt-4">
            <h2 className="text-center mb-4">Employee Performance Dashboard</h2>
            <table className="table table-striped table-bordered">
                <thead className="table-dark">
                    <tr>
                        <th>Employee Name</th>
                        <th>Tasks Completed</th>
                        <th>Productivity Score</th>
                    </tr>
                </thead>
                <tbody>
                    {performance.length === 0 ? (
                        <tr>
                            <td colSpan="3" className="text-center">No performance data available.</td>
                        </tr>
                    ) : (
                        performance.map(record => (
                            <tr key={record.id}>
                                <td>{record.employee.name}</td>
                                <td>{record.tasks_completed}</td>
                                <td>{record.productivity_score}</td>
                            </tr>
                        ))
                    )}
                </tbody>
            </table>
        </div>
    );
};

export default PerformanceDashboard;
