"use client";

import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
  CartesianGrid,
} from "recharts";

interface Props {
  invalidEmails: number;
  invalidPhones: number;
  duplicates: number;
  missingValues: number;
}

export default function AnalyticsChart({
  invalidEmails,
  invalidPhones,
  duplicates,
  missingValues,
}: Props) {
  const data = [
    {
      name: "Emails",
      value: invalidEmails,
    },
    {
      name: "Phones",
      value: invalidPhones,
    },
    {
      name: "Duplicates",
      value: duplicates,
    },
    {
      name: "Missing",
      value: missingValues,
    },
  ];

  return (
    <div className="bg-white rounded-2xl shadow-md p-6">
      <h2 className="text-xl font-bold mb-6">
        Data Quality Breakdown
      </h2>

      <div className="h-[350px] w-full">
        <ResponsiveContainer width="100%" height="100%">
          <BarChart data={data}>
            <CartesianGrid strokeDasharray="3 3" />

            <XAxis dataKey="name" />

            <YAxis />

            <Tooltip />

            <Bar
              dataKey="value"
              fill="#4f46e5"
              radius={[8, 8, 0, 0]}
            />
          </BarChart>
        </ResponsiveContainer>
      </div>
    </div>
  );
}