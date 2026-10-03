// A real question from the bank (content/ap-calc/questions/unit-2.json,
// ap-calc-u2-mcq-3), copied verbatim for the landing page so visitors can try
// the actual answer-and-explain flow before signing up. It lives here, not in
// the database, so rendering the landing page never reads or writes user data.
export const SAMPLE_COURSE_SLUG = "ap-calc";

export const SAMPLE_QUESTION = {
  meta: "AP Calculus AB · Unit 2 · Medium",
  stem: "How is the instantaneous rate of change of f(x) at x=a defined, in terms of a limit?",
  choices: [
    {
      label: "A",
      text: "$\\lim_{h \\to 0} \\dfrac{f(a+h) - f(a)}{h}$",
      isCorrect: true,
      explanation:
        "This is the standard difference-quotient definition of the instantaneous rate of change (the derivative) at x=a.",
    },
    {
      label: "B",
      text: "$\\lim_{h \\to 0} [f(a) + h]$",
      isCorrect: false,
      explanation: "This doesn't represent a rate of change formula at all; it's just adding h to f(a).",
    },
    {
      label: "C",
      text: "$\\dfrac{f(a)}{a}$",
      isCorrect: false,
      explanation: "Dividing the function value by the x-value is unrelated to the definition of instantaneous rate of change.",
    },
    {
      label: "D",
      text: "$\\lim_{h \\to \\infty} \\dfrac{f(a+h) - f(a)}{h}$",
      isCorrect: false,
      explanation:
        "Instantaneous rate of change involves h approaching 0 (an infinitesimally small interval), not h approaching infinity.",
    },
  ],
  explanation: "The instantaneous rate of change at x=a is defined as $\\lim_{h \\to 0} \\frac{f(a+h)-f(a)}{h}$.",
} as const;
