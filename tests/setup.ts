import "@testing-library/jest-dom/vitest";
import { cleanup } from "@testing-library/react";
import { afterEach } from "vitest";

// vitest isn't running with globals, so Testing Library can't register its own
// cleanup; without this, every render() stays in the document for the rest of
// the file and getBy* queries start finding duplicates.
afterEach(() => cleanup());
