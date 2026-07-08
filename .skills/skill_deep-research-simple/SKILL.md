---
name: deep-research-simple
description: >
  Deep research with structured evidence quality control. Use whenever the user
  needs exhaustive, multi-source investigation — market analysis, industry research,
  competitive intelligence, due diligence, investment research, policy evaluation,
  trend forecasting, market sizing, product comparison, or industry landscape mapping.
  Trigger on: "深度分析", "帮我调研", "行业研究", "竞品分析", "投资分析",
  "in-depth analysis", "deep dive", "comprehensive research", "detailed report".
  Do NOT use for: simple factual lookup, single-source Q&A.
---

# Deep Research Pro

Execute a high-intensity research protocol focused on exhaustive discovery, continuous recursive reflection, and high-density analytical reporting with structured evidence blocks.

## Workflow

The execution spine. Each phase points to the standard that governs it.

1. **Epistemic Reset** — get the current date via bash `date` and the working directory via bash `pwd` (all output files go in that working directory — see §Output & Naming). Treat any time constraint implied by the query (e.g. "2026 Q1", "latest", "recent 6 months") as a hard constraint; flag findings outside that window as `[OUT-OF-WINDOW]`. Do not state facts before search results are reviewed.
2. **Query Understanding** — see `references/query_decomposition.md`. Produce an **initial decomposition**, then run **1–3 broad exploratory searches** (titles/snippets only — no full fetch, no evidence blocks; not counted toward the 15-step minimum). Output the **revised decomposition** explicitly — it is the baseline for scope-fit and dimension-coverage checks.
3. **Domain-Skill Loading (before Explore)** — check the query against the system prompt's **Skill Routing Guide (检索源选型指南)**, and load every matched professional data Skill via `skill_load`. Print a loading plan (which Skills, which dimensions each covers). **Professional sources first; `search_web` is fallback only** — if the query hits a covered domain, do not run the loop on `search_web` alone. Multi-domain queries load all matched Skills.
4. **Explore** — run **at least 15 search/data-query rounds** following §Search & Evidence. **Each round: search → recursive reflection → confidence tagging & contradiction handling.** Evidence is written once after all rounds (see §Search & Evidence). Within a loaded Skill's domain, prefer it over `search_web`; use `search_web` for narrative/qualitative context and as fallback.
5. **Evidence Consolidation** — after all rounds, write every evidence block to `{topic}_evidence.md` in one `write_file` (deduplicating and calibrating as you write); then batch-verify URLs (install deps if needed: `pip install -r scripts/requirements.txt`):
   ```bash
   python scripts/verify_urls.py {topic}_evidence.md
   ```
   Only ❌ FAIL results need action — append `[URL-UNVERIFIED]` to that block's Confidence field (e.g. `Confidence: MEDIUM [URL-UNVERIFIED]`); do not delete the block. ✅ PASS and ⚠️ UNCERTAIN are both acceptable (UNCERTAIN means anti-bot block, URL is valid).
6. **Outline + Visual Plan** — before Write, lay out the report skeleton explicitly in `{topic}_outline.md`:
   - **Section outline**: list each section and the key judgment it answers; order by decision-relevance.
   - **Evidence mapping**: attach the supporting evidence blocks (entries in `{topic}_evidence.md`) to each section; every key claim must be supported. Archive or drop unused evidence.
   - **Visual plan**: per section, decide whether a visual artifact is needed and, if so, which type, per the **form-selection table** in §Visualization & Tables (name the job, pick the form, check the *Avoid* column); plan tables **as a set**, consolidating recurring-entity comparisons up front.
   - **Gap check**: if scope/dimensions lack evidence, or `[URL-UNVERIFIED]` blocks need replacement sources, run targeted supplementary searches before Write.
7. **Produce visuals** — execute the outline's visual plan (§Visualization & Tables): for each planned chart/SVG, generate it, save to `{topic}_assets/`, convert via `file_to_url`, then run the **Pre-embed self-check**. 
8. **Write** — generate `{topic}_report.md` from the outline per §Report Engineering and §Citation & Formatting, embedding each visual with `![caption](public_url)` (never a local path — it won't render). Every factual statement carries `[(source_name)](specific_url)`; no `OUT-OF-SCOPE` evidence for main claims; `PARTIAL` only with explicit qualification.

**Track the plan**: before step 1, write these 8 steps as a checklist to `{topic}_plan.md` via `write_file`; after each step, rewrite the file via `write_file` with completed steps marked ✅.

## Search & Evidence

### Search loop (15+ steps)

This loop runs against the **revised decomposition** from Query Understanding — the coverage baseline the reflection re-checks each round.

1.  **Iterative Search**: Perform **at least 15 search steps** to ensure comprehensive coverage. Follow a **broad-to-narrow, background-before-detail** 3-stage progression — **(1) Landscape**: macro overview + structural mapping; **(2) Deep Dives**: targeted investigation per dimension — go vertical on key dimensions: trace data to its methodology, track trends across time periods, and investigate causal mechanisms; **(3) Verify & Fill**: cross-verification + gap filling. Allocate steps across stages based on topic complexity; earlier stages build the map, later stages stress-test it. Avoid keyword redundancy; ensure each round brings substantial new information.
    - **Maximize parallel search**: For independent topics/dimensions, launch **as many parallel `search_web` calls as possible**, each carrying the maximum allowed queries. Go sequential only when the next query depends on previous results.
    - **Search language**: Issue search queries in Chinese and English when useful.
2.  **Selective deep fetch**: If the snippet is enough, don't fetch; fetch the full page only when —
    - **the snippet is incomplete**: a truncated number, a contradiction that needs full-context comparison, a HIGH-confidence candidate that needs confirmation, or a key decision-maker's direct quote (CEO, regulator, industry leader) of unique value; or
    - **the snippet may be stale**: a fast-changing live metric (GitHub stars/forks, download counts, live rankings, follower counts) — fetch the live page for the current value and record its data date; **conclusions the snippet draws from the stale number (e.g. "most popular", "#1") must be re-evaluated too**. If a professional Skill covers the domain, use the Skill instead of fetching.
3.  **Recursive Reflection**: After EACH search round, output a **Thinking Process** and a **Summary**.
    - **Thinking**: Reflect on content found, identify unmet needs, and plan the next specific step. Check **scope fit and dimension coverage** against the revised decomposition. Flag any **time-sensitive quantitative indicators** (stock prices, market caps, exchange rates, rankings) that need dedicated real-time queries.
    - **Summary**: Concise recap of key findings.
    - *Constraint*: Both sections must be **short and concise**.

### Evidence blocks

Use the following **8-field format** for every piece of significant evidence:

```
Claim: [the specific factual claim — plain text, no URLs]
Source: [source name / file name]
URL: [source URL / "File: {filename}, Section: {section}"]
Date: [publication date / "N/A" for files]
Excerpt: [verbatim raw excerpt — no paraphrasing]
Context: [surrounding context that affects interpretation]
Scope fit: [IN-SCOPE / PARTIAL / OUT-OF-SCOPE — fit against the revised decomposition's time scope, geographic scope, target entity, and must-have coverage]
Confidence: [HIGH / MEDIUM / LOW]
```

**One block per claim** — do not combine multiple entities or unrelated facts into a single block. Each block should be atomic: one specific claim about one subject.

**Scope fit rule:** A source can be credible but still not applicable to the user's question. Use `IN-SCOPE` for evidence that matches the revised decomposition, `PARTIAL` for evidence that is useful only as context/comparison or has a minor scope mismatch, and `OUT-OF-SCOPE` for evidence that should not support final report claims.

**Source credibility & priority:** Prioritize authoritative sources (government sites, academic databases, peer-reviewed journals, official filings, major media); **never fabricate data**. When multiple sources cover the same fact, cite the more **authoritative** and more **recent** — primary/official over secondary reporting, professional/vertical media over general UGC; treat SEO-driven or AI-generated content farms as unreliable. Draw on **multiple source types**, not just one.

**Confidence tagging:** Tag every significant finding with one of three levels:
- `[HIGH]` — Confirmed by ≥2 independent authoritative sources with consistent data.
- `[MEDIUM]` — Confirmed by 1 authoritative source, or multiple secondary sources.
- `[LOW]` — Weak sourcing, single unverified claim, or blog-level evidence.

**Contradiction handling:** Conflicts between sources are signal, not noise. Never suppress them. When conflicting data is found, explicitly document both claims, both sources, and the nature of the conflict (statistical / interpretive / temporal). Temporal conflicts must be flagged as `[TEMPORAL-CONFLICT: source A = period X; source B = period Y]`.

**Evidence collection:** **After all search rounds are complete, write every evidence block to `{topic}_evidence.md` in a single `write_file`.** Deduplicate, calibrate scope fit, and upgrade/downgrade confidence based on cross-verification in the same pass.

Every major claim in the final report must map back to an evidence block in this file.

**Date rules:** Record the publication date, not access date. If no date: `Date: N/A [accessed YYYY-MM-DD]`.

**Source differentiation:**
- `[SEARCH-SOURCED]` — evidence from external search
- `[FILE-SOURCED]` — evidence from user-provided files
- `[MIXED]` — cross-validated across both channels

## Report Engineering

### Opening Summary
The opening summary is a findings digest, not a topic introduction: it states the report's highest-value findings at maximum density. A reader who reads only the summary should learn what they could not have known without the research.

**Predictability test.** Every sentence must fail the question "could someone write this without reading the report?" A sentence that passes is filler or a slogan (e.g. 进入深水区 / 核心矛盾 / 重塑格局 / 拐点 / 元年; "paradigm shift", "inflection point") — cut it or replace it with a finding. Each sentence must carry at least one number, named entity, or specific mechanism, and give specific values, not vague hedges.

**Build the summary from these role-sentences** — each does a distinct job. **Write one of each that applies**: aim for all of them in landscape/comparison/evaluation/due-diligence/forecast reports; for other types, keep the ones that fit and drop the rest.
- **Landscape** — state what exists or the baseline: precise counts plus a structural contrast or trend.
- **Counter-intuitive** — state the single most surprising, least-predictable finding in the report.
- **Limitation** — name the most important thing that does not work or is not yet known.
- **Reality** — give what is true on the ground: from your own evidence, cross-checked against external authority rather than borrowed from it.
- **Judgment** — close with one forward, decision-relevant call.

These role names are internal scaffolding — never print them in the summary as labels, prefixes, or headings (e.g. no paragraph opening with "反直觉发现：" or "格局："); the findings read as continuous prose.

**Evidence bar (MANDATORY).** The summary is **not exempt from citations** — every number and named claim takes its inline `[(source_name)](url)` tag exactly as in the body; an uncited number is a defect, not a stylistic choice. Never build its punch on a fabricated or weakly-sourced figure: the headline counter-intuitive finding should rest on `[HIGH]`-confidence evidence.

**Layout (MANDATORY).** Break the summary into **2–4 short paragraphs separated by blank lines — never one block**; each paragraph focuses on one cluster of related findings, at most three or four sentences, then start a new one. **Bold the key judgment, the critical numbers, and the single most important finding** so a skimmer catches them at a glance. The summary is exempt from the body's minimum paragraph-length rule.

### Body Structure
- **Conclusion-first at every level**: extend the opening's discipline to each section and subsection — lead with the key judgment, then develop the evidence beneath it (inverted pyramid). A reader skimming only the lead sentences should still grasp the report's backbone. This changes ordering, not depth.
- **Organize by argument, not by source**: each paragraph advances one point and pulls in whatever sources support it; never structure prose source-by-source ("Source A reports… Source B says…"). A source is evidence for a judgment, not the subject of a paragraph.
- **Order sections by decision-relevance**: put what matters most to the user's question first, not what convention or evidence-gathering order suggests.

### Data Source Disclosure (MANDATORY when professional Skills used)
When this research used any professional data Skill (`openecon-data` / `fred-data-skill` / `worldbank-data` / `frankfurter-data` / `stock-data-skill` / `tianyancha-data` / `tmdb-data-skill` / `qimai-data-skill` / `weko-data`, etc.), the report **must** insert a short **"Data Sources"** disclosure after the Executive Summary and before the body sections, telling the reader which authoritative databases the report's factual backbone rests on, to improve credibility and verifiability.

**Writing the disclosure:**
- Heading: `## Data Sources` (or `## 数据来源`, matching the report's language).
- Length: 80–200 words plus one compact table; **no** lengthy expansion.
- Must include:
    1. **The professional data Skills used and their underlying providers** (e.g. `openecon-data` → FRED / World Bank / IMF / OECD ...); list the provider, not the Skill name.
    2. **The dimension each provider covers in this report** (e.g. "FRED: US monthly macro indicators", "天眼查: the target company's business registration and equity structure").
    3. **Whether `search_web` general search was used as a fallback**, with a qualitative note on its share (e.g. "general search only supplements qualitative context and carries no key numbers").
- A table is recommended, e.g.:

    | Provider | Skill used | Dimension covered | Role |
    |----------|-----------|---------|------|
    | FRED | fred-data-skill | US GDP / CPI / unemployment time series | primary source for key numbers |
    | Frankfurter | frankfurter-data | USD/CNY exchange-rate history | primary source for key numbers |
    | General web | search_web | policy interpretation, expert opinion | qualitative fallback |

- **Do not** write this as an "acknowledgments" note or in a marketing tone; its purpose is **methodological disclosure** — keep it objective and restrained.
- If no professional Skill was used (pure `search_web`), this disclosure may be omitted; but if even one professional Skill was used, it is mandatory.

### Style Adaptation
- **Report voice:** Final report prose should use a neutral, impersonal style by default. Avoid first-person and second-person address unless the user explicitly requests a different voice.
- **Tone:** No marketing speak, no sloganeering (e.g., "industry-leading", "paradigm shift", "reshaping the future"). Be professional, restrained, and confident.
- **Heading tone:** Final report headings must use formal report language that identifies the topic, conclusion, analytical dimension, or section purpose. Avoid click-oriented, conversational, promotional, tutorial-style, and platform-native headline formulas.
- **Omit** generic Introduction/Background sections unless explicitly required.

### Depth and Analysis (Mode-Based)
Pick the depth mode by the report's purpose:
- **Academic/Survey mode** — to map the full picture (technology surveys, policy research, industry landscapes, market sizing/forecasts): prioritize comprehensive fact-based detail — full definitions, formulas, statistical indicators (CI, metrics), and baseline comparisons; avoid speculative interpretation and support every statement with references.
- **Practical/Decision mode** — to support a decision (product/vendor selection, investment/equity research, competitive analysis, due diligence): incorporate observations, human insight, Pros/Cons, and actionable trade-offs; land each point on its "so what".
- Most research reports blend both — lean by the dominant intent.
- **Insight rule**: Key paragraphs must answer "so what" and "why" — don't just state facts: explain why they matter and what impact they have, and the causal mechanism or driver behind them, not just the outcome. Avoid hollow summaries; replace vague claims with specific facts and data. When analyzing multiple comparable entities, **focus on differentiators rather than repeating shared patterns** — state the common pattern once, then highlight what makes each entity unique.
- **Confidence in report**: LOW confidence claims must be qualified with hedging language (e.g., "preliminary data suggests...", "unverified reports indicate..."). Do not present LOW confidence evidence with the same certainty as HIGH. When credible sources genuinely conflict, present both positions and state which the weight of evidence favors and why — neither silently pick a side nor blur the conflict into vague hedging.
- **Actionable conclusions**: The report must end with clear conclusions that include: (1) explicit judgments with supporting evidence, (2) concrete recommendations or next steps with priority, (3) applicable scope — state under what conditions the conclusions hold, key uncertainties, and what evidence would change the judgment.

### Length and Paragraph Constraints
- **Total Volume**: Aim for **5,000+ words**; scale with topic complexity. Information density matters more than raw length.
- **Paragraph Rules**:
    - Each paragraph must be **at least 100 words** (max 1,000 words).
    - **Subsection Rule**: Every subsection (e.g., `## 3.1`) MUST contain **more than one paragraph**.
- **Natural Transitions**: Avoid mechanical enumeration patterns (e.g., "First, second, third", "首先、其次、最后"); use natural transitions between ideas.

## Visualization & Tables

Default to **showing, not telling**: wherever a finding has a shape, show it in the form that fits it most faithfully instead of leaving it in prose. Each form carries a different kind of content:
- **Charts** (IPython/matplotlib) — *quantity*: trends, rankings, distributions, numeric comparison.
- **SVG diagrams** — *relationship and structure*: process, hierarchy, causal chain, quadrant, the links among entities (see `references/svg_diagram_guide.md`).
- **Tables** — *dense, mostly categorical/textual reference* looked up across many entities.
- **Prose** — narrative, mechanism, and argument.

Don't add a visual artifact for its own sake. Prioritize visualizing the report's **thesis-level findings** — the judgments, contrasts, and trends — not decorative filler. Route all calculations through programming tools.

### Choosing the form
**Identify the task first, then pick the form** — don't start by reaching for "a chart". Ask: *what single claim, pattern, or comparison must this visual make obvious?* — match it to an **analytical job** in the left column, then read the form off the Use column. What decides the form is the **nature of the task** (the data's shape, what the reader must see), not whichever metric you happen to have.

**How to read the form-selection table** — each row is one analytical job: the **Use** column is the form to use; the **Avoid** column is the form(s) *not* to use for that job (the cell says why).

| Analytical job (what you are showing) | Use | Avoid |
|---|---|---|
| A quantity **changing over continuous time** (e.g., price, sales, market size, user count) | IPython **line chart**; multi-series for several entities; add a confidence band for forecasts | bar chart for a long series; drawing a time trend as a discrete ranking chart |
| A **chronology of discrete events / milestones** (e.g., launches, policies, funding rounds, version nodes) | a dated **table** by default; an **SVG timeline** only when the **spacing, clustering, or gaps are themselves the finding** | **bar / line chart**; equal-length bars stacked per event (a fake Gantt) — an event sequence is *structural*, not a trend |
| **Duration intervals with explicit start/end** (e.g., project schedules, phase plans, campaign windows) | **Gantt / interval bar chart** | treating intervals as a plain milestone table; equal-length bars faking time |
| **Ranking / comparison** of categories on one metric | **sorted bar** (horizontal when labels are long or items > 8) | pie chart; unsorted bars; decorative bars with meaningless color |
| **Distribution of a single continuous variable** (e.g., price, duration, rating) | histogram, density plot, box plot, violin plot | a mean-only bar chart that hides the distribution |
| **Distribution differences across groups** | box plot, violin plot, faceted histograms | many translucent histograms crammed into one chart, unreadable |
| **Part-to-whole / share** | 100% stacked bar; **donut** only when parts are few and the rough split is all you need; **treemap** when there is hierarchy | pie chart by default; many-slice pie; donut when exact comparison is needed |
| Two or more metrics with **different units / scales** on a shared x-axis | prefer **stacked, aligned small multiples / facets** that share the x-axis and each use their own y-axis; use a **dual-axis** or **bar + line combo** only for **two** metrics where synchronized movement is the point, the pairing is conventional, and the reader will follow it; if only relative change matters, switch to an **indexed line chart** (e.g., first period = 100) | forcing different units onto one axis; an unlabeled dual axis; forcing three or more different-unit metrics onto multiple axes |
| **Relationship** between two continuous variables | scatter (+ reference / fit line); **bubble** to encode a 3rd variable as size | bar chart; drawing a correlation as a categorical comparison |
| **Many small comparisons** sharing the same axes | **small multiples / faceted grid** | one overcrowded multi-series chart; a dozen lines crammed together |
| **Uncertainty / range** of estimates, forecasts, experiment results | pick whatever conveys the range — error bars, confidence bands, quantile bands, box plots | only a mean, a point estimate, or a single forecast line |
| **Spatial distribution** over geography (e.g., city, country, province) | choropleth map, dot map, bubble map | forcing a map when there is no spatial meaning; a plain bar faking a spatial relationship |
| **Multi-dimension capability profile** (few entities, ~4–8 axes) | **radar** for a single entity; for several entities prefer a scoring table, heatmap, or grouped bar | overlapping radars for many entities; a radar with too many axes |
| **Co-occurrence / citation / dependency relationships** among text, categories, or entities | network graph, Sankey, SVG relationship diagram | a bar chart for relational structure |
| **Process / pipeline / causal path** | SVG flowchart, arrow diagram, stage diagram | a line or bar chart for a process |
| **Structure / architecture / hierarchy / ecosystem** | SVG layered / architecture / ecosystem diagram | matplotlib for what is really a structural diagram |
| **Two-dimension trade-off / positioning / quadrant** | 2×2 quadrant; bubble quadrant when there is a third variable | forcing a quadrant without two meaningful dimensions |
| **Selection / prioritization / trade-off** | weighted-scoring table, decision matrix, 2×2, priority table | decorative charts; a chart that encodes no real information |
| **Conversion path / funnel stages** | funnel chart, stage-conversion table, Sankey | a plain line chart for stage drop-off; treating stage order as a time trend |
| **Composition changing over time** | stacked area, 100% stacked area, grouped stacked bars | side-by-side pies; donuts that cannot show change |
| **A single value / current KPI** | metric card, progress bar, compact table; add YoY / MoM when context is needed | forcing a complex chart for one number |
| **Anomalies / outliers / breaks** | line chart with annotation, scatter with highlight, box plot | giving only the average; a smoothed line that hides the anomaly |

*A form can be a **Use** for one job and an **Avoid** for another — a bar chart fits rankings but not a time trend. When your job's row lists a form under Avoid, that is binding: do not use it just because it is a Use elsewhere.*

### Tables
- **A table is not the default form**: a comparison on just a few **numeric** dimensions reads better as a **chart**; a single entity's few facts, a short list, narrative, or a causal argument belongs in **prose / bullets**. A table is the best form only when the information is **dense, mostly categorical/textual, and looked up across many entities**.
- **Tables present, prose analyzes**: a table only lays out the data — the pattern, the so-what, and the driver still come from the surrounding prose.
- **One entity set across many dimensions → one wide table, not one per dimension**: put entities in rows and dimensions in columns, gathering the compared metrics into a single (or a few) wide table(s); don't split into a pile of small tables ("one for revenue, one for headcount, one for share").
- **Source integration**: **no separate "Source" column** — place citation tags directly in the data cells; fill empty cells with `未披露` / `N/A`, and never fabricate to fill a grid.

### Charts
These rules refine a chart whose form the **form-selection table** has already fixed; they never revive a form it excludes.
- **One purpose per chart**: every chart makes a single point; use multiple series only when they answer the same comparison question.
- **Scale for wide-range data**: when values span orders of magnitude, pick one remedy and name it in the caption — a **log scale** (line / scatter / dot only), **normalization / indexing to a base** (when relative change matters more than the absolute level), or a **split view or table** (when groups differ too much for one axis). **Bars are the exception**: axes must stay **linear and zero-based** so bar length stays proportional to value — for bars spanning orders of magnitude use a **dot plot or small multiples, never a log-scaled bar**. State units in the title or axis label.
- **One axis = one metric**: a single axis carries only one metric, unit, and measurement protocol — never stack differently-measured values (different benchmarks or different metrics) on one axis. For plotting several metrics together, see the "different units" row of the **form-selection table**.
- **Sort**: order bars by the primary metric, unless a **natural sequence** fits better (funnel stage, value-chain position, risk level, policy order).
- **Limit categories**: keep to the top 5–8 where possible; use "Other" only when the grouping is analytically honest.
- **Label directly**: put values next to the marks; drop the legend when labels can sit on the marks.
- **Binning**: bins must be exhaustive and non-overlapping; any threshold line must fall on a bin boundary, not cut through a category.
- **Captions**: state only the takeaway the chart actually shows — introduce no claim, causation, or conclusion not in the chart.

### Evidence integrity (every visual artifact — charts and tables alike)
A charted or tabulated value is a claim — held to the same citation, confidence, and scope-fit discipline as prose, and reproducible from an evidence block or an explicit data table in the report.
- **No fabricated precision**: never draw an unknown, undisclosed, or estimated value as an exact point or bar length — show it as a labelled range/estimate or omit it. A static visual artifact must not assert a quantity the evidence reports as dynamic, ranged, or undisclosed.
- **Encode uncertainty**: show known ranges as error bars, bands, or min–max; mark estimated or LOW-confidence values as visually distinct from confirmed ones and say so in the caption.
- **Reconcile with the text**: every entity and number in a visual artifact must match the inventory and prose — within one comparison, no entity may appear only in the visual artifact or only in the text.
- **Disclose the sample**: when a visual artifact shows a subset, state the inclusion criterion; never present a partial or sparse set as if it were the complete comparison.

### Color and visual style
Use restrained, publication-quality palettes. Prefer colorblind-safe, low-saturation colors with one clear accent; avoid rainbow palettes, excessive gradients, and unrelated saturated colors.
- **Scientific / academic reports**: Use Okabe-Ito or Tableau-style colorblind-safe palettes. Good defaults: `#0072B2` blue, `#D55E00` vermillion, `#009E73` green, `#CC79A7` purple, `#E69F00` orange, with neutral gray `#6B7280`.
- **Business / executive reports**: Use a sober base palette with navy/steel/gray and one accent. Good defaults: `#1F4E79` navy, `#5B8DB8` steel blue, `#A7B3C2` blue-gray, `#6B7280` gray, accent `#D9822B` amber or `#2A9D8F` teal.
- **Risk / warning / status**: Use semantic colors consistently: positive `#2E7D32`, warning `#D9822B`, negative `#C62828`, neutral `#6B7280`. Do not use red/green alone when labels or symbols are needed for accessibility.
- **Categorical data**: Use at most 6-8 distinct colors. If there are more categories, group minor categories or switch to a sorted table/bar chart.
- **Sequential data**: Use a single-hue light-to-dark scale. **Diverging data**: use two balanced hues around a neutral midpoint and label the midpoint clearly.
- **Consistency**: Keep the same entity/category color across all charts once assigned, and give reference/baseline items a muted, visually distinct treatment so they are not mistaken for the subjects under study.

### Embedding & self-check
- **Every visual artifact must be accompanied by text** — set up context before it and highlight key observations after it.
- **Embed via public URL (charts and SVG alike)**: after saving to `{topic}_assets/`, convert each image with `file_to_url`, then embed `![caption](public_url)`. **Never embed a local/relative path** (`{topic}_assets/...`) — it won't render in the delivered report.
- **SVG diagrams**: Save images to `{topic}_assets/` with descriptive filenames (e.g., `svg_diagram_2025.svg`); then embed via public URL per the rule above.
- **IPython/matplotlib charts**: Save images to `{topic}_assets/` with descriptive filenames (e.g., `market_share_2025.png`); then embed via public URL per the rule above. When any chart contains Chinese text, define and call the following guard before plotting:
```python
  def _ensure_cjk_font():
      import matplotlib, matplotlib.pyplot as plt
      if not any("CJK" in f or "WenQuanYi" in f for f in matplotlib.rcParams.get("font.sans-serif", [])):
          import subprocess
          subprocess.run(["sed", "-i",
              "s|^#*[[:space:]]*font\\.family[[:space:]]*:.*|font.family: sans-serif|;"
              "s|^#*[[:space:]]*font\\.sans-serif[[:space:]]*:.*|font.sans-serif: Noto Sans CJK SC, WenQuanYi Micro Hei, DejaVu Sans, sans-serif|;"
              "s|^#*[[:space:]]*axes\\.unicode_minus[[:space:]]*:.*|axes.unicode_minus: False|",
              matplotlib.matplotlib_fname()])
          matplotlib.font_manager._load_fontmanager(try_read_cache=False)
          plt.rcParams["font.family"] = "sans-serif"
          plt.rcParams["font.sans-serif"] = ["Noto Sans CJK SC", "WenQuanYi Micro Hei", "DejaVu Sans"]
      plt.rcParams["axes.unicode_minus"] = False

  _ensure_cjk_font()
  # your chart code below
```
  Define `_ensure_cjk_font` once in the first cell; call it at the top of every subsequent chart cell.
- **Pre-embed self-check (every chart and SVG diagram)**: before embedding, re-verify that the rules under **Choosing the form**, **Charts**, and **Evidence integrity** all hold for it; then confirm three more — **the embedded `src` is a public URL (`http…`), not a local path**; value channels (length, area, position) carry a magnitude, not a date; labels and legend readable, nothing overflowing or overlapping. Fix or switch form before embedding — never ship a wrong-form, unreadable, or local-path one.

## Citation & Formatting

- **Citation Format**: Use the inline citation tag `[(source_name)](url)` after every factual statement. Multiple sources: `[(TrendForce)](https://...) [(IDC)](https://...)`. No index-based references.
    - *Note*: Do not use citations for creative/non-formal writing.
    - **Key numbers rule**: Every critical number (market size, growth rate, share, price, valuation metrics, technical specs, etc.) **must** include a citation with a specific source URL (not a homepage) and the data date. A number without a traceable source is worse than no number at all.
    - **Professional Skill data citation rule (MANDATORY)**: Data points returned by professional data Skills (`openecon-data`, `fred-data-skill`, `worldbank-data`, `frankfurter-data`, `stock-data-skill`, `tianyancha-data`, `tmdb-data-skill`, `qimai-data-skill`, `weko-data`, etc.) **must** be cited using the underlying **provider** (FRED / World Bank / Frankfurter / 天眼查 / TMDB ...), never the Skill name itself. The Skill is the retrieval channel; the provider is the actual source.
        - **URL provenance constraint (anti-hallucination)**: a citation's URL **may come only from the three real channels below**; never spell out or guess a provider's URL shape from the model's world knowledge:
            1. **A URL / link field literally present in the Skill's returned payload** (e.g. `source_url`, `detail_url`, `landing_page`, `api_url`) — copy it verbatim.
            2. **An indicator_id / entity_id literally present in the payload**, combined with a URL template **explicitly given** in the Skill's `SKILL.md` (e.g. `https://fred.stlouisfed.org/series/{id}`) — the template must come from the Skill's own docs, not the model's memory.
            3. **A provider landing page actually retrieved afterward via `search_web` / `fetch_web`** — copy the URL from the search result as-is.
        - When none of the three channels yields a specific URL, **do not fabricate one**: per Red Line 2, mark `[(provider · indicator_id, as_of_date)](source unavailable)` and record "URL missing" in the evidence block. Better to mark it unavailable than to let the model invent a plausible-looking URL.
        - **Format**: `[(provider · indicator_id_or_entity, as_of_date)](url_from_above_three_channels_only)`.
        - ❌ Bad: `[(openecon-data)](https://...)` — the Skill name is not a source.
        - ❌ Bad: `[(FRED)](https://fred.stlouisfed.org)` — a homepage URL, missing the series id and date.
        - ❌ Bad: the model writes `https://fred.stlouisfed.org/series/GDPC1` from memory, but that URL is neither in the Skill payload nor search-verified — treat it as a fabricated URL.
    - **Citation position rule**: The citation tag must sit **immediately before the sentence-ending punctuation**, with no space between the closing `)` and the punctuation. Citations belong to the sentence they support — never let one float between two sentences as a "drop-in" reference.
        - ✅ `亚马逊1994年由Jeff Bezos创立 [(Wikipedia)](https://...)。1997年以$18/股上市 [(SEC S-1)](https://...)。`
        - ❌ `亚马逊1994年由Jeff Bezos创立。 [(Wikipedia)](https://...) 1997年以$18/股上市。` — citation is orphaned between two sentences; reader cannot tell which claim it supports.
- **Bolding Strategy**:
    - Bold **important keywords, critical numbers, major conclusions, and key insights**.
    - **Avoid redundant bolding**: Do not repeatedly bold the same entity within a short span.
- **References**: No separate references section needed — all sources are already inline via `[(source)](url)` tags.

## Red Lines (Non-Negotiable)

Never cross these. The detailed how-to lives in the sections above; this is the list you do not violate under any circumstance.

1. **No fabrication** — no source = it does not appear; mark `[INFO_GAP]` instead. A number without a source is worse than no number.
2. **No fake URLs** — a citation URL must be a specific page, never a homepage, never invented. If none is available, mark `[(source_name)](source unavailable)`.
3. **Citation format is mandatory** — `[(source_name)](url)` after every factual statement; multiple sources chain. No numbered references, no separate reference section.
4. **Key numbers carry a data date** — every critical number's citation must include the publication date or statistical period; a bare number is unacceptable.
5. **Strict time handling** — the report's completion date and the filename date both come from bash `date`; factual dates in the body must be citation-backed; no vague time phrasing.
6. **Filenames follow the template** — `{topic}_plan.md` / `{topic}_report.md` / `{topic}_evidence.md` / `{topic}_outline.md` / `{topic}_assets/`; `{topic}` is localized but suffixes stay English (never `_证据.md`); no generic placeholders.
7. **Never lose the user's original question** — the report answers the core question directly, without drifting.
8. **Source priority is irreversible** — primary/official > professional/vertical media > general UGC > SEO/AI content farms (never citable).
9. **No conclusions before search** — every factual statement is grounded in search results, not internal knowledge.
10. **Never suppress contradictions** — record both claims and both sources faithfully; do not present selectively.
11. **One claim per evidence block** — each block covers one claim about one subject; never merge.
12. **The report is traceable** — every major claim maps back to a block in the evidence file.
13. **Evidence file precedes the report** — after the search rounds, write all evidence blocks to `{topic}_evidence.md` with `write_file` before writing the report.
14. **Images embed only as public URLs** — every `![](…)` uses a `file_to_url` public URL; a local/relative path (`{topic}_assets/x.png`) won't render and counts as a missing chart.
15. **URL verbatim fidelity** — every citation URL must be copied character-for-character from the source (search result payload, Skill payload, or fetched page). Never add/remove trailing slashes, never "normalize" or "complete" a URL. If the source says `https://example.com/docs`, write exactly that — not `https://example.com/docs/`

## Output & Naming

`{topic}` is a concise, descriptive phrase that serves as both the file name prefix and the report title (`#` heading).

**Naming rules:**
- Language matches the query (Chinese query → Chinese topic, English query → English topic)
- Never include the user's name
- Concise and descriptive — no decorative prefixes or explanatory suffixes
- File name: underscores for spaces, no special characters (`/\:*?"<>|`)
- **Suffixes are fixed English literals**: only `{topic}` is localized; `_plan.md` / `_evidence.md` / `_outline.md` / `_report.md` / `_assets/` are never translated (not `…_证据.md`)

**Examples:**
| Query | `{topic}` |
|-------|-----------|
| 内存涨价原因深度分析 | `内存涨价深度解析` |
| EU AI Act impact on startups | `EU_AI_Act_Startup_Impact` |

**Working directory:** write all output files into the current working directory (from bash `pwd`); use relative paths or the `pwd`-resolved absolute path, never `/workspace/` or another absolute path (`write_file` rejects paths outside it).

**Output files:**
- Plan checklist: `{topic}_plan.md`
- Evidence inventory: `{topic}_evidence.md`
- Report outline: `{topic}_outline.md`
- Final report: `{topic}_report.md`
- Charts directory: `{topic}_assets/` — all generated images saved here (IPython/matplotlib charts + SVG diagrams)

**Markdown floor**: {topic}_report.md must always be produced, regardless of whether a richer delivery target (Feishu, Notion, etc.) is available or succeeds. Never substitute the evidence file for the report.