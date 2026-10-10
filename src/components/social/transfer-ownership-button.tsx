import { TwoStepButton } from "@/components/social/two-step-button";

interface TransferOwnershipButtonProps {
  username: string;
  action: () => Promise<unknown>;
}

export function TransferOwnershipButton({ username, action }: TransferOwnershipButtonProps) {
  return (
    <TwoStepButton
      label={`Make ${username} the owner of this class`}
      trigger="Make owner"
      confirm="Yes, hand it over"
      working="Handing over…"
      failure="Could not hand the class over. Nothing was changed; try again."
      question={
        <>
          Make <span className="font-mono">{username}</span> the owner of this class? You become a regular member: you could no longer rename it, change its code, remove
          people or delete it. They could hand it back.
        </>
      }
      action={action}
    />
  );
}
