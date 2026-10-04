import { Button } from "@/components/ui/button";

// The button is here so the layout is settled; it does nothing yet.
export function AssignDailyFive() {
  return (
    <div className="flex flex-wrap items-center justify-between gap-x-8 gap-y-4">
      <p id="assign-daily-five-note" className="reading max-w-[52ch]">
        Not built yet. Assigning will give everyone in the class the same five questions for the day.
      </p>
      <Button type="button" size="lg" variant="outline" disabled aria-describedby="assign-daily-five-note">
        Assign Daily 5 set
      </Button>
    </div>
  );
}
