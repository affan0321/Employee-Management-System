// import axios from 'axios';

// const API_BASE_URL = "http://127.0.0.1:8000/api";

// export const getEmployees = async () => {
//     const response = await axios.get(`${API_BASE_URL}/employees/`);
//     return response.data;
// };

// export const addEmployee = async (employeeData) => {
//     const response = await axios.post(`${API_BASE_URL}/employees/`, employeeData);
//     return response.data;
// };


import axios from 'axios';

const API_BASE_URL = "http://127.0.0.1:8000/api";

// Fetch all employees
export const getEmployees = async () => {
    const response = await axios.get(`${API_BASE_URL}/employees/`);
    return response.data;
};

// Add a new employee
export const addEmployee = async (employeeData) => {
    const response = await axios.post(`${API_BASE_URL}/employees/`, employeeData);
    return response.data;
};

// Delete an employee
export const deleteEmployee = async (employeeId) => {
    await axios.delete(`${API_BASE_URL}/employees/${employeeId}/`);
};

export const getAttendance = async (date = null) => {
    const url = date ? `${API_BASE_URL}/attendance/?date=${date}` : `${API_BASE_URL}/attendance/`;
    const response = await axios.get(url);
    return response.data;
};

// Mark attendance for an employee
// export const markAttendance = async (employeeId) => {
//     const response = await axios.post(`${API_BASE_URL}/attendance/`, { employee: employeeId });
//     return response.data;
// };


export const markAttendance = async (employeeId) => {
    try {
        const response = await axios.post(`${API_BASE_URL}/attendance/`, { employee: employeeId });
        console.log("Attendance API Response:", response.data);
        return response.data;
    } catch (error) {
        console.error("Error marking attendance:", error.response.data);
        throw error;
    }
};

export const getEmployeePerformance = async () => {
    const response = await axios.get(`${API_BASE_URL}/performance/`);
    return response.data;
};

