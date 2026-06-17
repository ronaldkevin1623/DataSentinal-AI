import Link from "next/link";

export default function Navbar() {
  return (
    <nav className="bg-white border-b border-slate-200">
      <div className="max-w-7xl mx-auto px-6 py-4 flex items-center justify-between">
        <h1 className="text-2xl font-bold text-slate-900">
          DataSentinel AI
        </h1>

        <div className="flex gap-8 text-base font-medium">
          <Link
            href="/"
            className="text-slate-700 hover:text-indigo-600"
          >
            Home
          </Link>

          <Link
            href="/dashboard"
            className="text-slate-700 hover:text-indigo-600"
          >
            Dashboard
          </Link>
        </div>
      </div>
    </nav>
  );
}