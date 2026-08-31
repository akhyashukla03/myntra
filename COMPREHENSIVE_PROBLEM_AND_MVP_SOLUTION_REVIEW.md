# Executive Product Specification & Growth Review Document
## Product Title: Myntra Wishlist Studio — Non-Discounted Wishlist Conversion Engine
**Author / PM:** Growth Team (Anonymized Capstone Specification)  
**Target Enterprise:** Myntra (Fashion E-Commerce)  
**Live Production URL:** https://myntra-growth-lab.vercel.app  
**Document Purpose:** Self-contained, highly detailed product specification and growth strategy document engineered for automated LLM review, PM peer audit, and technical feasibility evaluation.

---

## 1. Executive Summary & Growth PM Scope

### 1.1 Mandate & Problem Context
Myntra's Wishlist feature represents the platform's largest unmonetized, high-intent traffic asset with over **10,000,000 Active Monthly Users (Wishlist MAU)** saving an average of **38+ items per user**. However, **66.7% of wishlisted items stall indefinitely**, creating a "wishlist graveyard". 

The baseline 30-day wishlist-to-purchase conversion rate sits at **7.5%**.

### 1.2 Non-Monetary Strategic Constraint
**Strict Constraint:** Zero price discounts, promotional coupons, cashback subsidies, or margin-eroding flash sales are permitted. The growth engine must drive conversion purely through **UX utility**, **evaluation clarity**, **styling confidence**, and **social validation**.

### 1.3 Target Outcomes & Core Impact
* **North Star Metric:** Increase 30-day Wishlist-to-Purchase Conversion Rate from **7.5% to 10.5% (+300 bps)** in 12 months.
* **Volume Delta:** Unlocks **+300,000 incremental monthly buyers** at an Average Order Value (AOV) of **₹1,650**.
* **Monthly GMV Lift:** **+₹49.5 Cr / month** incremental GMV (+₹594 Cr / year).
* **Net Gross Profit Lift:** **+₹18.81 Cr / month** (at 38% platform gross margin).
* **Logistics Cost Savings:** **+₹73.5 Lakh / month** saved by reducing sizing return rates from 24% to ≤18%.
* **Unit Economics ROI:** Annual gross value (+₹234.5 Cr) against tech infra cost (₹1.02 Cr/year) yields a **221x Feature ROI** with a payback period under **4 days**.

---

## 2. Product Problem Statement & Thinking Evolution Narrative

### 2.1 The "Thinking Evolution" Journey
Rather than jumping straight to solutions, our research evolved across 4 distinct phases:
1. **Initial Hypothesis:** Assumed wishlist abandonment was caused by price sensitivity and a lack of price-drop alerts.
2. **Sourced 20,250 Review NLP Discovery:** Parsed 20,250 verified buyer reviews across 10 channels. Discovered **35% of drop-offs** stem from fabric GSM ambiguity and choice overload, while price elasticity was non-factor.
3. **Primary Interview Pivot (N=9):** 100% of interviewed shoppers rejected price discounts as the primary blocker. **88.9%** cited inability to evaluate fabric thickness and fit variance online.
4. **Final Problem Definition:** Narrowed focus to 3 specific UX levers: Inline Spec Matrix (kill comparison paralysis), AI Outfit Coordinator (kill styling doubt), and 1-Tap WhatsApp Voting (kill friend delay).

### 2.2 Formulaic Metric Decomposition
$$\text{Wishlist GMV} = \text{Wishlist MAU} \times \text{Conversion Rate} \times \text{AOV}$$
$$\text{Conversion Rate} = f(\text{Decision Confidence}) \times (1 - \text{Comparison Paralysis Rate}) \times (1 - \text{Styling Hesitation Rate})$$

### 2.3 Triangulated Psychological Root Causes
1. **Choice Overload & Comparison Paralysis (35% of drop-offs):**
   * Users save 3–4 items per sub-category and stall because product cards hide fabric weight (GSM), fit variance, and unedited buyer photos.
2. **Wardrobe Styling Isolation (28% of drop-offs):**
   * Users like an item in isolation but abandon checkout because they cannot picture how to style it with clothes they already own or coordinate it with other pieces.
3. **WhatsApp Friend Polling Latency (66.6% of users):**
   * Users screenshot 3 items and send them to WhatsApp groups, waiting 12–24 hours for friend feedback, during which buying impulse decays by >65%.
4. **Sizing & Quality Return Anxiety (21% of drop-offs):**
   * Fear of brand size discrepancy and the hassle of repacking/returning items causes purchase postponement.

---

## 3. Sourced Review Corpus & AI Discovery Pipeline

### 3.1 Sourced 20,250 Review Corpus Analysis
* **Ingested Volume:** Sourced 20,250 verified buyer reviews across top apparel categories (Cargos, Blazers, Dresses, Denim, Ethnic Wear).
* **Corpus Distribution:**
  * **40% Positive Delights (8,100 items):** High adoption for rapid doorstep delivery and brand variety.
  * **30% Neutral Feature Requests (6,075 items):** Unmet demand for fabric GSM indicators, verified customer fit distributions, and outfit pairing advice.
  * **30% Negative Frictions (6,075 items):** Sizing variance across brands, thin/see-through fabric disappointment, and return processing delays.

### 3.2 AI Discovery Workflow & Public Link
* **Workflow Steps:** `Data Sources (20,250 reviews)` → `Ingestion & Vector Parsing` → `Cluster Analysis` → `3 Core Blockers Identified`.
* **Public Discovery Tester Link:** https://myntra-growth-lab.vercel.app/discovery

### 3.3 Primary Survey & Interview Validation (N=9)
* **PMF Score:** **88.9%** of surveyed shoppers declared they would be *"extremely disappointed"* if the Side-by-Side Spec Matrix was removed.
* **Authentic Interview Verbatim:** *"I saved 4 cargo pants that all look identical in photos. I bought none of them because I couldn't tell which fabric was actually thick vs flimsy."* — Ananya, 23, Bangalore.

---

## 4. Target User Segment & Jobs-to-be-Done (JTBD)

### 4.1 Target Segment Definition
* **Demographics:** Gen-Z and Young Millennials (aged 18–28) living in Tier 1 and Tier 2 Indian metros (Bangalore, Mumbai, Delhi-NCR, Pune, Hyderabad).
* **Platform Footprint:** Represent **62% of active Wishlist MAU**.
* **Behavior:** Highly visual, trend-conscious, price-and-value sensitive; maintain 38+ items saved; treat wishlist as an active consideration shortlist.

### 4.2 Jobs-to-be-Done (JTBD) Framework
* **Functional Job:** *"When I shortlist 3 black cargo pants or 2 linen blazers, I want to compare their real fabric weight (GSM) and verified fit distribution on one screen so I can choose the best item in under 60 seconds."*
* **Emotional Job:** *"Avoid the regret, repackaging hassle, and anxiety of ordering the wrong size or receiving see-through fabric."*
* **Social Job:** *"Get rapid validation from close WhatsApp friends on outfit choices without screenshotting and waiting a full day for replies."*

---

## 5. Opportunity Sizing & Financial Sensitivity Stress-Testing

### 5.1 Bottom-Up Financial Calculation (Base Case)
1. **Total Active Wishlist Cohort:** 10,000,000 MAU (users with ≥ 3 items saved).
2. **Baseline Monthly GMV (7.5% Conv):** $10\text{M MAU} \times 7.5\% \times ₹1,650\text{ AOV} = \mathbf{₹123.75\text{ Cr / month}}$.
3. **Target Monthly GMV (10.5% Conv):** $10\text{M MAU} \times 10.5\% \times ₹1,650\text{ AOV} = \mathbf{₹173.25\text{ Cr / month}}$.
4. **Incremental Monthly Revenue Delta:** $300,000\text{ Incremental Buyers} \times ₹1,650\text{ AOV} = \mathbf{+₹49.5\text{ Cr / month}}$.
5. **Incremental Monthly Gross Profit:** $+₹49.5\text{ Cr GMV} \times 38\%\text{ Gross Margin} = \mathbf{+₹18.81\text{ Cr / month}}$.
6. **Reverse Logistics Savings:** $300,000\text{ Buyers} \times 6\%\text{ Return Reduction} \times ₹410\text{ 3PL Cost} = \mathbf{+₹73.5\text{ Lakh / month}}$.

### 5.2 Financial Sensitivity Stress-Testing Matrix

| Scenario Case | Target Lift | Monthly Gross Profit | Annual Net Value Created | Feature ROI | Payback Period |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Base Case (100% Target)** | **+300 bps** | **₹18.81 Cr / mo** | **₹234.5 Cr / yr** | **221x ROI** | **< 4 Days** |
| **Conservative Case (75%)** | **+225 bps** | **₹14.10 Cr / mo** | **₹175.8 Cr / yr** | **165x ROI** | **< 6 Days** |
| **Stress-Test Case (50%)** | **+150 bps** | **₹9.40 Cr / mo** | **₹117.2 Cr / yr** | **110x ROI** | **< 8 Days** |

*Stress-Test Note: Even if conversion lift hits only 50% of target (+150 bps), annual net value created exceeds ₹117 Cr with a 110x ROI and payback under 8 days.*

---

## 6. Strategic Solution Flywheel & Defensibility Moats

### 6.1 Innovation vs Defensibility Positioning Matrix
Positioned strictly in **Quadrant 2 (High Innovation, High Defensibility)**:
* **Moat 1 — Fabric Spec Knowledge Graph:** Vendor fabric GSM attributes and verified review NLP fit distributions aggregated over 20M+ historical purchases.
* **Moat 2 — Viral WhatsApp Social Loop:** 1-tap micro-voting cards driving organic acquisition and reactivating dormant users.
* **Moat 3 — Styling Knowledge Graph:** Color theory and seasonality guardrails preventing AI styling hallucinations.

### 6.2 Three-Horizon Strategy & RICE Prioritization

| Horizon | Feature Component | Reach | Impact | Confidence | Effort | RICE Score | Status |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **H1 (MVP)** | **Side-by-Side Spec & GSM Matrix** | 3.5M | 3.0 | 90% | 2.5 PM-mo | **3,780** | **Vetted MVP (Rank #1)** |
| **H1 (MVP)** | **1-Tap WhatsApp Social Voting Card** | 2.8M | 2.5 | 85% | 2.0 PM-mo | **2,975** | **Vetted MVP (Rank #2)** |
| **H1 (MVP)** | **AI Coordinated Look Builder** | 3.2M | 2.0 | 80% | 3.5 PM-mo | **2,740** | **Vetted MVP (Rank #3)** |
| **H2 (Growth)** | Occasion Auto-Clustering Smart Folders | 4.5M | 1.5 | 80% | 2.0 PM-mo | **2,700** | Phase 2 Expansion |
| **H2 (Growth)** | Localized Community Trend Polls | 2.1M | 1.5 | 70% | 3.0 PM-mo | **1,470** | Phase 3 Expansion |
| **H3 (Vision)** | AR Virtual Try-On Wardrobe | 1.5M | 2.0 | 50% | 5.0 PM-mo | **600** | Long-Term Research |

---

## 7. Deployed MVP Solution Showcase ("Myntra Wishlist Studio")

**Public Production Deployment URL:** https://myntra-growth-lab.vercel.app

### 7.1 Deployed Wireframe Module Breakdown
1. **Module 1: Side-by-Side Spec Matrix (RICE #1):** Compares 2–4 selected items inline across Fabric GSM weight (240 GSM Heavy vs 160 GSM Light), Verified Fit Consensus (88% True to Size), and Real Customer Buyer Photos.
2. **Module 2: AI Coordinated Look Builder (RICE #3):** Generates 3 curated outfits matching wishlisted items. Offers 1-tap *"Add Complete Look to Bag"*, expanding AOV by +₹450.
3. **Module 3: 1-Tap WhatsApp Voting Card (RICE #2):** Generates shareable voting cards with live option polling + instant AI community fallback (`78% Choice`) reducing delay from 18h to 2s.

---

## 8. Technical Architecture & 4-Layer System Stack

```
[Layer 1: Client UI - React 18 / Vite / Custom Responsive CSS]
                                  │
                                  ▼
[Layer 2: Decision Engine - Fabric GSM Normalizer | Vector Matcher | Review NLP]
                                  │
                                  ▼
[Layer 3: Catalog Specs & Ops - Vendor GSM CDN | Buyer Review Photos]
                                  │
                                  ▼
[Layer 4: Social & Analytics - WhatsApp Webhook Sync | Amplitude Telemetry]
```

### 8.1 4-Stage User Emotional State Transition Map
1. **Stage 1 (Wishlist - Confused):** Overwhelmed by 6 similar cargos → launches Spec Matrix → sees GSM weight difference in 15s.
2. **Stage 2 (Styling - Hesitant):** Unsure how to pair → explores AI Looks → sees complete Friday look → adds bundle to bag.
3. **Stage 3 (Validation - Delayed):** Wants friend opinion → sends 1-tap WhatsApp card → gets instant votes + 78% community consensus.
4. **Stage 4 (Checkout - Confident):** Buys without discounts → zero return anxiety → +₹1,650 GMV unlocked.

---

## 9. Success Metrics, Telemetry & A/B Experimentation Design

### 9.1 Visual Metric Hierarchy Tree
* **North Star Metric:** 30-Day Wishlist-to-Purchase Conversion Rate (7.5% → 10.5%, +300 bps).
  * **Leading Indicator 1:** Side-by-Side Spec Matrix Adoption (≥ 35% Active Adoption).
  * **Leading Indicator 2:** AI Look-to-Bag Move Rate (≥ 22% Move-to-Bag).
  * **Leading Indicator 3:** WhatsApp Social Voting Share Rate (≥ 18% Share Rate).
  * **Counter Guardrail Metric:** Sizing & Quality Return Rate (24% Baseline → ≤ 18% Target).

### 9.2 Complete Amplitude Telemetry Schema

| Event Name | Trigger Condition | Payload Properties | Growth Insight Tracked |
| :--- | :--- | :--- | :--- |
| `wishlist_studio_launched` | User opens Wishlist tab | `user_id`, `saved_item_count`, `active_folders_count` | Top-of-funnel studio entry |
| `spec_comparison_viewed` | User selects 2-4 items and taps Compare | `compared_skus`, `category_id`, `gsm_weights`, `fit_scores` | Comparison intent velocity |
| `photo_cycler_toggled` | User flips between model & buyer photos | `sku_id`, `photo_type` (`studio` vs `customer`), `time_spent` | Visual verification depth |
| `ai_outfit_look_explored` | User clicks an AI outfit look | `seed_sku`, `paired_skus`, `look_category` | Cross-category styling intent |
| `bundle_moved_to_bag` | User taps 1-Tap Add Look to Bag | `bundle_skus`, `total_bundle_price`, `aov_lift` | AOV expansion tracking |
| `social_poll_card_generated` | User taps Share to WhatsApp | `compared_skus`, `share_medium` (`whatsapp`), `fallback_shown` | Viral social loop virality |

---

## 10. Operational Risk Mitigation & Automated Circuit Breakers

### 10.1 Automated Feature-Flag Circuit Breaker Rules
1. **Return Rate Circuit Breaker:** If overall product return rate exceeds **> 24%** over a 72-hour rolling window, the system automatically rolls back the comparison matrix to baseline.
2. **API Latency Circuit Breaker:** If p95 API response latency exceeds **> 800ms** for 15 consecutive minutes, the AI styling engine automatically pivots to static pre-computed look fallbacks.
3. **Primary Adoption Safeguard (Kill Threshold 1):** If Spec Matrix adoption is **< 15% at Day 30**, the system automatically triggers a redesign of comparison attributes for top 5 apparel categories.

---
*End of Comprehensive Product Specification & Growth Review Document.*
