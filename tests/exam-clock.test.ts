import { describe, expect, it } from "vitest";
import { secondsRemaining } from "@/lib/study/exam-clock";

const START = Date.UTC(2026, 9, 5, 12, 0, 0);
const MIN = 60_000;

describe("secondsRemaining", () => {
  it("is the full time at the start", () => {
    expect(secondsRemaining(START, 190, START)).toBe(190 * 60);
  });

  it("counts down with real time, so a reload resumes the clock instead of resetting it", () => {
    // The reviewer's case: 17 seconds in, reload. The clock must read 3:09:43, not 3:10:00.
    expect(secondsRemaining(START, 190, START + 17_000)).toBe(190 * 60 - 17);
    expect(secondsRemaining(START, 190, START + 45 * MIN)).toBe(145 * 60);
  });

  it("reaches zero exactly at the end and never goes negative", () => {
    expect(secondsRemaining(START, 190, START + 190 * MIN)).toBe(0);
    expect(secondsRemaining(START, 190, START + 190 * MIN + 1)).toBe(0);
    expect(secondsRemaining(START, 190, START + 24 * 60 * MIN)).toBe(0);
  });

  it("rounds a partial second up, so the clock never shows 0:00 with time left", () => {
    expect(secondsRemaining(START, 1, START + 59_500)).toBe(1);
  });

  it("gives nobody more than the full time if this machine's clock is behind", () => {
    expect(secondsRemaining(START, 190, START - 5 * MIN)).toBe(190 * 60);
  });
});
