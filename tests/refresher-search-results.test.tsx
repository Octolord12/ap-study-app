import { render, screen, within } from "@testing-library/react";
import { describe, expect, it } from "vitest";
import { RefresherSearchForm } from "@/components/study/refresher-search-form";
import { RefresherSearchResults } from "@/components/study/refresher-search-results";
import type { RefresherHit } from "@/lib/study/refresher-search";

const hit = (over: Partial<RefresherHit> = {}): RefresherHit => ({
  topicName: "Mean Value Theorem",
  topicSlug: "mean-value-theorem",
  unitSlug: "unit-5",
  unitName: "Analytical Applications",
  unitNumber: 5,
  inName: true,
  snippet: "…the mean value idea says some point has the average rate…",
  ...over,
});

describe("RefresherSearchResults", () => {
  it("asks for a query when there is none, with the allowed length", () => {
    render(<RefresherSearchResults courseSlug="ap-calc" query={null} hits={null} />);
    expect(screen.getByText(/Type 2 to 60 characters/)).toBeTruthy();
  });

  it("says plainly when nothing matches, quoting the query", () => {
    render(<RefresherSearchResults courseSlug="ap-calc" query="zebra" hits={[]} />);
    expect(screen.getByText(/No refresher mentions/).textContent).toContain("zebra");
  });

  it("links each result to its topic page and shows the unit it belongs to", () => {
    render(<RefresherSearchResults courseSlug="ap-calc" query="mean value" hits={[hit()]} />);
    const link = screen.getByRole("link");
    expect(link.getAttribute("href")).toBe("/courses/ap-calc/units/unit-5/topics/mean-value-theorem");
    expect(link.textContent).toContain("Unit 5 · Analytical Applications");
  });

  it("highlights the matched words in the title and the snippet, keeping their own capitalization", () => {
    render(<RefresherSearchResults courseSlug="ap-calc" query="mean value" hits={[hit()]} />);
    const marks = [...document.querySelectorAll("mark")].map((m) => m.textContent);
    expect(marks).toEqual(["Mean Value", "mean value"]);
  });

  it("counts the topics, and says when the list was cut", () => {
    const { unmount } = render(<RefresherSearchResults courseSlug="ap-calc" query="x" hits={[hit(), hit({ topicSlug: "b" })]} />);
    expect(screen.getByRole("status").textContent).toBe("2 topics");
    unmount();
    render(<RefresherSearchResults courseSlug="ap-calc" query="x" hits={[hit()]} />);
    expect(screen.getByRole("status").textContent).toBe("1 topic");
  });

  it("shows text from a refresher as text: markup in it is not interpreted", () => {
    const evil = hit({ snippet: '<img src=x onerror="alert(1)"> mean value <script>alert(2)</script>', topicName: "<b>Bold</b> mean value" });
    const { container } = render(<RefresherSearchResults courseSlug="ap-calc" query="mean value" hits={[evil]} />);
    expect(container.querySelector("img")).toBeNull();
    expect(container.querySelector("script")).toBeNull();
    expect(container.querySelector("b")).toBeNull();
    expect(container.textContent).toContain('<img src=x onerror="alert(1)">');
  });
});

describe("RefresherSearchForm", () => {
  it("is a plain GET form to this course's search page, so it works without JavaScript", () => {
    render(<RefresherSearchForm courseSlug="ap-calc" />);
    const form = screen.getByRole("search");
    expect(form.getAttribute("method")).toBe("get");
    expect(form.getAttribute("action")).toBe("/courses/ap-calc/search");
    expect(within(form).getByRole("searchbox").getAttribute("name")).toBe("q");
  });

  it("limits the query to the lengths the server enforces, and refills the box", () => {
    render(<RefresherSearchForm courseSlug="ap-calc" query="mean value" />);
    const box = screen.getByRole("searchbox") as HTMLInputElement;
    expect(box.minLength).toBe(2);
    expect(box.maxLength).toBe(60);
    expect(box.required).toBe(true);
    expect(box.value).toBe("mean value");
  });
});
