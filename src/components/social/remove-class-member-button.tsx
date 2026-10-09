import { ConfirmRemoveButton } from "@/components/social/confirm-remove-button";

interface RemoveClassMemberButtonProps {
  username: string;
  action: () => Promise<unknown>;
}

export function RemoveClassMemberButton({ username, action }: RemoveClassMemberButtonProps) {
  return (
    <ConfirmRemoveButton
      label={`Remove ${username} from this class`}
      question={
        <>
          Remove <span className="font-mono">{username}</span> from this class? They would no longer see it or appear on its leaderboard, but anyone with the invite code can
          join again.
        </>
      }
      action={action}
    />
  );
}
