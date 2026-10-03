import { renderContentToHtml } from "@/lib/content/render";

export interface RenderedRubricLine {
  id: string;
  points: number;
  description: string;
  descriptionHtml: string;
}

// Rubric lines are shown inside a Client Component (FrqSelfGrade) and a list
// on the admin page, neither of which can run the markdown/KaTeX pipeline
// itself, so they're rendered here on the server -- same reason as
// renderQuizQuestions. `description` stays as plain text for anything that
// only needs the words.
export async function renderRubric(rubric: unknown, courseSlug: string): Promise<RenderedRubricLine[]> {
  const lines = rubric as { id: string; points: number; description: string }[];
  return Promise.all(
    lines.map(async (line) => ({
      id: line.id,
      points: line.points,
      description: line.description,
      descriptionHtml: await renderContentToHtml(line.description, courseSlug),
    })),
  );
}
