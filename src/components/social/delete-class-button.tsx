import { TwoStepButton } from "@/components/social/two-step-button";

interface DeleteClassButtonProps {
  name: string;
  memberCount: number;
  action: () => Promise<unknown>;
}

export function DeleteClassButton({ name, memberCount, action }: DeleteClassButtonProps) {
  const others = memberCount - 1;
  const whoLoses = others <= 0 ? "You lose" : others === 1 ? "The 1 other person in it loses" : `The ${others} other people in it lose`;
  return (
    <TwoStepButton
      label={`Delete the class ${name}`}
      trigger="Delete class"
      confirm="Yes, delete it"
      working="Deleting…"
      failure="Could not delete the class. Nothing was changed; try again."
      question={
        <>
          Delete <span className="font-semibold">{name}</span>? {whoLoses} the class and its leaderboard. Nobody&apos;s
          answers or XP are touched. This cannot be undone; a new class would need a new invite code.
        </>
      }
      action={action}
    />
  );
}
