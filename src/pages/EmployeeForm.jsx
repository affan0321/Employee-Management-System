import React, { useState } from "react";
import { addEmployee } from "../services/api";

const EmployeeForm = ({ onEmployeeAdded }) => {
    const [employee, setEmployee] = useState({
        name: "",
        position: "",
        department: "",
        contact: ""
    });

    const handleChange = (e) => {
        setEmployee({ ...employee, [e.target.name]: e.target.value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        await addEmployee(employee);
        setEmployee({ name: "", position: "", department: "", contact: "" });
        onEmployeeAdded();  // Refresh employee list after adding
    };

    return (
        <form onSubmit={handleSubmit}>
            <input type="text" name="name" placeholder="Name" value={employee.name} onChange={handleChange} required />
            <input type="text" name="position" placeholder="Position" value={employee.position} onChange={handleChange} required />
            <input type="text" name="department" placeholder="Department" value={employee.department} onChange={handleChange} required />
            <input type="text" name="contact" placeholder="Contact" value={employee.contact} onChange={handleChange} required />
            <button type="submit">Add Employee</button>
        </form>
    );
};

export default EmployeeForm;
