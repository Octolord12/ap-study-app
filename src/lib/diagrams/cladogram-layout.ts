// Pure layout for the cladogram: a rectangular tree, left to right, every tip at the right edge. Branch lengths
// carry no meaning (a cladogram shows branching order, not time), so a node's x is just its depth.
import type { CladogramNode } from "@/lib/content/diagram-schema";

export interface CladogramDims {
  stem: number; // the short line in front of the root
  treeWidth: number; // root to tips
  rowHeight: number; // between tips
  marginTop: number;
  marginBottom: number;
  labelRoom: number; // right of the tips, for their names
}

export const CLADOGRAM_DIMS: CladogramDims = { stem: 28, treeWidth: 250, rowHeight: 30, marginTop: 28, marginBottom: 14, labelRoom: 170 };

// A trait label sits on its branch and is about 60px wide, so a level needs this much room or the label runs into
// the connector and the label of the next level. A deep tree (the six-animal vertebrate tree is five levels deep)
// is therefore drawn wider than the minimum treeWidth.
export const CLADOGRAM_LEVEL_WIDTH = 80;

// The room right of the tips follows the longest tip name (13px type, about 7.6px a character, plus the numbered
// circle's room), up to labelRoom. A tree of short names is not drawn with a wide empty margin, which on a phone
// would shrink the whole figure and its labels for nothing.
export const CLADOGRAM_CHAR_WIDTH = 7.6;

export interface PlacedNode {
  x: number;
  y: number;
  isTip: boolean;
  label?: string;
  mark?: string;
  trait?: string;
  branchFromX: number; // where the branch into this node starts (the parent's x, or the stem's start for the root)
}

export interface CladogramLayout {
  width: number;
  height: number;
  nodes: PlacedNode[];
  // vertical connectors, one per internal node: x from yTop to yBottom
  connectors: { x: number; yTop: number; yBottom: number }[];
}

export function tipCount(node: CladogramNode): number {
  return node.children?.length ? node.children.reduce((n, c) => n + tipCount(c), 0) : 1;
}

// Branches on the longest path from the root to a tip.
export function treeDepth(node: CladogramNode): number {
  return node.children?.length ? 1 + Math.max(...node.children.map(treeDepth)) : 0;
}

export function tipLabels(node: CladogramNode): string[] {
  return node.children?.length ? node.children.flatMap(tipLabels) : [node.label ?? ""];
}

export function layoutCladogram(root: CladogramNode, dims: CladogramDims = CLADOGRAM_DIMS): CladogramLayout {
  const depth = Math.max(1, treeDepth(root));
  const treeWidth = Math.max(dims.treeWidth, depth * CLADOGRAM_LEVEL_WIDTH);
  const rootX = dims.stem;
  const tipX = rootX + treeWidth;
  const longest = Math.max(0, ...tipLabels(root).map((l) => l.length));
  const labelRoom = Math.min(dims.labelRoom, Math.max(60, Math.ceil(longest * CLADOGRAM_CHAR_WIDTH) + 24));
  const nodes: PlacedNode[] = [];
  const connectors: CladogramLayout["connectors"] = [];
  let nextRow = 0;

  function place(node: CladogramNode, level: number, branchFromX: number): PlacedNode {
    const isTip = !node.children?.length;
    const x = isTip ? tipX : rootX + (level / depth) * treeWidth;
    let y: number;
    let placed: PlacedNode;
    if (isTip) {
      y = dims.marginTop + nextRow * dims.rowHeight;
      nextRow += 1;
      placed = { x, y, isTip, label: node.label, mark: node.mark, trait: node.trait, branchFromX };
    } else {
      const kids = node.children!.map((c) => place(c, level + 1, x));
      y = (kids[0].y + kids[kids.length - 1].y) / 2;
      connectors.push({ x, yTop: kids[0].y, yBottom: kids[kids.length - 1].y });
      placed = { x, y, isTip, mark: node.mark, trait: node.trait, branchFromX };
    }
    nodes.push(placed);
    return placed;
  }

  place(root, 0, 0);
  const rows = nextRow;
  return {
    width: tipX + labelRoom,
    height: dims.marginTop + (rows - 1) * dims.rowHeight + dims.marginBottom + 14,
    nodes,
    connectors,
  };
}
