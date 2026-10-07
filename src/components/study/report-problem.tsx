import { reportMailto } from "@/lib/site-contact";

// Opens the reader's mail app with the question's id filled in, so a report says which
// one it is about. Worth more than the generic footer link: it points at shaky content.
export function ReportProblem({ id, kind = "question", className }: { id: string; kind?: "question" | "free-response prompt" | "refresher"; className?: string }) {
  return (
    <a
      href={reportMailto(kind, id)}
      className={`text-sm font-semibold underline underline-offset-4 hover:bg-mark hover:text-on-mark hover:no-underline ${className ?? ""}`}
    >
      Report a problem with this {kind === "free-response prompt" ? "prompt" : kind}
    </a>
  );
}
