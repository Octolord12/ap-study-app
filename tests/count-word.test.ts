import { describe, expect, it } from "vitest";
import { countWord } from "@/lib/count-word";

describe("countWord", () => {
  it("spells out zero to ten", () => {
    expect(countWord(0)).toBe("zero");
    expect(countWord(4)).toBe("four");
    expect(countWord(5)).toBe("five");
    expect(countWord(10)).toBe("ten");
  });

  it("capitalizes on request", () => {
    expect(countWord(5, true)).toBe("Five");
  });

  it("falls back to the numeral for larger or odd values", () => {
    expect(countWord(11)).toBe("11");
    expect(countWord(2.5)).toBe("2.5");
    expect(countWord(-1)).toBe("-1");
  });
});
