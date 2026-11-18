import { renderChoiceTextToHtml, renderContentToHtml } from "@/lib/content/render";
import { courseAccent, courseTabLabel } from "@/lib/content/course-accent";
import { SAMPLE_QUESTIONS } from "@/lib/marketing/sample-question";
import { shuffleChoices } from "@/lib/study/shuffle-choices";

export interface RenderedSampleChoice {
  label: string;
  displayLabel: string;
  textHtml: string;
  explanationHtml: string;
  isCorrect: boolean;
}

export interface RenderedSample {
  courseSlug: string;
  accent: string | undefined;
  tab: string;
  course: string;
  unit: string;
  stemHtml: string;
  explanationHtml: string;
  choices: RenderedSampleChoice[];
}

type Unshuffled = Omit<RenderedSample, "choices"> & { choices: Omit<RenderedSampleChoice, "displayLabel">[] };

// The samples never change, so the markdown pipeline (Shiki and KaTeX) runs once per server process, not on every
// visit. Only the order of the choices is decided per visit (see `renderSamples`).
let cache: Promise<Unshuffled[]> | undefined;

function build(): Promise<Unshuffled[]> {
  return Promise.all(
    SAMPLE_QUESTIONS.map(async (q) => {
      const [stemHtml, explanationHtml, choices] = await Promise.all([
        renderContentToHtml(q.stem, q.courseSlug),
        renderContentToHtml(q.explanation, q.courseSlug),
        Promise.all(
          q.choices.map(async (c) => ({
            label: c.label,
            isCorrect: c.isCorrect,
            textHtml: await renderChoiceTextToHtml(c.text, q.courseSlug),
            explanationHtml: await renderContentToHtml(c.explanation, q.courseSlug),
          })),
        ),
      ]);
      return {
        courseSlug: q.courseSlug,
        accent: courseAccent(q.courseSlug),
        tab: courseTabLabel(q.courseSlug, q.course),
        course: q.course,
        unit: q.unit,
        stemHtml,
        explanationHtml,
        choices,
      };
    }),
  );
}

// Every sample, rendered, with its choices shuffled for this visit like the real questions.
export async function renderSamples(random?: () => number): Promise<RenderedSample[]> {
  cache ??= build().catch((error) => {
    cache = undefined;
    throw error;
  });
  const samples = await cache;
  return samples.map((s) => ({ ...s, choices: shuffleChoices(s.choices, random) }));
}
