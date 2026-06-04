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
dependency:
  python:
    - httpx>=0.27
---

# Deep Research Pro

Execute a high-intensity research protocol focused on exhaustive discovery, continuous recursive reflection, and high-density analytical reporting with structured evidence blocks.

## Pre-Flight: Epistemic Reset Rule

Before any analysis or search begins:

1.  **Assume internal knowledge is outdated or incomplete.** Retrieve the current date and time using the bash tool (`date`).
2.  **Time-awareness**: When the user's query implies a time constraint (e.g., "2026 Q1", "latest", "current", "recent 6 months"), treat that implied time range as a hard constraint. Search queries must target that window; findings outside it must be flagged as `[OUT-OF-WINDOW]`.
3.  **Search language rule**: Issue search queries in the same language as the user's message.
4.  **No claims before evidence.** Avoid generating factual statements before search outputs are reviewed.

## 📂 Output Paths & Naming

`{topic}` is a concise, engaging phrase that serves as both the file name prefix and the report title (`#` heading).

**Naming rules:**
- Language matches the query (中文 query → 中文 topic, English query → English topic)
- Never include the user's name
- Concise and engaging — no decorative prefixes or explanatory suffixes
- File name: underscores for spaces, no special characters (`/\:*?"<>|`)

**Examples:**
| Query | `{topic}` |
|-------|-----------|
| 内存涨价原因深度分析 | `内存涨价深度解析` |
| EU AI Act impact on startups | `EU_AI_Act_Startup_Impact` |

**Output files:**
- Evidence inventory: `{topic}_evidence.md`
- Final report: `{topic}_report.md`
- Charts directory: `{topic}_assets/` — all generated images saved here (IPython charts + SVG diagrams)

**Markdown floor**: {topic}_report.md must always be produced, regardless of whether a richer delivery target (Feishu, Notion, etc.) is available or succeeds. Never substitute the evidence file for the report.

## 🚀 Research & Discovery Phase (The 15+ Step Loop)

1.  **Iterative Search**: Perform **at least 15 search steps** to ensure comprehensive coverage. Follow a **coarse-to-fine** 3-stage progression — **(1) Landscape**: macro overview + structural mapping, **(2) Deep Dives**: targeted investigation per dimension — go vertical on key dimensions: trace data to its methodology, track trends across time periods, and investigate causal mechanisms, **(3) Verify & Fill**: cross-verification + gap filling. Allocate steps across stages based on topic complexity; earlier stages should build the map, later stages should stress-test it. Avoid keyword redundancy; ensure each round brings substantial new information.
    - **Maximize parallel search**: For independent topics/dimensions, launch **as many parallel `search_web` calls as possible**, each filled with the maximum allowed queries. Sequential calls only when the next query depends on previous results.
2.  **Credibility & Verification**: Prioritize authoritative sources (government sites, academic databases, peer-reviewed journals, official filings, major media). **Never fabricate data.** Every statistic and claim must be accurate and traceable. Avoid content farms, anonymous blogs, and SEO aggregators.
    - **Source selection rule**: When multiple sources cover the same fact, prefer the more **authoritative** and more **recent** one for citation. Prefer primary/official sources over secondary reporting, and professional/vertical media over general UGC platforms. Treat SEO-driven or AI-generated content farms as unreliable.
    - **Source diversity**: Ensure evidence draws from **multiple source types** (official documents, academic papers, industry reports, media, corporate filings, expert commentary). Avoid over-reliance on any single type.
    - **Selective deep fetch**: Only fetch when the snippet alone is **insufficient** to support the claim — if the snippet already contains the complete data point, skip the fetch. When fetching is needed, prioritize: HIGH confidence candidates that need confirmation, numerical claims where the snippet is truncated, contradictions that require full-context comparison, and **direct quotes from key decision-makers** (CEOs, regulators, industry leaders) that provide unique insight.
3.  **Recursive Reflection**: After EACH search round, output a **Thinking Process** and a **Summary**.
    - **Thinking**: Reflect on content found, identify unmet needs, and plan the next specific step. Check **dimension coverage** — are there important angles not yet explored, or unexpected dimensions surfaced during search that deserve follow-up? Check whether the topic involves **time-sensitive quantitative indicators** (e.g., stock prices, market caps, exchange rates, rankings) that require dedicated real-time queries.
    - **Summary**: Concise recap of key findings.
    - *Constraint*: Both sections must be **short and concise**.
4.  **Confidence Tagging**: Tag every significant finding with one of three confidence levels:
    - `[HIGH]` — Confirmed by ≥2 independent authoritative sources with consistent data.
    - `[MEDIUM]` — Confirmed by 1 authoritative source, or multiple secondary sources.
    - `[LOW]` — Weak sourcing, single unverified claim, or blog-level evidence.
5.  **Contradiction Handling**: Conflicts between sources are signal, not noise. Never suppress contradictions. When conflicting data is found, explicitly document both claims, both sources, and the nature of the conflict (statistical / interpretive / temporal). Temporal conflicts must be flagged as `[TEMPORAL-CONFLICT: source A = period X; source B = period Y]`.

## Structured Evidence Block

Use the following **7-field format** for every piece of significant evidence:

```
Claim: [the specific factual claim — plain text, no URLs]
Source: [source name / file name]
URL: [source URL / "File: {filename}, Section: {section}"]
Date: [publication date / "N/A" for files]
Excerpt: [verbatim raw excerpt — no paraphrasing]
Context: [surrounding context that affects interpretation]
Confidence: [HIGH / MEDIUM / LOW]
```

**One block per claim** — do not combine multiple entities or unrelated facts into a single block. Each block should be atomic: one specific claim about one subject.

### Incremental Collection

- **During search**: After each search round's reflection, immediately **append** any valuable findings as evidence blocks to `{topic}_evidence.md`. Keep the bar low for inclusion at this stage — capturing more is better than losing data to context compaction.
- **After all search steps**: Perform a **final consolidation pass** on `{topic}_evidence.md` — deduplicate, upgrade/downgrade confidence levels based on cross-verification, and remove entries that are no longer relevant.

Every major claim in the final report must map back to an evidence block in this file.

**Date rules:** Record the publication date, not access date. If no date: `Date: N/A [accessed YYYY-MM-DD]`.

**Source differentiation:**
- `[SEARCH-SOURCED]` — evidence from external search
- `[FILE-SOURCED]` — evidence from user-provided files
- `[MIXED]` — cross-validated across both channels

## 📝 Report Engineering Standards

### 1. Structural Logic & Opening
#### Executive Summary
Every report must open with a 300-500 word summary that satisfies **all** of the following requirements:

1. **Directly answers the core question.** No "this report will explore..." preamble.
2. **States key findings with supporting numbers.** Concrete figures, not hedged language.
3. **Delivers the bottom-line judgment.** One sentence a decision-maker would quote.
4. **Uses a layered, modular structure.** Parallel entities across parallel attributes must be rendered as tables or tight lists — never prose.

**Success criterion:** a reader who only reads this section gets 80% of the report's value.

#### Style Adaptation
- **Default:** strict academic report format.
- **If a specific style is implied** (story, interview, case narrative, etc.): adhere to that style instead.
- **Omit** generic Introduction/Background sections unless explicitly required.

### 2. Depth and Analysis (Mode-Based)
- **Academic/Survey Mode**:
    - Prioritize comprehensive fact-based detail. Include full definitions, formulas, statistical indicators (CI, metrics), and baseline comparisons.
    - Avoid speculative interpretation; ensure all statements are supported by references.
- **Lifestyle/Practical Mode**:
    - Incorporate observations, human insights, Pros/Cons, and actionable trade-offs.
    - Reflect on implications and explain why certain patterns matter.
- **Insight rule**: Key paragraphs must answer "so what" — don't just state facts, explain why they matter and what impact they have. Avoid hollow summaries; replace vague claims with specific facts and data. When analyzing multiple comparable entities, **focus on differentiators rather than repeating shared patterns** — state the common pattern once, then highlight what makes each entity unique.
- **Confidence in report**: LOW confidence claims must be qualified with hedging language (e.g., "preliminary data suggests...", "unverified reports indicate..."). Do not present LOW confidence evidence with the same certainty as HIGH.
- **Tone**: No marketing speak, no sloganeering (e.g., "industry-leading", "paradigm shift", "reshaping the future"). Be professional, restrained, and confident.
- **Actionable conclusions**: The report must end with clear conclusions that include: (1) explicit judgments with supporting evidence, (2) concrete recommendations or next steps with priority, (3) applicable scope — state under what conditions the conclusions hold, key uncertainties, and what evidence would change the judgment.

### 3. Length and Paragraph Constraints
- **Total Volume**: Aim for **5,000+ words**; scale with topic complexity. Information density matters more than raw length.
- **Paragraph Rules**:
    - Each paragraph must be **at least 100 words** (max 1,000 words).
    - **Subsection Rule**: Every subsection (e.g., `## 3.1`) MUST contain **more than one paragraph**.
- **Natural Transitions**: Avoid mechanical enumeration patterns (e.g., "First, second, third", "首先、其次、最后"); use natural transitions between ideas.

### 4. Mandatory Table Architecture
- **Usage**: Use tables for comparisons, data summaries, and structured results. **Do not use tables for narrative analysis** — entity deep-dives, causal explanations, and arguments should be written as prose. Vary presentation formats across sections; avoid repeating the same table layout throughout the report.
- **Centralized Comparison**: Aggregate recurring entities, models, or metrics from across different sections into single, coherent comparison tables.
- **Source Integration**: **Do not include a separate "Source" column**. Place citation tags directly within the data cells.

## ⚖️ Formatting & Citation Rules

- **Citation Format**: Use the inline citation tag `[(source_name)](url)` after every factual statement. Multiple sources: `[(TrendForce)](https://...) [(IDC)](https://...)`. No index-based references.
    - *Note*: Do not use citations for creative/non-formal writing.
    - **Key numbers rule**: Every critical number (market size, growth rate, share, price, valuation metrics, technical specs, etc.) **must** include a citation with a specific source URL (not a homepage) and the data date. A number without a traceable source is worse than no number at all.
    - **Citation position rule**: The citation tag must sit **immediately before the sentence-ending punctuation**, with no space between the closing `)` and the punctuation. Citations belong to the sentence they support — never let one float between two sentences as a "drop-in" reference.
        - ✅ `亚马逊1994年由Jeff Bezos创立 [(Wikipedia)](https://...)。1997年以$18/股上市 [(SEC S-1)](https://...)。`
        - ❌ `亚马逊1994年由Jeff Bezos创立。 [(Wikipedia)](https://...) 1997年以$18/股上市。` — citation is orphaned between two sentences; reader cannot tell which claim it supports.
- **Bolding Strategy**:
    - Bold **important keywords, critical numbers, major conclusions, and key insights**.
    - **Avoid redundant bolding**: Do not repeatedly bold the same entity within a short span.
- **Rich presentation**: The report should be visually rich. **Default to visual/structured formats over prose** — use tables for comparisons, SVG diagrams for relationships/flows, IPython charts for data trends, LaTeX (`$...$`) for precise definitions or metrics, and code blocks for technical specifics. A report with only plain text paragraphs is underdelivering. Every major section should contain at least one non-prose element.
    - **Visualization tools**: Use **SVG** for structural/relational diagrams (flowcharts, sequence diagrams, architecture, causal chains) — see `references/svg_diagram_guide.md` for specs and
  delivery workflow. Use **IPython** for numerical/statistical charts (trends, bar charts, distributions). Prioritize programming tools for all calculations.
- **Visuals**: Every chart or visualization **must** be accompanied by text — set up context before the figure and highlight key observations after it.
    - **SVG diagrams**: Save images to `{topic}_assets/` with descriptive filenames (e.g., `svg_diagram_2025.svg`).
    - **IPython charts**: Save images to `{topic}_assets/` with descriptive filenames (e.g., `market_share_2025.png`). After saving, convert each image to a public URL via `file_to_url`, then embed in the report using `![caption](public_url)`. When any chart contains Chinese text, define and call the following guard before plotting:
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
- **References**: No separate references section needed — all sources are already inline via `[(source)](url)` tags.

## 🛠 Execution Workflow
1. **Epistemic Reset**: Get current date, check time constraints.
2. **Query Understanding**: Refer to `references/query_decomposition.md`. Identify the core question, decision intent, task type, and inferred implicit dimensions. Then conduct **1-3 broad exploratory searches** to validate and expand the initial dimensions — **only scan titles and snippets**, do not fetch full pages or record evidence blocks. These searches do not count toward the 15-step minimum. **Output the analysis result explicitly** — core question, decision intent, task type, and the updated dimension list — before starting the Explore step. This output serves as the baseline for dimension coverage checks during Recursive Reflection.
3. **Explore**: Conduct a minimum of 15 search rounds with concise recursive reflections, confidence tagging, contradiction handling, and **incremental evidence collection** (append to `{topic}_evidence.md` after each round).
4. **Evidence Consolidation**:
   - Deduplicate and calibrate the evidence blocks in `{topic}_evidence.md`.
   - **URL batch verification**: Install dependencies if needed (`pip install -r scripts/requirements.txt`), then verify all URLs:
     ```bash
     python scripts/verify_urls.py {topic}_evidence.md
     ```
     Only ❌ FAIL results need action — append `[URL-UNVERIFIED]` to that evidence block's Confidence field (e.g., `Confidence: MEDIUM [URL-UNVERIFIED]`). Do not delete the block. ✅ PASS and ⚠️ UNCERTAIN are both considered accessible (UNCERTAIN means anti-bot block, URL is valid).
5. **Outline**: Draft a section outline and map evidence blocks to each section — ensure every section has sufficient support and no collected evidence is left unused. **If critical gaps are found (dimensions identified in Query Understanding but lacking evidence, or `[URL-UNVERIFIED]` blocks needing replacement sources), conduct targeted supplementary searches before proceeding to Write.**
6. **Write**: Generate the report at `{topic}_report.md`. Follow the report engineering standards, embed visualizations (SVG diagrams, IPython charts, tables, LaTeX) as needed, and save generated images to `{topic}_assets/`. When generating SVG diagrams, follow `references/svg_diagram_guide.md`. **Key reminder**: every factual statement must have `[(source_name)](specific_url)` — no exceptions, no homepage URLs, no fabricated sources. For `[URL-UNVERIFIED]` evidence with no verified alternative, either use a domain-level URL or omit the claim if LOW confidence.
