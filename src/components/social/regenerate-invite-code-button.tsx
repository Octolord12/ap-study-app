import { TwoStepButton } from "@/components/social/two-step-button";

interface RegenerateInviteCodeButtonProps {
  action: () => Promise<unknown>;
}

export function RegenerateInviteCodeButton({ action }: RegenerateInviteCodeButtonProps) {
  return (
    <TwoStepButton
      label="Make a new invite code for this class"
      trigger="New code"
      confirm="Yes, make a new code"
      working="Changing…"
      failure="Could not change the code. Nothing was changed; try again."
      question="Make a new invite code? The current one stops working right away, so anyone who has not joined yet will need the new one. People already in the class stay."
      action={action}
    />
  );
}
