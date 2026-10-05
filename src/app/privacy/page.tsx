import type { Metadata } from "next";
import { privacyMailto } from "@/lib/site-contact";
import { Page, PageHeader, Section } from "@/components/ui/page";

export const metadata: Metadata = { title: "Privacy" };

// Every statement here has to stay true of the code. tests/privacy-page.test.tsx
// ties the cookie name to the code and fails if an analytics package is added;
// if you add tracking, a new cookie, or a new kind of stored data, update this.
const UPDATED = "October 4, 2026";

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

      <Section label="What we collect">
        <Points
          items={[
            "When you sign up: your name, a username, your email address and a password. The password is stored only as a salted hash, so nobody can read it.",
            "As you study: the questions you answer and the choice you made, how long each answer took, and your XP, level, streak, badges, boss battle results and timed exams.",
            "Free-response work: the answers you type and the points you give yourself.",
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
            "Your browser's local storage remembers your light or dark choice and whether sound is muted. These stay on your device.",
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
            "To see what we hold about you, correct it, delete your account and its data, or be removed from the waitlist, write to us. There is no button for this yet, so it is done by request.",
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
