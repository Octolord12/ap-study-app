import { Button } from "@/components/ui/button";
import { Field } from "@/components/ui/field";
import { Input } from "@/components/ui/input";
import { MAX_QUERY_LENGTH, MIN_QUERY_LENGTH } from "@/lib/study/refresher-search";

// A plain GET form (works without JavaScript); the results page reads the query from the URL.
export function RefresherSearchForm({ courseSlug, query }: { courseSlug: string; query?: string }) {
  return (
    <form action={`/courses/${courseSlug}/search`} method="get" role="search" className="flex max-w-md flex-wrap items-end gap-3">
      <Field id="q" label="Search the refreshers" hint="A topic, or a word from the notes." className="min-w-48 flex-1">
        <Input id="q" name="q" type="search" key={query ?? ""} defaultValue={query ?? ""} required minLength={MIN_QUERY_LENGTH} maxLength={MAX_QUERY_LENGTH} autoComplete="off" />
      </Field>
      <Button type="submit" size="lg">
        Search
      </Button>
    </form>
  );
}
