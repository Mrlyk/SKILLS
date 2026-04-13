# Pattern Library

**This file defines the reusable visual patterns used by the diagram skill.**
The color palette defines *how things look*.
This pattern library defines *how ideas should be structured visually*.

Use these patterns to turn user intent into diagrams that feel editorial, calm, and article-ready.

## Core Principle

A good diagram should not merely display information.
It should make a claim obvious.

Choose a pattern based on the **argument** the diagram is making:

- Is this showing a sequence?
- A comparison?
- A system boundary?
- A loop?
- A branching decision?
- A layered architecture?
- A group overlap?
- Central coordination?

The wrong pattern makes the content feel busy even when the styling is correct.

## Pattern Selection Rules

Choose the pattern that best matches the user's explanatory intent.

| User Intent | Preferred Pattern |
|---|---|
| Explain a sequence of steps | Linear Workflow |
| Show retries, iteration, refinement | Feedback Loop Workflow |
| Show decisions or branching logic | Decision Tree / Branch Workflow |
| Compare before/after or old/new | Split Comparison |
| Show components inside systems | Grouped Architecture |
| Show layered stack or hierarchy | Layered Stack |
| Show shared responsibility or overlap | Venn / Overlap |
| Show one central concept with supporting ideas | Hub-and-Spoke |
| Show multiple workers operating in parallel | Parallel Fan-out / Fan-in |
| Explain a supporting fact or note | Callout Annotation |

### Pattern Priority Rule

When multiple patterns seem possible:
1. Prefer the pattern with the **clearest reading order**
2. Prefer the pattern with the **fewest crossing lines**
3. Prefer the pattern that supports the **main claim in one glance**
4. Prefer **comparison** over complicated topology when the core message is contrast
5. Prefer **grouped architecture** over workflow when containment matters more than time

## Universal Composition Rules

These rules apply to all patterns.

### 1. One dominant idea per diagram
A diagram should explain one main point.
Secondary details should support that point, not compete with it.

### 2. Reading order must be obvious
The viewer should know where to start and where to look next within 3 seconds.

Default reading directions:
- left to right for workflows and comparisons
- top to bottom for stacks and hierarchies
- outer to inner for containment diagrams

### 3. Keep hierarchy shallow
Prefer at most:
- 1 title level
- 1 section/group level
- 1 node level
- optional annotation level

Avoid deeply nested visual structures.

### 4. Use whitespace as structure
Spacing should separate groups before boxes do.

### 5. Use containers sparingly
Do not put every label in a box.
Use free-floating text when the relationship is already clear.

### 6. Reduce visual grammar before adding color
First solve layout, grouping, and connector logic.
Then add semantic color.

## Pattern 1: Linear Workflow

### Use When
- the process is mostly sequential
- each step leads to the next
- the key message is procedural flow

### Typical Examples
- prompt → retrieve → reason → answer
- gather context → take action → verify → done
- ingest → index → retrieve → generate

### Visual Structure
- one row or one column of nodes
- evenly spaced
- consistent connector style
- optional small labels over arrows

### SVG Layout Rules
- Use 3 to 7 major steps
- Equal spacing between nodes: 200px center-to-center horizontal, or 120px vertical
- Keep the main path perfectly straight (all nodes share the same y for horizontal, same x for vertical)
- Connectors are simple straight `<path>` elements: `M {x1} {y} L {x2} {y}`
- Start node at leftmost/topmost position

### Node Rules
- start node: Start/Trigger semantic type
- processing steps: AI/LLM or Primary/Neutral
- end node: End/Success

### Connector Rules
- primary flow only
- use optional arrow labels only when they clarify transformation

### Anti-Patterns
- too many side annotations
- mixing architecture grouping into a simple flow
- long paragraphs inside nodes

## Pattern 2: Feedback Loop Workflow

### Use When
- the process involves retry, refinement, evaluation, or iteration
- the key message is that work loops until success criteria are met

### Typical Examples
- generate → evaluate → revise
- gather context → act → verify → retry
- agent loop with human steering

### Visual Structure
- one main forward path
- one loop-back connector
- optional external interrupt or override

### SVG Layout Rules
- Keep the main path straight (horizontal or vertical)
- Route the loop-back path **above or below** the main flow, never through nodes
- Feedback path uses a U-shape with 3-4 waypoints:
  ```
  M {end_x} {end_y}
  L {end_x} {loop_y}
  L {start_x} {loop_y}
  L {start_x} {start_y}
  ```
  Where `loop_y` is 60-80px above (or below) the main path
- Avoid multiple visible loops

### Connector Semantics
- forward path = solid primary
- retry loop = feedback connector
- human interrupt = dashed human-override connector

### Anti-Patterns
- multiple overlapping loopbacks
- loop connector passing through nodes
- showing every internal retry as a separate visible step

## Pattern 3: Branch Workflow / Decision Tree

### Use When
- a choice meaningfully changes the path
- the diagram needs to show approval, routing, or gating

### Typical Examples
- policy check → allow / deny
- retrieve enough context? yes / no
- task type → choose specialized agent

### Visual Structure
- one incoming path
- one decision node (diamond)
- 2 to 4 outgoing branches
- branches should be visually balanced

### SVG Layout Rules
- Decision diamond at the branching point, centered
- Branches fan out symmetrically (evenly spaced vertically or horizontally)
- Branch labels placed near the divergence point, as `<text>` elements offset 8-12px from the connector
- L-shape connectors from diamond to branch targets
- Rejoin branches with Z-shape connectors only if paths truly converge

### Node Rules
- decision nodes: diamond (rotated `<rect>`)
- do not use Decision styling for generic steps

### Connector Rules
- branch labels should be short: yes / no / low confidence / use tool
- keep branches separated with at least 80px whitespace

### Anti-Patterns
- more than 4 branches from one decision
- unlabeled branch semantics
- arbitrary diamonds everywhere

## Pattern 4: Parallel Fan-out / Fan-in

### Use When
- one task splits into multiple concurrent workers
- multiple results are aggregated into one outcome

### Typical Examples
- planner → multiple subagents → synthesizer
- query → parallel retrieval sources → ranker
- dispatcher → workers → reducer

### Visual Structure
- one source node
- 2 to 5 parallel branches
- one merge or synthesis node

### SVG Layout Rules
- Source node centered at left (or top)
- Parallel workers arranged in a vertical column (or horizontal row), evenly spaced at 100-120px apart
- Merge node centered at right (or bottom), aligned with source node
- Fan-out connectors: L-shape from source to each worker
- Fan-in connectors: L-shape from each worker to merge node
- All worker nodes should have identical width and height

### Semantic Rules
- worker nodes: AI/LLM or Secondary / Context depending on role
- merge node: Tertiary / Control

### Anti-Patterns
- uneven branch spacing
- showing too many workers (max 5)
- converging lines crossing each other

## Pattern 5: Split Comparison

### Use When
- the point is contrast between two states or approaches
- before/after or without/with AI is the main message

### Typical Examples
- before AI vs with AI
- prompt engineering vs context engineering
- baseline vs improved system

### Visual Structure
- two or three large side-by-side panels
- mirrored or comparable composition
- minimal connectors across panels

### SVG Layout Rules
- Panels as `<g>` groups with background `<rect>`, placed side by side
- Equal panel width: `(viewBox_width - 3 * margin) / 2` for two panels
- Panel gap: 30-40px between panels
- Panel titles centered within each panel
- Mirror internal layouts for easy visual comparison
- Optional divider line between panels: a vertical `<line>` with muted stroke

### Title Rules
- title should state the comparison claim, not just the categories

### Anti-Patterns
- unrelated layouts in each panel
- overusing arrows between panels
- too much text explaining what the eye should already see

## Pattern 6: Grouped Architecture

### Use When
- the main point is system boundaries, modules, resources, or containment
- components belong to subsystems more than they happen in time

### Typical Examples
- agent config + virtual machine
- application + tools + storage + runtime
- sandbox boundaries and policy layers

### Visual Structure
- large outer groups or panels
- smaller nodes inside groups
- connectors between components or between groups
- optional annotation callouts

### SVG Layout Rules
- Define container `<g>` groups first (background `<rect>` renders behind children)
- Place containers with 40-60px gap between them
- Internal nodes: 20-30px padding from container edges
- Use L-shape or Z-shape connectors between nodes across containers
- Orthogonal routing preferred: connectors exit at edge centers

### Grouping Rules
- use containers to indicate ownership or environment
- use softer grouping (dashed `<rect>`) for conceptual regions
- keep nesting shallow (max 3 levels)

### Anti-Patterns
- excessive nesting
- using workflow arrows when simple adjacency is enough
- putting every sentence inside a container

## Pattern 7: Layered Stack

### Use When
- the diagram explains hierarchy, dependency, or abstraction layers
- the order is vertical, not procedural

### Typical Examples
- model layer / orchestration layer / tool layer
- UI / services / storage
- policy / execution / filesystem

### Visual Structure
- stacked horizontal bands
- optional small dependencies between layers
- labels aligned consistently

### SVG Layout Rules
- Full-width horizontal `<rect>` bands stacked vertically
- Band height: 80-120px per layer
- Band gap: 10-20px between layers (or no gap for a tight stack)
- Layer labels centered or left-aligned within each band
- Optional downward arrows between layers using simple straight connectors
- Top layer = highest abstraction

### Anti-Patterns
- turning a stack into a workflow
- too many internal arrows
- inconsistent widths without semantic reason

## Pattern 8: Hub-and-Spoke

### Use When
- one central entity connects to several supporting concepts
- the point is central coordination, not sequence

### Typical Examples
- a central model using tools
- one orchestrator with multiple capabilities
- one concept with several implications

### Visual Structure
- one central dominant node
- 3 to 6 surrounding nodes
- minimal connector complexity

### SVG Layout Rules
- Central node at viewBox center, slightly larger than surrounding nodes (180x70 vs 140x60)
- Surrounding nodes arranged in a circle or semicircle around center
- For N spokes, position each at angle `i * (360/N)` degrees, radius 180-220px from center
- Calculate spoke positions: `x = cx + r * cos(angle)`, `y = cy + r * sin(angle)`
- Connectors: straight lines from center node edge to spoke node edge
- Preserve visual symmetry

### Anti-Patterns
- using hub-and-spoke for actual sequential workflows
- too many spokes (max 6)
- unequal visual weight making the composition drift

## Pattern 9: Venn / Overlap

### Use When
- the message is shared responsibility, convergence, or blended ownership
- overlap itself is the idea

### Typical Examples
- product / design / engineering overlap
- multiple disciplines converging under AI
- overlapping capability zones

### Visual Structure
- 2 or 3 overlapping circles or rounded rectangles
- labels placed in or near each region
- center overlap may carry emphasis if meaningful

### SVG Layout Rules
- Use `<circle>` or `<ellipse>` elements with `opacity="0.5"` or `fill-opacity="0.5"`
- For 2 circles: horizontal offset of about 60% of diameter so overlap is visible
- For 3 circles: arrange in a triangle pattern with pairwise overlaps
- Limit to 2-3 shapes maximum
- Label placement:
  - Unique regions: `<text>` positioned at the non-overlapping center of each shape
  - Overlap region: `<text>` centered in the intersection area
- Use semantic fill colors with reduced opacity for the shapes

### Anti-Patterns
- more than 3 overlapping groups
- forcing workflow semantics into overlap shapes
- too much text in intersections

## Pattern 10: Callout Annotation

### Use When
- one supporting fact or note clarifies a main diagram
- the annotation is helpful but not central to the structure

### Typical Examples
- "contents of skill directories live in the file system"
- "human can interrupt, steer, or add context"
- "policy layer enforces sandbox restrictions"

### Visual Structure
- small callout box outside the main flow
- one connector pointing to the referenced region
- minimal text

### SVG Layout Rules
- Callout box: small `<rect>` (200-280px wide, 40-60px tall) with Pill or Primary styling
- Position outside the main flow area, 40-60px away from the referenced element
- Connector: a dashed `<path>` with optional connector (no arrowhead, or use context arrow)
- Text: muted fill (#7A756E), font-size 13-14
- 1 to 3 callouts per diagram maximum

### Anti-Patterns
- too many callouts
- callouts becoming the dominant content
- crossing callout connectors over main structure

## Pattern Combination Rules

Patterns can be combined, but only when one pattern is clearly primary.

### Good Combinations
- Grouped Architecture + Callout Annotation
- Linear Workflow + Feedback Loop
- Split Comparison + Simple Workflow
- Parallel Fan-out / Fan-in + Grouped Architecture
- Hub-and-Spoke + Callout Annotation

### Risky Combinations
- Split Comparison + Architecture + Workflow all together
- Venn + Workflow
- Layered Stack + Branch Tree + Fan-out all together

### Combination Rule
If combining patterns increases cognitive load more than it increases explanatory value, split into two diagrams instead.

## Density Guidelines

### Simple
- 3-5 nodes
- 1 primary pattern
- almost no annotations

### Medium
- 6-12 nodes
- 1 primary pattern
- 1 secondary pattern allowed
- 1-3 callouts

### Dense
- 12-20 nodes
- only when architecture or sequence genuinely requires it
- strong grouping required
- must preserve obvious reading order

### Hard Limit Guidance
A single editorial diagram should usually avoid:
- more than 20 visible nodes
- more than 4 semantic colors
- more than 3 nested group levels
- more than 2 visible loopbacks
- more than 5 parallel branches

## Node Content Rules

### Labels
- keep labels short (2-4 words)
- prefer nouns or verb phrases
- avoid full-sentence labels inside nodes
- if a label must wrap, use `<tspan>` elements with `dy` spacing

### Good Examples
- Gather context
- Verify results
- Retrieved docs
- Policy layer
- Remote MCP server

### Weak Examples
- This stage is where the system gathers context from different sources
- Use the tool when it is appropriate and then maybe verify output

## Connector Grammar

Use connectors consistently to preserve meaning.

| Connector Style | Meaning |
|---|---|
| Solid | primary path |
| Dashed | optional, inferred, soft relationship, human-overridable |
| U-shape return | feedback loop |
| L-shape / Z-shape | structured orthogonal connection |
| Straight | simple step progression or hub-spoke |
| No arrowhead | grouping, alignment, weak association |

### Connector Routing in SVG

All connectors are `<path>` elements. Three routing strategies:

**Straight**: when source and target are aligned
```xml
<path d="M {x1} {y1} L {x2} {y2}" .../>
```

**L-shape** (one turn): for adjacent-row or adjacent-column connections
```xml
<path d="M {x1} {y1} L {turn_x} {y1} L {turn_x} {y2}" .../>
```

**Z-shape** (two turns): for connections that need to bridge horizontal and vertical gaps
```xml
<path d="M {x1} {y1} L {mid_x} {y1} L {mid_x} {y2} L {x2} {y2}" .../>
```

### Connector Anti-Overlap Rules

These are the most important rules for readable diagrams:

1. **Port distribution**: Before routing any connector, assign exit/entry ports for all connectors on each node. No two connectors may use the same port on the same node. If forced, use the top or bottom port as overflow.
2. **Corridor separation**: When multiple connectors share a horizontal or vertical path segment, offset each by 12px. Never let two connectors run on the exact same line.
3. **Crossing bridges**: When two connectors cross, the lower-priority connector gets a small 8px-radius arc at the crossing point.
4. **Planning order**: Route the main flow path first. Then route secondary connectors, adjusting ports and offsets to avoid the main path.

### General Connector Rules
- Layout first, connect second
- Minimize crossings
- Label connectors only when the transformation is important
- Keep at least 20px clearance between connectors and unrelated nodes

## Choosing Between Workflow and Architecture

This is the most common mistake.

Choose **Workflow** when:
- time/order is the main message
- the viewer should understand what happens next

Choose **Architecture** when:
- containment/boundary is the main message
- the viewer should understand what belongs where

Choose **Comparison** when:
- the core message is "this structure changed"

## Visual Review Checklist

Before finalizing, verify:

### Argument
- Can the main point be understood in one sentence?
- Does the chosen pattern support that point?

### Reading Order
- Is the start obvious?
- Is the main path visually dominant?
- Are groups clear before the viewer reads labels?

### Density
- Are there too many nodes?
- Are there too many accents?
- Can any labels become free text instead of boxes?

### Connectors
- Are any connectors overlapping? (Most critical check — see anti-overlap rules in SKILL.md)
- Has each node's ports been distributed so no two connectors exit/enter the same port?
- Are parallel connectors offset by at least 12px from each other?
- Do unavoidable crossings have bridge arcs?
- Are all connectors perpendicular to node edges at both ends (>= 20px stub/approach)?
- Any crossings that can be removed by rerouting?
- Any loopbacks that can be simplified?
- Are dashed lines used sparingly?

### Balance
- Does the composition feel centered and stable?
- Is whitespace distributed intentionally?
- Is there one focal point rather than many?

## Pattern Fallback Rules

When the structure is ambiguous:

1. default to **Linear Workflow** for process-like user input
2. default to **Grouped Architecture** for system/component descriptions
3. default to **Split Comparison** for before/after content
4. default to **Callout Annotation** rather than adding extra nodes
5. split into multiple diagrams rather than forcing a hybrid

## Output Planning Template

Before rendering, the system should internally identify:

- **main claim**
- **primary pattern**
- **secondary pattern** if any
- **reading direction**
- **main flow**
- **semantic node types**
- **groups/panels**
- **required annotations**

Example:

- main claim: Agent skills extend model capability through a runtime environment
- primary pattern: Grouped Architecture
- secondary pattern: Callout Annotation
- reading direction: left to right
- main flow: configuration → runtime execution
- groups: agent configuration, virtual machine, remote servers
- annotations: skill directories live in filesystem

## Non-Goals

Do not use this pattern library to create:
- dense UML-style enterprise diagrams
- BPMN-heavy process charts
- dashboard-like product graphics
- decorative posters with no explanatory structure
- deeply technical notation unless the user explicitly asks for it
