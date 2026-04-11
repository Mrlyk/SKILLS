# Color Palette & Brand Style

**This is the single source of truth for all colors and brand-specific styles.**
To customize diagrams for a different visual identity, edit this file. Everything else in the skill should stay universal and semantic.

This palette is optimized for:
- warm editorial tech-blog diagrams
- low-density explanatory flowcharts
- architecture diagrams with soft grouping
- restrained comparison charts
- large-title, article-embedded visuals

It is **not** optimized for dashboards, neon UI, or high-saturation infographics.

## Core Style Principles

1. **Colors encode meaning, not decoration.**
2. **Most of the canvas should remain neutral.**
3. **Accent colors should be sparse and semantic.**
4. **Strokes are always darker than fills.**
5. **Typography and spacing carry more hierarchy than color.**
6. **Prefer calm, editorial contrast over vivid UI contrast.**
7. **Default to no shadows and no gradients.**

## Shape Colors (Semantic)

Colors encode meaning, not decoration. Each semantic purpose has a fill/stroke pair.

| Semantic Purpose | Fill | Stroke |
|---|---|---|
| Primary/Neutral | #E6E2DA | #8C867F |
| Secondary / Context | #EAF4FB | #6FA8D6 |
| Tertiary / Control | #EEEAF9 | #9A90D6 |
| Start/Trigger | #F8E9E1 | #D88966 |
| End/Success | #CFE8D7 | #71AE88 |
| Warning/Reset | #F3E4DA | #C88E6A |
| Decision | #E6D7B4 | #BFA777 |
| AI/LLM | #D7E6DC | #7FB08F |
| Inactive/Disabled | #EFECE6 | #B4AEA6 |
| Error | #F8DFDA | #D96B63 |

**Rule**: Always pair a darker stroke with a lighter fill for contrast.

### SVG Attribute Mapping

Apply colors as inline SVG attributes on `<rect>`, `<circle>`, `<polygon>`, or `<path>` elements:

```xml
<rect fill="#E6E2DA" stroke="#8C867F" stroke-width="1.8" rx="10" .../>
```

Never use CSS classes or external stylesheets. All styling must be inline for maximum portability.

### Semantic Interpretation

- **Primary/Neutral**: default blocks, generic system components, standard containers
- **Secondary / Context**: files, skills, tools, docs, retrieved context, storage-like resources
- **Tertiary / Control**: routers, memory, evaluators, aggregators, orchestration, policy layers
- **Start/Trigger**: user input, prompt input, external trigger, human intervention
- **End/Success**: verified result, completed output, accepted answer, successful state
- **Warning/Reset**: retry, reset, re-entry, interrupt, caution, manual steering
- **Decision**: branch points, filters, approval logic, yes/no gates
- **AI/LLM**: model calls, agent workers, active execution stages, reasoning stages
- **Inactive/Disabled**: optional items, de-emphasized elements, unavailable or future elements
- **Error**: failures, blocked execution, invalid state, rejected result, deny path

## Text Colors (Hierarchy)

Use fill color on `<text>` elements to create visual hierarchy.

| Level | Color | Use For |
|---|---|---|
| Title | #1F1F1C | Main diagram title |
| Subtitle | #5F5A54 | Section headers, panel titles |
| Body/Detail | #4F4A44 | Labels, annotations, helper copy |
| Muted/Support | #7A756E | Secondary annotations, non-primary labels |
| On light fills | #2D2B28 | Text inside most boxes and panels |

### SVG Text Example

```xml
<!-- Title -->
<text fill="#1F1F1C" font-size="32" font-weight="700" text-anchor="middle">Title</text>

<!-- Subtitle -->
<text fill="#5F5A54" font-size="20" font-weight="600">Section Header</text>

<!-- Body label -->
<text fill="#2D2B28" font-size="16">Node Label</text>

<!-- Muted -->
<text fill="#7A756E" font-size="13">Supporting note</text>
```

### Text Hierarchy Rules

- Use **Title** for the single main headline only.
- Use **Subtitle** for section names, panel labels, and major group headings.
- Use **Body/Detail** for node labels, arrow annotations, and supporting explanation.
- Use **Muted/Support** for optional captions or low-priority labels.
- Prefer free-floating text over unnecessary containers.

## Evidence Artifact Colors

Used for code snippets, data examples, and other concrete evidence inside technical diagrams.

| Artifact | Fill | Stroke | Text Color |
|---|---|---|---|
| Code snippet | #EEF3F7 | #B7C9D8 | #44515C |
| JSON/data example | #EEF4EE | #B9CCBE | #46574C |
| Terminal/CLI example | #F3F1EC | #C8C1B6 | #4C4943 |
| File tree / spec excerpt | #EDF2F8 | #B8C6D8 | #506070 |

### Evidence Rules

- Evidence blocks should look quieter than primary diagram nodes.
- Use evidence artifacts only when concrete examples improve understanding.
- Do not make evidence artifacts the most visually dominant element.

## Default Stroke & Line Colors

| Element | Color |
|---|---|
| Structural lines (dividers, trees, timelines) | #8C867F |
| Secondary structural lines | #9A948C |
| Grouping boundary (solid) | #8C867F |
| Grouping boundary (dashed) | #B9B3AB |

### Line Rules

- Main flows inherit meaning from the source node where possible.
- Structural dividers should stay neutral.
- Do not use pure black lines unless the whole diagram is monochrome.
- Dashed lines (`stroke-dasharray="6 6"`) indicate optionality, inferred paths, soft grouping, or human-overridable behavior.

## Background

| Property | Value |
|---|---|
| Canvas background | #F2EFE8 |
| Panel background | #FAF8F4 |
| Alternate panel background | #F6F4EE |
| Soft emphasis background | #F3F0E9 |

### SVG Background Implementation

```xml
<!-- Full canvas background as first element after <defs> -->
<rect width="100%" height="100%" fill="#F2EFE8"/>
```

### Background Rules

- Keep the overall canvas warm and light.
- Avoid pure white full-canvas backgrounds.
- Panels should be only slightly lighter than the canvas, not strongly contrasted.

## Container Styles

| Container Type | Fill | Stroke | rx | Stroke Width |
|---|---|---|---|---|
| Outer panel | #FAF8F4 | #8C867F | 16 | 2.0 |
| Inner panel | #FAF8F4 | #8C867F | 10 | 1.8 |
| Neutral node | #E6E2DA | #8C867F | 10 | 1.8 |
| Semantic node | semantic fill | semantic stroke | 10 | 1.8 |
| Pill label | #FAF8F4 | #8C867F | 30 | 1.8 |
| Soft grouping region | #F6F4EE | #B9B3AB | 12 | 1.5 dashed |
| Inactive placeholder | #EFECE6 | #B4AEA6 | 10 | 1.6 |

### SVG Container Example

```xml
<g>
  <rect x="80" y="120" width="480" height="500" rx="16"
        fill="#FAF8F4" stroke="#8C867F" stroke-width="2"/>
  <text x="100" y="150" font-size="20" font-weight="600" fill="#5F5A54">Panel Title</text>
  <!-- child nodes here -->
</g>
```

### Container Rules

- Prefer rounded rectangles over sharp-cornered boxes.
- Use pills (rx=30) for small categorical labels or compact component tags.
- Use soft grouping regions (dashed stroke) to imply relationship without visual clutter.
- Avoid nested containers deeper than 3 levels.

## Connector Styles

| Connector Type | Color | Width | Dash | Arrow Marker | Use For |
|---|---|---|---|---|---|
| Primary flow | #7A756E | 1.8 | none | #arrow-primary | Main process path |
| Optional flow | #9A948C | 1.6 | 6 6 | #arrow-optional | Optional / inferred path |
| Feedback loop | #8E8982 | 1.8 | none | #arrow-feedback | Retry / iterative loop |
| Human override | #D88966 | 1.8 | 6 6 | #arrow-human | Human interrupt / steering |
| Context link | #7FB08F | 1.8 | none | #arrow-context | Context injection / supporting flow |
| Error path | #D96B63 | 1.8 | none | #arrow-error | Failure / blocked path |

### SVG Connector Example

```xml
<path d="M 260 180 L 350 180 L 350 300 L 440 300" fill="none"
      stroke="#7A756E" stroke-width="1.8" marker-end="url(#arrow-primary)"/>
```

### Arrow Rule

All connectors use open chevron arrowheads defined as SVG `<marker>` elements with `<polyline>`. This is the single most recognizable visual element of Anthropic-style diagrams. Never use filled/block/triangle arrowheads.

### Connector Rules

- Use L-shape or Z-shape `<path>` routing for clean orthogonal connections.
- Use straight lines when source and target are horizontally or vertically aligned.
- Use dashed connectors (`stroke-dasharray="6 6"`) sparingly.
- Main flow should be visually obvious within 3 seconds.

## Geometry Tokens

| Token | Value |
|---|---|
| Small rx | 4 |
| Medium rx | 10 |
| Large rx | 16 |
| Pill rx | 30 |
| Default stroke width | 1.8 |
| Panel stroke width | 2.0 |
| Dashed pattern | 6 6 |

### Geometry Rules

- Keep rx consistent across the diagram.
- Prefer a single rx family per diagram.
- Avoid mixing very thick and very thin strokes.
- Use panel strokes slightly heavier than internal strokes.

## Typography & Spacing

| Token | Value |
|---|---|
| Title font-size | 28-36 |
| Section title font-size | 18-22 |
| Body label font-size | 14-17 |
| Caption font-size | 11-13 |
| Title font-weight | 700 |
| Section font-weight | 600 |
| Body font-weight | 400 |
| Multi-line tspan dy | 18-22 |
| Outer canvas padding | 60 |
| Section gap | 28 |
| Internal box padding | 12-18 |
| Grid step | 10 |
| Default node gap | 60-80 |
| Large panel gap | 32-48 |

### Typography Rules

- The title should be large and editorial.
- Do not overuse bold inside nodes.
- Prefer short labels over wrapped text.
- Spacing should do more work than font variation.
- Use `text-anchor="middle"` and `dominant-baseline="central"` for centered text in nodes.

## Semantic Mapping Rules

Use this mapping when converting user intent into styled nodes.

- Use **AI/LLM** for model calls, agent workers, reasoning stages, execution stages.
- Use **Secondary / Context** for files, documents, tools, skills, retrieved context, and system resources.
- Use **Tertiary / Control** for routers, memory, evaluators, aggregators, controllers, and orchestration logic.
- Use **Start/Trigger** for prompts, users, interrupts, external systems, and manual input.
- Use **End/Success** for verified outputs, final answers, completed jobs, and accepted results.
- Use **Warning/Reset** for retry paths, resets, re-entry points, and caution states.
- Use **Decision** only for branch points, gates, approvals, filters, and yes/no logic.
- Use **Inactive/Disabled** for placeholders, disabled features, optional future nodes.
- Use **Error** for blocked execution, denied action, invalid state, failed validation.

## Diagram-Type Defaults

### Workflow Diagram
- Background: canvas background (#F2EFE8)
- Nodes: AI/LLM, Start/Trigger, End/Success, Decision as needed
- Connectors: primary flow + optional feedback loop
- Layout: clean linear or gently branching
- Emphasis: flow clarity

### Architecture Diagram
- Background: canvas background with panel grouping
- Nodes: Primary/Neutral + Secondary / Context + Tertiary / Control
- Connectors: L-shape orthogonal
- Layout: grouped systems and interfaces
- Emphasis: containment and interaction

### Comparison Diagram
- Background: two or more large neutral panels side by side
- Nodes: soft semantic fills
- Connectors: minimal
- Layout: mirrored or side-by-side
- Emphasis: contrast in structure, not color

## Non-Goals

Avoid these unless the user explicitly requests them:
- saturated brand colors
- drop shadows
- glossy UI treatments
- gradients
- icon-heavy decoration
- dense legends
- more than 4 semantic accent colors in one diagram
- dashboard aesthetics

## Fallback Rules

If semantic meaning is unclear:
1. default to **Primary/Neutral**
2. use **Secondary / Context** for passive information objects
3. use **AI/LLM** for active computational steps
4. use **Tertiary / Control** for routing or memory-like logic
5. use **Start/Trigger** only when something truly initiates flow

If too many colors are present:
- collapse low-priority semantics into **Primary/Neutral**
- keep only the 2-3 most meaningful accent categories

If a diagram feels too busy:
- remove containers before removing spacing
- reduce connector count before reducing color
- demote secondary labels to muted text
