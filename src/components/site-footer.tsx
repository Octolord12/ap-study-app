// TODO(owner): confirm this wording before launch. It states the facts we
// can stand behind (no affiliation, content not reviewed by College Board)
// and nothing about review status of our own content.
export function SiteFooter() {
  return (
    <footer className="border-t border-border">
      <div className="mx-auto w-full max-w-[67.5rem] px-4 py-6 sm:px-6">
        <p className="max-w-[70ch] text-xs leading-relaxed text-muted-foreground">
          AP® and Advanced Placement® are registered trademarks of College Board, which is not affiliated with this site
          and does not endorse it. Questions here are written for practice and have not been reviewed by College Board.
        </p>
      </div>
    </footer>
  );
}
