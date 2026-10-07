// Where mistakes, suggestions and privacy questions go. The address is never
// printed on a page: the links below open the reader's mail app already
// addressed to it, with a subject and a prompt for what to write. (It is in the
// link's href, so it isn't hidden from someone who views the page source. A
// contact form would hide it, but needs an email service this app doesn't have.)
const CONTACT_EMAIL = "virajrpoddar@gmail.com";

// encodeURIComponent, not URLSearchParams: mail apps read "+" as a literal plus.
function mailto(subject: string, body: string): string {
  return `mailto:${CONTACT_EMAIL}?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
}

export function feedbackMailto(): string {
  return mailto(
    "AP Study App: mistake or suggestion",
    "What did you find, or what would you like to see?\n\n\nWhere was it? (course, unit, question)\n\n",
  );
}

export function privacyMailto(): string {
  return mailto("AP Study App: privacy question", "What would you like to ask or have changed?\n\n");
}

// A mistake report about one question or free-response prompt. The id is in the
// subject and the body so it is clear which one, without the student having to
// describe where it was; it contains nothing personal.
export function reportMailto(kind: "question" | "free-response prompt" | "refresher", id: string): string {
  return mailto(
    `AP Study App: problem with ${kind} ${id}`,
    `What is wrong with it?\n\n\n(Please leave the line below, it tells us which one.)\n${{ question: "Question", "free-response prompt": "Prompt", refresher: "Refresher" }[kind]} ID: ${id}\n`,
  );
}
