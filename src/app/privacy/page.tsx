import type { Metadata } from "next";
import { MINIMUM_AGE } from "@/lib/age";
import { privacyMailto } from "@/lib/site-contact";
import { Page, PageHeader, Section } from "@/components/ui/page";

export const metadata: Metadata = { title: "Privacy" };

// Every statement here has to stay true of the code. tests/privacy-page.test.tsx
// ties the cookie name to the code and fails if an analytics package is added;
// if you add tracking, a new cookie, or a new kind of stored data, update this.
const UPDATED = "October 5, 2026";

function Points({ items }: { items: React.ReactNode[] }) {
  return (
    <ul className="grid max-w-[64ch] gap-3">
      {items.map((item, i) => (
        <li key={i} className="reading relative pl-6 text-[1.0625rem]">
          <span aria-hidden className="absolute top-[0.6em] left-0 size-2.5 rounded-full border-[1.5px] border-foreground" />
          {item}
        </li>
      ))}
    </ul>
  );
}

export default function PrivacyPage() {
  return (
    <Page>
      <PageHeader
        eyebrow="Privacy"
        title="What this site keeps"
        description={`What we collect, who can see it, and how to ask about it. Last updated ${UPDATED}.`}
      />

      <Section label="Who it's for">
        <p className="reading max-w-[64ch]">
          This site is for people who are {MINIMUM_AGE} or older, and signing up asks you to confirm that. We don&apos;t ask for your birth
          date, and we don&apos;t knowingly keep information about anyone under {MINIMUM_AGE}. If you think someone under {MINIMUM_AGE} has an
          account or is on the waitlist, write to us and we will delete it.
        </p>
      </Section>

      <Section label="What we collect">
        <Points
          items={[
            "When you sign up: your name, a username, your email address and a password. The password is stored only as a salted hash, so nobody can read it.",
            "As you study: the questions you answer and the choice you made, how long each answer took, and your XP, level, streak, badges, boss battle results and timed exams.",
            "Free-response work: the answers you type and the points you give yourself.",
            "If you ask to reset your password: your email address is used to send you a one-time link that works for an hour. We keep only a fingerprint of the link's code, not the code, and that record goes away with your account. We also email you when your password changes.",
            "If you set an exam date for a course: that date.",
            "If you use friends or classes: who your friends are, and the classes you created or joined.",
            "If you join the waitlist: your email address, and nothing else. It is used once, to tell you when a new subject is ready.",
            "Our host keeps ordinary server logs, which include things like your IP address and the pages you request.",
          ]}
        />
      </Section>

      <Section label="Who can see it">
        <Points
          items={[
            "Other students see your username, and your XP on leaderboards. They never see your name or your email.",
            "Friends see your username. Members of a class, including its owner, see the usernames of the class's members.",
            "You can leave leaderboards in Settings. That removes you from them completely.",
            "Your answers and your free-response work are private to your account.",
            "Our email service, Resend, handles the message when we send you a password reset link or a notice that your password changed.",
            "The person who runs this site can read the database.",
          ]}
        />
      </Section>

      <Section label="What we don't do">
        <Points items={["We don't run ads, we don't use analytics or tracking scripts, and we don't sell your information."]} />
      </Section>

      <Section label="Cookies and storage">
        <Points
          items={[
            "A sign-in cookie keeps you logged in. It is removed when you log out.",
            <>
              A cookie named <code>ap-cram</code> is set only if you turn on Cram Mode. It lasts 7 days and holds your account ID, so a
              different student on the same device does not get your setting.
            </>,
            "Your browser's local storage remembers your light or dark choice and whether sound is muted. During a timed exam it also keeps your answers, so a reload doesn't lose them; they are removed when you submit. These stay on your device.",
          ]}
        />
      </Section>

      <Section label="Where it is stored">
        <p className="reading max-w-[64ch]">
          Account and study data live in a database hosted by Neon in the United States. The site itself runs on Vercel.
        </p>
      </Section>

      <Section label="Your choices">
        <Points
          items={[
            "Leave leaderboards in Settings. Sound and dark mode are in the account menu. You can log out at any time.",
            "Change your password, or delete your account and everything tied to it, in Settings. To see what we hold about you, have it corrected, or be removed from the waitlist without an account, write to us.",
          ]}
        />
        <p className="reading mt-6 max-w-[64ch]">
          <a
            href={privacyMailto()}
            className="font-semibold underline underline-offset-4 hover:bg-mark hover:text-on-mark hover:no-underline"
          >
            Write to us about privacy
          </a>
        </p>
      </Section>
    </Page>
  );
}
