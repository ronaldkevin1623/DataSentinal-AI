import Link from "next/link";

export default function HomePage() {
  return (
    <main className="min-h-screen bg-gradient-to-br from-slate-900 via-indigo-900 to-slate-950 flex items-center justify-center">

      <div className="text-center text-white">

        <h1 className="text-6xl font-black">
          DataSentinel AI
        </h1>

        <p className="mt-6 text-xl text-slate-300 max-w-2xl">
          Enterprise Transaction Data Validation,
          Cleansing and Processing Platform
        </p>

        <div className="mt-10">

          <Link
            href="/dashboard"
            className="bg-indigo-600 hover:bg-indigo-700 px-8 py-4 rounded-xl text-lg font-semibold"
          >
            Open Dashboard
          </Link>

        </div>

      </div>

    </main>
  );
}