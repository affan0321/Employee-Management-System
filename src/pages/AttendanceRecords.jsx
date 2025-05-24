// import React, { useEffect, useState } from "react";
// import { getAttendance } from "../services/api";

// const AttendanceRecords = () => {
//     const [attendance, setAttendance] = useState([]);
//     const [date, setDate] = useState("");

//     const fetchAttendance = () => {
//         getAttendance(date).then(setAttendance);
//     };

//     useEffect(() => {
//         fetchAttendance();
//     }, [date]);

//     return (
//         <div>
//             <h2>Attendance Records</h2>
//             <input type="date" value={date} onChange={(e) => setDate(e.target.value)} />
//             <button onClick={fetchAttendance}>Filter by Date</button>

//             {attendance.length === 0 ? <p>No records found.</p> : (
//                 <ul>
//                     {attendance.map(record => (
//                         <li key={record.id}>{record.employee.name} - {record.date}</li>
//                     ))}
//                 </ul>
//             )}
//         </div>
//     );
// };

// const AttendanceRecords = () => {
//     const [attendance, setAttendance] = useState([]);
//     const [date, setDate] = useState("");

//     const fetchAttendance = async () => {
//         const records = await getAttendance(date);
//         console.log("Attendance Data:", records);  // Debugging
//         setAttendance(records);
//     };

//     useEffect(() => {
//         fetchAttendance();
//     }, [date]);

//     return (
//         <div>
//             <h2>Attendance Records</h2>
//             <input type="date" value={date} onChange={(e) => setDate(e.target.value)} />
//             <button onClick={fetchAttendance}>Filter by Date</button>

//             {attendance.length === 0 ? <p>No records found.</p> : (
//                 <ul>
//                     {attendance.map(record => (
//                         <li key={record.id}>
//                             {record.employee ? record.employee.name : "Unknown Employee"} - {record.date}
//                         </li>
//                     ))}
//                 </ul>
//             )}
//         </div>
//     );
// };


// export default AttendanceRecords;


import React, { useEffect, useState } from "react";
import { getAttendance } from "../services/api";

const AttendanceRecords = () => {
    const [attendance, setAttendance] = useState([]);
    const [date, setDate] = useState("");

    const fetchAttendance = () => {
        getAttendance(date).then(setAttendance);
    };

    useEffect(() => {
        fetchAttendance();
    }, [date]);

    return (
        <div className="container mt-4">
            <h2 className="text-center mb-4">Attendance Records</h2>
            <div className="mb-3">
                <input type="date" className="form-control" value={date} onChange={(e) => setDate(e.target.value)} />
                <button className="btn btn-primary mt-2" onClick={fetchAttendance}>Filter by Date</button>
            </div>
            <table className="table table-striped table-bordered">
                <thead className="table-primary">
                    <tr>
                        <th>Employee Name</th>
                        <th>Date</th>
                    </tr>
                </thead>
                <tbody>
                    {attendance.length === 0 ? (
                        <tr>
                            <td colSpan="2" className="text-center">No records found.</td>
                        </tr>
                    ) : (
                        attendance.map(record => (
                            <tr key={record.id}>
                                <td>{record.employee ? record.employee.name : "Unknown Employee"}</td>
                                <td>{record.date}</td>
                            </tr>
                        ))
                    )}
                </tbody>
            </table>
        </div>
    );
};

export default AttendanceRecords;
