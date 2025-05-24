// import React, { useEffect, useState } from 'react';
// import { getEmployees } from '../services/api';

// const EmployeeList = () => {
//     const [employees, setEmployees] = useState([]);

//     // useEffect(() => {
//     //     getEmployees().then(data => setEmployees(data));
//     // }, []);

//     useEffect(() => {
//     getEmployees().then(data => {
//         console.log("Fetched Employees:", data); // Debugging
//         setEmployees(data);
//     }).catch(error => {
//         console.error("Error fetching employees:", error);
//     });
// }, []);


//     return (
//         <div>
//             <h2>Employee List</h2>
//             <ul>
//                 {employees.map(emp => (
//                     <li key={emp.id}>{emp.name} - {emp.position}</li>
//                 ))}
//             </ul>
//         </div>
//     );
// };

// export default EmployeeList;



// import React, { useEffect, useState } from "react";
// import { getEmployees, deleteEmployee } from "../services/api";
// import EmployeeForm from "./EmployeeForm";

// const EmployeeList = () => {
//     const [employees, setEmployees] = useState([]);

//     useEffect(() => {
//         fetchEmployees();
//     }, []);

//     const fetchEmployees = () => {
//         getEmployees().then(data => setEmployees(data));
//     };

//     const handleDelete = async (id) => {
//         await deleteEmployee(id);
//         fetchEmployees();  // Refresh list after deletion
//     };

//     return (
//         <div>
//             <h2>Employee List</h2>
//             <EmployeeForm onEmployeeAdded={fetchEmployees} />
//             {employees.length === 0 ? (
//                 <p>No employees found.</p>
//             ) : (
//                 <ul>
//                     {employees.map(emp => (
//                         <li key={emp.id}>
//                             {emp.name} - {emp.position}
//                             <button onClick={() => handleDelete(emp.id)}>Delete</button>
//                         </li>
//                     ))}
//                 </ul>
//             )}
//         </div>
//     );
// };

// export default EmployeeList;



import React, { useEffect, useState } from "react";
import { getEmployees, deleteEmployee } from "../services/api";

const EmployeeList = () => {
    const [employees, setEmployees] = useState([]);

    useEffect(() => {
        getEmployees().then(setEmployees);
    }, []);

    const handleDelete = async (id) => {
        await deleteEmployee(id);
        setEmployees(employees.filter(emp => emp.id !== id)); // Update state
    };

    return (
        <div className="container mt-4">
            <h2 className="text-center mb-4">Employee List</h2>
            <table className="table table-bordered table-hover">
                <thead className="table-dark">
                    <tr>
                        <th>ID</th>
                        <th>Name</th>
                        <th>Position</th>
                        <th>Department</th>
                        <th>Contact</th>
                        <th>Action</th>
                    </tr>
                </thead>
                <tbody>
                    {employees.map(emp => (
                        <tr key={emp.id}>
                            <td>{emp.id}</td>
                            <td>{emp.name}</td>
                            <td>{emp.position}</td>
                            <td>{emp.department}</td>
                            <td>{emp.contact}</td>
                            <td>
                                <button className="btn btn-danger btn-sm" onClick={() => handleDelete(emp.id)}>Delete</button>
                            </td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default EmployeeList;

