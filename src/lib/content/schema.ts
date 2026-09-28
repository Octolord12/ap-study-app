import { z } from "zod";

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
});

export const RubricLineSchema = z.object({
  id: z.string().min(1),
  points: z.number().int().positive(),
  description: z.string().min(1),
});

export const FRQSchema = z.object({
  id: z.string().min(1),
  unit: z.string().min(1),
  topic: z.string().min(1),
  prompt: z.string().min(1),
  pointValue: z.number().int().positive(),
  rubric: z.array(RubricLineSchema).min(1),
  sampleResponse: z.string().min(1),
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

export const ExamSectionSchema = z.object({
  type: z.enum(["MCQ", "FRQ", "SAQ", "DBQ", "LEQ"]),
  questionCount: z.number().int().positive(),
  durationMinutes: z.number().int().positive(),
  scoreWeight: z.number().min(0).max(1),
  calculatorAllowed: z.boolean().optional(),
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
export type Topic = z.infer<typeof TopicSchema>;
export type Unit = z.infer<typeof UnitSchema>;
export type Course = z.infer<typeof CourseSchema>;
