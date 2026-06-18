import Link from "next/link";

export default function HomePage() {
  return (
    <main className="min-h-screen bg-gradient-to-br from-slate-900 via-indigo-900 to-slate-950 flex items-center justify-center px-6">

      <div className="max-w-6xl mx-auto text-center text-white">

        <h1 className="text-6xl md:text-7xl font-black mb-6">
          DataSentinel AI
        </h1>

        <p className="text-2xl md:text-3xl font-semibold text-indigo-200">
          Enterprise Transaction Validation Platform
        </p>

        <p className="mt-4 text-lg text-slate-300 max-w-3xl mx-auto">
          Validate, Cleanse, Audit and Process Transaction Data
          with automated quality checks, country-specific
          validation rules and enterprise-grade reporting.
        </p>

        <div className="mt-10">
          <Link
            href="/dashboard"
            className="bg-indigo-600 hover:bg-indigo-700 transition-all duration-300 px-8 py-4 rounded-xl text-lg font-semibold shadow-lg"
          >
            Open Dashboard
          </Link>
        </div>

        {/* Features */}

        <div className="grid md:grid-cols-4 gap-6 mt-16">

          <div className="bg-white/10 backdrop-blur-sm rounded-2xl p-6 border border-white/10">
            <div className="text-4xl mb-3"></div>

            <h3 className="font-bold text-lg mb-2">
              Phone Validation
            </h3>

            <p className="text-slate-300 text-sm">
              Country-specific phone number validation
              using configurable international rules.
            </p>
          </div>

          <div className="bg-white/10 backdrop-blur-sm rounded-2xl p-6 border border-white/10">
            <div className="text-4xl mb-3"></div>

            <h3 className="font-bold text-lg mb-2">
              Data Quality Checks
            </h3>

            <p className="text-slate-300 text-sm">
              Detect missing values, duplicates,
              invalid formats and integrity issues.
            </p>
          </div>

          <div className="bg-white/10 backdrop-blur-sm rounded-2xl p-6 border border-white/10">
            <div className="text-4xl mb-3"></div>

            <h3 className="font-bold text-lg mb-2">
              Audit Reporting
            </h3>

            <p className="text-slate-300 text-sm">
              Generate professional audit reports,
              error reports and validation summaries.
            </p>
          </div>

          <div className="bg-white/10 backdrop-blur-sm rounded-2xl p-6 border border-white/10">
            <div className="text-4xl mb-3"></div>

            <h3 className="font-bold text-lg mb-2">
              CSV Chunk Processing
            </h3>

            <p className="text-slate-300 text-sm">
              Automatically split large datasets into
              manageable chunks for efficient processing.
            </p>
          </div>

        </div>

        {/* Supported Formats */}

        <div className="mt-12 text-slate-400 text-sm">
          Supports CSV, XLSX and International Transaction Datasets
        </div>

      </div>

    </main>
  );
}