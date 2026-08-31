import React, { useState } from 'react';
import { ShieldAlert, ShieldCheck, AlertTriangle, RefreshCw, Cpu, Users, Layers, Zap, GitCommit, CheckCircle2 } from 'lucide-react';

export const RISKS_DATA = [
  {
    id: "risk_1",
    name: "AI Styling Mismatch & Clashing Recommendations",
    category: "AI & Algorithmic Quality",
    probability: "Medium",
    severity: "High",
    failureMode: "Generative AI recommends clashing styles, seasonal mismatches (e.g., heavy wool sweater with beach shorts), or culturally inappropriate pairings, damaging trust.",
    mitigationStrategy: "Curated Fashion Knowledge Graph Rules Layer: All AI outfit combinations pass through deterministic taxonomy rules (Color Theory, Seasonality, Occasion Matrix) before rendering.",
    healthThreshold: "Look Quality Approval Score >= 92%",
    statusBadge: "Knowledge Graph Filter"
  },
  {
    id: "risk_2",
    name: "Social Voting Asynchronous Latency",
    category: "User Behavior & Friction",
    probability: "High",
    severity: "Medium",
    failureMode: "Users share WhatsApp voting cards but friends take 12-24 hours to reply, causing the shopping impulse to fade and resulting in 65% drop-off.",
    mitigationStrategy: "Instant AI Community Consensus Fallback: When a user generates a poll, the system instantly displays 'AI Stylist & Community Consensus (e.g., 78% of shoppers with your style preference chose Option A)' so users can decide immediately without waiting.",
    healthThreshold: "Instant Decision Rate >= 45%",
    statusBadge: "Instant AI Fallback"
  },
  {
    id: "risk_3",
    name: "Incomplete Vendor Catalog Metadata (Missing GSM / Fit Scores)",
    category: "Data & Supply Chain",
    probability: "Medium",
    severity: "Medium",
    failureMode: "Third-party brand sellers fail to provide fabric GSM weight or structured fit measurements, creating empty spec rows in Comparison Studio.",
    mitigationStrategy: "Automated NLP Review Extraction & Vendor Portal Enforcement: Backfill missing specs by scraping verified buyer review sentiment ('Fabric feels thick/thin', 'Runs small') + mandate GSM specs for top 500 brand SKUs.",
    healthThreshold: "Catalog Metadata Coverage >= 95%",
    statusBadge: "Review NLP Auto-Fill"
  },
  {
    id: "risk_4",
    name: "Cognitive UI Overload & Wishlist Navigation Clutter",
    category: "UX & Product Experience",
    probability: "Low",
    severity: "High",
    failureMode: "Adding comparison buttons, filters, and outfit cards makes the wishlist feel too heavy or complicated for casual bookmarkers.",
    mitigationStrategy: "Progressive Disclosure & 1-Tap Floating Pill: The standard wishlist remains clean. Comparison Matrix only activates via a non-intrusive bottom dock when 2+ items in a category are selected.",
    healthThreshold: "Item Deletion Velocity <= 5%/wk",
    statusBadge: "Progressive Dock UX"
  },
  {
    id: "risk_5",
    name: "Size Stockout During Evaluation Dwell Period",
    category: "Inventory & Conversion",
    probability: "Medium",
    severity: "High",
    failureMode: "While a user spends 2-3 days comparing options or waiting for votes, their preferred size sells out, resulting in permanent cart abandonment.",
    mitigationStrategy: "Real-Time Urgency Badge & 1-Click Similar Match: Show real-time 'Only 2 left in Size M' badges in Comparison Studio + provide instant 'Substitute with similar fit' alternative.",
    healthThreshold: "Stockout Cart Loss <= 4%",
    statusBadge: "Real-Time Stock Alerts"
  }
];

export const ROLLOUT_STAGES = [
  {
    stage: "Phase 1: Alpha Testing",
    traffic: "1% Internal Users (Employees + Power Shoppers)",
    duration: "Week 1",
    focus: "Verify API latency (<450ms), Knowledge Graph styling rules, and WhatsApp voting webhooks.",
    exitCriteria: "Zero critical crash bugs, p95 API latency < 350ms."
  },
  {
    stage: "Phase 2: Canary Cohort A/B Test",
    traffic: "10% Active Mobile App Users (50k Control / 50k Variant)",
    duration: "Weeks 2 - 5 (30-day cohort)",
    focus: "Measure 30-day conversion lift, Comparison Studio adoption, and Sizing Return Rate guardrail.",
    exitCriteria: "Statistically significant conversion lift >= +150 bps, Fit Returns <= 19%."
  },
  {
    stage: "Phase 3: Broad Phased Expansion",
    traffic: "50% All Mobile App Users",
    duration: "Weeks 6 - 7",
    focus: "Stress test backend recommendation engine under peak flash sale traffic.",
    exitCriteria: "Server error rate < 0.05%, server CPU utilization < 60%."
  },
  {
    stage: "Phase 4: Full Production Rollout",
    traffic: "100% General Availability",
    duration: "Week 8 onwards",
    focus: "Continuous monitoring of +₹49.5 Cr GMV monthly lift and return logistics cost savings.",
    exitCriteria: "Target 10.5% conversion maintained sustainably."
  }
];

export default function RisksMitigationsStudio() {
  const [activeTab, setActiveTab] = useState('RISKS'); // 'RISKS' or 'ROLLOUT'

  return (
    <div className="module-container">
      {/* Top Banner */}
      <div className="discovery-hero-banner">
        <div className="hero-content">
          <div className="hero-badge">
            <ShieldAlert size={14} className="text-pink" />
            <span>Part 7: Risks, Failure Modes & Mitigation Architecture</span>
          </div>
          <h1 className="hero-title">Proactive Risk Management & Guardrails</h1>
          <p className="hero-subtitle">
            Systematic failure mode identification, engineering & UX mitigations, and phased canary deployment circuit breakers.
          </p>
        </div>

        {/* Sub Navigation */}
        <div className="hero-nav-tabs">
          <button
            className={`hero-tab-btn ${activeTab === 'RISKS' ? 'active' : ''}`}
            onClick={() => setActiveTab('RISKS')}
          >
            <AlertTriangle size={16} />
            <span>1. 5 Critical Risks & Mitigations</span>
          </button>
          <button
            className={`hero-tab-btn ${activeTab === 'ROLLOUT' ? 'active' : ''}`}
            onClick={() => setActiveTab('ROLLOUT')}
          >
            <GitCommit size={16} />
            <span>2. Phased Rollout & Circuit Breakers</span>
          </button>
        </div>
      </div>

      <div className="discovery-tab-content">
        {/* TAB 1: 5 CRITICAL RISKS */}
        {activeTab === 'RISKS' && (
          <div className="discovery-section">
            <div className="section-header">
              <div>
                <h2 className="section-title">Critical Failure Modes & Mitigation Architecture</h2>
                <p className="section-subtitle">
                  Proactive technical, algorithmic, and behavioral safeguards protecting user trust and margin integrity.
                </p>
              </div>
            </div>

            <div className="feed-grid" style={{ gridTemplateColumns: '1fr' }}>
              {RISKS_DATA.map((risk) => (
                <div key={risk.id} className="feedback-card" style={{ padding: '1.5rem' }}>
                  <div className="card-top-meta">
                    <div style={{ display: 'flex', alignItems: 'center', gap: '0.6rem' }}>
                      <span className="source-tag">{risk.category}</span>
                      <span className="barrier-badge badge-pink">{risk.statusBadge}</span>
                    </div>
                    <div style={{ display: 'flex', gap: '0.4rem' }}>
                      <span className="return-badge risk-med">Prob: {risk.probability}</span>
                      <span className="return-badge" style={{ background: 'rgba(239, 68, 68, 0.15)', color: '#EF4444' }}>
                        Severity: {risk.severity}
                      </span>
                    </div>
                  </div>

                  <h3 className="card-title" style={{ fontSize: '1.15rem' }}>
                    {risk.name}
                  </h3>

                  {/* Failure Mode */}
                  <div style={{ background: 'rgba(239, 68, 68, 0.06)', borderLeft: '3px solid #EF4444', padding: '0.75rem 1rem', borderRadius: '0 8px 8px 0' }}>
                    <span style={{ fontSize: '0.72rem', fontWeight: 800, color: '#EF4444', textTransform: 'uppercase' }}>
                      Potential Failure Mode:
                    </span>
                    <p style={{ fontSize: '0.85rem', color: '#F9FAFB', marginTop: '0.2rem', lineHeight: 1.5 }}>
                      {risk.failureMode}
                    </p>
                  </div>

                  {/* Mitigation Strategy */}
                  <div style={{ background: 'rgba(16, 185, 129, 0.06)', borderLeft: '3px solid #10B981', padding: '0.75rem 1rem', borderRadius: '0 8px 8px 0' }}>
                    <span style={{ fontSize: '0.72rem', fontWeight: 800, color: '#10B981', textTransform: 'uppercase' }}>
                      Proactive Mitigation Strategy:
                    </span>
                    <p style={{ fontSize: '0.85rem', color: '#F9FAFB', marginTop: '0.2rem', lineHeight: 1.5 }}>
                      {risk.mitigationStrategy}
                    </p>
                  </div>

                  <div className="card-footer" style={{ borderTop: '1px solid rgba(255,255,255,0.06)' }}>
                    <span style={{ color: 'var(--text-secondary)' }}>Automated Guardrail Health Metric:</span>
                    <span style={{ fontWeight: 800, color: '#34D399' }}>{risk.healthThreshold}</span>
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}

        {/* TAB 2: PHASED ROLLOUT & CIRCUIT BREAKERS */}
        {activeTab === 'ROLLOUT' && (
          <div className="discovery-section">
            <div className="section-header">
              <div>
                <h2 className="section-title">Phased Canary Rollout & Automated Circuit Breakers</h2>
                <p className="section-subtitle">
                  Staged 4-phase deployment minimizing blast radius with automated rollback triggers.
                </p>
              </div>
            </div>

            <div className="funnel-steps-list">
              {ROLLOUT_STAGES.map((stg, idx) => (
                <div key={idx} className="stage-card" style={{ padding: '1.5rem' }}>
                  <div className="stage-header">
                    <div className="stage-title-wrap">
                      <span className="stage-step-num">{idx + 1}</span>
                      <div>
                        <h3 className="stage-name" style={{ fontSize: '1.05rem' }}>{stg.stage}</h3>
                        <div style={{ fontSize: '0.75rem', color: 'var(--myntra-pink)', fontWeight: 700 }}>
                          {stg.traffic} • Duration: {stg.duration}
                        </div>
                      </div>
                    </div>
                  </div>

                  <p className="stage-desc" style={{ marginTop: '0.5rem' }}>
                    <strong>Validation Focus:</strong> {stg.focus}
                  </p>

                  <div className="key-quote-box" style={{ background: 'rgba(16, 185, 129, 0.06)', borderLeftColor: '#10B981', marginTop: '0.5rem' }}>
                    <span className="quote-label" style={{ color: '#10B981' }}>Gate Exit Criteria:</span>
                    <span className="quote-text" style={{ fontStyle: 'normal', color: '#F9FAFB' }}>
                      {stg.exitCriteria}
                    </span>
                  </div>
                </div>
              ))}
            </div>

            {/* Circuit Breaker Box */}
            <div className="growth-summary-box" style={{ background: 'rgba(239, 68, 68, 0.08)', borderColor: 'rgba(239, 68, 68, 0.3)', marginTop: '1.5rem' }}>
              <ShieldAlert size={22} className="text-red" />
              <div>
                <strong style={{ color: '#EF4444' }}>Automated Rollback Circuit Breakers:</strong>
                <p style={{ marginTop: '0.25rem', fontSize: '0.85rem' }}>
                  If <strong>Fit Returns exceed 24%</strong>, <strong>API p95 latency spikes &gt; 800ms</strong>, or <strong>Wishlist Deletion rate spikes &gt; 8%</strong> during any rollout phase, the feature flag automatically disables new comparisons and routes users back to standard wishlist UI within 60 seconds without client updates.
                </p>
              </div>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}
