import type { Metadata } from "next";
import { notFound } from "next/navigation";
import { requireUserId } from "@/lib/auth/session";
import { getDb } from "@/lib/db";
import { renderContentToHtml } from "@/lib/content/render";
import { FrqSelfGrade } from "@/components/study/frq-self-grade";
import { renderRubric } from "@/lib/study/render-rubric";
import { DiagramRenderer } from "@/components/diagrams/diagram-renderer";
import { Html } from "@/components/ui/html";
import { Page } from "@/components/ui/page";
import { Sheet } from "@/components/ui/sheet";
import type { Diagram } from "@/lib/content/diagram-schema";
import { isPaperLinedCourse } from "@/lib/content/paper-lined";
import Link from "next/link";

export const metadata: Metadata = { title: "Free-response practice" };

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
  const rubric = await renderRubric(frq.rubric, courseSlug);
  const diagram = (frq.diagram as Diagram | null) ?? null;
  const paperLined = isPaperLinedCourse(courseSlug);

  return (
    <Page>
      <div className="grid gap-x-10 gap-y-3 md:grid-cols-[10.5rem_minmax(0,1fr)]">
        <div className="space-y-3 md:pt-1">
          <p className="eyebrow !text-foreground">
            Free response
            <br />
            {frq.pointValue} point{frq.pointValue === 1 ? "" : "s"}
          </p>
          <Link
            href={`/courses/${courseSlug}/units/${unitSlug}`}
            className="eyebrow inline-block underline underline-offset-4 hover:bg-mark hover:text-on-mark hover:no-underline"
          >
            Back to unit
          </Link>
        </div>

        <div className="min-w-0 space-y-6">
          <Sheet lined={paperLined}>
            <Html html={promptHtml} />
            {diagram && <DiagramRenderer diagram={diagram} />}
          </Sheet>

          <FrqSelfGrade
            frqPromptId={frq.id}
            pointValue={frq.pointValue}
            rubric={rubric}
            sampleResponseHtml={sampleResponseHtml}
            paperLined={paperLined}
          />
        </div>
      </div>
    </Page>
  );
}
