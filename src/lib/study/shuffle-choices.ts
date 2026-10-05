// Answer choices are shuffled every time a question is shown, so the position
// of the right answer carries no information (the authored content has it in
// slot A for ~99% of Calculus and 100% of Physics questions).
//
// A choice keeps its authored `label` as its identity: that is what the client
// sends back, what is stored on QuestionAttempt.chosenLabel and what is graded
// against Choice.label. Only what the student *sees* changes: the order, and
// `displayLabel`, the letter shown for the slot it landed in.

export interface PresentedChoice {
  label: string;
  displayLabel: string;
}

// Uniform Fisher-Yates. It can return the authored order by chance (1 in 24 for
// four choices); forcing a different order every time would bias the result.
export function shuffleChoices<T extends { label: string }>(choices: readonly T[], random: () => number = Math.random): (T & PresentedChoice)[] {
  const order = [...choices];
  for (let i = order.length - 1; i > 0; i--) {
    const j = Math.floor(random() * (i + 1));
    [order[i], order[j]] = [order[j], order[i]];
  }
  return order.map((choice, i) => ({ ...choice, displayLabel: String.fromCharCode(65 + i) }));
}

// authored label -> letter shown now
export function displayLabelMap(choices: PresentedChoice[]): Record<string, string> {
  return Object.fromEntries(choices.map((c) => [c.label, c.displayLabel]));
}

// Text can point at a choice by letter ("even fewer than option A"). The letter
// is only right in the authored order, so rewrite those references to the
// letters now on screen. Only "choice/option/answer/response/statement/letter X"
// is rewritten: a bare "A" or "(a)" is far more often math or code (f(a),
// a.equals(b)). tests/choice-letters-audit.test.ts checks that no content uses
// any other form.
const LETTER_REFERENCE = /\b((?:[Cc]hoices?|[Oo]ptions?|[Aa]nswers?|[Rr]esponses?|[Ss]tatements?|[Ll]etter)\s+\(?)([A-E])(\)?)(?![A-Za-z0-9_(]|\.[A-Za-z0-9_])/g;

export function remapChoiceLetters(text: string, displayByLabel: Record<string, string>): string {
  return text.replace(LETTER_REFERENCE, (match, before: string, letter: string, after: string) => {
    const shown = displayByLabel[letter];
    return shown ? `${before}${shown}${after}` : match;
  });
}
