"use client";

import { useState } from "react";
import Navbar from "@/components/Navbar";
import AnalyticsChart from "@/components/AnalyticsChart";
import DownloadSection from "@/components/DownloadSection";
import { DataGrid } from "@mui/x-data-grid";
import {
  Card,
  CardContent,
  Typography,
  LinearProgress,
  Chip,
  Alert,
  Button
} from "@mui/material";

import DownloadIcon from "@mui/icons-material/Download";
export default function DashboardPage() {
  const [file, setFile] = useState<File | null>(null);
  const [results, setResults] = useState<any>(null);
  const [loading, setLoading] = useState(false);

  async function uploadFile() {
    if (!file) {
      alert("Please select a CSV file.");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    setLoading(true);

    try {
      const response = await fetch(
        "http://127.0.0.1:8000/upload",
        {
          method: "POST",
          body: formData,
        }
      );

      const data = await response.json();

      setResults(data);
    } catch (error) {
      console.error(error);
      alert("Upload failed.");
    }

    setLoading(false);
  }

  return (
    <>
      <Navbar />

      <main className="min-h-screen bg-gradient-to-br from-slate-100 via-blue-50 to-indigo-100 px-6 py-10">

        <div className="w-full px-8">

          <h1 className="text-5xl font-black text-slate-900">
            Dataset Analysis Dashboard
          </h1>

          <p className="mt-3 text-lg text-slate-600">
            Upload transaction datasets and perform enterprise-grade
            validation, cleansing and AI-powered analysis.
          </p>

          {/* Upload Section */}

          <div className="bg-white rounded-3xl shadow-lg p-12 mt-10">

  <h2 className="text-3xl font-bold text-slate-900 text-center mb-8">
    Upload Transaction Dataset
  </h2>

  <div className="flex flex-col lg:flex-row items-center gap-6">

    <input
      type="file"
      accept=".csv,.xlsx,.xls"
      onChange={(e) =>
        setFile(
          e.target.files?.[0] || null
        )
      }
      className="flex-1 border-2 border-slate-300 rounded-xl p-5 text-lg"
    />

    <button
      onClick={uploadFile}
      className="
bg-indigo-600
hover:bg-indigo-700
transition
text-white
px-12
py-5
rounded-2xl
text-xl
font-bold
shadow-xl
whitespace-nowrap
"
    >
      {loading
        ? "Analyzing Dataset..."
        : "Analyze Dataset"}
    </button>

  </div>

</div>
          
          {results && (

            <div className="mt-10">

              {/* KPI Cards */}

              <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-4 gap-8">

                <div className="bg-white rounded-3xl shadow-lg p-8 min-h-[180px]">
                  <p className="text-slate-500">
                    Total Rows
                  </p>

                  <h3 className="text-6xl font-black text-slate-900 mt-2">
                    {results.total_rows}
                  </h3>
                </div>

                <Card elevation={4}>
  <CardContent>

    <Typography
      variant="body2"
      sx={{
  color: "#334155",
  fontWeight: 500
}}
    >
      Quality Score
    </Typography>

    <Typography
  variant="h3"
  sx={{
    fontWeight: "bold",
    color:
      results.quality_score >= 90
        ? "success.main"
        : results.quality_score >= 75
        ? "primary.main"
        : results.quality_score >= 50
        ? "warning.main"
        : "error.main"
  }}
>
  {results.quality_score}
</Typography>

    <LinearProgress
      variant="determinate"
      value={results.quality_score}
      sx={{
        mt: 2,
        height: 10,
        borderRadius: 5
      }}
    />

    <div className="mt-4">

      {results.quality_score >= 90 && (
        <Chip
          label="Excellent"
          color="success"
        />
      )}

      {results.quality_score >= 75 &&
        results.quality_score < 90 && (
        <Chip
          label="Good"
          color="primary"
        />
      )}

      {results.quality_score >= 50 &&
        results.quality_score < 75 && (
        <Chip
          label="Average"
          color="warning"
        />
      )}

      {results.quality_score < 50 && (
        <Chip
          label="Poor"
          color="error"
        />
      )}

    </div>

  </CardContent>
</Card>

                <div className="bg-white rounded-3xl shadow-lg p-8 min-h-[180px]">
                  <p className="text-slate-500">
                    Duplicate Rows
                  </p>

                  <h3 className="text-6xl font-black text-red-600 mt-2">
                    {results.duplicate_rows}
                  </h3>
                </div>

                <div className="bg-white rounded-3xl shadow-lg p-8 min-h-[180px]">
                  <p className="text-slate-500">
                    Missing Values
                  </p>

                  <h3 className="text-6xl font-black text-orange-500 mt-2">
                    {results.missing_values}
                  </h3>
                </div>

              </div>

              {/* Validation Summary */}

              {/* Validation Summary */}

<Card
  elevation={3}
  sx={{
    mt: 4,
    borderRadius: 4
  }}
>
  <CardContent>

    <Typography
      variant="h5"
      sx={{
        fontWeight: 700,
        mb: 3
      }}
    >
      Validation Summary
    </Typography>

    <div className="grid md:grid-cols-3 gap-6">

      <Card elevation={1}>
        <CardContent>

          <Typography
            variant="body2"
            sx={{
  color: "#334155",
  fontWeight: 500
}}
          >
            Invalid Emails
          </Typography>

          <Typography
            variant="h4"
            color="error"
            sx={{ fontWeight: 700 }}
          >
            {results.invalid_emails}
          </Typography>

        </CardContent>
      </Card>

      <Card elevation={1}>
        <CardContent>

          <Typography
            variant="body2"
            sx={{
  color: "#334155",
  fontWeight: 500
}}
          >
            Invalid Phones
          </Typography>

          <Typography
            variant="h4"
            color="error"
            sx={{ fontWeight: 700 }}
          >
            {results.invalid_phones}
          </Typography>

        </CardContent>
      </Card>

      <Card elevation={1}>
        <CardContent>

          <Typography
            variant="body2"
            sx={{
  color: "#334155",
  fontWeight: 500
}}
          >
            Future Dates
          </Typography>

          <Typography
            variant="h4"
            color="warning.main"
            sx={{ fontWeight: 700 }}
          >
            {results.future_dates}
          </Typography>

        </CardContent>
      </Card>

    </div>

  </CardContent>
</Card>

              {/* Transaction Validation */}

              {/* Transaction Validation */}

<Card
  elevation={3}
  sx={{
    mt: 4,
    borderRadius: 4
  }}
>
  <CardContent>

    <Typography
      variant="h5"
      sx={{
        fontWeight: 700,
        mb: 3
      }}
    >
      Transaction Validation
    </Typography>

    <div className="grid md:grid-cols-4 gap-6">

      <Card elevation={1}>
        <CardContent>
          <Typography
            variant="body2"
            sx={{
  color: "#334155",
  fontWeight: 500
}}
          >
            Invalid Order Dates
          </Typography>

          <Typography
            variant="h4"
            color="error"
            sx={{ fontWeight: 700 }}
          >
            {results.invalid_order_dates}
          </Typography>
        </CardContent>
      </Card>

      <Card elevation={1}>
        <CardContent>
          <Typography
            variant="body2"
            sx={{
  color: "#334155",
  fontWeight: 500
}}
          >
            Invalid Quantity
          </Typography>

          <Typography
            variant="h4"
            color="error"
            sx={{ fontWeight: 700 }}
          >
            {results.invalid_quantity}
          </Typography>
        </CardContent>
      </Card>

      <Card elevation={1}>
        <CardContent>
          <Typography
            variant="body2"
            sx={{
  color: "#334155",
  fontWeight: 500
}}
          >
            Invalid Price
          </Typography>

          <Typography
            variant="h4"
            color="error"
            sx={{ fontWeight: 700 }}
          >
            {results.invalid_price}
          </Typography>
        </CardContent>
      </Card>
      <Card elevation={1}>
  <CardContent>

    <Typography
      variant="body2"
      sx={{
        color: "#334155",
        fontWeight: 500
      }}
    >
      Invalid Date Formats
    </Typography>

    <Typography
      variant="h4"
      color="error"
      sx={{
        fontWeight: 700
      }}
    >
      {results.invalid_date_formats}
    </Typography>

  </CardContent>
</Card>

    </div>

  </CardContent>
</Card>

              {/* Payment Validation */}

              <div className="bg-white rounded-3xl shadow-md p-8 mt-8">

                <h2 className="text-3xl font-bold text-slate-900 mb-6">
                  Payment Validation
                </h2>

                <div className="border rounded-xl p-5">

                  <p className="text-slate-500">
                    Invalid Payment Modes
                  </p>

                  <h3 className="text-4xl font-bold text-red-500 mt-2">
                    {results.invalid_payment_modes}
                  </h3>

                </div>

              </div>

              {/* AI Insights */}

              <Card
  elevation={3}
  sx={{
    mt: 4,
    borderRadius: 4
  }}
>
  <CardContent>

    <Typography
      variant="h5"
      sx={{
        fontWeight: 700,
        mb: 3
      }}
    >
      AI Insights
    </Typography>

    <Alert severity="info">
      {results.ai_insight}
    </Alert>

  </CardContent>
</Card>
            {/* Dataset Profile */}

<div className="bg-white rounded-3xl shadow-md p-8 mt-8">

  <h2 className="text-3xl font-bold text-slate-900 mb-6">
    Dataset Profile
  </h2>

  <div className="grid md:grid-cols-4 gap-6">

    <div className="border rounded-xl p-5">
      <p className="text-slate-500">
        Total Columns
      </p>

      <h3 className="text-4xl font-bold text-indigo-600 mt-2">
        {results.total_columns}
      </h3>
    </div>

    <div className="border rounded-xl p-5">
      <p className="text-slate-500">
        Numeric Columns
      </p>

      <h3 className="text-4xl font-bold text-green-600 mt-2">
        {results.numeric_columns}
      </h3>
    </div>

    <div className="border rounded-xl p-5">
      <p className="text-slate-500">
        Categorical Columns
      </p>

      <h3 className="text-4xl font-bold text-purple-600 mt-2">
        {results.categorical_columns}
      </h3>
    </div>

    <div className="border rounded-xl p-5">
      <p className="text-slate-500">
        Memory Usage
      </p>

      <h3 className="text-4xl font-bold text-orange-500 mt-2">
        {results.memory_usage_mb} MB
      </h3>
    </div>

  </div>

</div>
{/* Analytics Dashboard */}

<div className="mt-8">

  {results?.total_rows > 0 && (
  <AnalyticsChart
    invalidEmails={results.invalid_emails}
    invalidPhones={results.invalid_phones}
    duplicates={results.duplicate_rows}
    missingValues={results.missing_values}
  />
)}

</div>

{/* Column Summary */}

<div className="bg-white rounded-3xl shadow-md p-8 mt-8">

  <h2 className="text-3xl font-bold text-slate-900 mb-6">
    Column Analysis
  </h2>

  <DataGrid
  autoHeight
  rows={
    results.column_summary?.map(
      (
        col: any,
        index: number
      ) => ({
        id: index,
        ...col,
      })
    )
  }
  columns={[
    {
      field: "column",
      headerName: "Column",
      flex: 1,
    },
    {
      field: "dtype",
      headerName: "Data Type",
      flex: 1,
    },
    {
      field: "missing_values",
      headerName: "Missing Values",
      flex: 1,
    },
    {
      field: "unique_values",
      headerName: "Unique Values",
      flex: 1,
    },
  ]}
/>

  </div>
              {/* Recommendations */}

              <div className="bg-white rounded-3xl shadow-md p-8 mt-8">

                <h2 className="text-3xl font-bold text-slate-900 mb-4">
                  Recommendations
                </h2>

                <ul className="space-y-3">

  {results.duplicate_rows > 0 && (
    <li>✓ Remove duplicate records</li>
  )}

  {results.invalid_emails > 0 && (
    <li>✓ Fix invalid email addresses</li>
  )}

  {results.invalid_phones > 0 && (
    <li>✓ Fix invalid phone numbers</li>
  )}

  {results.future_dates > 0 && (
    <li>✓ Remove future dates</li>
  )}

  {results.invalid_order_dates > 0 && (
    <li>✓ Validate order dates</li>
  )}

  {results.invalid_payment_modes > 0 && (
    <li>✓ Correct payment modes</li>
  )}

  {results.missing_values > 0 && (
    <li>✓ Fill missing values</li>
  )}

</ul>

              </div>

              {/* Downloads */}

              <DownloadSection
  cleanedFile={results.cleaned_file}
  errorReport={results.error_report}
/>

              {/* CSV Chunking */}

              {/* CSV Chunk Downloads */}

<div className="bg-white rounded-3xl shadow-md p-8 mt-8">

  <h2 className="text-3xl font-bold text-slate-900 mb-6">
    CSV Chunk Downloads
  </h2>

  <p className="mb-4 text-slate-600">
    Total Chunks Generated:
    <span className="ml-2 font-bold text-indigo-600">
      {results.chunks_created}
    </span>
  </p>

  <div className="flex flex-wrap gap-4">

    {Array.from(
      { length: results.chunks_created },
      (_, i) => i + 1
    ).map((chunk) => (

      <a
  key={chunk}
  href={`http://127.0.0.1:8000/download/chunk/${chunk}`}
  target="_blank"
  rel="noopener noreferrer"
>
  <Button
    variant="contained"
    startIcon={<DownloadIcon />}
  >
    Chunk {chunk}
  </Button>
</a>

    ))}

  </div>

</div>

                        </div>

          )}

          {/* Footer */}

          

        </div>

      </main>
      <footer className="mt-20 bg-white border-t shadow-inner">

  <div className="max-w-[1700px] mx-auto py-8 text-center">

    <h3 className="text-2xl font-bold text-slate-900">
      DataSentinel AI
    </h3>

    <p className="mt-2 text-slate-600">
      Enterprise Transaction Data Validation & Processing Platform
    </p>

    <p className="mt-2 text-slate-500">
      Validate • Cleanse • Audit • Process
    </p>

    <p className="mt-4 text-sm text-slate-400">
      © 2026 DataSentinel AI. All Rights Reserved.
    </p>

  </div>

</footer>
    </>
  );
}