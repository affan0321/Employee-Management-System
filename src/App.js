// import React from "react";
// import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
// import EmployeeList from "./pages/EmployeeList";

// const App = () => {
//     return (
//         <Router>
//             <Routes>
//                 <Route path="/" element={<EmployeeList />} />
//             </Routes>
//         </Router>
//     );
// };

// export default App;


// import React from "react";
// import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
// import EmployeeList from "./pages/EmployeeList";

// const App = () => {
//     return (
//         <Router>
//             <Routes>
//                 <Route path="/" element={<EmployeeList />} />
//             </Routes>
//         </Router>
//     );
// };

// export default App;


// import React, { useState } from "react";
// import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
// import EmployeeList from "./pages/EmployeeList";
// import MarkAttendance from "./pages/MarkAttendance";
// import AttendanceRecords from "./pages/AttendanceRecords";

// const App = () => {
//     const [attendanceUpdated, setAttendanceUpdated] = useState(false);

//     const refreshAttendance = () => {
//         console.log("Refreshing attendance records...");
//         setAttendanceUpdated(!attendanceUpdated); // Toggle state to trigger refresh
//     };

//     return (
//         <Router>
//             <nav>
//                 <a href="/">Employees</a>
//                 <a href="/mark-attendance">Mark Attendance</a>
//                 <a href="/attendance-records">Attendance Records</a>
//             </nav>
//             <Routes>
//                 <Route path="/" element={<EmployeeList />} />
//                 <Route path="/mark-attendance" element={<MarkAttendance onAttendanceMarked={refreshAttendance} />} />
//                 <Route path="/attendance-records" element={<AttendanceRecords key={attendanceUpdated} />} />
//             </Routes>
//         </Router>
//     );
// };

// export default App;

import React from "react";
import { BrowserRouter as Router, Route, Routes, Link } from "react-router-dom";
import EmployeeList from "./pages/EmployeeList";
import MarkAttendance from "./pages/MarkAttendance";
import AttendanceRecords from "./pages/AttendanceRecords";
import PerformanceDashboard from "./pages/PerformanceDashboard";
import EmployeeDashboard from "./pages/EmployeeDashboard";
import AnalyticsDashboard from "./pages/AnalyticsDashboard";

const App = () => {
    return (
        <Router>
            <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
                <div className="container">
                    <Link className="navbar-brand" to="/">Employee Manager</Link>
                    <div className="navbar-nav">
                        <Link className="nav-link" to="/">Employees</Link>
                        <Link className="nav-link" to="/mark-attendance">Mark Attendance</Link>
                        <Link className="nav-link" to="/attendance-records">Attendance Records</Link>
                        <Link className="nav-link" to="/performance-dashboard">Performance Dashboard</Link> 
                        <Link className="nav-link" to="/employee-dashboard">Employee Dashboard</Link>
                        <Link className="nav-link" to="/analytic-dashboard">Analytic Dashboard</Link>  
                    </div>
                </div>
            </nav>

            <div className="container mt-4">
                <Routes>
                    <Route path="/" element={<EmployeeList />} />
                    <Route path="/mark-attendance" element={<MarkAttendance />} />
                    <Route path="/attendance-records" element={<AttendanceRecords />} />
                    <Route path="/performance-dashboard" element={<PerformanceDashboard />} />
                    <Route path="/employee-dashboard" element={<EmployeeDashboard />} />
                    <Route path="/analytic-dashboard" element={<AnalyticsDashboard />} />
                </Routes>
            </div>
        </Router>
    );
};

export default App;

