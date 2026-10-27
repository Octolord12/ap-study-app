import { DiagramRenderer } from "@/components/diagrams/diagram-renderer";
import { Html } from "@/components/ui/html";
import type { Diagram } from "@/lib/content/diagram-schema";
import type { RenderedFrqPrompt } from "@/lib/study/render-frq-prompt";

// The set-up text, then the figure it describes, then the lettered parts that refer to it. A prompt that
// could not be split has all its text in `introHtml`, so its figure follows the text as it always did.
export function FrqPrompt({ prompt, diagram, className }: { prompt: RenderedFrqPrompt; diagram: Diagram | null; className?: string }) {
  return (
    <>
      <Html html={prompt.introHtml} className={className} />
      {diagram && (
        <div className="my-4">
          <DiagramRenderer diagram={diagram} />
        </div>
      )}
      {prompt.partsHtml && <Html html={prompt.partsHtml} />}
    </>
  );
}
