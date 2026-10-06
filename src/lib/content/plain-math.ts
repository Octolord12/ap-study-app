// Authored content (explanations, answer choices, FRQ samples) often writes
// math in typewriter style outside any $...$ -- "m/s^2", "x^3", "F_net",
// "sqrt(x)", "->" -- which the markdown pipeline shows literally. This turns
// that into notation a student can read, without touching anything inside
// math delimiters or code, so it's safe to run on already-correct content.
//
// Digit exponents become plain unicode superscripts (x² / m/s²), matching
// what much of the content already writes by hand and staying in the body
// font. Everything else (letter exponents, subscripts, roots) needs real
// math typesetting, so it's wrapped in $...$ for KaTeX -- but only for the
// math courses, since in AP CSA an underscore is an identifier
// (total_score) and "->" is code (myDog->bark()), not math.

const SUPERSCRIPT: Record<string, string> = {
  "0": "⁰",
  "1": "¹",
  "2": "²",
  "3": "³",
  "4": "⁴",
  "5": "⁵",
  "6": "⁶",
  "7": "⁷",
  "8": "⁸",
  "9": "⁹",
  "-": "⁻",
};

// Odd entries of String.split are the captured (protected) spans.
const PROTECTED_SPANS = /(```[\s\S]*?```|`[^`\n]*`|\$\$[\s\S]*?\$\$|\$[^$\n]*\$)/g;

function mapPlain(text: string, transform: (plain: string) => string): string {
  return text
    .split(PROTECTED_SPANS)
    .map((part, i) => (i % 2 === 1 ? part : transform(part)))
    .join("");
}

const SUPERSCRIPT_TO_ASCII: Record<string, string> = Object.fromEntries(
  Object.entries(SUPERSCRIPT).map(([ascii, sup]) => [sup, ascii]),
);

function toSuperscript(exponent: string): string {
  return [...exponent].map((ch) => SUPERSCRIPT[ch] ?? ch).join("");
}

// A base that already had its digit exponent turned into a unicode
// superscript ("x²" in "x^2e^x") is about to go inside $...$; hand KaTeX
// real LaTeX (x^{2}) rather than leaning on its unicode support.
function superscriptsToLatex(base: string): string {
  return base.replace(/[⁰¹²³⁴⁵⁶⁷⁸⁹⁻]+/g, (run) => `^{${[...run].map((ch) => SUPERSCRIPT_TO_ASCII[ch]).join("")}}`);
}

// Authors write multiplication as a bare "*" ("4*pi*r^2 * dr/dt"), which
// markdown reads as italic markers -- eating the asterisks and italicizing
// whatever sits between them. Intentional **bold** pairs are left alone (no
// content uses single-asterisk italics). In the math courses it becomes a
// real multiplication dot; elsewhere (AP CSA, where * is Java's operator)
// it's escaped so it stays a literal asterisk.
// An attribution line under a source passage (`*Source: A Cairo chronicler, 1260*`) is intentional italics
// too: escaping its asterisks printed them literally under every History passage.
const BOLD_PAIR = /(\*\*[^*\n]+\*\*|\*Source: [^*\n]+\*)/;
function fixAsterisks(plain: string, replacement: string): string {
  return plain
    .split(BOLD_PAIR)
    .map((part, i) => (i % 2 === 1 ? part : part.replace(/(?<!\\)\*/g, replacement)))
    .join("");
}

function unwrapGroup(exponent: string): string {
  const wrapped = /^[({]([\s\S]*)[)}]$/.exec(exponent);
  return wrapped ? wrapped[1] : exponent;
}

function replaceSqrt(plain: string): string {
  let out = "";
  let i = 0;
  while (i < plain.length) {
    const at = plain.indexOf("sqrt(", i);
    if (at === -1) {
      out += plain.slice(i);
      break;
    }
    const insideWord = at > 0 && /\p{L}/u.test(plain[at - 1]);
    let depth = 0;
    let close = -1;
    if (!insideWord) {
      for (let j = at + 4; j < plain.length; j++) {
        if (plain[j] === "(") depth++;
        else if (plain[j] === ")" && --depth === 0) {
          close = j;
          break;
        }
      }
    }
    if (close === -1) {
      out += plain.slice(i, at + 5);
      i = at + 5;
      continue;
    }
    out += `${plain.slice(i, at)}$\\sqrt{${plain.slice(at + 5, close)}}$`;
    i = close + 1;
  }
  return out;
}

const DIGIT_EXPONENT = /(?<=[\p{L}\p{N})\]])\^(-?\d+)(?!\.\d)/gu;
const GENERAL_EXPONENT =
  /(\([^()]*\)|[\p{L}\p{N}]+(?:\.\d+)?)\^(\{[^{}]*\}|\([^()]*\)|-?[\p{L}\p{N}]+(?:\.\d+)?)/gu;
const SUBSCRIPT = /(?<![\p{L}_])(\p{L}{1,3})_([\p{L}\p{N}]{1,10})(?![\p{L}\p{N}_])/gu;
const LIMIT_SUBSCRIPT = /\blim_\{([^{}]*)\}/g;

export function normalizePlainMath(markdown: string, { mathCourse }: { mathCourse: boolean }): string {
  let text = markdown;
  if (mathCourse) {
    text = mapPlain(text, replaceSqrt);
    text = mapPlain(text, (plain) =>
      plain.replace(LIMIT_SUBSCRIPT, (_, sub: string) => `$\\lim_{${sub.replace(/->/g, "\\to ")}}$`),
    );
  }
  text = mapPlain(text, (plain) => plain.replace(DIGIT_EXPONENT, (_, exp: string) => toSuperscript(exp)));
  text = mapPlain(text, (plain) => fixAsterisks(plain, mathCourse ? "·" : "\\*"));
  if (!mathCourse) return text;

  text = mapPlain(text, (plain) =>
    plain.replace(
      GENERAL_EXPONENT,
      (_, base: string, exp: string) => `$${superscriptsToLatex(base)}^{${unwrapGroup(exp)}}$`,
    ),
  );
  text = mapPlain(text, (plain) => plain.replace(SUBSCRIPT, (_, base: string, sub: string) => `$${base}_{${sub}}$`));
  return mapPlain(text, (plain) => plain.replace(/\s->\s/g, " → "));
}
