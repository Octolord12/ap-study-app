import { describe, expect, it } from "vitest";
import { normalizePlainMath } from "@/lib/content/plain-math";

const math = (s: string) => normalizePlainMath(s, { mathCourse: true });
const other = (s: string) => normalizePlainMath(s, { mathCourse: false });

describe("normalizePlainMath", () => {
  it("turns digit exponents into plain superscripts (units, powers)", () => {
    expect(math("2.5 m/s^2")).toBe("2.5 m/s²");
    expect(math("≈ 0.94 m/s^2")).toBe("≈ 0.94 m/s²");
    expect(math("x^3+1 factors as (x+1)(x^2-x+1)")).toBe("x³+1 factors as (x+1)(x²-x+1)");
    expect(math("(3x+1)^4 and 10^-3")).toBe("(3x+1)⁴ and 10⁻³");
  });

  it("typesets letter/expression exponents with KaTeX", () => {
    expect(math("derivative of x^n is n*x^(n-1)")).toBe("derivative of $x^{n}$ is n*$x^{n-1}$");
    expect(math("= e^(2x) * 2 = 2e^(2x)")).toBe("= $e^{2x}$ * 2 = $2e^{2x}$");
    expect(math("x^2.5")).toBe("$x^{2.5}$");
  });

  it("typesets square roots, including nested parens and exponents inside", () => {
    expect(math("z = sqrt(60^2+80^2) = sqrt(10000)")).toBe("z = $\\sqrt{60^2+80^2}$ = $\\sqrt{10000}$");
    expect(math("sqrt((x+1)/2)")).toBe("$\\sqrt{(x+1)/2}$");
    expect(math("unbalanced sqrt(x")).toBe("unbalanced sqrt(x");
  });

  it("typesets subscripts and arrows", () => {
    expect(math("a = F_net/m, v_f=3 m/s")).toBe("a = $F_{net}$/m, $v_{f}$=3 m/s");
    expect(math("KE_rot = (1/2)Iω^2")).toBe("$KE_{rot}$ = (1/2)Iω²");
    expect(math("4x^3 -> x^4, -6x -> -3x^2")).toBe("4x³ → x⁴, -6x → -3x²");
  });

  it("handles coefficient-attached, long, and limit subscripts", () => {
    expect(math("so 12 = 5v_f, giving v_f = 2.4")).toBe("so 12 = 5$v_{f}$, giving $v_{f}$ = 2.4");
    expect(math("KE_before = 81 J and m_bullet·v_bullet")).toBe("$KE_{before}$ = 81 J and $m_{bullet}$·$v_{bullet}$");
    expect(math("ρ_object/ρ_fluid")).toBe("$ρ_{object}$/$ρ_{fluid}$");
    expect(math("Left-hand limit: lim_{x->3^-} (x^2 + k)")).toBe("Left-hand limit: $\\lim_{x\\to 3^-}$ (x² + k)");
  });

  it("leaves math, inline code, and fenced code untouched", () => {
    expect(math("already $x^2 + y_1$ fine")).toBe("already $x^2 + y_1$ fine");
    expect(math("$$\\sqrt{x}^2$$")).toBe("$$\\sqrt{x}^2$$");
    expect(math("code `a^2 + b_1` here")).toBe("code `a^2 + b_1` here");
    expect(math("```\nint y = x^2;\n```")).toBe("```\nint y = x^2;\n```");
  });

  it("does not touch spaced operators or ordinary prose", () => {
    expect(math("a ^ b means XOR")).toBe("a ^ b means XOR");
    expect(math("The rate is 4.9 m/s² downward.")).toBe("The rate is 4.9 m/s² downward.");
  });

  it("outside the math courses only fixes digit exponents, never code-like text", () => {
    expect(other("O(n^2)")).toBe("O(n²)");
    expect(other("n^2")).toBe("n²");
    expect(other("total_score")).toBe("total_score");
    expect(other("myDog->bark();")).toBe("myDog->bark();");
    expect(other("sqrt(x) and a^b")).toBe("sqrt(x) and a^b");
  });

  it("is idempotent", () => {
    const once = math("F_net = m*a, x^3 + e^(2x), sqrt(x), 4x^3 -> x^4, 9.8 m/s^2");
    expect(math(once)).toBe(once);
  });
});
