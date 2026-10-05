import { describe, expect, it } from "vitest";
import { feedbackMailto, privacyMailto } from "@/lib/site-contact";

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
