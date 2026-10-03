import Link from "next/link";
import { describeExamFormat, formatDuration } from "@/lib/content/exam-format";

interface CourseRowProps {
  slug: string;
  name: string;
  description: string;
  examFormat: unknown;
  enrolled: boolean;
}

// One course in the index: name and enrolled marker on the left, a two-line
// description and the exam format on the right. The whole row is the link.
export function CourseRow({ slug, name, description, examFormat, enrolled }: CourseRowProps) {
  const format = examFormat as Parameters<typeof describeExamFormat>[0];
  return (
    <li>
      <Link
        href={`/courses/${slug}`}
        className="group grid gap-x-8 gap-y-2 py-6 md:grid-cols-[minmax(0,1.1fr)_minmax(0,1fr)]"
      >
        <div>
          <h3 className="heading text-2xl underline-offset-4 decoration-2 group-hover:underline">{name}</h3>
          {enrolled ? <span className="mt-2 inline-block bg-mark px-1.5 text-xs font-semibold text-on-mark">Enrolled</span> : null}
        </div>
        <div>
          <p className="line-clamp-2 text-sm leading-relaxed text-muted-foreground">{description}</p>
          <p className="eyebrow mt-2">
            {describeExamFormat(format)} · {formatDuration(format.totalDurationMinutes)}
          </p>
        </div>
      </Link>
    </li>
  );
}
