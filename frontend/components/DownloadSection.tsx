interface Props {
  cleanedFile: string;
  errorReport: string;
}

export default function DownloadSection({
  cleanedFile,
  errorReport,
}: Props) {
  const API = "http://127.0.0.1:8000";

  return (
    <div className="bg-white rounded-2xl shadow-md p-6">
      <h2 className="text-xl font-bold mb-6">
        Generated Files
      </h2>

      <div className="flex gap-4 flex-wrap">

        <a
          href={`${API}/download/cleaned`}
          className="bg-green-600 text-white px-5 py-3 rounded-xl"
        >
          Download Clean CSV
        </a>

        <a
          href={`${API}/download/errors`}
          className="bg-red-600 text-white px-5 py-3 rounded-xl"
        >
          Download Error Report
        </a>

        <a
          href={`${API}/download/audit`}
          target="_blank"
          className="bg-blue-600 hover:bg-blue-700 text-white px-5 py-3 rounded-xl"
        >
          Download Audit Report
        </a>

      </div>
    </div>
  );
}