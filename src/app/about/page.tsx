import type { Metadata } from "next";
import Link from "next/link";
import { getDb } from "@/lib/db";
import { MINIMUM_AGE } from "@/lib/age";
import { feedbackMailto } from "@/lib/site-contact";
import { SOCIAL_SAFETY_NOTE } from "@/lib/social/copy";
import { listCourses } from "@/lib/study/queries";
import { Page, PageHeader, Section } from "@/components/ui/page";

export const metadata: Metadata = { title: "About and FAQ" };

const LINK = "font-semibold underline underline-offset-4 hover:bg-mark hover:text-on-mark hover:no-underline";

function list(names: string[]): string {
  if (names.length <= 1) return names.join("");
  return `${names.slice(0, -1).join(", ")} and ${names[names.length - 1]}`;
}

// Every answer here has to stay true. The review count is read from the database, so
// it changes by itself if content is ever approved in /admin/review; nothing about
// price is stated on purpose (the owner chose not to say yet); the builder is
// described, not named (also the owner's choice).
export default async function AboutPage() {
  const db = getDb();
  const [courses, questions, reviewedQuestions, prompts, reviewedPrompts, refreshers, reviewedRefreshers] = await Promise.all([
    listCourses(),
    db.question.count(),
    db.question.count({ where: { reviewed: true } }),
    db.fRQPrompt.count(),
    db.fRQPrompt.count({ where: { reviewed: true } }),
    db.topic.count({ where: { refresher: { not: null } } }),
    db.topic.count({ where: { refresher: { not: null }, refresherReviewed: true } }),
  ]);
  // The refreshers are written with AI help like the questions, so they are counted the same way.
  const total = questions + prompts + refreshers;
  const reviewed = reviewedQuestions + reviewedPrompts + reviewedRefreshers;

  return (
    <Page>
      <PageHeader eyebrow="About" title="About and FAQ" description="What this is, who it's for, and the questions parents and students ask first." />

      <Section label="What it is">
        <p className="reading max-w-[64ch]">
          AP Study App is a practice site for {list(courses.map((c) => c.name))}. You answer a question, then read why every choice is right or
          wrong, not only the one you picked. It also has a daily set of five, timed practice exams, free-response practice, and boss
          battles at the end of each unit.
        </p>
      </Section>

      <Section label="Who built it">
        <p className="reading max-w-[64ch]">Built by one person for students preparing for AP exams.</p>
      </Section>

      <Section label="The questions">
        <div className="reading max-w-[64ch] space-y-3">
          <p>
            The questions, answers, explanations and topic refreshers were written with the help of AI. For math and physics, the calculated answers were checked with
            software.
          </p>
          <p>
            {reviewed === 0
              ? "None of them has been checked by a teacher yet, so some may contain mistakes."
              : reviewed >= total
                ? `All ${total.toLocaleString("en-US")} have been checked by a person. A check is not a guarantee, so a mistake can still get through.`
                : `${reviewed.toLocaleString("en-US")} of ${total.toLocaleString("en-US")} have been checked by a person. The rest have not, so some may contain mistakes.`}{" "}
            They are practice questions in the style of the exams. They are not College Board questions, and College Board has not reviewed them.
          </p>
          <p>
            Found a mistake? Every question has a &ldquo;Report a problem&rdquo; link that says which one it is. Or{" "}
            <a href={feedbackMailto()} className={LINK}>
              send a suggestion
            </a>
            .
          </p>
        </div>
      </Section>

      <Section label="Safety">
        <div className="reading max-w-[64ch] space-y-3">
          <p>The site is for people who are {MINIMUM_AGE} or older, and signing up asks you to confirm that.</p>
          <p>
            Friends and classes are optional. {SOCIAL_SAFETY_NOTE} Leaderboards show a username and XP, and anyone can leave them in Settings.
          </p>
        </div>
      </Section>

      <Section label="Data">
        <p className="reading max-w-[64ch]">
          We keep the account details a student gives us and their study activity. We don&apos;t run ads or tracking scripts and we don&apos;t sell
          information. Everything, including how to delete an account, is on the{" "}
          <Link href="/privacy" className={LINK}>
            Privacy page
          </Link>
          .
        </p>
      </Section>

      <Section label="Progress">
        <p className="reading max-w-[64ch]">
          The Progress page shows days studied, questions answered, accuracy by unit, the topics a student finds hardest, and the time spent
          answering. There is no separate parent account yet, so the easiest way to see it is to look at it together.
        </p>
      </Section>

      <Section label="Exam scores">
        <p className="reading max-w-[64ch]">
          The score range after a practice exam is a rough guide from multiple-choice accuracy alone. It is not a prediction of the real score. The
          results page also shows which units lost the most points, with a quiz of exactly the questions that were missed.
        </p>
      </Section>
    </Page>
  );
}
