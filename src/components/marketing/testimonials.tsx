import type { Testimonial } from "@/lib/marketing/testimonials";
import { RuledList, Section } from "@/components/ui/page";

// Renders nothing until there is something real to show.
export function Testimonials({ items }: { items: Testimonial[] }) {
  if (items.length === 0) return null;

  return (
    <Section label="From students">
      <RuledList>
        {items.map((item) => (
          <li key={`${item.name}-${item.quote.slice(0, 24)}`} className="py-6">
            <figure>
              <blockquote className="reading max-w-[56ch] text-xl">&ldquo;{item.quote}&rdquo;</blockquote>
              <figcaption className="eyebrow mt-3">
                {item.name}
                {item.course ? ` · ${item.course}` : ""}
                {item.apScore ? ` · Scored ${item.apScore}` : ""}
              </figcaption>
            </figure>
          </li>
        ))}
      </RuledList>
    </Section>
  );
}
