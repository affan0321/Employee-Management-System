import React from "react";
import { Line } from "react-chartjs-2";
import { Chart as ChartJS } from "chart.js/auto";

const MultiAxisChart = () => {
  const data = {
    labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul"], // ✅ X-axis labels
    datasets: [
      {
        label: "Dataset 1",
        data: [30, 50, 20, 60, 40, 80, 55], // ✅ Sample data
        borderColor: "#FF6384",
        backgroundColor: "rgba(255,99,132,0.5)",
        yAxisID: "y", // ✅ Assign dataset to first Y-axis
      },
      {
        label: "Dataset 2",
        data: [20, -40, 30, -60, 50, -80, 40], // ✅ Sample data
        borderColor: "#36A2EB",
        backgroundColor: "rgba(54,162,235,0.5)",
        yAxisID: "y1", // ✅ Assign dataset to second Y-axis
      },
    ],
  };

  const options = {
    responsive: true,
    scales: {
      y: {
        type: "linear",
        position: "left",
        min: -100,
        max: 100,
      },
      y1: {
        type: "linear",
        position: "right",
        min: -100,
        max: 100,
      },
    },
  };

  return (
    <div style={{ width: "600px", margin: "20px auto" }}>
      <h3>Multi-Axis Line Chart</h3>
      <Line data={data} options={options} />
    </div>
  );
};

export default MultiAxisChart;
