import { cn } from "cn";

// One tick per question, like the answer sheet's numbered rows: done are
// filled, the current one is highlighted, the rest are empty. It shows where
// you are, never how you're doing.
export function QuizProgress({ total, current, className }: { total: number; current: number; className?: string }) {
  return (
    <span role="img" aria-label={`Question ${current + 1} of ${total}`} className={cn("flex max-w-40 flex-wrap gap-1", className)}>
      {Array.from({ length: total }, (_, i) => (
        <i
          key={i}
          aria-hidden
          className={cn(
            "block size-2.5 border-[1.5px] border-foreground",
            i < current && "bg-foreground",
            i === current && "bg-mark"
          )}
        />
      ))}
    </span>
  );
}
