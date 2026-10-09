import { ConfirmRemoveButton } from "@/components/social/confirm-remove-button";

interface RemoveFriendButtonProps {
  username: string;
  action: () => Promise<unknown>;
}

export function RemoveFriendButton({ username, action }: RemoveFriendButtonProps) {
  return (
    <ConfirmRemoveButton
      label={`Remove ${username} from your friends`}
      question={
        <>
          Remove <span className="font-mono">{username}</span> from your friends? To add them again you would send a new request.
        </>
      }
      action={action}
    />
  );
}
