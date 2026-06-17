interface StatsCardProps {
  title: string;
  value: string;
}

export default function StatsCard({
  title,
  value,
}: StatsCardProps) {
  return (
    <div className="bg-white p-6 rounded-2xl border shadow-md">
      <p className="text-slate-600 font-medium">
        {title}
      </p>

      <h2 className="text-4xl font-bold text-slate-900 mt-2">
        {value}
      </h2>
    </div>
  );
}