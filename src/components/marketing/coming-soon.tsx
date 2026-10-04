import { RuledList, Section } from "@/components/ui/page";
import { WaitlistForm } from "@/components/marketing/waitlist-form";

// Subjects we would like to add. Not built, no dates promised; edit freely.
const PLANNED_SUBJECTS = ["AP U.S. History", "AP Biology", "AP Calculus BC"];

export function ComingSoon() {
  return (
    <Section label="What's next" note="Not built yet. No dates promised.">
      <div className="grid gap-x-12 gap-y-8 lg:grid-cols-[minmax(0,1fr)_minmax(0,1.1fr)]">
        <div>
          <p className="reading max-w-[46ch]">The four exams above are what&apos;s here today. These are the subjects we want to add next.</p>
          <RuledList className="mt-4 max-w-sm">
            {PLANNED_SUBJECTS.map((subject) => (
              <li key={subject} className="flex items-baseline justify-between gap-4 py-3">
                <span className="heading text-lg">{subject}</span>
                <span className="eyebrow">Planned</span>
              </li>
            ))}
          </RuledList>
        </div>
        <WaitlistForm />
      </div>
    </Section>
  );
}
