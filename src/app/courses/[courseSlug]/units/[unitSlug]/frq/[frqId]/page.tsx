import Link from "next/link";
import { notFound } from "next/navigation";
import { requireUserId } from "@/lib/auth/session";
import { getDb } from "@/lib/db";
import { renderContentToHtml } from "@/lib/content/render";
import { FrqSelfGrade, type RubricLineView } from "@/components/study/frq-self-grade";
import { DiagramRenderer } from "@/components/diagrams/diagram-renderer";
import type { Diagram } from "@/lib/content/diagram-schema";
import { isPaperLinedCourse } from "@/lib/content/paper-lined";

export default async function FrqPracticePage({
  params,
}: {
  params: Promise<{ courseSlug: string; unitSlug: string; frqId: string }>;
}) {
  await requireUserId();
  const { courseSlug, unitSlug, frqId } = await params;

  const frq = await getDb().fRQPrompt.findUnique({ where: { id: frqId } });
  if (!frq) notFound();

  const [promptHtml, sampleResponseHtml] = await Promise.all([
    renderContentToHtml(frq.prompt, courseSlug),
    renderContentToHtml(frq.sampleResponse, courseSlug),
  ]);
  const rubric = frq.rubric as unknown as RubricLineView[];
  const diagram = (frq.diagram as Diagram | null) ?? null;
  const paperLined = isPaperLinedCourse(courseSlug);

  return (
    <div className="mx-auto w-full max-w-2xl px-6 py-10">
      <p className="mb-4 text-sm text-muted-foreground">
        <Link href={`/courses/${courseSlug}/units/${unitSlug}`} className="hover:text-foreground">
          Back to unit
        </Link>
      </p>

      <div className={paperLined ? "paper-lined mb-6 rounded-lg border border-border p-6" : "mb-6 rounded-lg border border-border p-6"}>
        <p className="mb-3 text-xs font-semibold uppercase tracking-wide text-muted-foreground">
          Free response -- {frq.pointValue} point{frq.pointValue === 1 ? "" : "s"}
        </p>
        <div
          className="prose prose-neutral dark:prose-invert max-w-none"
          dangerouslySetInnerHTML={{ __html: promptHtml }}
        />
        {diagram && <DiagramRenderer diagram={diagram} />}
      </div>

      <FrqSelfGrade
        frqPromptId={frq.id}
        pointValue={frq.pointValue}
        rubric={rubric}
        sampleResponseHtml={sampleResponseHtml}
        paperLined={paperLined}
      />
    </div>
  );
}
