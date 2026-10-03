import { cn } from "cn"

// Renders HTML produced by renderContentToHtml. The HTML is only ever built
// from our own authored content (never end-user input), so
// dangerouslySetInnerHTML doesn't open an XSS hole.
//   block (default): stems, explanations, FRQ prompts -- full prose styling.
//   inline: answer-choice text, which sits beside its letter on one line; the
//     renderer always wraps text in a block <p>, so flatten it.
export function Html({
  html,
  size = "base",
  inline = false,
  className,
}: {
  html: string
  size?: "base" | "sm"
  inline?: boolean
  className?: string
}) {
  return (
    <div
      className={cn(
        "reading",
        inline ? "[&_p]:m-0 [&_p]:inline" : "prose max-w-none",
        size === "sm" && "reading-sm",
        className
      )}
      dangerouslySetInnerHTML={{ __html: html }}
    />
  )
}
