interface Props {
  duplicates: number;
  missingValues: number;
  invalidEmails: number;
  invalidPhones: number;
}

export default function RecommendationPanel({
  duplicates,
  missingValues,
  invalidEmails,
  invalidPhones,
}: Props) {
  const recommendations = [];

  if (duplicates > 0)
    recommendations.push(
      `Remove ${duplicates} duplicate records`
    );

  if (missingValues > 0)
    recommendations.push(
      `Fill ${missingValues} missing values`
    );

  if (invalidEmails > 0)
    recommendations.push(
      `Correct ${invalidEmails} invalid email addresses`
    );

  if (invalidPhones > 0)
    recommendations.push(
      `Correct ${invalidPhones} invalid phone numbers`
    );

  return (
    <div className="bg-white rounded-2xl shadow-md p-6 mb-8">
      <h2 className="text-xl font-bold mb-4">
        AI Recommendations
      </h2>

      <ul className="space-y-3">
        {recommendations.map((item, index) => (
          <li
            key={index}
            className="text-slate-700"
          >
            ✓ {item}
          </li>
        ))}
      </ul>
    </div>
  );
}