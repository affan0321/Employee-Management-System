import React, { useEffect, useState } from "react";
import { Bar, Line, Pie } from "react-chartjs-2";
import { Chart as ChartJS } from "chart.js/auto";

const AnalyticsDashboard = () => {
  const [hiringData, setHiringData] = useState([]);
  const [attendanceData, setAttendanceData] = useState([]);

  useEffect(() => {
    // ✅ Fetch hiring trends
    fetch("http://127.0.0.1:8000/api/hiring-trends/")
      .then((res) => res.json())
      .then((data) => setHiringData(data));

    // ✅ Fetch attendance reports
    fetch("http://127.0.0.1:8000/api/attendance-reports/")
      .then((res) => res.json())
      .then((data) => setAttendanceData(data));
  }, []);

  // ✅ Bar Chart: Hiring Trends
  const hiringChartData = {
    labels: hiringData.map((item) => item.month),
    datasets: [
      {
        label: "New Employees Hired",
        data: hiringData.map((item) => item.count),
        backgroundColor: "#36A2EB",
      },
    ],
  };

  // ✅ Line Chart: Attendance Reports
  const attendanceChartData = {
    labels: attendanceData.map((record) => record.date),
    datasets: [
      {
        label: "Attendance Count",
        data: attendanceData.map((record) => record.attendance),
        borderColor: "#FF6384",
        fill: true,
      },
    ],
  };

  return (
    <div>
      <h2>📊 Employee Analytics Dashboard</h2>

      {/* <div style={{ width: "600px", margin: "20px auto" }}>
        <h3>Hiring Trends</h3>
        <Bar data={hiringChartData} />
      </div> */}

      <div style={{ width: "600px", margin: "20px auto" }}>
        <h3>Attendance Reports</h3>
        <Line data={attendanceChartData} />
      </div>
    </div>
  );
};

export default AnalyticsDashboard;
