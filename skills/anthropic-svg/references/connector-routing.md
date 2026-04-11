# Connector Routing Rules

This file contains the detailed rules for routing SVG connectors to avoid overlaps, ensure perpendicular entry/exit, and maintain visual clarity. Read this file whenever you need to draw connectors between nodes.

## Table of Contents

- Rule 1: Port selection
- Rule 2: Parallel offset
- Rule 3: Crossover bridge
- Rule 4: Perpendicular entry and exit
- Connector path templates
- Waypoint calculation process

## Rule 1: Port selection (choose different exit/entry edges)

Each node has 4 connection ports: **top-center**, **right-center**, **bottom-center**, **left-center**.

**Port assignment process** — for each node, before drawing any connector:

1. List all connectors attached to this node (both outgoing and incoming).
2. Assign each connector to a different port. Prefer the port that faces the target/source node.
3. If two connectors would use the same port (e.g., two outgoing connectors both want to exit right), reassign one to an adjacent port (top or bottom).

**Port selection priority for outgoing connectors:**
- Target is to the right → exit **right**
- Target is below → exit **bottom**
- Target is above → exit **top**
- Target is to the left → exit **left**
- Target is in the same direction as another connector from this node → use **top** or **bottom** as alternate

**Port selection priority for incoming connectors:**
- Source is to the left → enter **left**
- Source is above → enter **top**
- Source is below → enter **bottom**
- Source is to the right → enter **right**

**Example — node A has 3 outgoing connections:**
```
A → B (B is to the right)     → exit A.right,  enter B.left
A → C (C is below-right)      → exit A.bottom, enter C.left
A → D (D is also to the right)→ exit A.top,    enter D.left  (A.right already taken)
```

This distributes connectors around the node perimeter, preventing them from merging into a single exit point.

## Rule 2: Parallel offset (spread lines that share a corridor)

When two or more connectors run through the same horizontal or vertical corridor (same direction, overlapping path segments), offset each subsequent connector by **12px** perpendicular to the flow direction.

**How to detect shared corridors:**
- Two horizontal segments are "shared" if their y-values are within 8px of each other and their x-ranges overlap
- Two vertical segments are "shared" if their x-values are within 8px of each other and their y-ranges overlap

**Offset assignment:**
- First connector: stays at the natural position (midpoint between nodes)
- Second connector: offset +12px
- Third connector: offset -12px
- Fourth connector: offset +24px
- Pattern: 0, +12, -12, +24, -24, ...

**Example — two connectors both route through the same vertical channel at x=400:**
```xml
<!-- Connector 1: uses x=400 (natural position) -->
<path d="M 300 200 L 400 200 L 400 350 L 500 350" .../>

<!-- Connector 2: offset to x=412 -->
<path d="M 300 220 L 412 220 L 412 380 L 500 380" .../>
```

**Practical application for Z-shape connectors:**
When multiple Z-shape connectors share the same middle vertical segment, spread them:
```
Connector 1: mid_x = 400
Connector 2: mid_x = 412
Connector 3: mid_x = 388
```

## Rule 3: Crossover bridge (visual indicator at crossing points)

When two connectors must cross (unavoidable after applying Rules 1 and 2), add a small arc "bridge" on one of the connectors at the crossing point. This makes it visually clear that the lines cross without connecting.

**Implementation:** Replace the straight segment at the crossing point with a small semicircular arc:

```xml
<!-- Before: straight line crossing at point (400, 300) -->
<path d="M 350 300 L 450 300" .../>

<!-- After: line with bridge arc at crossing point -->
<path d="M 350 300 L 392 300 A 8 8 0 0 1 408 300 L 450 300" .../>
```

The arc `A 8 8 0 0 1 {x+16} {y}` creates a small 8px-radius bump over the crossing. Rules:
- Arc radius: 8px
- The bridge goes on the connector that was drawn **later** (lower priority)
- Bridge direction: upward for horizontal lines (`0 0 1`), rightward for vertical lines
- For vertical line crossing a horizontal line:
  ```xml
  <path d="M 400 250 L 400 292 A 8 8 0 0 1 400 308 L 400 380" .../>
  ```

## Rule 4: Perpendicular entry and exit (mandatory)

**This rule is non-negotiable.** Every connector must leave a node perpendicular to the edge it exits from, and enter a node perpendicular to the edge it enters. The first segment after leaving a node and the last segment before entering a node must extend straight outward from the edge for at least 20px before making any turn.

**What this means for each port:**
- Exit **right** → first segment goes **horizontal right** (increasing x)
- Exit **left** → first segment goes **horizontal left** (decreasing x)
- Exit **top** → first segment goes **vertical up** (decreasing y)
- Exit **bottom** → first segment goes **vertical down** (increasing y)
- Enter **left** → last segment arrives **horizontal right** (increasing x, entering from left)
- Enter **right** → last segment arrives **horizontal left** (decreasing x, entering from right)
- Enter **top** → last segment arrives **vertical down** (increasing y, entering from top)
- Enter **bottom** → last segment arrives **vertical up** (decreasing y, entering from bottom)

**Common mistake:** A connector exits the bottom of node A and needs to reach the left of node B. The WRONG way is to draw a diagonal or to arrive at B's left edge with a vertical segment. The CORRECT way:

```
WRONG:  M 200 260 L 400 300              ← diagonal, not perpendicular at either end
WRONG:  M 200 260 L 400 260 L 400 300    ← exits bottom but immediately goes horizontal (not perpendicular to bottom edge)

RIGHT:  M 200 260 L 200 300 L 380 300    ← exits bottom vertically, then horizontal into B.left
```

**The stub rule:** After exiting a port, draw a straight stub of at least 20px in the perpendicular direction before making any turn. Before entering a port, the connector must approach straight for at least 20px.

```
Exit right port at (260, 180):
  First waypoint: (280, 180)    ← 20px horizontal stub rightward
  Then turn to next waypoint

Enter left port at (400, 300):
  Second-to-last waypoint: (380, 300)    ← approach from 20px to the left
  Last point: (400, 300)
```

## Connector path templates

All templates follow Rule 4 (perpendicular entry/exit). The stub segments ensure clean perpendicular connections at both ends.

**Straight connector** (source and target aligned on same axis):
```xml
<path d="M {x1} {y1} L {x2} {y2}" fill="none"
      stroke="#7A756E" stroke-width="1.8" marker-end="url(#arrow-primary)"/>
```

**L-shape connector** (one turn, perpendicular ports):
```xml
<!-- Exit right (horizontal stub), turn, enter top (vertical approach) -->
<path d="M {x1} {y1} L {x2} {y1} L {x2} {y2}" fill="none"
      stroke="#7A756E" stroke-width="1.8" marker-end="url(#arrow-primary)"/>
```

**Z-shape connector** (two turns, same-axis ports with offset):
```xml
<!-- Exit right (horizontal stub), vertical bridge, enter left (horizontal approach) -->
<path d="M {x1} {y1} L {mid_x} {y1} L {mid_x} {y2} L {x2} {y2}" fill="none"
      stroke="#7A756E" stroke-width="1.8" marker-end="url(#arrow-primary)"/>
```

**S-shape connector** (three turns, for cross-axis connections needing stubs at both ends):
```xml
<!-- Exit bottom (vertical stub), horizontal bridge, vertical bridge, enter left (horizontal approach) -->
<path d="M {x1} {y1} L {x1} {stub_y} L {mid_x} {stub_y} L {mid_x} {y2} L {x2} {y2}" fill="none"
      stroke="#7A756E" stroke-width="1.8" marker-end="url(#arrow-primary)"/>
```
Use S-shape when the exit port and entry port are on different axes (e.g., exit bottom, enter left) and a simple L-shape would violate the perpendicular rule.

**U-shape return connector** (feedback loop, 4 waypoints):
```xml
<!-- Exit bottom (vertical stub), horizontal return, enter top (vertical approach) -->
<path d="M {x1} {y1} L {x1} {loop_y} L {x2} {loop_y} L {x2} {y2}" fill="none"
      stroke="#8E8982" stroke-width="1.8" marker-end="url(#arrow-feedback)"/>
```

## Waypoint calculation process

Follow this process for every connector, in order:

1. **Identify source port and target port** using Rule 1 (port selection). Record exit coordinates `(x1, y1)` and entry coordinates `(x2, y2)`.
2. **Choose routing shape** based on port positions:
   - Same axis (both horizontal or both vertical) → straight line
   - Perpendicular (e.g., exit right, enter top) → L-shape
   - Same side but offset (e.g., exit right, enter left, different y) → Z-shape
   - Cross-axis with both stubs needed → S-shape
   - Return path (target is behind source) → U-shape
3. **Calculate mid-point for turns**: place the turn at the midpoint between source and target.
4. **Check for conflicts** with all previously planned connectors:
   - Shared corridor? → apply Rule 2 (parallel offset of 12px)
   - Crossing? → apply Rule 3 (add bridge arc)
5. **Clearance check**: ensure at least 20px gap between connector paths and unrelated nodes. If a path runs too close to a node, add an extra waypoint to route around it.
6. **Feedback loops**: route above or below the main flow path, using 3-4 waypoints to create a U-shape return path.
