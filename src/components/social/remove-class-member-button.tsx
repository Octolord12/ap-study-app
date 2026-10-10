import { TwoStepButton } from "@/components/social/two-step-button";

interface RemoveClassMemberButtonProps {
  username: string;
  action: () => Promise<unknown>;
  blockAction: () => Promise<unknown>;
}

export function RemoveClassMemberButton({ username, action, blockAction }: RemoveClassMemberButtonProps) {
  return (
    <TwoStepButton
      label={`Remove ${username} from this class`}
      question={
        <>
          Remove <span className="font-mono">{username}</span> from this class? They would no longer see it or appear on its leaderboard. &ldquo;Yes, remove&rdquo; lets
          them join again with the invite code; &ldquo;Remove and block&rdquo; does not.
        </>
      }
      action={action}
      alternate={{ confirm: "Remove and block", working: "Blocking…", action: blockAction }}
    />
  );
}
