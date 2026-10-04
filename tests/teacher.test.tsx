import { render, screen } from "@testing-library/react";
import { describe, expect, it } from "vitest";
import { selectClass } from "@/lib/teacher/select-class";
import { AssignDailyFive } from "@/components/teacher/assign-daily-five";
import { ClassWeaknesses } from "@/components/teacher/class-weaknesses";

describe("selectClass", () => {
  const classes = [{ id: "a" }, { id: "b" }];

  it("picks the requested class when it is one of the teacher's", () => {
    expect(selectClass(classes, "b")).toEqual({ id: "b" });
  });

  it("falls back to the first class for a missing or foreign id", () => {
    expect(selectClass(classes, undefined)).toEqual({ id: "a" });
    expect(selectClass(classes, "someone-elses-class")).toEqual({ id: "a" });
  });

  it("returns null when there are no classes", () => {
    expect(selectClass([], "a")).toBeNull();
  });
});

describe("ClassWeaknesses", () => {
  it("says it is not built yet and shows no numbers when it has no rows", () => {
    const { container } = render(<ClassWeaknesses items={[]} />);
    expect(screen.getByText(/Not built yet/)).toBeInTheDocument();
    expect(screen.getByText("No data yet")).toBeInTheDocument();
    expect(container.textContent).not.toMatch(/\d+%/);
  });

  it("renders a row per unit when given data", () => {
    render(
      <ClassWeaknesses
        items={[{ unitId: "u1", unitName: "Limits and Continuity", classAccuracyPercent: 54, studentsBelowProficient: 7, studentsTried: 12 }]}
      />,
    );
    expect(screen.getByText("Limits and Continuity")).toBeInTheDocument();
    expect(screen.getByText("54%")).toBeInTheDocument();
    expect(screen.getByText("7 of 12")).toBeInTheDocument();
  });
});

describe("AssignDailyFive", () => {
  it("is disabled and explains why", () => {
    render(<AssignDailyFive />);
    const button = screen.getByRole("button", { name: "Assign Daily 5 set" });
    expect(button).toBeDisabled();
    expect(button).toHaveAccessibleDescription(/Not built yet/);
  });
});
