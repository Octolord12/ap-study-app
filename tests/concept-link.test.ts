import { describe, expect, it } from "vitest";
import { topicHref, topicKey } from "@/lib/study/concept-link";

describe("topicHref", () => {
  it("goes to the refresher page when the topic has one", () => {
    expect(topicHref("ap-calc", "unit-3-x", "chain-rule", true)).toBe("/courses/ap-calc/units/unit-3-x/topics/chain-rule");
  });

  it("keeps the unit's filtered question list when it does not", () => {
    expect(topicHref("ap-calc", "unit-3-x", "chain-rule", false)).toBe("/courses/ap-calc/units/unit-3-x?topic=chain-rule");
  });
});

describe("topicKey", () => {
  it("is the same unit/topic key the content files and conceptLink use", () => {
    expect(topicKey("unit-3-x", "chain-rule")).toBe("unit-3-x/chain-rule");
  });
});
