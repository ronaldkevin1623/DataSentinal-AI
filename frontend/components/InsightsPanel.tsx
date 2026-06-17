export default function InsightsPanel() {
  return (
    <div className="bg-white p-6 rounded-2xl border shadow-sm">
      <h2 className="text-xl font-bold mb-4">
        AI Insights
      </h2>

      <ul className="space-y-3 text-gray-700">
        <li>• 12 invalid phone numbers detected</li>
        <li>• Singapore records show highest error rate</li>
        <li>• 5 duplicate transactions found</li>
        <li>• Data quality score exceeds 90%</li>
      </ul>
    </div>
  );
}