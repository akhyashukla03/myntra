import React, { useState } from 'react';
import { Activity, Award, ShieldAlert, SplitSquareVertical, BarChart2, CheckCircle2, TrendingUp, AlertTriangle, Layers, Database } from 'lucide-react';

export const METRICS_TABLE = [
  {
    category: "North Star Metric",
    name: "30-Day Wishlist-to-Purchase Conversion Rate",
    type: "Lagging Business Metric",
    baseline: "7.5%",
    target: "10.5% (+300 bps)",
    formula: "Users purchasing >= 1 wishlisted item in 30 days / Total users who added >= 1 item to wishlist in the period",
    importance: "Direct growth team mandate: measures how effectively high-intent demand converts into transactions without discounts."
  },
  {
    category: "Lagging Financial Impact",
    name: "Monthly Incremental Non-Discounted GMV",
    type: "Financial Output",
    baseline: "₹0 (Baseline)",
    target: "+₹49.5 Cr / month",
    formula: "(Variant Buyers - Control Buyers) * Average Order Value (₹1,650)",
    importance: "Measures monetization lift while guaranteeing 0% gross margin dilution."
  },
  {
    category: "Leading Indicator",
    name: "Side-by-Side Comparison Engagement Rate",
    type: "User Behavior (Feature Adoption)",
    baseline: "12% (Manual toggling)",
    target: ">= 35% of Wishlist Visitors",
    formula: "Users launching comparison studio / Total wishlist page visitors",
    importance: "Validates that users are actively using the evaluation tool to resolve comparison paralysis."
  },
  {
    category: "Leading Indicator",
    name: "AI Outfit Matcher Look-to-Bag Conversion",
    type: "User Behavior (Styling Utility)",
    baseline: "8.4% (Single item checkout)",
    target: ">= 22% of Look Explorers",
    formula: "Users adding full look bundle to bag / Users viewing AI coordinated looks",
    importance: "Demonstrates that outfit styling directly overcomes single-piece coordination doubt."
  },
  {
    category: "Leading Indicator",
    name: "WhatsApp Social Voting Card Share Rate",
    type: "User Behavior (Peer Validation)",
    baseline: "5.0% (Screenshots)",
    target: ">= 18% of Multi-Item Evaluators",
    formula: "Voting links shared to WhatsApp / Sessions with >= 2 items in comparison",
    importance: "Measures viral social loop adoption and peer decision speed."
  },
  {
    category: "Guardrail Metric",
    name: "Fit & Sizing Return Rate",
    type: "Post-Purchase Health Guardrail",
    baseline: "24.0%",
    target: "<= 18.0% (-600 bps)",
    formula: "Returns initiated due to sizing/fabric mismatch / Total items delivered",
    importance: "CRITICAL GUARDRAIL: Ensures that conversion lift is driven by true fit confidence, not rushed buys that trigger returns."
  },
  {
    category: "Guardrail Metric",
    name: "Wishlist Item Deletion Velocity",
    type: "UX Experience Guardrail",
    baseline: "4.2% per week",
    target: "<= 5.0% per week",
    formula: "Items deleted from wishlist / Total active wishlist inventory",
    importance: "Guarantees users do not experience cognitive overload or purge their bookmarks."
  },
  {
    category: "Guardrail Metric",
    name: "Comparison Matrix API Latency (p95)",
    type: "Technical Performance Guardrail",
    baseline: "320 ms",
    target: "< 450 ms (p95)",
    formula: "Time to render side-by-side spec cards and customer photos",
    importance: "Maintains snappy, frictionless browsing experience on 4G/5G mobile networks."
  }
];

export const TRACKING_EVENTS = [
  {
    eventName: "wishlist_studio_launched",
    trigger: "User clicks 'Launch Comparison' or selects occasion filter",
    properties: ["user_id", "occasion_category", "shortlisted_items_count", "session_dwell_time"]
  },
  {
    eventName: "spec_comparison_viewed",
    trigger: "User compares 2-4 items side-by-side",
    properties: ["product_ids", "fabric_gsm_viewed", "fit_consensus_score", "photo_cycled_count"]
  },
  {
    eventName: "ai_outfit_look_explored",
    trigger: "User clicks 'AI Outfit Matcher' on any wishlisted item",
    properties: ["base_product_id", "look_theme", "bundle_total_price", "look_index"]
  },
  {
    eventName: "bundle_moved_to_bag",
    trigger: "User clicks 'Add Complete Look to Bag'",
    properties: ["base_product_id", "paired_product_ids", "total_bundle_value", "discount_applied (0)"]
  },
  {
    eventName: "social_poll_card_generated",
    trigger: "User generates WhatsApp voting card link",
    properties: ["option_a_id", "option_b_id", "channel (whatsapp)", "poll_id"]
  },
  {
    eventName: "social_poll_vote_submitted",
    trigger: "Friend submits a vote on the shared micro-card",
    properties: ["poll_id", "voted_option", "response_latency_seconds"]
  }
];

export default function SuccessMetricsStudio() {
  const [activeTab, setActiveTab] = useState('FRAMEWORK'); // 'FRAMEWORK', 'AB_TEST', 'TELEMETRY'

  return (
    <div className="module-container">
      {/* Top Banner */}
      <div className="discovery-hero-banner">
        <div className="hero-content">
          <div className="hero-badge">
            <Activity size={14} className="text-pink" />
            <span>Part 6: Success Metrics & Evaluation Framework</span>
          </div>
          <h1 className="hero-title">Measurement Hierarchy, A/B Testing & Telemetry</h1>
          <p className="hero-subtitle">
            Comprehensive metric definitions, statistical experimentation design (Control vs Variant), and event tracking dictionary.
          </p>
        </div>

        {/* Sub Navigation */}
        <div className="hero-nav-tabs">
          <button
            className={`hero-tab-btn ${activeTab === 'FRAMEWORK' ? 'active' : ''}`}
            onClick={() => setActiveTab('FRAMEWORK')}
          >
            <BarChart2 size={16} />
            <span>1. Metric Hierarchy & Rationale</span>
          </button>
          <button
            className={`hero-tab-btn ${activeTab === 'AB_TEST' ? 'active' : ''}`}
            onClick={() => setActiveTab('AB_TEST')}
          >
            <SplitSquareVertical size={16} />
            <span>2. A/B Experimentation Design</span>
          </button>
          <button
            className={`hero-tab-btn ${activeTab === 'TELEMETRY' ? 'active' : ''}`}
            onClick={() => setActiveTab('TELEMETRY')}
          >
            <Database size={16} />
            <span>3. Telemetry Event Dictionary</span>
          </button>
        </div>
      </div>

      <div className="discovery-tab-content">
        {/* TAB 1: METRICS HIERARCHY TABLE */}
        {activeTab === 'FRAMEWORK' && (
          <div className="discovery-section">
            <div className="section-header">
              <div>
                <h2 className="section-title">Success Metrics Hierarchy & Target Thresholds</h2>
                <p className="section-subtitle">
                  Balancing conversion velocity with post-purchase customer health and margin preservation.
                </p>
              </div>
            </div>

            <div className="category-table-wrapper">
              <table className="category-table">
                <thead>
                  <tr>
                    <th>Metric Classification</th>
                    <th>Metric Name & Formula</th>
                    <th>Baseline</th>
                    <th>Target Goal</th>
                    <th>Strategic PM Rationale</th>
                  </tr>
                </thead>
                <tbody>
                  {METRICS_TABLE.map((m, mIdx) => (
                    <tr key={mIdx}>
                      <td>
                        <span className={`return-badge ${
                          m.category === 'North Star Metric' ? 'risk-low' :
                          m.category === 'Guardrail Metric' ? 'risk-med' : 'share-pill'
                        }`}>
                          {m.category}
                        </span>
                      </td>
                      <td>
                        <div className="cat-name-cell">{m.name}</div>
                        <div className="friction-cell" style={{ marginTop: '0.2rem' }}>
                          <code>{m.formula}</code>
                        </div>
                      </td>
                      <td>{m.baseline}</td>
                      <td>
                        <span className="conv-pill" style={{ fontWeight: 800 }}>{m.target}</span>
                      </td>
                      <td>
                        <div className="friction-cell">{m.importance}</div>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </div>
        )}

        {/* TAB 2: A/B TESTING EXPERIMENTATION DESIGN */}
        {activeTab === 'AB_TEST' && (
          <div className="discovery-section">
            <div className="section-header">
              <div>
                <h2 className="section-title">A/B Testing Cohort Experimentation Architecture</h2>
                <p className="section-subtitle">
                  Rigorous 30-day randomized controlled trial testing the full Wishlist Studio suite against standard wishlist UI.
                </p>
              </div>
            </div>

            <div className="funnel-pillars-grid">
              {/* Cohort A: Control */}
              <div className="pillar-card">
                <div className="pillar-top">
                  <span className="pillar-num" style={{ background: '#4B5563' }}>A</span>
                  <h3 className="pillar-title">Control Group (50% Traffic)</h3>
                </div>
                <p className="pillar-desc">
                  Users receive the <strong>standard Myntra wishlist experience</strong> (static vertical product feed with bookmarking, no side-by-side matrix, no AI look builder).
                </p>
                <div className="pillar-metrics-list">
                  <div className="pillar-metric-item">
                    <span className="metric-kpi-name">Sample Size</span>
                    <span className="metric-kpi-target">100,000 Users</span>
                  </div>
                  <div className="pillar-metric-item">
                    <span className="metric-kpi-name">Expected Baseline Conversion</span>
                    <span className="metric-kpi-target">7.5%</span>
                  </div>
                </div>
              </div>

              {/* Cohort B: Variant */}
              <div className="pillar-card">
                <div className="pillar-top">
                  <span className="pillar-num pillar-purple">B</span>
                  <h3 className="pillar-title">Variant: Wishlist Studio (50% Traffic)</h3>
                </div>
                <p className="pillar-desc">
                  Users receive the <strong>Myntra Wishlist Studio MVP</strong> (Smart Occasion Folders, Side-by-Side Comparison Studio, AI Look Matcher, 1-Tap WhatsApp Voting).
                </p>
                <div className="pillar-metrics-list">
                  <div className="pillar-metric-item">
                    <span className="metric-kpi-name">Sample Size</span>
                    <span className="metric-kpi-target">100,000 Users</span>
                  </div>
                  <div className="pillar-metric-item">
                    <span className="metric-kpi-name">Target Conversion</span>
                    <span className="metric-kpi-target text-pink">10.5% (+300 bps)</span>
                  </div>
                </div>
              </div>
            </div>

            {/* Statistical Power Box */}
            <div className="charts-two-col" style={{ marginTop: '1rem' }}>
              <div className="chart-card">
                <div className="chart-header">
                  <h3 className="chart-title">Statistical Experiment Rigor</h3>
                  <span className="chart-badge">Parameters</span>
                </div>
                <div className="bars-list">
                  <div className="action-point">
                    <span className="point-number">1</span>
                    <div><strong>Test Duration:</strong> 30 Days (captures full customer consideration & payroll cycle).</div>
                  </div>
                  <div className="action-point">
                    <span className="point-number">2</span>
                    <div><strong>Statistical Confidence:</strong> 95% (alpha = 0.05, p &lt; 0.05).</div>
                  </div>
                  <div className="action-point">
                    <span className="point-number">3</span>
                    <div><strong>Statistical Power:</strong> 80% with Minimum Detectable Effect (MDE) of ±0.5%.</div>
                  </div>
                </div>
              </div>

              <div className="chart-card">
                <div className="chart-header">
                  <h3 className="chart-title">Decision Rollout Framework</h3>
                  <span className="chart-badge">Go / No-Go</span>
                </div>
                <div className="bars-list">
                  <div className="action-point">
                    <span className="point-number">✓</span>
                    <div><strong>Full Rollout Criteria:</strong> Conversion lift &ge; +150 bps (p &lt; 0.05) AND Fit Return Rate &le; 19%.</div>
                  </div>
                  <div className="action-point">
                    <span className="point-number">⚠</span>
                    <div><strong>Iterate Criteria:</strong> Conversion lift between +50 to +150 bps; refine AI Look styling recommendations.</div>
                  </div>
                  <div className="action-point">
                    <span className="point-number">✕</span>
                    <div><strong>Kill Criteria:</strong> Sizing returns spike &gt; 24% or 30-day conversion neutral/negative.</div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        )}

        {/* TAB 3: TELEMETRY & EVENT INSTRUMENTATION */}
        {activeTab === 'TELEMETRY' && (
          <div className="discovery-section">
            <div className="section-header">
              <div>
                <h2 className="section-title">Telemetry & Product Analytics Event Dictionary</h2>
                <p className="section-subtitle">
                  Schema of front-end and back-end events tracking user evaluation actions in Wishlist Studio.
                </p>
              </div>
            </div>

            <div className="feed-grid">
              {TRACKING_EVENTS.map((event, eIdx) => (
                <div key={eIdx} className="feedback-card">
                  <div className="card-top-meta">
                    <span className="source-tag">Analytics Event</span>
                    <span className="barrier-badge badge-pink">{event.eventName}</span>
                  </div>
                  <div className="card-title" style={{ fontSize: '0.92rem' }}>
                    Trigger: <em>"{event.trigger}"</em>
                  </div>
                  <div className="key-quote-box">
                    <span className="quote-label">Payload Properties:</span>
                    <div style={{ display: 'flex', gap: '0.4rem', flexWrap: 'wrap', marginTop: '0.3rem' }}>
                      {event.properties.map((prop, pIdx) => (
                        <code key={pIdx} style={{ background: 'rgba(255,255,255,0.08)', padding: '0.15rem 0.4rem', borderRadius: '4px', fontSize: '0.75rem' }}>
                          {prop}
                        </code>
                      ))}
                    </div>
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}
      </div>
    </div>
  );
}
