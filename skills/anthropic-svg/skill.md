---
name: anthropic-svg
description: Generate editorial-style diagrams in the Anthropic blog visual style as SVG files. Use this skill whenever the user wants to create a diagram, flowchart, architecture diagram, comparison chart, or any visual that should look like Anthropic's blog article illustrations. Trigger on prompts like "draw a diagram", "create a flowchart", "visualize this process", "make an architecture diagram", "画流程图", "画架构图", "帮我画", or any request to turn text/process descriptions into a visual. This skill produces the calm, editorial, publication-quality look characteristic of Anthropic's technical blog.
---

# Anthropic-SVG Diagram Skill

Generate SVG diagrams that match the editorial, warm, minimalist visual style of Anthropic's blog article illustrations.

## Workflow

```
User text → DiagramSpec (written out as text) → Styled SVG → .svg file
```

## Step 1: Analyze the Request

Determine:
- **Main claim**: What is the one thing this diagram should make obvious?
- **Pattern**: Which visual pattern best serves that claim? (See Step 2 and `references/pattern-library.md`)
- **Reading direction**: left-to-right for workflows/comparisons; top-to-bottom for stacks/hierarchies

When uncertain about pattern, default rules:
- Sequential steps → Linear Workflow
- System components/containment → Grouped Architecture
- Before/after or two approaches → Split Comparison
- Overlap/shared ownership → Venn
- Central coordination → Hub-and-Spoke

## Step 2: Build the DiagramSpec

Before writing any SVG, write out the diagram plan explicitly as text — this helps catch structural mistakes before committing to coordinates. Output the DiagramSpec in this format:

```
**DiagramSpec**

main_claim: [one sentence — what is the diagram making obvious?]
pattern: [primary pattern]
secondary_pattern: [optional, or none]
reading_direction: [left-to-right / top-to-bottom]
title: "Diagram Title"
canvas_size: [estimated width x height]

nodes:
  - id: n1
    label: "Short label"
    semantic_type: [primary | secondary | tertiary | start | end | warning | decision | ai_llm | inactive | error]
    shape: [rect | pill | diamond]
    position: [x, y]
    size: [width, height]
    group: [container_id if inside a container, else none]

connections:
  - from: n1
    to: n2
    label: ""
    style: [primary | optional | feedback | human | context | error]
    exit_port: [right | bottom | top | left]
    entry_port: [left | top | bottom | right]
    route_shape: [straight | L-shape | Z-shape | U-shape]
    waypoints: [list of x,y turning points]
    offset: [0 | +12 | -12 | ...]   # parallel offset if sharing corridor with another connector

groups:
  - id: g1
    label: "Panel title"
    type: [outer_panel | inner_panel | soft_region]
    bounds: [x, y, width, height]
    children: [n1, n2, ...]
```

Writing this out is an internal planning step — clarify the structure in your own reasoning before committing to SVG. After writing the DiagramSpec, **proceed immediately to Step 3** without waiting for user confirmation. Read `references/pattern-library.md` for layout rules per pattern type.

**Language consistency**: Write the DiagramSpec — and all node labels, titles, and edge labels in the final SVG — in the same language the user used. If the user wrote in Chinese, the diagram text should be Chinese too.

## Step 3: Generate SVG

### SVG document structure

```xml
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}">
  <defs>
    <!-- Arrow markers go here -->
  </defs>
  <!-- Background -->
  <!-- Outer border -->
  <!-- Title -->
  <!-- Groups/Panels (render before nodes so they sit behind) -->
  <!-- Nodes -->
  <!-- Connectors (render last so they sit on top) -->
</svg>
```

Use `viewBox="0 0 {width} {height}"` with no fixed `width`/`height` attributes, so the SVG scales adaptively. Typical canvas sizes:
- Simple diagrams (3-6 nodes): `0 0 1000 600`
- Medium diagrams (7-12 nodes): `0 0 1200 800`
- Complex diagrams (13-20 nodes): `0 0 1400 1000`

Adjust as needed based on actual content.

### Arrow marker definitions

**The single most important style rule**: all arrows use open chevron arrowheads. This is the signature visual element.

Define one marker per connector color in `<defs>`. Each marker uses a `<polyline>` to draw an open V shape:

```xml
<defs>
  <marker id="arrow-primary" viewBox="0 0 10 10" refX="10" refY="5"
          markerWidth="8" markerHeight="8" orient="auto-start-reverse" markerUnits="strokeWidth">
    <polyline points="0,1 10,5 0,9" fill="none" stroke="#7A756E" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
  </marker>
  <marker id="arrow-optional" viewBox="0 0 10 10" refX="10" refY="5"
          markerWidth="8" markerHeight="8" orient="auto-start-reverse" markerUnits="strokeWidth">
    <polyline points="0,1 10,5 0,9" fill="none" stroke="#9A948C" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
  </marker>
  <marker id="arrow-feedback" viewBox="0 0 10 10" refX="10" refY="5"
          markerWidth="8" markerHeight="8" orient="auto-start-reverse" markerUnits="strokeWidth">
    <polyline points="0,1 10,5 0,9" fill="none" stroke="#8E8982" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
  </marker>
  <marker id="arrow-human" viewBox="0 0 10 10" refX="10" refY="5"
          markerWidth="8" markerHeight="8" orient="auto-start-reverse" markerUnits="strokeWidth">
    <polyline points="0,1 10,5 0,9" fill="none" stroke="#D88966" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
  </marker>
  <marker id="arrow-context" viewBox="0 0 10 10" refX="10" refY="5"
          markerWidth="8" markerHeight="8" orient="auto-start-reverse" markerUnits="strokeWidth">
    <polyline points="0,1 10,5 0,9" fill="none" stroke="#7FB08F" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
  </marker>
  <marker id="arrow-error" viewBox="0 0 10 10" refX="10" refY="5"
          markerWidth="8" markerHeight="8" orient="auto-start-reverse" markerUnits="strokeWidth">
    <polyline points="0,1 10,5 0,9" fill="none" stroke="#D96B63" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
  </marker>
</defs>
```

Never use filled/block arrowheads. The open chevron is the defining visual signature.

### Background

```xml
<rect width="100%" height="100%" fill="#F2EFE8"/>
```

### Outer border

Every diagram gets a single outer border — a thin rounded rectangle that frames the entire composition. Place this immediately after the background.

```xml
<rect x="20" y="20" width="{viewBox_width - 40}" height="{viewBox_height - 40}" rx="8" fill="none" stroke="#B9B3AB" stroke-width="1.5"/>
```

### Title

```xml
<text x="{viewBox_width / 2}" y="70" text-anchor="middle" font-size="32" font-weight="700" fill="#1F1F1C">Diagram Title</text>
```

### Node templates by semantic type

Each node is a `<g>` group containing a `<rect>` (or shape) and `<text>`. Apply styles based on semantic role — the color encodes meaning.

| Semantic type | fill | stroke | text fill | rx | Notes |
|---|---|---|---|---|---|
| **Primary / Neutral** | #E6E2DA | #8C867F | #2D2B28 | 10 | Default for generic components |
| **Secondary / Context** | #EAF4FB | #6FA8D6 | #2D2B28 | 10 | Files, tools, docs, storage |
| **Tertiary / Control** | #EEEAF9 | #9A90D6 | #2D2B28 | 10 | Routers, memory, orchestration |
| **Start / Trigger** | #F8E9E1 | #D88966 | #D88966 | 30 | User input, external trigger (pill shape via large rx) |
| **End / Success** | #CFE8D7 | #71AE88 | #2D2B28 | 10 | Completed output, accepted result |
| **Warning / Reset** | #F3E4DA | #C88E6A | #2D2B28 | 10 | Retry, reset, interrupt |
| **Decision** | #E6D7B4 | #BFA777 | #2D2B28 | 2 | Diamond shape — use rotated rect (see below) |
| **AI / LLM** | #D7E6DC | #7FB08F | #2D2B28 | 10 | Model calls, agent workers |
| **Inactive / Disabled** | #EFECE6 | #B4AEA6 | #7A756E | 10 | Optional, de-emphasized |
| **Error** | #F8DFDA | #D96B63 | #2D2B28 | 10 | Failures, blocked execution |
| **Pill label** | #FAF8F4 | #8C867F | #2D2B28 | 30 | Small categorical labels |
| **Code/evidence block** | #EEF3F7 | #B7C9D8 | #44515C | 4 | Code snippets, data examples |

**Standard rect node example:**
```xml
<g>
  <rect x="100" y="150" width="160" height="60" rx="10"
        fill="#E6E2DA" stroke="#8C867F" stroke-width="1.8"/>
  <text x="180" y="185" text-anchor="middle" dominant-baseline="central"
        font-size="16" fill="#2D2B28">Label</text>
</g>
```

**Pill node example (Start/Trigger):**
```xml
<g>
  <rect x="100" y="150" width="160" height="60" rx="30"
        fill="#F8E9E1" stroke="#D88966" stroke-width="1.8"/>
  <text x="180" y="185" text-anchor="middle" dominant-baseline="central"
        font-size="16" font-weight="700" fill="#D88966">User Input</text>
</g>
```

**Diamond node example (Decision):**
```xml
<g transform="translate(250, 300)">
  <rect x="-50" y="-35" width="100" height="70" rx="2"
        transform="rotate(45)"
        fill="#E6D7B4" stroke="#BFA777" stroke-width="1.8"/>
  <text x="0" y="0" text-anchor="middle" dominant-baseline="central"
        font-size="14" fill="#2D2B28">Yes/No?</text>
</g>
```

For semantic meaning of each type, read `references/color-palette.md` → Semantic Mapping Rules section.

### Text handling

SVG `<text>` does not support automatic word wrapping. Rules:
- Keep labels short (2-4 words preferred)
- If a label must be longer, split into multiple `<tspan>` elements stacked vertically:

```xml
<text x="180" text-anchor="middle" font-size="16" fill="#2D2B28">
  <tspan x="180" y="175">First line</tspan>
  <tspan x="180" dy="20">Second line</tspan>
</text>
```

- Use `dy` attribute for line spacing (typically 18-22px for font-size 16)
- When using multi-line text, increase the node height accordingly

### Container / panel styles

Containers are `<g>` groups with a background `<rect>` and a title `<text>`. Render containers before their children so the background sits behind.

**Outer panel** (large system boundary):
```xml
<g>
  <rect x="80" y="120" width="480" height="500" rx="16"
        fill="#FAF8F4" stroke="#8C867F" stroke-width="2"/>
  <text x="100" y="150" font-size="20" font-weight="600" fill="#5F5A54">Panel Title</text>
  <!-- Children go here -->
</g>
```

**Inner panel** (subsystem or grouping):
```xml
<g>
  <rect x="100" y="170" width="300" height="200" rx="10"
        fill="#FAF8F4" stroke="#8C867F" stroke-width="1.8"/>
  <text x="116" y="195" font-size="17" font-weight="600" fill="#5F5A54">Sub-panel</text>
</g>
```

**Soft region** (dashed grouping, no strong boundary):
```xml
<g>
  <rect x="100" y="170" width="300" height="200" rx="12"
        fill="#F6F4EE" stroke="#B9B3AB" stroke-width="1.5" stroke-dasharray="6 6"/>
  <text x="116" y="195" font-size="16" fill="#7A756E">Region Label</text>
</g>
```

### Connector styles

All connectors use `<path>` elements with L-shape or Z-shape routing. Calculate waypoints manually based on source and target node positions.

| Connector type | stroke | stroke-width | dash | marker-end | Use for |
|---|---|---|---|---|---|
| **Primary flow** | #7A756E | 1.8 | none | url(#arrow-primary) | Main process path |
| **Optional / inferred** | #9A948C | 1.6 | 6 6 | url(#arrow-optional) | Optional path |
| **Feedback loop** | #8E8982 | 1.8 | none | url(#arrow-feedback) | Retry / iterative loop |
| **Human override** | #D88966 | 1.8 | 6 6 | url(#arrow-human) | Human interrupt |
| **Context / support** | #7FB08F | 1.8 | none | url(#arrow-context) | Context injection |
| **Error path** | #D96B63 | 1.8 | none | url(#arrow-error) | Failure path |

For dashed connectors, add `stroke-dasharray="6 6"` to the path.

**Edge label** (optional, placed near the midpoint of the path):
```xml
<text x="{mid_x}" y="{mid_y - 8}" text-anchor="middle" font-size="13" fill="#7A756E">label</text>
```

### Connector routing — avoiding overlaps

**This is the most common quality issue in generated diagrams.** Read `references/connector-routing.md` for the full routing rules with examples and SVG `<path>` templates. The four mandatory rules are:

1. **Port selection**: Each node has 4 ports (top/right/bottom/left). No two connectors may use the same port on the same node. Distribute connectors across different edges.
2. **Parallel offset**: When connectors share a corridor, offset each subsequent line by 12px (pattern: 0, +12, -12, +24...).
3. **Crossover bridge**: Unavoidable crossings get an 8px-radius arc bump (`A 8 8 0 0 1`).
4. **Perpendicular entry/exit**: Every connector must leave and enter nodes perpendicular to the edge, with a >= 20px straight stub before the first turn and after the last turn.

**Routing process**: Route the main flow path first, then secondary connectors. For each connector: assign ports (Rule 1) → choose shape (straight/L/Z/S/U) → check for corridor conflicts (Rule 2) → add bridges at crossings (Rule 3) → verify perpendicularity (Rule 4).

Five connector shapes are available — **straight**, **L-shape** (1 turn), **Z-shape** (2 turns), **S-shape** (3 turns, for cross-axis port combinations), and **U-shape** (feedback loops). See `references/connector-routing.md` for SVG `<path>` templates for each.


## Step 4: Layout rules

These rules keep diagrams feeling calm and well-composed:

- **Node spacing**: minimum 80px horizontal gap between adjacent nodes; 60px vertical gap
- **Recommended horizontal pitch**: 200px center-to-center for workflow steps
- **Recommended vertical pitch**: 120px center-to-center for parallel elements
- **Canvas padding**: 60px around the outermost content (inside the outer border)
- **Grid alignment**: snap all positions to multiples of 10
- **Node size**: standard nodes 140x60 to 180x70; wide containers 300-600+
- **Keep layout flat**: max 3 nesting levels; prefer whitespace over extra containers

For pattern-specific layout rules, read `references/pattern-library.md`.

## Step 5: Write and open

1. Write the complete SVG to a descriptive `.svg` file in the current working directory.
   - Filename: lowercase with hyphens, e.g., `agent-loop.svg`, `context-engineering.svg`
2. Open the file: `open <filename>.svg` (macOS) or `start <filename>.svg` (Windows) or `xdg-open <filename>.svg` (Linux)

## Quality checklist

Before finalizing the SVG, verify:

- [ ] SVG root has `xmlns="http://www.w3.org/2000/svg"` and `viewBox` (no fixed width/height)
- [ ] `<defs>` section contains all needed arrow markers with open chevron `<polyline>`
- [ ] Background `<rect>` with `fill="#F2EFE8"` is present
- [ ] Outer border `<rect>` is present (x=20, y=20, covers content + padding)
- [ ] Title is large (font-size >= 28), bold, dark (#1F1F1C), horizontally centered
- [ ] Every arrow uses `marker-end="url(#arrow-{type})"` — never filled arrowheads
- [ ] **No two connectors share the same path segment** — parallel connectors are offset by 12px
- [ ] **No two connectors use the same port on any node** — ports are distributed across top/right/bottom/left
- [ ] **Crossings have bridge arcs** — unavoidable crossings use `A 8 8 0 0 1` arc bumps
- [ ] **Connectors are perpendicular to node edges** — every connector's first segment exits perpendicular to the port edge with >= 20px stub, and last segment enters perpendicular with >= 20px approach
- [ ] Node colors follow semantic meaning, not decoration
- [ ] Main flow path is visually dominant within 3 seconds
- [ ] No more than 4 semantic accent colors in one diagram
- [ ] All coordinates are multiples of 10
- [ ] Text labels are short; multi-line text uses `<tspan>` with `dy` spacing
- [ ] Containers render before their children (background behind content)
- [ ] Connectors render last (on top of everything)
- [ ] SVG is well-formed XML — all tags closed, special characters escaped (`&amp;` `&lt;` `&gt;`)
- [ ] No `style` or `class` attributes that depend on external CSS — all styling is inline

## Reference files

- `references/color-palette.md` — Full semantic color rules, text hierarchy, container specs, background values, geometry tokens. Read when you need to choose colors or verify a semantic mapping.
- `references/pattern-library.md` — 10 diagram patterns with layout rules, anti-patterns, and combination rules. Read when the pattern choice is ambiguous or the layout needs fine-tuning.
- `references/connector-routing.md` — Detailed connector routing rules (port selection, parallel offset, crossover bridge, perpendicular entry/exit) with SVG `<path>` templates. **Read this file before drawing any connectors.**
