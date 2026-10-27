import { z } from "zod";
import { DiagramSchema } from "./diagram-schema";

// Structural shape of the JSON files in /content. Semantic checks (exactly one
// correct choice, rubric points summing to pointValue, unit/topic references
// resolving, etc.) live in ./validate.ts, not here -- Zod only proves the shape.

export const DifficultySchema = z.enum(["easy", "medium", "hard"]);

export const ChoiceSchema = z.object({
  label: z.enum(["A", "B", "C", "D", "E"]),
  text: z.string().min(1),
  isCorrect: z.boolean(),
  explanation: z.string().min(1),
});

export const QuestionSchema = z.object({
  id: z.string().min(1),
  unit: z.string().min(1),
  topic: z.string().min(1),
  difficulty: DifficultySchema,
  stem: z.string().min(1),
  choices: z.array(ChoiceSchema).min(4).max(5),
  explanation: z.string().min(1),
  conceptLink: z.string().min(1),
  reviewed: z.boolean(),
  diagram: DiagramSchema.optional(),
});

export const RubricLineSchema = z.object({
  id: z.string().min(1),
  points: z.number().int().positive(),
  description: z.string().min(1),
});

// Which exam section a prompt is drawn for. Left out, it means plain "FRQ", the one
// free-response section CSA, Calc and Physics have; World History must say SAQ, DBQ or LEQ; AP Biology's six
// questions are six kinds (see ExamSectionSchema.kinds): experimental results (with and without graphing),
// scientific investigation, conceptual analysis, analyzing a model, analyzing data. AP Statistics' four questions are
// four kinds too: formulating questions and collecting data, analyzing data and interpreting results, inference, and a
// multi-focus question over several content areas.
export const FrqTypeSchema = z.enum([
  "FRQ",
  "SAQ",
  "DBQ",
  "LEQ",
  "RESULTS",
  "RESULTS_GRAPH",
  "INVESTIGATION",
  "CONCEPT",
  "MODEL",
  "DATA",
  "COLLECT_DATA",
  "ANALYZE_DATA",
  "INFERENCE",
  "MULTI_FOCUS",
]);

export const FRQSchema = z.object({
  id: z.string().min(1),
  unit: z.string().min(1),
  topic: z.string().min(1),
  type: FrqTypeSchema.optional(),
  prompt: z.string().min(1),
  pointValue: z.number().int().positive(),
  rubric: z.array(RubricLineSchema).min(1),
  sampleResponse: z.string().min(1),
  reviewed: z.boolean(),
  diagram: DiagramSchema.optional(),
});

// A short written refresher for one topic (content/<course>/refreshers/*.json, an array of these).
// Markdown, with $...$ math and code fences like every other field. Which topic it belongs to is
// "<unit>/<topic>", the same key a question's conceptLink uses.
export const RefresherSchema = z.object({
  unit: z.string().min(1),
  topic: z.string().min(1),
  body: z.string().min(1),
  reviewed: z.boolean(),
});

export const TopicSchema = z.object({
  slug: z.string().min(1),
  order: z.number().int().positive(),
  name: z.string().min(1),
});

export const UnitSchema = z.object({
  slug: z.string().min(1),
  order: z.number().int().positive(),
  name: z.string().min(1),
  weightingMin: z.number().int().min(0).max(100),
  weightingMax: z.number().int().min(0).max(100),
  topics: z.array(TopicSchema).min(1),
});

export const ExamSectionSchema = z
  .object({
    type: z.enum(["MCQ", "FRQ", "SAQ", "DBQ", "LEQ"]),
    questionCount: z.number().int().positive(),
    durationMinutes: z.number().int().positive(),
    scoreWeight: z.number().min(0).max(1),
    calculatorAllowed: z.boolean().optional(),
    // One prompt of each kind, in this order; see lib/content/exam-sections.ts. Only on a free-response section.
    kinds: z.array(FrqTypeSchema).min(2).optional(),
  })
  .superRefine((section, ctx) => {
    if (!section.kinds) return;
    if (section.type === "MCQ") ctx.addIssue({ code: "custom", message: "kinds belongs on a free-response section, not MCQ" });
    if (section.kinds.length !== section.questionCount) ctx.addIssue({ code: "custom", message: `kinds lists ${section.kinds.length} but questionCount is ${section.questionCount}` });
    if (new Set(section.kinds).size !== section.kinds.length) ctx.addIssue({ code: "custom", message: "kinds must be different from one another" });
  });

export const CourseSchema = z.object({
  slug: z.string().min(1),
  name: z.string().min(1),
  description: z.string().min(1),
  colorTheme: z.string().min(1),
  examFormat: z.object({
    totalDurationMinutes: z.number().int().positive(),
    sections: z.array(ExamSectionSchema).min(1),
  }),
});

export type Choice = z.infer<typeof ChoiceSchema>;
export type Question = z.infer<typeof QuestionSchema>;
export type RubricLine = z.infer<typeof RubricLineSchema>;
export type FRQ = z.infer<typeof FRQSchema>;
export type FrqType = z.infer<typeof FrqTypeSchema>;
export type Topic = z.infer<typeof TopicSchema>;
export type Refresher = z.infer<typeof RefresherSchema>;
export type Unit = z.infer<typeof UnitSchema>;
export type Course = z.infer<typeof CourseSchema>;
