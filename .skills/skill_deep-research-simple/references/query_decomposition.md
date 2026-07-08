# Query Decomposition Guide

Use this guide during the **Query Understanding** step to create an initial analysis framework before exploratory searches, then revise it after scanning exploratory search titles and snippets.

---

## 1. Concrete Scope

Answer these scope questions before any search. These fields prevent the research from drifting beyond the user's actual request.

| Field | Requirement |
|---|---|
| **Time scope** | Required. Extract the explicit or implied time range. If absent, write "Not specified" and state whether current data is still required. |
| **Geographic scope** | Required. Extract the country, region, city, jurisdiction, or market scope. If absent, write "Not specified" or a justified default such as "global". |
| **Target object** | Required. Identify the specific entity, population, industry, product, technology, policy, market, or phenomenon being studied. |
| **Environment / operating context** | Optional. Extract only when the user states or strongly implies deployment, usage, regulatory, budget, technical, organizational, or market-context constraints. Do not invent one if absent. |

---

## 2. Intent and Coverage

After scope is fixed, answer these questions as the initial decomposition:

| Field | Requirement |
|---|---|
| **Core question** | One sentence — what exactly needs to be answered? |
| **Decision intent** | What will the reader DO with this report? (e.g., vendor selection, investment decision, strategic planning, policy evaluation, competitive response, learning) |
| **Task type** | Which category below best matches? (technology survey, competitive analysis, company due diligence, investment/equity research, policy research, trend forecast, market sizing, product / solution selection, industry landscape, or other) |
| **Must-have coverage** | User-explicit requirements and logically mandatory components of the request. These outrank inferred dimensions. |
| **Inferred dimensions** | Professional dimensions a knowledgeable reader would expect to see, even if not explicitly requested. Use the implicit dimensions table below + the general expansion rules. |
| **Exclusions** | Topics, geographies, time periods, entities, or interpretations that are explicitly excluded or implied out of scope by the concrete scope. |
| **Ambiguities** | Constraints that remain unclear and could materially affect the search strategy or final judgment. |

---

## 3. Implicit Dimensions

### 3.1 General Expansion Rules (apply to all task types)

- **Entity → products/services → value chain position → upstream suppliers and downstream customers**
- **Listed company → latest financials, current valuation (sector-appropriate metrics: PE/PB/PS/EV-EBITDA), institutional consensus, and risk factors**
- **Industry trend → affected players across the full value chain, with beneficiaries and losers at each layer**
- When the query does not clearly match any task type below, **default to the widest reasonable scope**.

### 3.2 Task-Type Dimension Checklist

| Task Type | Required Implicit Dimensions |
|-----------|------------------------------|
| **Technology survey** | Timeline (origin → current → future), mainstream vs niche approaches, SOTA markers, research gaps, mechanism-level explanations, failure cases / counter-examples |
| **Competitive analysis** | Comparison table, product / pricing / customers / financials / team for each player, market share / positioning, "implications for us", win/loss mechanisms |
| **Company due diligence** | Ownership structure, financials (recent quarterly + annual), team & management, product portfolio, market position, risks + counter-factual ("what if X fails") |
| **Investment / equity research** | Latest quarterly earnings, current stock price, current PE/PB (no annual forecast substitutes), recent announcements, institutional holdings/consensus, catalysts & risks, valuation comparison with peers, **portfolio positioning / priority ranking, time-horizon outlook (short / medium / long term), and reversal signals to monitor** |
| **Policy research** | Central / local / industry-level timeline, affected stakeholders (beneficiaries / losers / neutral), policy intent vs side effects, implementation status / enforcement cases |
| **Trend forecast** | Data-backed arguments, contrarian / opposing views, uncertainty ranges, leading indicators, reversal conditions, historical analogies |
| **Market sizing** | TAM / SAM / SOM breakdown, methodology / data source caliber, growth drivers, scenarios where drivers fail, competitive landscape summary (key players and shares) |
| **Product / solution selection** | Evaluation criteria with priorities, feature comparison across candidates, pricing / licensing models, integration complexity, community / ecosystem maturity, migration cost, decision framework ("choose A if..., choose B if...") |
| **Industry landscape** | Value chain mapping (upstream → midstream → downstream), key players and positioning at each layer, competitive dynamics, entry barriers, recent M&A / funding events, technology and regulatory drivers, emerging disruptors |

---

## 4. Decomposition Principles

### 4.1 Scope before expansion

Always preserve the user's time scope, geographic scope, target object, must-have coverage, and exclusions before adding inferred dimensions. Do not let a broad task-type checklist override concrete user constraints.

### 4.2 Coverage over precision

It is better to cover a dimension shallowly than to miss it entirely. When in doubt, **include it** — depth can be added during the Deep Dives stage.

### 4.3 MECE

Dimensions should be **mutually exclusive** (minimal overlap) and **collectively exhaustive** (no critical gaps):
- If two dimensions cover similar ground → **merge** them.
- If a gap is discovered → **add** a new dimension.

### 4.4 Granularity floor

Every sub-question must be **specific enough to form 1-2 concrete search queries**. If it cannot, split it further.

Example:
- Too coarse: "Analyze the upstream" → cannot form a query
- Right level: "What are the top 3 DRAM wafer suppliers and their capacity allocation in 2026?" → directly searchable