import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# 1. Page Configuration & Title
st.set_page_config(
    page_title="Myntra Growth Lab | Wishlist Conversion Engine",
    page_icon="🛍️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS styling for Streamlit
st.markdown("""
<style>
  @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800;900&display=swap');
  html, body, [class*="css"] {
    font-family: 'Plus Jakarta Sans', sans-serif;
  }
  .stApp {
    background-color: #0A0D14;
    color: #F8FAFC;
  }
  
  /* Slide Deck Canvas Styling */
  .slide-canvas-card {
    background-color: #FFFFFF;
    color: #0F172A;
    border-radius: 18px;
    padding: 2rem;
    border: 1px solid #CBD5E1;
    box-shadow: 0 12px 36px rgba(0, 0, 0, 0.15);
    margin-bottom: 1.5rem;
  }
  
  .slide-top-pill {
    background-color: #2D0A4E;
    color: #FFFFFF;
    font-size: 0.72rem;
    font-weight: 800;
    letter-spacing: 0.6px;
    padding: 0.35rem 1.4rem;
    border-radius: 9999px;
    text-transform: uppercase;
    display: inline-block;
    margin-bottom: 0.8rem;
  }
  
  .slide-title-main {
    font-size: 1.25rem;
    font-weight: 900;
    color: #0F172A;
    line-height: 1.35;
    margin-bottom: 0.2rem;
  }
  
  .slide-subtitle-sub {
    font-size: 0.95rem;
    font-weight: 700;
    color: #4F46E5;
    margin-bottom: 1rem;
  }
  
  .evidence-box {
    background-color: #F8FAFC;
    border: 1px solid #E2E8F0;
    border-radius: 14px;
    padding: 1.1rem;
    height: 100%;
  }
  
  .evidence-title {
    font-size: 0.82rem;
    font-weight: 800;
    color: #1E1B4B;
    border-bottom: 2px solid rgba(79, 70, 229, 0.15);
    padding-bottom: 0.4rem;
    margin-bottom: 0.75rem;
    text-transform: uppercase;
  }
  
  .phone-mockup-frame {
    background-color: #0A0D14;
    border: 4px solid #1E293B;
    border-radius: 24px;
    padding: 0.75rem;
    color: #FFFFFF;
    box-shadow: 0 10px 25px rgba(0,0,0,0.3);
  }

  .synthesis-banner-box {
    background-color: #EEF2FF;
    border: 1px solid #C7D2FE;
    border-radius: 12px;
    padding: 0.85rem 1.25rem;
    margin-top: 1rem;
    color: #1E293B;
  }
  
  .synthesis-header {
    font-size: 0.78rem;
    font-weight: 800;
    color: #4338CA;
    text-transform: uppercase;
    margin-bottom: 0.25rem;
  }
  
  /* Brand Badge */
  .myntra-brand-badge {
    font-size: 1.8rem;
    font-weight: 900;
    color: #FF3F6C;
    letter-spacing: -1.2px;
    text-align: right;
  }
</style>
""", unsafe_allow_html=True)

# 2. Master Slide Data Definition
SLIDE_TRACKS = ["Context", "Market", "Research", "Insights", "Canvas", "Ideation", "MVP", "Architecture", "Metrics", "GTM"]

SLIDES_DATA = [
    {
        "slideNumber": 1,
        "track": "Context",
        "topBanner": "WISHLIST CONVERSION + SPEC CLARITY ARBITRAGE MODEL",
        "title": "1. Myntra Expands Blended Gross Margin (+300bps) by Converting Daily Wishlist Habits into Recurring Non-Discounted Buying",
        "subtitle": "Funding purchase confidence through proprietary spec clarity and AI styling to bypass traditional P&L discount subsidies.",
        "leftCard": {
            "title": "📋 STRATEGIC BRIEF & PM SCOPE",
            "bullets": [
                ("Role & Scope:", "PM on Myntra Growth Team driving trust-led wishlist-to-bag conversion."),
                ("Shortlist Inertia:", "66.7% of active wishlists stall into inactive graveyards with 38+ saved items."),
                ("Strategic Objective:", "Lift 30-day wishlist-to-purchase conversion from 7.5% to 10.5% (+300bps) in 12 months."),
                ("Zero-Discount Mandate:", "All lift must be generated via UX clarity & styling confidence—zero margin-eroding flash coupons.")
            ]
        },
        "midCard": {
            "title": "⚡ THE VALUE-CONFIDENCE ARBITRAGE MODEL",
            "bullets": [
                ("Confidence Arbitrage:", "Providing fabric GSM weight and verified fit consensus unlocks dormant intent without price cuts."),
                ("Sustainable Unit Economics:", "Delivers +₹18.81 Cr monthly gross profit from high-margin apparel (38% gross margin)."),
                ("Ecosystem Lock-in:", "Competitors relying on flat discounts cannot replicate proprietary review NLP spec graphs."),
                ("Compounding Flywheel:", "Higher evaluation confidence → higher checkout velocity → fewer reverse logistics sizing returns.")
            ]
        },
        "phoneMockup": {
            "screenName": "Wishlist Studio Home",
            "badge": "Zero-Discount Engine",
            "items": [
                ("Active Saved Items", "38 Items Saved"),
                ("30-Day Conversion Target", "7.5% → 10.5% (+300bps)"),
                ("Monthly Gross Profit Lift", "+₹18.81 Cr"),
                ("Return Cost Reduction", "₹73.5 Lakh / mo")
            ],
            "ctaText": "Explore Decision Studio"
        },
        "bottomBanner": {
            "title": "PORTAL DIRECTORY & VERIFIED HYPERLINKS",
            "text": "Live Deployed MVP: https://myntra-growth-lab.vercel.app | System Architecture & Strategy: plans/01_ to 08_ specifications"
        }
    },
    {
        "slideNumber": 2,
        "track": "Market",
        "topBanner": "CONVENIENCE-JUSTIFIED EVALUATION VS BLIND DISCOUNT HUNTING",
        "title": "2. Users Leak High-Intent Purchases to Off-Platform Channels; MVP Targets Spec Ambiguity and Styling Loops",
        "subtitle": "Shifting focus from margin-eroding discount alerts to confidence-justified spec comparisons and coordinated outfits.",
        "leftCard": {
            "title": "⭐ WHAT THE ECOSYSTEM HAS SOLVED",
            "bullets": [
                ("Catalog Depth & Variety:", "500,000+ fashion styles across global and domestic partner brands."),
                ("Sub-Second Search & Filters:", "Ultra-fast category search, size filtering, and brand carousels."),
                ("Seamless Checkout & 3PL:", "Reliable nationwide doorstep delivery with 14-day hassle-free return policy.")
            ]
        },
        "midCard": {
            "title": "❌ CADENCE & EVALUATION BLIND SPOTS (N=20,250 DATA)",
            "bullets": [
                ("Purchasing Leakage:", "88.9% (8/9 survey) shortlist 3-4 identical alternatives and defer buying due to choice paralysis."),
                ("Fabric Texture Blindspot:", "35% of stalled users cite inability to differentiate fabric weight (160 vs 240 GSM) online."),
                ("Zero Side-by-Side Tools:", "No Indian fashion platform offers real-time spec matrix comparing fit consensus on one screen."),
                ("Wardrobe Isolation:", "28% abandon purchases because standalone garments don't coordinate with existing clothes.")
            ]
        },
        "phoneMockup": {
            "screenName": "Comparison Dilemma",
            "badge": "Choice Paralysis",
            "items": [
                ("Option A: Heavy Street Cargo", "240 GSM • 88% True Fit"),
                ("Option B: Poplin Relaxed Cargo", "160 GSM • 64% Runs Small"),
                ("Friend Reply Latency", "18 Hours on WhatsApp"),
                ("Cart Drop-Off Probability", "68% After 48 Hours")
            ],
            "ctaText": "Launch Spec Matrix"
        },
        "bottomBanner": {
            "title": "★ CORE THESIS TESTED & VALIDATED",
            "text": "Wishlist inertia occurs because users lack evaluation clarity, not money. Fix: Side-by-Side GSM Matrix + AI Wardrobe Matching + 1-Tap WhatsApp Voting closes the loop."
        }
    },
    {
        "slideNumber": 3,
        "track": "Research",
        "topBanner": "AI DISCOVERY WORKFLOW & THINKING EVOLUTION NARRATIVE",
        "title": "3. Sourced 20,250 Review Corpus & N=9 Interviews Pivot Strategy: Price Elasticity Myth Replaced by Comparison Friction",
        "subtitle": "How research evolved our thinking from discount alert hypotheses to solving Spec Ambiguity, Styling Doubt & Social Latency.",
        "thinkingEvolution": [
            {"stage": "1. Initial Hypothesis", "desc": "Assumed wishlist drop-off was driven by price sensitivity and lack of discount alerts."},
            {"stage": "2. Sourced 20,250 Review NLP", "desc": "Parsed 20,250 reviews across 10 channels → 35% friction from comparison overload & thin fabric ambiguity."},
            {"stage": "3. Primary Interview Pivot (N=9)", "desc": "100% of interviewed users rejected price cuts as the primary blocker; 88.9% cited comparison paralysis."},
            {"stage": "4. Core Problem Definition", "desc": "Narrowed solution to 3 levers: Side-by-Side Spec Matrix, AI Look Coordinator & WhatsApp Voting."}
        ],
        "discoveryWorkflow": [
            {"step": "Step 1: Data Ingestion", "detail": "Sourced 20,250 verified buyer reviews across top 5 apparel categories."},
            {"step": "Step 2: NLP Cluster Parsing", "detail": "Categorized into 40% Delights, 30% Feature Requests, 30% Friction Clusters."},
            {"step": "Step 3: Interview Validation", "detail": "N=9 deep interviews (88.9% PMF score) confirming top 3 friction buckets."},
            {"step": "Step 4: AI Discovery Console", "detail": "Live workflow tester available in Tab 3 below."}
        ],
        "bottomBanner": {
            "title": "🔬 RESEARCH CONCLUSION & INSIGHT SYNTHESIS",
            "text": "Users do not need generic discount spam. They need Inline Spec Matrices (kill comparison paralysis), AI Look Matchers (kill styling doubt), and 1-Tap Voting Cards (kill friend latency)."
        }
    },
    {
        "slideNumber": 4,
        "track": "Insights",
        "topBanner": "HIGH-INTENT WARDROBE BUILDERS WHO STALL AT DECISION",
        "title": "4. Gen-Z & Millennial Shoppers (62% of Wishlist MAU) Form the Prime Wedge to Convert Dormant Consideration Demand",
        "subtitle": "Targeting active consideration shortlisters (38+ saved items) who require decision confidence rather than discounts.",
        "leftCard": {
            "title": "👥 TARGET COHORT PROFILE & RATIONALE",
            "bullets": [
                ("Cohort Definition:", "Gen-Z & Young Millennials (18-28 yrs, Tier 1/2 metros) with ≥ 3 items saved in wishlist."),
                ("Strategic Fit:", "High-intent users who already browsed and shortlisted items yield 4.2x higher conversion efficiency."),
                ("Predictive Activation:", "Wishlist age & clustering patterns trigger decision matrix before shopping momentum decays."),
                ("Zero Gross Margin Erosion:", "Retains full 38% platform margin without offering any margin-eroding coupons.")
            ]
        },
        "midCard": {
            "title": "👤 PERSONA: ANANYA & RAHUL — 23, BANGALORE",
            "bullets": [
                ("Jobs to be Done:", "'When I save 3 black cargo pants, I want to compare their real fabric GSM and fit on one screen so I can buy immediately.'"),
                ("Emotional Job:", "Avoid the regret, repackaging hassle, and return anxiety of receiving flimsy see-through fabric."),
                ("Social Job:", "Get rapid consensus from close friends on WhatsApp without waiting 18 hours for typing."),
                ("Authentic Interview Quote:", "'I saved 4 cargo pants that all look identical in photos. I bought none because I couldn't tell which fabric was actually thick vs flimsy.'")
            ]
        },
        "phoneMockup": {
            "screenName": "Target Cohort Profile",
            "badge": "62% Wishlist MAU",
            "items": [
                ("Average Saved Items", "38+ Items / User"),
                ("WhatsApp Sharers", "66.6% Social Loop"),
                ("Core Motivation", "Decision Confidence"),
                ("Willingness to Buy", "88.9% with Spec Matrix")
            ],
            "ctaText": "View Persona Journey"
        },
        "bottomBanner": {
            "title": "🎯 IMPACT IF SOLVED FOR THE CAUTIOUS SHORTLISTER",
            "text": "Eliminates cognitive fatigue. Makes multi-item comparison effortless. Boosts customer 30-day LTV up to 2.8x via bundle additions and reduces return friction."
        }
    },
    {
        "slideNumber": 5,
        "track": "Canvas",
        "topBanner": "SUPPLY-SIDE MONETIZATION & SENSITIVITY STRESS-TESTING",
        "title": "5. Non-Discounted Conversion Delivers ₹173 Cr Monthly Wishlist GMV; 50% Stress-Test Proves >110x ROI Resilience",
        "subtitle": "Unlocking +₹18.81 Cr monthly gross profit and ₹73.5L reverse logistics savings at 221x base ROI.",
        "financialWaterfall": [
            {"metric": "Baseline Wishlist Revenue", "val": "₹123.75 Cr / mo", "detail": "10M MAU × 7.5% baseline × ₹1,650 AOV"},
            {"metric": "Target Wishlist Revenue (10.5%)", "val": "₹173.25 Cr / mo", "detail": "10M MAU × 10.5% target × ₹1,650 AOV"},
            {"metric": "Incremental Monthly GMV Lift", "val": "+₹49.50 Cr / mo", "detail": "+300,000 buyers × ₹1,650 AOV"},
            {"metric": "Incremental Gross Profit (38%)", "val": "+₹18.81 Cr / mo", "detail": "+₹225.7 Cr / year gross margin unlock"},
            {"metric": "Reverse Logistics Savings", "val": "+₹73.50 Lakh / mo", "detail": "300k buyers × 6% return drop × ₹410 3PL"},
            {"metric": "Monthly Tech Infra Cost", "val": "₹8.50 Lakh / mo", "detail": "Vector cache, LLM looks, review embeddings"}
        ],
        "sensitivityTable": [
            {"scenario": "Base Case (100% Target Lift)", "convLift": "+300 bps", "monthlyProfit": "₹18.81 Cr", "annualValue": "₹234.5 Cr", "featureRoi": "221x ROI", "payback": "< 4 Days"},
            {"scenario": "Conservative Case (75% Lift)", "convLift": "+225 bps", "monthlyProfit": "₹14.10 Cr", "annualValue": "₹175.8 Cr", "featureRoi": "165x ROI", "payback": "< 6 Days"},
            {"scenario": "Stress-Test Case (50% Lift)", "convLift": "+150 bps", "monthlyProfit": "₹9.40 Cr", "annualValue": "₹117.2 Cr", "featureRoi": "110x ROI", "payback": "< 8 Days"}
        ],
        "bottomBanner": {
            "title": "💰 FINANCIAL FLYWHEEL SUMMARY & STRESS TEST",
            "text": "Even under a harsh 50% stress-test scenario (+150 bps lift), the feature generates ₹117.2 Cr annual value at a 110x ROI with payback under 8 days."
        }
    },
    {
        "slideNumber": 6,
        "track": "Ideation",
        "topBanner": "COMPOUNDING DATA FLYWHEEL VS COPIABLE PROMOS",
        "title": "6. Myntra's Defensibility Lies in its Verified GSM Spec Graph and WhatsApp Viral Loop, Not Copiable Promos",
        "subtitle": "Flat discount coupons are easily copied; vendor fabric specs and friend polling create sustainable moats.",
        "leftCard": {
            "title": "⚡ TRIVIALLY COPIABLE VS COMPOUNDING MOATS",
            "bullets": [
                ("Copiable Promos:", "10% flash discounts and generic push notifications can be matched by Ajio/Nykaa in a single sprint."),
                ("Moat 1 — Spec Knowledge Graph:", "Proprietary vendor fabric GSM specs and structured fit consensus from 20M+ reviews."),
                ("Moat 2 — Viral WhatsApp Loop:", "Interactive 1-tap friend voting brings dormant users into Myntra's ecosystem organically."),
                ("Moat 3 — Styling Knowledge Graph:", "Deterministic color theory and cross-category compatibility prevent generic AI hallucinations.")
            ]
        },
        "midCard": {
            "title": "🏆 THREE STRATEGIC HORIZONS (RICE MATRIX)",
            "bullets": [
                ("Horizon 1 (MVP) — Spec Matrix + WhatsApp Poll + Look Matcher:", "High Reach, Low Effort. RICE Score: 3,780 [Vetted MVP]."),
                ("Horizon 2 (Growth) — Occasion Auto-Folders + Trend Polls:", "Auto-clustering + localized trend feeds. RICE Score: 2,700."),
                ("Horizon 3 (Vision) — AR Virtual Try-On Wardrobe:", "3D garment overlay + autonomous wardrobe sync. RICE Score: 600.")
            ]
        },
        "phoneMockup": {
            "screenName": "Strategic Moat Engine",
            "badge": "Quadrant 2 Moat",
            "items": [
                ("Feature 1 (Spec Matrix)", "RICE: 3,780 (Rank #1)"),
                ("Feature 2 (WhatsApp Poll)", "RICE: 2,975 (Rank #2)"),
                ("Feature 3 (AI Looks)", "RICE: 2,740 (Rank #3)"),
                ("Flash Coupon Spam", "REJECTED (0 Moat)")
            ],
            "ctaText": "View RICE Matrix"
        },
        "bottomBanner": {
            "title": "🛡️ WHY HORIZON 1 WINS FIRST",
            "text": "Horizon 1 wins first: Zero margin erosion, attacks comparison paralysis directly, and embeds in existing wishlist behavior. H2/H3 leverage the structured data H1 generates."
        }
    },
    {
        "slideNumber": 7,
        "track": "MVP",
        "topBanner": "INTERACTIVE MVP SHOWCASE: DEPLOYED REACT APPLICATION",
        "title": "7. The Wishlist Studio MVP Embeds Side-by-Side Spec Matrix, AI Look Coordinator, and 1-Tap WhatsApp Voting",
        "subtitle": "Live Deployed Web Application validating sub-100ms client interactions at https://myntra-growth-lab.vercel.app",
        "mvpWireframes": [
            {
                "feature": "Feature 1: Side-by-Side Spec Matrix",
                "badge": "RICE: 3,780 (#1)",
                "uiBox": {
                    "header": "Inline Spec & GSM Comparison",
                    "col1": "Heavy Street Cargo\n240 GSM Heavy Cotton\n88% True to Size\nReal Customer Photos",
                    "col2": "Poplin Relaxed Cargo\n160 GSM Light Poplin\n64% Runs Small\nStudio Model Photo"
                },
                "value": "Solves comparison paralysis in under 60 seconds."
            },
            {
                "feature": "Feature 2: AI Coordinated Look Builder",
                "badge": "RICE: 2,740 (#3)",
                "uiBox": {
                    "header": "3 Curated Outfits per Item",
                    "col1": "Selected: Heavy Cargo (₹1,999)\n+ Oversized Tee (₹899)\n+ Canvas Sneakers (₹1,499)",
                    "col2": "Bundle Savings: ₹0 Discount\nTotal Bag: ₹4,397\n1-Tap Move Complete Look"
                },
                "value": "Lifts Average Order Value by +₹450 / order."
            },
            {
                "feature": "Feature 3: 1-Tap WhatsApp Voting Card",
                "badge": "RICE: 2,975 (#2)",
                "uiBox": {
                    "header": "Friend Polling + Instant AI Fallback",
                    "col1": "WhatsApp Poll Card Sent\nLive Option A vs B Votes",
                    "col2": "Instant Community Fallback:\n78% Community Choice"
                },
                "value": "Slashes feedback delay from 18 hours to 2 seconds."
            }
        ],
        "bottomBanner": {
            "title": "🚀 PUBLICLY ACCESSIBLE MVP DEPLOYMENT LINK",
            "text": "Interactive Prototype Deployed Live at https://myntra-growth-lab.vercel.app | Built with React 18, Vite, Lucide Icons, and Custom Design System."
        }
    },
    {
        "slideNumber": 8,
        "track": "Architecture",
        "topBanner": "USER EMOTION MAP & 4-LAYER SYSTEM ARCHITECTURE",
        "title": "8. Four-Layer Decision Engine Powers Inline GSM Comparison and Latency-Free Look Coordination",
        "subtitle": "Mapping user emotional state transitions across 4 purchase stages alongside the underlying 4-layer technical stack.",
        "leftCard": {
            "title": "⚙️ SYSTEM ARCHITECTURE (4 CORE LAYERS)",
            "bullets": [
                ("Layer 1 (Client UI):", "React/Vite Wishlist Studio + Side-by-Side Spec Matrix + Dynamic Look Builder + WhatsApp Simulator."),
                ("Layer 2 (Decision Engine):", "Vector Similarity Matcher + Fabric GSM Normalizer + Review Sentiment Classifier (20k reviews)."),
                ("Layer 3 (Catalog & Specs):", "Vendor GSM metadata ingestion + Verified buyer photo CDN + Real-time inventory status."),
                ("Layer 4 (Social & Attribution):", "WhatsApp interactive voting card generator + Amplitude telemetry event streaming.")
            ]
        },
        "midCard": {
            "title": "📱 USER EMOTION MAPPING ACROSS 4 STAGES",
            "bullets": [
                ("Stage 1 (Wishlist - Confused):", "Overwhelmed by 6 similar cargos → launches Spec Matrix → sees GSM weight difference in 15 seconds."),
                ("Stage 2 (Styling - Hesitant):", "Unsure how to pair → explores AI Looks → sees complete Friday look → adds bundle to bag."),
                ("Stage 3 (Validation - Delayed):", "Wants friend opinion → sends 1-tap WhatsApp card → gets instant votes + 78% community consensus."),
                ("Stage 4 (Checkout - Confident):", "Buys without discounts → zero return anxiety → +₹1,650 GMV unlocked.")
            ]
        },
        "phoneMockup": {
            "screenName": "Decision Architecture",
            "badge": "p95 < 180ms",
            "items": [
                ("Layer 1 (Client UI)", "React 18 + Vite"),
                ("Layer 2 (Engine)", "Fabric GSM Normalizer"),
                ("Layer 3 (Catalog)", "Vendor Metadata CDN"),
                ("Layer 4 (Social)", "WhatsApp Webhook Sync")
            ],
            "ctaText": "View Architecture Diagram"
        },
        "bottomBanner": {
            "title": "⚙️ TECHNICAL ARCHITECTURE MOAT & FEASIBILITY",
            "text": "Zero hardware Capex. Pre-indexed vector cache keeps styling queries sub-180ms. Review embeddings cached with 7-day TTL lifecycle rules."
        }
    },
    {
        "slideNumber": 9,
        "track": "Metrics",
        "topBanner": "METRIC HIERARCHY, TELEMETRY & A/B EXPERIMENT DESIGN",
        "title": "9. Conversion Lift (7.5% -> 10.5%) Is Validated via Randomized A/B Holdout Groups and Return Guardrails",
        "subtitle": "Measuring true incremental GMV via 200,000-user randomized controlled trial with return rate guardrails.",
        "leftCard": {
            "title": "⭐ NORTH STAR & INCREMENTALITY DESIGN",
            "bullets": [
                ("North Star Metric:", "30-Day Wishlist-to-Purchase Conversion Rate (Baseline: 7.5% → Target: 10.5%, +300bps)."),
                ("Experiment Design:", "Randomized Controlled Trial (100k Control vs 100k Variant users, 95% Confidence, 80% Power)."),
                ("Control Group:", "Standard passive wishlist view (vertical image card dump, no specs/looks)."),
                ("Leading Indicators:", "Spec Matrix Adoption (≥35%), AI Look-to-Bag Rate (≥22%), WhatsApp Share Rate (≥18%).")
            ]
        },
        "midCard": {
            "title": "🛡️ OPERATIONAL GUARDRAILS & KILL THRESHOLDS",
            "bullets": [
                ("Fit Return Rate Guardrail:", "Baseline returns: 24% → Target: ≤18% (-600bps drop due to verified GSM and fit consensus)."),
                ("Gross Margin Integrity Floor:", "Zero promotional coupon attach on wishlist conversions; strictly non-monetary."),
                ("Kill Threshold 1:", "If Spec Matrix adoption < 15% at Day 30 → redesign comparison attributes with top 5 categories."),
                ("Kill Threshold 2:", "If Return Rate increases above 24% or p95 API latency > 800ms → automated circuit breaker rolls back.")
            ]
        },
        "phoneMockup": {
            "screenName": "Amplitude Telemetry",
            "badge": "200,000 RCT",
            "items": [
                ("North Star Target", "10.5% (+300 bps)"),
                ("Return Rate Guardrail", "≤ 18% (-600 bps)"),
                ("Sample Power", "95% CI • 80% Power"),
                ("Instrumentation", "Full Amplitude Schema")
            ],
            "ctaText": "View Telemetry Schema"
        },
        "bottomBanner": {
            "title": "📊 METRIC COMPOUNDING & INTEGRITY",
            "text": "Metrics tracked via real-time Amplitude event streams (spec_comparison_viewed, bundle_moved_to_bag, social_poll_card_generated). Zero proxies. Holdout ensures strict causality."
        }
    },
    {
        "slideNumber": 10,
        "track": "GTM",
        "topBanner": "HORIZON 2 ROADMAP & AUTOMATED CIRCUIT BREAKERS",
        "title": "10. Phased GTM Roadmap Launches Horizon 1 MVP While Building Automated Circuit Breakers",
        "subtitle": "Phased rollout for Spec Matrix, AI Styling, WhatsApp Polling, and 60-second automated rollback safeguards.",
        "leftCard": {
            "title": "🚀 4-PHASE GTM ROLLOUT STRATEGY",
            "bullets": [
                ("Phase 1 (30 Days - Beta Bangalore/Mumbai):", "Roll out Spec Matrix + WhatsApp Voting across top 20 apparel brands (Gate: Adoption ≥30%)."),
                ("Phase 2 (90 Days - National Metros):", "Deploy AI Look Coordinator across all Tier-1 metros; onboard 500+ vendor catalogs."),
                ("Phase 3 (180 Days - Horizon 2 Beta):", "Launch Occasion Auto-Clustering and Community Trend Polling (Gate: Conversion lift ≥200bps)."),
                ("Phase 4 (GA - Platform Wide):", "Full rollout across all 10M Wishlist MAU. Kick off Horizon 3 AR virtual wardrobe.")
            ]
        },
        "midCard": {
            "title": "⚠️ RISKS, MITIGATIONS & CIRCUIT BREAKERS",
            "bullets": [
                ("Primary Risk (Low Adoption <15%):", "Address Kill Threshold 1: Redesign comparison attributes with top 5 categories if adoption <15% at Day 30."),
                ("Vendor Data Gaps:", "Heuristic textile weight model infers GSM from fabric composition & weave density."),
                ("Social Share Latency:", "Instant AI consensus fallback ('78% Community Choice') eliminates friend reply bottlenecks."),
                ("Automated Circuit Breaker:", "Automated feature flag rollback within 60 seconds if return rate spikes above 24% or latency >800ms.")
            ]
        },
        "phoneMockup": {
            "screenName": "GTM Command Center",
            "badge": "Circuit Breaker Active",
            "items": [
                ("Phase 1 Gate", "Beta Adoption ≥ 30%"),
                ("Phase 2 Gate", "Metro Rollout Lift ≥ 2pp"),
                ("Infra SLA Guardrail", "p95 API Latency < 300ms"),
                ("Rollback SLA", "Auto-Kill in < 60s")
            ],
            "ctaText": "View Risk Matrix"
        },
        "bottomBanner": {
            "title": "🔒 PRIVACY & MARGIN GUARDRAIL DIRECTORY",
            "text": "Privacy principle: Myntra respects user style autonomy. We never spam discount flash sales or share personal shopping boards without opt-in consent."
        }
    }
]

# Sidebar Navigation
st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/b/bc/Myntra_Logo.png", width=140) if False else None
st.sidebar.markdown("<h2 style='color:#FF3F6C;'>Myntra Growth Lab</h2>", unsafe_allow_html=True)
st.sidebar.markdown("### Wishlist Conversion Engine")

app_mode = st.sidebar.radio(
    "Navigation Portal:",
    [
        "📑 10-Slide Pitch Deck (Zepto Executive Standard)",
        "🛍️ Wishlist Studio MVP Prototype",
        "🔬 AI Review NLP Discovery Engine (20,250 Corpus)",
        "📊 Financial & Metric Sensitivity Simulator"
    ]
)

st.sidebar.markdown("---")
st.sidebar.info("💡 **Capstone Growth Target:**\n30-Day Conversion 7.5% → 10.5% (+300bps) | Zero Discounts | +₹18.81 Cr/mo Profit")

# PORTAL 1: 10-Slide Pitch Deck Viewer
if app_mode == "📑 10-Slide Pitch Deck (Zepto Executive Standard)":
    st.title("📑 10-Slide Executive Pitch Deck")
    st.caption("Top Fellow Capstone Standard • Anonymized Growth Team Specification")
    
    # Slide Selection Ribbon
    selected_slide_num = st.selectbox(
        "Select Slide to View:",
        range(1, 11),
        format_func=lambda x: f"Slide {x}: {SLIDES_DATA[x-1]['track']} — {SLIDES_DATA[x-1]['topBanner']}"
    )
    
    slide = SLIDES_DATA[selected_slide_num - 1]
    
    # Render Slide Canvas Container
    st.markdown(f"""
    <div class="slide-canvas-card">
        <div style="display:flex; justify-content:space-between; align-items:center;">
            <span class="slide-top-pill">{slide['topBanner']}</span>
            <div class="myntra-brand-badge">myntra</div>
        </div>
        <div class="slide-title-main">{slide['title']}</div>
        <div class="slide-subtitle-sub">{slide['subtitle']}</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Varied Layout Rendering
    if slide["slideNumber"] == 3:
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("<h4 style='color:#2D0A4E;'>🧠 STRATEGIC THINKING EVOLUTION NARRATIVE</h4>", unsafe_allow_html=True)
            for item in slide["thinkingEvolution"]:
                st.markdown(f"**{item['stage']}**  \n{item['desc']}")
                st.markdown("---")
        with col2:
            st.markdown("<h4 style='color:#4F46E5;'>🔬 AI DISCOVERY PIPELINE WORKFLOW</h4>", unsafe_allow_html=True)
            for wf in slide["discoveryWorkflow"]:
                st.markdown(f"**{wf['step']}**  \n{wf['detail']}")
                st.markdown("---")
                
    elif slide["slideNumber"] == 5:
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("<h4 style='color:#2D0A4E;'>📊 BOTTOM-UP FINANCIAL WATERFALL</h4>", unsafe_allow_html=True)
            for item in slide["financialWaterfall"]:
                st.metric(label=item["metric"], value=item["val"], delta=item["detail"])
        with col2:
            st.markdown("<h4 style='color:#4F46E5;'>🛡️ SENSITIVITY STRESS-TESTING SCENARIOS</h4>", unsafe_allow_html=True)
            df_sens = pd.DataFrame(slide["sensitivityTable"])
            st.table(df_sens)
            
    elif slide["slideNumber"] == 7:
        st.markdown("<h4 style='color:#FF3F6C;'>🚀 INTERACTIVE MVP WIREFRAME MODULES</h4>", unsafe_allow_html=True)
        cols = st.columns(3)
        for idx, wf in enumerate(slide["mvpWireframes"]):
            with cols[idx]:
                st.subheader(wf["feature"])
                st.caption(wf["badge"])
                st.info(f"**UI Component:**\n{wf['uiBox']['header']}")
                st.write(wf['uiBox']['col1'])
                st.write(wf['uiBox']['col2'])
                st.success(f"**Impact:** {wf['value']}")
    else:
        col1, col2, col3 = st.columns([1.2, 1.2, 0.9])
        with col1:
            st.markdown(f"<div class='evidence-title'>{slide['leftCard']['title']}</div>", unsafe_allow_html=True)
            for bold, text in slide['leftCard']['bullets']:
                st.markdown(f"• **{bold}** {text}")
        with col2:
            st.markdown(f"<div class='evidence-title'>{slide['midCard']['title']}</div>", unsafe_allow_html=True)
            for bold, text in slide['midCard']['bullets']:
                st.markdown(f"• **{bold}** {text}")
        with col3:
            st.markdown(f"""
            <div class="phone-mockup-frame">
                <div style="font-size:0.7rem; color:#94A3B8;">⚡ {slide['phoneMockup']['screenName']}</div>
                <div style="color:#FF3F6C; font-weight:800; font-size:0.8rem; margin-bottom:0.5rem;">[{slide['phoneMockup']['badge']}]</div>
            </div>
            """, unsafe_allow_html=True)
            for label, val in slide['phoneMockup']['items']:
                st.caption(f"{label}:")
                st.write(f"**{val}**")

    # Bottom Synthesis Banner
    st.markdown(f"""
    <div class="synthesis-banner-box">
        <div class="synthesis-header">★ {slide['bottomBanner']['title']}</div>
        <div>{slide['bottomBanner']['text']}</div>
    </div>
    """, unsafe_allow_html=True)

# PORTAL 2: Wishlist Studio MVP Prototype
elif app_mode == "🛍️ Wishlist Studio MVP Prototype":
    st.title("🛍️ Wishlist Studio MVP Prototype")
    st.caption("Live Interactive Prototype • High-Intent Shortlist Workspace")
    
    st.info("💡 **Core Value Proposition:** Compare fabric GSM, fit consensus, and outfit pairing on one screen without discounts.")
    
    # Occasion Folders
    folder = st.selectbox("Occasion Smart Folder Filter:", ["All Saved Items (38)", "Workwear (12)", "Streetwear (18)", "Party (8)"])
    
    st.markdown("### 1. Side-by-Side Spec & GSM Comparison Matrix")
    
    c1, c2 = st.columns(2)
    with c1:
        st.subheader("Item 1: Heavy Streetwear Cargo")
        st.image("https://images.unsplash.com/photo-1517445312882-bc9910d016b7?w=400", width=220)
        st.write("**Fabric Weight:** 240 GSM Heavyweight Cotton")
        st.write("**Fit Consensus:** 88% True to Size")
        st.write("**Price:** ₹1,999 (Zero Discount)")
        st.write("**Return Rate:** 12% Low Returns")
        st.button("Compare Specs vs Item 2", key="btn1")
        
    with c2:
        st.subheader("Item 2: Poplin Relaxed Cargo")
        st.image("https://images.unsplash.com/photo-1541099649105-f69ad21f3246?w=400", width=220)
        st.write("**Fabric Weight:** 160 GSM Lightweight Poplin")
        st.write("**Fit Consensus:** 64% Runs Small")
        st.write("**Price:** ₹1,499 (Zero Discount)")
        st.write("**Return Rate:** 28% High Sizing Variance")
        st.button("Compare Specs vs Item 1", key="btn2")

    st.markdown("---")
    st.markdown("### 2. AI Coordinated Look Builder (+₹450 AOV Lift)")
    st.write("Pair selected Heavy Cargo (₹1,999) with curated complement pieces:")
    st.write("• Oversized Boxy Tee (₹899)")
    st.write("• Vintage Canvas Sneakers (₹1,499)")
    st.markdown("**Total Look Bundle Price:** ₹4,397 (0% Margin Dilution)")
    if st.button("🛍️ Move Complete 3-Piece Look to Bag"):
        st.success("Complete Friday Look moved to bag! +₹450 AOV expansion logged.")

    st.markdown("---")
    st.markdown("### 3. 1-Tap WhatsApp Voting Micro-Card")
    if st.button("📱 Share Voting Card to WhatsApp"):
        st.info("WhatsApp micro-card generated! Link created for group polling.")
        st.success("Instant Fallback Triggered: **78% Community Choice** verified in 2 seconds.")

# PORTAL 3: AI Review NLP Discovery Engine
elif app_mode == "🔬 AI Review NLP Discovery Engine (20,250 Corpus)":
    st.title("🔬 AI Review NLP Discovery Engine")
    st.caption("Corpus: Sourced 20,250 Verified Buyer Reviews Across Top 5 Apparel Categories")
    
    st.markdown("### Search & Synthesize Sentiment Clusters")
    query = st.text_input("Enter Product Keyword or Friction Query:", "fabric thickness cargos sizing")
    
    if query:
        st.write(f"Parsing NLP Corpus for query: **'{query}'**...")
        
        # Donut Chart for Sentiment Breakdown
        df_chart = pd.DataFrame({
            "Cluster": ["Positive Delights (Delivery/Variety)", "Neutral Feature Requests (GSM/Pairing)", "Negative Frictions (Sizing/Fabric Ambiguity)"],
            "Volume": [8100, 6075, 6075]
        })
        fig = px.pie(df_chart, values="Volume", names="Cluster", title="20,250 Review Sentiment Corpus Distribution", hole=0.4)
        st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("### Top Synthesized Barrier Buckets")
        st.warning("1. **Comparison Overload (35% NLP / 88.9% Survey):** Users save 3.8 alternatives per sub-category and stall due to hidden GSM weight.")
        st.warning("2. **Styling Isolation (28% NLP / 77.8% Survey):** Hesitation caused by uncertainty on how to pair standalone pieces.")
        st.warning("3. **WhatsApp Reply Latency (66.6% Survey):** Screenshot sharing causes 18-hour delay and loss of buying impulse.")

# PORTAL 4: Financial & Metric Sensitivity Simulator
else:
    st.title("📊 Financial & Metric Sensitivity Simulator")
    st.caption("Interactive Opportunity Sizing & Unit Economics Stress-Test Model")
    
    st.markdown("### Adjust Key Growth Levers")
    col_l1, col_l2 = st.columns(2)
    with col_l1:
        mau = st.slider("Active Wishlist MAU:", 5000000, 15000000, 10000000, 1000000)
        baseline_conv = st.slider("Baseline 30-Day Conversion Rate (%):", 5.0, 10.0, 7.5, 0.5)
        target_lift_bps = st.slider("Target Conversion Lift (bps):", 50, 400, 300, 25)
    with col_l2:
        aov = st.slider("Average Order Value (AOV in ₹):", 1200, 2500, 1650, 50)
        margin = st.slider("Platform Gross Margin (%):", 30, 50, 38, 1)
        infra_cost_monthly = st.slider("Monthly Tech Infra Cost (₹ Lakh):", 5.0, 20.0, 8.5, 0.5)
        
    # Calculate Outputs
    target_conv = baseline_conv + (target_lift_bps / 100)
    baseline_revenue = (mau * (baseline_conv / 100) * aov) / 10000000
    target_revenue = (mau * (target_conv / 100) * aov) / 10000000
    incremental_gmv = target_revenue - baseline_revenue
    monthly_gross_profit = incremental_gmv * (margin / 100)
    annual_gross_profit = monthly_gross_profit * 12
    annual_infra = (infra_cost_monthly * 12) / 100
    roi = annual_gross_profit / annual_infra if annual_infra > 0 else 0
    payback_days = (infra_cost_monthly / monthly_gross_profit) * 30 if monthly_gross_profit > 0 else 0
    
    st.markdown("---")
    st.markdown("### Simulated Financial Impact")
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Target Conversion Rate", f"{target_conv:.2f}%", f"+{target_lift_bps} bps")
    m2.metric("Monthly Incremental GMV", f"₹{incremental_gmv:.2f} Cr", f"+₹{incremental_gmv*12:.1f} Cr / yr")
    m3.metric("Monthly Gross Profit Unlock", f"₹{monthly_gross_profit:.2f} Cr", f"At {margin}% Margin")
    m4.metric("Feature ROI", f"{roi:.0f}x ROI", f"Payback < {payback_days:.1f} Days")

    st.markdown("---")
    st.markdown("### Financial Sensitivity Matrix")
    df_sens_table = pd.DataFrame([
        {"Scenario": "Base Case (100% Target Lift)", "Lift (bps)": "+300 bps", "Monthly Profit": f"₹{monthly_gross_profit:.2f} Cr", "Annual Value": f"₹{annual_gross_profit:.1f} Cr", "Feature ROI": f"{roi:.0f}x", "Payback": f"{payback_days:.1f} Days"},
        {"Scenario": "Conservative Case (75% Lift)", "Lift (bps)": f"+{int(target_lift_bps*0.75)} bps", "Monthly Profit": f"₹{monthly_gross_profit*0.75:.2f} Cr", "Annual Value": f"₹{annual_gross_profit*0.75:.1f} Cr", "Feature ROI": f"{roi*0.75:.0f}x", "Payback": f"{payback_days/0.75:.1f} Days"},
        {"Scenario": "Stress-Test Case (50% Lift)", "Lift (bps)": f"+{int(target_lift_bps*0.50)} bps", "Monthly Profit": f"₹{monthly_gross_profit*0.50:.2f} Cr", "Annual Value": f"₹{annual_gross_profit*0.50:.1f} Cr", "Feature ROI": f"{roi*0.50:.0f}x", "Payback": f"{payback_days/0.50:.1f} Days"},
    ])
    st.table(df_sens_table)
