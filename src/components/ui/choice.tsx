import * as React from "react"
import { Check, X } from "lucide-react"
import { Html } from "@/components/ui/html"

export type ChoiceState = "idle" | "correct" | "wrong"

// A bubble-sheet answer row. Three pieces:
//   ChoiceList   fieldset + legend around a set of rows (radio group)
//   Choice       an interactive row (native radio, so arrow keys work)
//   ChoiceRow    the same face with no input, for review screens
// Once an answer is revealed, rows take data-state="correct" | "wrong" and
// show an icon AND a word -- color is never the only signal.

export function ChoiceList({ legend, children }: { legend: string; children: React.ReactNode }) {
  return (
    <fieldset className="m-0 min-w-0 border-0 p-0">
      <legend className="sr-only">{legend}</legend>
      {children}
    </fieldset>
  )
}

interface FaceProps {
  label: string
  textHtml: string
  explanationHtml?: string
  revealed: boolean
  state: ChoiceState
  verdict?: string
  input?: React.ReactNode
}

function ChoiceFace({ label, textHtml, explanationHtml, revealed, state, verdict, input }: FaceProps) {
  const icon = state === "correct" ? <Check className="size-4" strokeWidth={2.5} aria-hidden /> : state === "wrong" ? <X className="size-4" strokeWidth={2.5} aria-hidden /> : null

  return (
    <>
      {input}
      <span className="sr-only">{label}.</span>
      <span className="choice-bubble" aria-hidden>
        {icon ?? label}
      </span>
      <span className="min-w-0">
        <Html html={textHtml} inline className={state === "correct" ? "font-semibold" : undefined} />
        {revealed && explanationHtml ? <Html html={explanationHtml} size="sm" className="mt-1.5 opacity-85" /> : null}
      </span>
      <span className="choice-verdict">{verdict}</span>
    </>
  )
}

function verdictFor(state: ChoiceState, override?: string) {
  if (override) return override
  return state === "correct" ? "Correct" : state === "wrong" ? "Your answer" : undefined
}

export function Choice({
  name,
  label,
  textHtml,
  explanationHtml,
  checked,
  disabled,
  revealed,
  state = "idle",
  verdict,
  onSelect,
}: {
  name: string
  label: string
  textHtml: string
  explanationHtml?: string
  checked: boolean
  disabled?: boolean
  revealed: boolean
  state?: ChoiceState
  verdict?: string
  onSelect: () => void
}) {
  return (
    <label className="choice" data-revealed={revealed} data-state={state}>
      <ChoiceFace
        label={label}
        textHtml={textHtml}
        explanationHtml={explanationHtml}
        revealed={revealed}
        state={state}
        verdict={verdictFor(state, verdict)}
        input={
          <input type="radio" name={name} value={label} checked={checked} disabled={disabled} onChange={onSelect} />
        }
      />
    </label>
  )
}

export function ChoiceRow({
  label,
  textHtml,
  explanationHtml,
  state = "idle",
  verdict,
}: {
  label: string
  textHtml: string
  explanationHtml?: string
  state?: ChoiceState
  verdict?: string
}) {
  return (
    <div className="choice cursor-default" data-revealed="true" data-state={state}>
      <ChoiceFace
        label={label}
        textHtml={textHtml}
        explanationHtml={explanationHtml}
        revealed
        state={state}
        verdict={verdictFor(state, verdict)}
      />
    </div>
  )
}
