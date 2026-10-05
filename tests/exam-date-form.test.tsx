import { fireEvent, render, screen, waitFor } from "@testing-library/react";
import { beforeEach, describe, expect, it, vi } from "vitest";

const action = vi.hoisted(() => ({ setExamDate: vi.fn() }));
vi.mock("@/lib/study/exam-date-actions", () => action);

import { ExamDateForm } from "@/components/study/exam-date-form";

describe("ExamDateForm", () => {
  beforeEach(() => vi.clearAllMocks());

  it("starts empty, with a Save button and no Remove button", () => {
    render(<ExamDateForm courseId="c1" currentIso={null} />);
    expect((screen.getByLabelText("Exam date") as HTMLInputElement).value).toBe("");
    expect(screen.getByRole("button", { name: "Save date" })).toBeInTheDocument();
    expect(screen.queryByRole("button", { name: "Remove date" })).not.toBeInTheDocument();
  });

  it("shows the saved date and offers to change or remove it", () => {
    render(<ExamDateForm courseId="c1" currentIso="2027-05-03" />);
    expect((screen.getByLabelText("Exam date") as HTMLInputElement).value).toBe("2027-05-03");
    expect(screen.getByRole("button", { name: "Change date" })).toBeInTheDocument();
    expect(screen.getByRole("button", { name: "Remove date" })).toBeInTheDocument();
  });

  it("shows the server's error next to the field, and keeps what was typed", async () => {
    action.setExamDate.mockResolvedValue({ error: "That date has already passed." });
    render(<ExamDateForm courseId="c1" currentIso={null} />);
    fireEvent.change(screen.getByLabelText("Exam date"), { target: { value: "2020-01-01" } });
    fireEvent.submit(screen.getByLabelText("Exam date").closest("form")!);
    await waitFor(() => expect(screen.getByRole("alert")).toHaveTextContent("That date has already passed."));
  });

  it("confirms a save", async () => {
    action.setExamDate.mockResolvedValue({ message: "Saved." });
    render(<ExamDateForm courseId="c1" currentIso={null} />);
    fireEvent.change(screen.getByLabelText("Exam date"), { target: { value: "2027-05-03" } });
    fireEvent.submit(screen.getByLabelText("Exam date").closest("form")!);
    await waitFor(() => expect(screen.getByRole("status")).toHaveTextContent("Saved."));
  });

  it("removes the date through its own form, with the clear intent", async () => {
    action.setExamDate.mockResolvedValue({ message: "Date removed." });
    render(<ExamDateForm courseId="c1" currentIso="2027-05-03" />);
    fireEvent.submit(screen.getByRole("button", { name: "Remove date" }).closest("form")!);
    await waitFor(() => expect(action.setExamDate).toHaveBeenCalled());
    const [courseId, , data] = action.setExamDate.mock.calls[0] as [string, unknown, FormData];
    expect(courseId).toBe("c1");
    expect(data.get("intent")).toBe("clear");
  });
});
