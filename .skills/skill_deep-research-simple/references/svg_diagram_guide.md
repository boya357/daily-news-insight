# SVG Diagram Guide

Hand-written SVG for structural/relational diagrams only — flow, layered architecture, quadrant,
causal chain, timeline. Numeric data (trends, shares, distributions) → IPython/matplotlib, not here.

The diagram is embedded **directly as SVG** (`![caption](svg_url)`) and rendered by the viewer, so
text stays crisp and selectable and there is no rasterization step or extra dependency — the model
just emits an SVG string. The cost: SVG has **no auto-layout**. Overlap, text overflow, and crossing
arrows are the default failures, so the pre-checks (§4) and complexity budget (§1) are what keep
layout correct. When a diagram would exceed the budget, **split it into several small diagrams**
rather than overcrowding one.

## 1. Visual tokens

**Palette** — 7-level, semantic. Colour encodes *category* or *intensity*, never order; same-class
nodes share a colour; neutral/structural content is grey. Max 2–3 colour families per diagram.
Default to purple / teal / coral / grey for generic content; reserve blue / green / amber / red
for true info / success / warning / error meaning.

| Family | 50 (light fill) | 600 (stroke / mid) | 800 (text on fill) |
|---|---|---|---|
| Blue (info) | `#E6F1FB` | `#185FA5` | `#0C447C` |
| Teal (success) | `#E1F5EE` | `#0F6E56` | `#085041` |
| Amber (emphasis) | `#FAEEDA` | `#854F0B` | `#633806` |
| Coral (warning) | `#FAECE7` | `#993C1D` | `#712B13` |
| Purple (category) | `#EEEDFE` | `#534AB7` | `#3C3489` |
| Grey (neutral) | `#F1EFE8` | `#5F5E5A` | `#2C2C2A` |

- Use **50 fill + 600 stroke + 800 text**. Text sitting on a coloured fill uses that family's 800 —
  never plain black or grey.
- **Typography**: system `sans-serif`. Two sizes only — 14px (title / node name) / 12px (subtitle /
  note). Two weights only — 400 (body) / 500 (emphasis). **sentence case** throughout (no Title Case, no ALL CAPS).
- **Stroke**: 0.5px reads as precise and is the default; bump to 1px only if a target downscales it
  into invisibility. Rounded corners `rx="8"`. Transparent background — no wrapping `<rect>` fill.
- **Complexity budget**: ≤6 nodes side-by-side, ≤10–12 nodes total, subtitle ≤7 words (detail goes
  in prose), nesting ≤5 levels. Over budget → split into multiple diagrams.

## 2. Chinese fonts

Direct-embed SVG is rendered on the **viewer's** machine, so there is no container rasterization and
no font install to worry about — you only need a correct declaration:

- Put `font-family="'Noto Sans CJK SC',sans-serif"` on every `<text>`.
- **CJK width ≠ Latin width.** At 14px a Chinese glyph ≈ **14px**, a Latin char ≈ 8px. Budget box
  widths with **14px per CJK char** — the common "8px × chars" rule is Latin-only and under-sizes
  Chinese boxes by ~40% (guaranteed overflow). See §4 pre-checks.
- **Rasterize only as a fallback** (target can't render embedded SVG): `pip install cairosvg`
  (container has Noto CJK SC), `cairosvg x.svg -o x.png`, embed the PNG.

## 3. Base structure

```xml
<svg width="100%" viewBox="0 0 680 H" xmlns="http://www.w3.org/2000/svg" role="img">
  <title>{one-line description}</title>
  <desc>{longer note for screen readers}</desc>
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5"
            markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M2 1L8 5L2 9" fill="none" stroke="#5F5E5A"
            stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
    </marker>
  </defs>
  <!-- content -->
</svg>
```
- viewBox width fixed at **680** (markdown content-column width); height = lowest element y + 40.
- Safe area: x ∈ [40, 640], y ∈ [40, H−40]. Transparent background.
- Marker stroke is a fixed token colour. (`stroke="context-stroke"` would auto-match the line colour
  but is SVG2-only and fails on librsvg / many PDF renderers — avoid, or define one marker per colour.)

## 4. Geometric pre-checks (run before emitting)

1. **Width budget**: label px ≈ chars × **14 (CJK)** or × 8 (Latin), + 12px padding each side.
   "认证服务" (4 CJK) ≈ 56px + padding → ≥80px box. Wrap with `<tspan x="cx" dy="1.2em">` rather than overflow.
2. **No overlap**: a box's right edge < next box's left edge − 20px.
3. **Arrows don't cross unrelated boxes** — if a straight line would pass through one, use the L-bend path.
4. **Connectors must set `fill="none"`** — SVG paths default to black fill and become solid blobs otherwise.
5. Avoid `text-anchor="end"` at x<60 (overflows left of the viewBox).
6. Centre box labels: `text-anchor="middle" dominant-baseline="central"` at the box centre.

## 5. Shape snippets

```xml
<!-- one-line node (44h) -->
<rect x="100" y="20" width="180" height="44" rx="8" fill="#E6F1FB" stroke="#185FA5" stroke-width="0.5"/>
<text x="190" y="42" text-anchor="middle" dominant-baseline="central"
      font-size="14" font-weight="500" fill="#0C447C">节点标题</text>

<!-- two-line node (56h) -->
<rect x="100" y="20" width="200" height="56" rx="8" fill="#E1F5EE" stroke="#0F6E56" stroke-width="0.5"/>
<text x="200" y="38" text-anchor="middle" dominant-baseline="central"
      font-size="14" font-weight="500" fill="#085041">标题</text>
<text x="200" y="58" text-anchor="middle" dominant-baseline="central"
      font-size="12" fill="#0F6E56">副标题说明</text>

<!-- straight arrow -->
<line x1="200" y1="64" x2="200" y2="100" stroke="#5F5E5A" stroke-width="1" marker-end="url(#arrow)"/>

<!-- L-bend (route around a box) -->
<path d="M x1 y1 L x1 ymid L x2 ymid L x2 y2" fill="none" stroke="#5F5E5A" stroke-width="1" marker-end="url(#arrow)"/>
```

Other layouts — **layered architecture**: stacked full-width bands, components inside each with equal
gaps. **2×2 quadrant**: two crossing axes, label the four ends, place items by position.
**Timeline** (only when spacing/clustering is the point — otherwise a table): for many events or
long / CJK labels, use a **vertical spine** — events as nodes top→bottom in chronological order, date
on one side of the spine, label on the other; reserve the **horizontal** axis (ticks, date below /
event above) for a few short-labeled events. Events are nodes on the spine, **never a stack of
equal-length bars**.

## 6. Self-check before embedding
- No text overflows its box; no two boxes/labels overlap; CJK boxes sized at 14px/char.
- Arrows touch box edges, point correctly, carry the marker, set `fill="none"`; none cross unrelated boxes.
- `viewBox` set, transparent background, ≤3 colour families, two font sizes, CJK `font-family` present.

## 7. Deliver
Write the `.svg` to `{topic}_assets/`, `file_to_url` it, embed `![caption](url)`. Fallback only if the
target cannot render embedded SVG: `pip install cairosvg && cairosvg x.svg -o x.png`, then embed the PNG.