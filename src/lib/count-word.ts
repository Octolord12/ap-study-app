const WORDS = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"];

// Small counts read better as words in headlines ("Five exams"); anything past ten stays a numeral.
export function countWord(n: number, capitalize = false): string {
  const word = Number.isInteger(n) && n >= 0 && n < WORDS.length ? WORDS[n] : String(n);
  return capitalize ? word.charAt(0).toUpperCase() + word.slice(1) : word;
}
