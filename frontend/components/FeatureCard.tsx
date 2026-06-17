interface FeatureCardProps {
  title: string;
  description: string;
}

export default function FeatureCard({
  title,
  description,
}: FeatureCardProps) {
  return (
    <div className="bg-white p-8 rounded-3xl border border-slate-200 shadow-lg hover:shadow-2xl hover:-translate-y-2 transition-all duration-300">
      <h3 className="text-xl font-bold text-slate-900">
        {title}
      </h3>

      <p className="mt-4 text-slate-600 text-base">
        {description}
      </p>
    </div>
  );
}