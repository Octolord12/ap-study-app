import { render, screen } from "@testing-library/react";
import { afterEach, beforeEach, describe, expect, it, vi } from "vitest";
import { ExamCountdown } from "@/components/study/exam-countdown";

// Today, for the student: Monday 2026-10-05, afternoon, local time.
const NOW = new Date(2026, 9, 5, 15, 0, 0);

function show(props: Partial<React.ComponentProps<typeof ExamCountdown>> = {}) {
  return render(<ExamCountdown examDateIso="2026-11-04" total={300} tried={60} newPerDay={8} cramOn={false} {...props} />);
}

describe("ExamCountdown", () => {
  beforeEach(() => {
    vi.useFakeTimers();
    vi.setSystemTime(NOW);
  });
  afterEach(() => vi.useRealTimers());

  it("shows the date, the days left and the daily goal", () => {
    show(); // 30 days, 240 untried
    expect(screen.getByText("Wednesday, November 4, 2026")).toBeInTheDocument();
    expect(screen.getByText("30")).toBeInTheDocument();
    expect(screen.getByText("days to go")).toBeInTheDocument();
    expect(screen.getByText("8 new questions a day")).toBeInTheDocument();
    expect(screen.getByText("12 minutes")).toBeInTheDocument();
    expect(screen.getByText(/240 questions you have not tried yet, at 90 seconds each/)).toBeInTheDocument();
  });

  it("says on pace when this week's rate would finish in time", () => {
    show({ newPerDay: 9 });
    expect(screen.getByText(/On pace: this week you tried 9 new questions a day/)).toBeInTheDocument();
  });

  it("says behind, with the number needed, when it would not", () => {
    show({ newPerDay: 2.5 });
    expect(screen.getByText(/Behind pace: this week you tried 2.5 new questions a day, and 8 a day would finish in time/)).toBeInTheDocument();
  });

  it("encourages a student who has not started instead of calling them behind", () => {
    show({ tried: 0, newPerDay: 0 });
    expect(screen.getByText(/You have not started yet. Begin with 10 questions today/)).toBeInTheDocument();
    expect(screen.queryByText(/Behind pace/)).not.toBeInTheDocument();
  });

  it("uses the singular for one day", () => {
    show({ examDateIso: "2026-10-06", total: 10, tried: 5 });
    expect(screen.getByText("day to go")).toBeInTheDocument();
    expect(screen.getByText("5 new questions a day")).toBeInTheDocument();
  });

  it("suggests Cram Mode in the last two weeks, unless it is already on", () => {
    const { unmount } = show({ examDateIso: "2026-10-15" });
    expect(screen.getByRole("link", { name: "Cram Mode" })).toHaveAttribute("href", "/dashboard");
    unmount();
    show({ examDateIso: "2026-10-15", cramOn: true });
    expect(screen.queryByRole("link", { name: "Cram Mode" })).not.toBeInTheDocument();
  });

  it("does not push Cram Mode when the exam is far off", () => {
    show();
    expect(screen.queryByRole("link", { name: "Cram Mode" })).not.toBeInTheDocument();
  });

  it("says so once every question has been tried", () => {
    show({ tried: 300 });
    expect(screen.getByText(/You have tried every question/)).toBeInTheDocument();
    expect(screen.queryByText(/new questions a day/)).not.toBeInTheDocument();
  });

  it("marks exam day and a date that has passed", () => {
    const { unmount } = show({ examDateIso: "2026-10-05" });
    expect(screen.getByText("It is exam day.")).toBeInTheDocument();
    unmount();
    show({ examDateIso: "2026-10-01" });
    expect(screen.getByText(/That date was 4 days ago/)).toBeInTheDocument();
  });

  it("offers a way to change the date where there is no form on the page", () => {
    show({ changeHref: "/courses/ap-calc#exam-date" });
    expect(screen.getByRole("link", { name: "Change the date" })).toHaveAttribute("href", "/courses/ap-calc#exam-date");
  });

  it("counts days from the student's own calendar date, not UTC", () => {
    // 9pm Monday Pacific is already Tuesday in UTC. The local date must win.
    vi.setSystemTime(new Date(2026, 9, 5, 21, 0, 0));
    show({ examDateIso: "2026-10-06" });
    expect(screen.getByText("day to go")).toBeInTheDocument();
  });
});
