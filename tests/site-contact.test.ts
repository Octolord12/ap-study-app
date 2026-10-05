import { describe, expect, it } from "vitest";
import { feedbackMailto, privacyMailto, reportMailto } from "@/lib/site-contact";

function parts(url: string) {
  const [scheme, rest] = url.split(":");
  const [address, query] = rest.split("?");
  const params = new URLSearchParams(query);
  return { scheme, address, subject: params.get("subject"), body: params.get("body"), query };
}

describe("contact links", () => {
  it("open a mail message addressed to the contact, with a subject and a prompt", () => {
    const f = parts(feedbackMailto());
    expect(f.scheme).toBe("mailto");
    expect(f.address).toBe("virajrpoddar@gmail.com");
    expect(f.subject).toBe("AP Study App: mistake or suggestion");
    expect(f.body).toContain("What did you find, or what would you like to see?");
    expect(f.body).toContain("Where was it? (course, unit, question)");
  });

  it("uses a separate subject for privacy questions", () => {
    const p = parts(privacyMailto());
    expect(p.address).toBe("virajrpoddar@gmail.com");
    expect(p.subject).toBe("AP Study App: privacy question");
  });

  it("encodes spaces as %20, not '+', which mail apps would show as a literal plus", () => {
    for (const url of [feedbackMailto(), privacyMailto()]) {
      expect(parts(url).query).not.toContain("+");
      expect(parts(url).query).toContain("%20");
    }
  });
});

describe("per-item report link", () => {
  it("puts the question's id in the subject and the body, so the report says which one", () => {
    const r = parts(reportMailto("question", "ap-calc-u1-mcq-4"));
    expect(r.address).toBe("virajrpoddar@gmail.com");
    expect(r.subject).toBe("AP Study App: problem with question ap-calc-u1-mcq-4");
    expect(r.body).toContain("Question ID: ap-calc-u1-mcq-4");
  });

  it("works for free-response prompts too", () => {
    const r = parts(reportMailto("free-response prompt", "ap-calc-u1-frq-1"));
    expect(r.subject).toBe("AP Study App: problem with free-response prompt ap-calc-u1-frq-1");
    expect(r.body).toContain("Prompt ID: ap-calc-u1-frq-1");
  });

  it("encodes spaces as %20", () => {
    expect(parts(reportMailto("question", "x")).query).not.toContain("+");
  });
});
