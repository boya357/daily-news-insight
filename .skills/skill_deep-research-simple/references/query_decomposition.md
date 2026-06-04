# Query Decomposition Guide

Use this guide during the **Query Understanding** step to decompose the user's question into a complete analysis framework before searching.

---

## 1. Core Analysis

Answer these 4 questions explicitly before starting any search:

| # | Question | Purpose |
|---|----------|---------|
| 1 | **Core question** | One sentence — what exactly needs to be answered? |
| 2 | **Decision intent** | What will the reader DO with this report? (e.g., vendor selection, investment decision, strategic planning, policy evaluation, competitive response, learning) |
| 3 | **Task type** | Which category below best matches? (technology survey, competitive analysis, company due diligence, investment/equity research, policy research, trend forecast, market sizing, or other) |
| 4 | **Inferred dimensions** | What dimensions would a knowledgeable reader expect to see, even if not explicitly requested? Use the implicit dimensions table below + the general expansion rules. |

---

## 2. Implicit Dimensions

### 2.1 General Expansion Rules (apply to all task types)

- **Entity → products/services → value chain position → upstream suppliers and downstream customers**
- **Listed company → latest financials, current valuation (sector-appropriate metrics: PE/PB/PS/EV-EBITDA), institutional consensus, and risk factors**
- **Industry trend → affected players across the full value chain, with beneficiaries and losers at each layer**
- When the query does not clearly match any task type below, **default to the widest reasonable scope**.

### 2.2 Task-Type Dimension Checklist

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

## 3. Decomposition Principles

### 3.1 Coverage over precision

It is better to cover a dimension shallowly than to miss it entirely. When in doubt, **include it** — depth can be added during the Deep Dives stage.

### 3.2 MECE

Dimensions should be **mutually exclusive** (minimal overlap) and **collectively exhaustive** (no critical gaps):
- If two dimensions cover similar ground → **merge** them.
- If a gap is discovered → **add** a new dimension.

### 3.3 Granularity floor

Every sub-question must be **specific enough to form 1-2 concrete search queries**. If it cannot, split it further.

Example:
- Too coarse: "Analyze the upstream" → cannot form a query
- Right level: "What are the top 3 DRAM wafer suppliers and their capacity allocation in 2026?" → directly searchable
