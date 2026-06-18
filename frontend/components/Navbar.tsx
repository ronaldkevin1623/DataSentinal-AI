import Link from "next/link";

export default function Navbar() {
  return (
    <nav className="bg-white border-b border-slate-200">
      <div className="w-full px-10 py-4 flex items-center justify-between">
        <div>
  <h1 className="text-3xl font-black text-slate-900">
    DataSentinel AI
  </h1>

  <p className="text-sm text-slate-500">
    Enterprise Data Validation Platform
  </p>
</div>

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