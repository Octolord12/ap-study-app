// One question per course for the landing page's binder, so a visitor can try the real answer-and-explain flow
// before signing up. They live here, not in the database, so rendering the landing page never reads or writes
// user data. The Calculus AB item is copied verbatim from the bank (content/ap-calc/questions/unit-2.json,
// ap-calc-u2-mcq-3); the others are written for this page with their answers worked out by hand and none refers
// to a choice by letter (the choices are shuffled on every visit).

export interface SampleChoice {
  label: string;
  text: string;
  isCorrect: boolean;
  explanation: string;
}

export interface SampleQuestionData {
  courseSlug: string;
  course: string;
  unit: string;
  stem: string;
  choices: readonly SampleChoice[];
  explanation: string;
}

export const SAMPLE_QUESTIONS: readonly SampleQuestionData[] = [
  {
    courseSlug: "ap-csa",
    course: "AP Computer Science A",
    unit: "Unit 1, Primitive Types",
    stem: "What is printed by the following statement?\n\n```java\nSystem.out.println(7 / 2 + 7 % 2);\n```",
    choices: [
      { label: "A", text: "3", isCorrect: false, explanation: "That is 7 / 2 on its own. The remainder, 7 % 2 = 1, is added as well." },
      { label: "B", text: "3.5", isCorrect: false, explanation: "3.5 would be decimal division. Both operands are int, so 7 / 2 is 3." },
      { label: "C", text: "4", isCorrect: true, explanation: "Integer division gives 7 / 2 = 3, the remainder 7 % 2 is 1, and the sum is 4." },
      { label: "D", text: "4.5", isCorrect: false, explanation: "This treats 7 / 2 as 3.5 and adds 1. Integer division drops the fraction." },
    ],
    explanation: "Both operands are int, so 7 / 2 is integer division and gives 3. The expression 7 % 2 is the remainder, 1. The sum is 4.",
  },
  {
    courseSlug: "ap-world",
    course: "AP World History: Modern",
    unit: "Unit 4, Transoceanic Interconnections",
    stem: "Which effect of the Columbian Exchange most directly helped populations grow in Afro-Eurasia between 1500 and 1800?",
    choices: [
      {
        label: "A",
        text: "The shipment of silver from Europe to the Americas, which lowered food prices across Asia",
        isCorrect: false,
        explanation: "Silver mostly flowed out of the Americas to Europe and Asia, so the direction is backwards, and it does not explain population growth.",
      },
      {
        label: "B",
        text: "The adoption of American crops such as potatoes and maize, which fed more people per acre of land",
        isCorrect: true,
        explanation: "Potatoes, maize and sweet potatoes grew in poor soil and gave more calories per acre, which supported larger populations in Europe and China.",
      },
      {
        label: "C",
        text: "The spread of smallpox and measles from the Americas across Europe and Asia, which raised birth rates",
        isCorrect: false,
        explanation: "Disease moved mainly the other way. Smallpox and measles from Europe devastated Native American populations.",
      },
      {
        label: "D",
        text: "The decline of the Atlantic slave trade, which freed farm labor for cultivation in Africa",
        isCorrect: false,
        explanation: "The Atlantic slave trade grew between 1500 and 1800. It did not decline in this period.",
      },
    ],
    explanation:
      "American food crops grew in poor soil and gave more calories per acre, which supported larger populations in Europe and China. Disease moved mainly from Europe to the Americas, and silver flowed out of the Americas.",
  },
  {
    courseSlug: "ap-us-history",
    course: "AP U.S. History",
    unit: "Unit 3, 1754 to 1800",
    stem: "The Proclamation of 1763 was intended mainly to",
    choices: [
      {
        label: "A",
        text: "limit conflict with Native nations by barring colonial settlement west of the Appalachian Mountains",
        isCorrect: true,
        explanation: "After the French and Indian War, Britain wanted to avoid costly frontier wars, so it banned settlement west of the Appalachians.",
      },
      {
        label: "B",
        text: "raise revenue from the colonies by taxing printed materials such as newspapers, pamphlets and legal papers",
        isCorrect: false,
        explanation: "That describes the Stamp Act of 1765. The proclamation was about western land, not revenue.",
      },
      {
        label: "C",
        text: "force colonists to house and supply British soldiers in their private homes and barns",
        isCorrect: false,
        explanation: "That describes the Quartering Act. The proclamation did not deal with soldiers' housing.",
      },
      {
        label: "D",
        text: "end colonial trade with France by requiring all goods to pass through British ports",
        isCorrect: false,
        explanation: "That is closer to the Navigation Acts, which began in the 1650s and predate the proclamation.",
      },
    ],
    explanation:
      "After the French and Indian War, Britain wanted to avoid costly wars with Native nations, so it banned settlement west of the Appalachians. Many colonists resented it. The other choices describe the Stamp Act, the Quartering Act and the Navigation Acts.",
  },
  {
    courseSlug: "ap-calc",
    course: "AP Calculus AB",
    unit: "Unit 2, Differentiation: Definition and Fundamental Properties",
    stem: "How is the instantaneous rate of change of f(x) at x=a defined, in terms of a limit?",
    choices: [
      {
        label: "A",
        text: "$\\lim_{h \\to 0} \\dfrac{f(a+h) - f(a)}{h}$",
        isCorrect: true,
        explanation: "This is the standard difference-quotient definition of the instantaneous rate of change (the derivative) at x=a.",
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
        explanation: "Instantaneous rate of change involves h approaching 0 (an infinitesimally small interval), not h approaching infinity.",
      },
    ],
    explanation: "The instantaneous rate of change at x=a is defined as $\\lim_{h \\to 0} \\frac{f(a+h)-f(a)}{h}$.",
  },
  {
    courseSlug: "ap-calc-bc",
    course: "AP Calculus BC",
    unit: "Unit 10, Infinite Sequences and Series",
    stem: "For $n \\ge 1$, which of the following series converges?",
    choices: [
      { label: "A", text: "$\\sum \\dfrac{1}{n^2}$", isCorrect: true, explanation: "A p-series converges when $p > 1$. Here $p = 2$." },
      { label: "B", text: "$\\sum \\dfrac{1}{n}$", isCorrect: false, explanation: "This is the harmonic series, a p-series with $p = 1$, which diverges." },
      { label: "C", text: "$\\sum \\dfrac{1}{\\sqrt{n}}$", isCorrect: false, explanation: "Here $p = \\tfrac{1}{2}$, which is not greater than 1, so the series diverges." },
      { label: "D", text: "$\\sum \\dfrac{n}{n + 1}$", isCorrect: false, explanation: "The terms approach 1, not 0, so the series diverges by the nth-term test." },
    ],
    explanation: "A p-series $\\sum \\frac{1}{n^p}$ converges when $p > 1$. Here $p = 2$, so $\\sum \\frac{1}{n^2}$ converges. The terms of the last series approach 1, so it diverges.",
  },
  {
    courseSlug: "ap-physics-1",
    course: "AP Physics 1",
    unit: "Unit 5, Momentum",
    stem: "A 0.50 kg ball hits a wall moving at 4.0 m/s and bounces straight back at 3.0 m/s. What is the magnitude of the impulse the wall exerts on the ball?",
    choices: [
      { label: "A", text: "0.50 N·s", isCorrect: false, explanation: "This subtracts the speeds (4.0 − 3.0) and so ignores that the velocity reverses direction." },
      { label: "B", text: "2.0 N·s", isCorrect: false, explanation: "This is the mass times the incoming speed, 0.50 × 4.0. The ball also leaves at 3.0 m/s the other way." },
      { label: "C", text: "3.5 N·s", isCorrect: true, explanation: "Take away from the wall as positive: Δp = 0.50 × (3.0 − (−4.0)) = 3.5 N·s." },
      { label: "D", text: "7.0 N·s", isCorrect: false, explanation: "This adds the speeds but forgets to multiply by the mass." },
    ],
    explanation: "Impulse equals the change in momentum, and the velocity reverses. Δp = 0.50 × (3.0 − (−4.0)) = 3.5 N·s.",
  },
  {
    courseSlug: "ap-biology",
    course: "AP Biology",
    unit: "Unit 2, Cells",
    stem: "An animal cell is placed in a solution with a higher solute concentration than its cytoplasm. What happens to the cell?",
    choices: [
      {
        label: "A",
        text: "Water enters the cell by osmosis, and the cell swells and may burst",
        isCorrect: false,
        explanation: "That happens in a hypotonic solution, where the outside has less solute than the cell.",
      },
      {
        label: "B",
        text: "Solutes leave the cell by active transport until both sides are equal",
        isCorrect: false,
        explanation: "Active transport needs energy and a pump, and it is not what balances this. Water moves instead.",
      },
      {
        label: "C",
        text: "Nothing changes, because the membrane blocks the movement of water",
        isCorrect: false,
        explanation: "Water crosses the plasma membrane, through aquaporins and across the lipid bilayer, so the cell does change.",
      },
      {
        label: "D",
        text: "Water leaves the cell by osmosis, and the cell shrinks",
        isCorrect: true,
        explanation: "The solution is hypertonic. Water moves toward the higher solute concentration, which is outside the cell.",
      },
    ],
    explanation:
      "The solution is hypertonic to the cell. Water moves by osmosis toward the higher solute concentration, which is outside, so the cell loses water and shrinks. A cell swells and may burst only in a hypotonic solution.",
  },
  {
    courseSlug: "ap-statistics",
    course: "AP Statistics",
    unit: "Unit 3, Inference for Categorical Data",
    stem: "A 95% confidence interval for a population proportion is (0.42, 0.58). Which statement is the correct interpretation?",
    choices: [
      {
        label: "A",
        text: "There is a 95% probability that the sample proportion is between 0.42 and 0.58, the ends of the interval.",
        isCorrect: false,
        explanation: "The sample proportion is known exactly (0.50, the midpoint), so it carries no probability.",
      },
      {
        label: "B",
        text: "We are 95% confident that the interval from 0.42 to 0.58 captures the true population proportion.",
        isCorrect: true,
        explanation: "Confidence describes the method: about 95% of intervals built this way capture the true proportion.",
      },
      {
        label: "C",
        text: "About 95% of individuals in the population have a value between 0.42 and 0.58.",
        isCorrect: false,
        explanation: "The interval estimates a population proportion. It does not say where individual values fall.",
      },
      {
        label: "D",
        text: "If we took another sample, there is a 95% chance its proportion would fall in this interval.",
        isCorrect: false,
        explanation: "A new sample gives a new interval and a new proportion, and the chance of landing here is not 95%.",
      },
    ],
    explanation:
      "Confidence describes the method: about 95% of intervals built this way capture the true proportion. The interval is about the population proportion, not individuals and not future samples.",
  },
];
