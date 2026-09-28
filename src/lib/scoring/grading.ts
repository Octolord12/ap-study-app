// FRQ grading sits behind this interface so a future AIGradingStrategy (Claude API)
// can be dropped in without touching the FRQ practice UI. Only SelfGradingStrategy
// exists for now: the student reads the rubric and checks off which lines they hit.

export interface RubricLine {
  id: string;
  points: number;
  description: string;
}

export interface GradingInput {
  responseText: string;
  rubric: RubricLine[];
  maxPoints: number;
}

export interface LineFeedback {
  ruleId: string;
  awarded: boolean;
}

export interface GradingResult {
  pointsAwarded: number;
  maxPoints: number;
  perLineFeedback: LineFeedback[];
}

export interface GradingStrategy<TContext = unknown> {
  grade(input: GradingInput, context: TContext): Promise<GradingResult>;
}

export interface SelfGradingContext {
  // Rubric line IDs the student says their own response satisfied.
  checkedLineIds: string[];
}

export class SelfGradingStrategy implements GradingStrategy<SelfGradingContext> {
  async grade(input: GradingInput, context: SelfGradingContext): Promise<GradingResult> {
    const checked = new Set(context.checkedLineIds);

    const perLineFeedback: LineFeedback[] = input.rubric.map((line) => ({
      ruleId: line.id,
      awarded: checked.has(line.id),
    }));

    const pointsAwarded = input.rubric
      .filter((line) => checked.has(line.id))
      .reduce((sum, line) => sum + line.points, 0);

    return { pointsAwarded, maxPoints: input.maxPoints, perLineFeedback };
  }
}
