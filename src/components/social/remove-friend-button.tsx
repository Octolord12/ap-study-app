import { TwoStepButton } from "@/components/social/two-step-button";

interface RemoveFriendButtonProps {
  username: string;
  action: () => Promise<unknown>;
}

export function RemoveFriendButton({ username, action }: RemoveFriendButtonProps) {
  return (
    <TwoStepButton
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
