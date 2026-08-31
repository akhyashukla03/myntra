import React, { useState } from 'react';
import { Target, TrendingUp, Activity, ShieldAlert, Scale, Calculator, Sliders, Sparkles, ShieldCheck, Database, SplitSquareVertical, AlertTriangle } from 'lucide-react';
import { METRICS_TABLE, TRACKING_EVENTS } from '../SuccessMetrics/SuccessMetricsStudio';
import { RISKS_DATA } from '../RisksMitigations/RisksMitigationsStudio';

export const INITIAL_SOLUTIONS = [
  {
    id: "sol_1",
    name: "Side-by-Side Comparison Studio",
    pillar: "Pillar 1: Evaluation Efficiency",
    description: "Compare 2-4 shortlisted items on fabric GSM, verified fit consensus, and customer photos.",
    reach: 3500000,
    impact: 3,
    confidence: 0.90,
    effort: 2.5,
    rationale: "Solves comparison paralysis (35% of all drop-offs) with low-to-medium technical complexity."
  },
  {
    id: "sol_2",
    name: "1-Tap WhatsApp Social Voting Card",
    pillar: "Pillar 2: Social Validation",
    description: "Generates a shareable micro-card where friends vote Option A vs B with live sync.",
    reach: 2800000,
    impact: 2.5,
    confidence: 0.85,
    effort: 2.0,
    rationale: "Eliminates 12-24hr screenshot latency; leverages existing WhatsApp viral loop with zero friction."
  },
  {
    id: "sol_3",
    name: "AI Outfit Matcher & Coordinated Look Builder",
    pillar: "Pillar 3: Styling Coordination",
    description: "Generates 3 complete curated looks matching wishlisted items with 1-tap bundle add.",
    reach: 3200000,
    impact: 2.0,
    confidence: 0.80,
    effort: 3.5,
    rationale: "Solves styling hesitation (28% drop-off) and lifts Average Order Value via cross-category add."
  },
  {
    id: "sol_4",
    name: "Smart Occasion Auto-Clustering Folders",
    pillar: "Pillar 4: Wishlist Organization",
    description: "Automatically categorizes raw wishlist bookmarks into 'Workwear', 'Streetwear', 'Party'.",
    reach: 4500000,
    impact: 1.5,
    confidence: 0.80,
    effort: 2.0,
    rationale: "Reduces graveyard clutter, but lower standalone conversion impact without comparison clarity."
  },
  {
    id: "sol_5",
    name: "Automated Push Notification Price Alerts",
    pillar: "Discarded Alternative",
    description: "Alerts users when wishlisted items drop by 5-10% in price.",
    reach: 5000000,
    impact: 1.0,
    confidence: 0.70,
    effort: 1.5,
    rationale: "REJECTED: Violates zero-discount constraint and dilutes platform gross margins."
  }
];

export default function ProblemStrategyStudio() {
  const [activeTab, setActiveTab] = useState('METRICS_SIMULATOR'); // 'METRICS_SIMULATOR', 'RICE_PRIORITIZATION', 'SUCCESS_METRICS', 'RISKS_GUARDRAILS'

  // Metric Tree Simulator Levers
  const [activeWishlistUsers, setActiveWishlistUsers] = useState(10000000);
  const [compareAdoption, setCompareAdoption] = useState(35);
  const [outfitAdoption, setOutfitAdoption] = useState(24);
  const [socialAdoption, setSocialAdoption] = useState(18);
  const [avgOrderValue, setAvgOrderValue] = useState(1650);

  const baselineConvRate = 7.5;
  const compareLift = (compareAdoption / 100) * 1.5;
  const outfitLift = (outfitAdoption / 100) * 1.2;
  const socialLift = (socialAdoption / 100) * 0.8;
  const totalLiftPercent = compareLift + outfitLift + socialLift;
  const targetConvRate = (baselineConvRate + totalLiftPercent).toFixed(2);
  const totalLiftBps = Math.round(totalLiftPercent * 100);

  const baselineBuyers = Math.round(activeWishlistUsers * (baselineConvRate / 100));
  const targetBuyers = Math.round(activeWishlistUsers * (Number(targetConvRate) / 100));
  const incrementalBuyers = targetBuyers - baselineBuyers;
  const incrementalGMVCr = ((incrementalBuyers * avgOrderValue) / 10000000).toFixed(2);
  const returnSavingsCr = ((incrementalBuyers * 0.06 * 450) / 10000000).toFixed(2);

  // RICE calculation
  const calculateRice = (item) => {
    return Math.round((item.reach * item.impact * item.confidence) / (item.effort * 10000));
  };
  const sortedSolutions = [...INITIAL_SOLUTIONS].sort((a, b) => calculateRice(b) - calculateRice(a));

  return (
    <div className="module-container">
      {/* Top Banner */}
      <div className="discovery-hero-banner">
        <div className="hero-content">
          <div className="hero-badge">
            <TrendingUp size={14} className="text-pink" />
            <span>Growth Strategy & Decision Modeling Suite</span>
          </div>
          <h1 className="hero-title">Growth PM Strategy, Metric Tree & Prioritization Hub</h1>
          <p className="hero-subtitle">
            Consolidating mathematical opportunity sizing, live feature sensitivity modeling, RICE scoring, Amplitude event schemas, and risk guardrails.
          </p>
        </div>

        {/* 4 Clean Sub-Tabs */}
        <div className="hero-nav-tabs">
          <button
            className={`hero-tab-btn ${activeTab === 'METRICS_SIMULATOR' ? 'active' : ''}`}
            onClick={() => setActiveTab('METRICS_SIMULATOR')}
          >
            <Calculator size={16} />
            <span>1. Metric Tree & Live Simulator</span>
          </button>

          <button
            className={`hero-tab-btn ${activeTab === 'RICE_PRIORITIZATION' ? 'active' : ''}`}
            onClick={() => setActiveTab('RICE_PRIORITIZATION')}
          >
            <Scale size={16} />
            <span>2. Problem Framing & RICE Matrix</span>
          </button>

          <button
            className={`hero-tab-btn ${activeTab === 'SUCCESS_METRICS' ? 'active' : ''}`}
            onClick={() => setActiveTab('SUCCESS_METRICS')}
          >
            <Activity size={16} />
            <span>3. Success Metrics & Amplitude Schema</span>
          </button>

          <button
            className={`hero-tab-btn ${activeTab === 'RISKS_GUARDRAILS' ? 'active' : ''}`}
            onClick={() => setActiveTab('RISKS_GUARDRAILS')}
          >
            <ShieldAlert size={16} />
            <span>4. Rollout Guardrails & Risk Mitigation</span>
          </button>
        </div>
      </div>

      <div className="discovery-tab-content">
        {/* TAB 1: Metric Tree & Live Simulator */}
        {activeTab === 'METRICS_SIMULATOR' && (
          <div className="discovery-section">
            <div className="metric-tree-card">
              <div className="tree-header">
                <TrendingUp size={20} className="text-pink" />
                <h2 className="tree-title">North Star Metric Decomposition Formula</h2>
              </div>

              <div className="formula-display-box">
                <div className="formula-main">
                  <span className="formula-term">30-Day Wishlist Conv. Rate (%)</span>
                  <span className="formula-op">=</span>
                  <span className="formula-term">Wishlist Discovery Rate</span>
                  <span className="formula-op">&times;</span>
                  <span className="formula-term">Multi-Item Compare Rate</span>
                  <span className="formula-op">&times;</span>
                  <span className="formula-term">Move-to-Bag Rate</span>
                  <span className="formula-op">&times;</span>
                  <span className="formula-term">(1 &minus; Sizing Return Rate)</span>
                </div>
                <p className="formula-caption">
                  Every product lever directly lifts an input metric while safeguarding margin integrity (zero promo codes).
                </p>
              </div>

              <div className="funnel-pillars-grid">
                <div className="pillar-card">
                  <div className="pillar-top">
                    <span className="pillar-num">1</span>
                    <h3 className="pillar-title">Intent & Organization</h3>
                  </div>
                  <p className="pillar-desc">Transforms the raw bookmarking graveyard into structured occasion folders.</p>
                  <div className="pillar-metrics-list">
                    <div className="pillar-metric-item">
                      <span className="metric-kpi-name">Occasion Folder Adoption</span>
                      <span className="metric-kpi-target">Target: &ge; 40%</span>
                    </div>
                  </div>
                </div>

                <div className="pillar-card">
                  <div className="pillar-top">
                    <span className="pillar-num pillar-purple">2</span>
                    <h3 className="pillar-title">Evaluation Efficiency</h3>
                  </div>
                  <p className="pillar-desc">Eliminates side-by-side comparison paralysis between subtle silhouette variations.</p>
                  <div className="pillar-metrics-list">
                    <div className="pillar-metric-item">
                      <span className="metric-kpi-name">Side-by-Side Compare Rate</span>
                      <span className="metric-kpi-target">Target: &ge; 35%</span>
                    </div>
                  </div>
                </div>

                <div className="pillar-card">
                  <div className="pillar-top">
                    <span className="pillar-num pillar-blue">3</span>
                    <h3 className="pillar-title">Checkout Confidence</h3>
                  </div>
                  <p className="pillar-desc">Resolves single-item styling hesitation and sizing anxiety before checkout.</p>
                  <div className="pillar-metrics-list">
                    <div className="pillar-metric-item">
                      <span className="metric-kpi-name">Outfit Matcher Bundle Add</span>
                      <span className="metric-kpi-target">Target: &ge; 22%</span>
                    </div>
                  </div>
                </div>
              </div>
            </div>

            {/* Live Interactive Sensitivity Simulator */}
            <div className="simulator-section-card">
              <div className="sim-header">
                <div className="sim-title-row">
                  <Calculator size={22} className="text-pink" />
                  <div>
                    <h2 className="sim-title">Live Growth & Sensitivity Simulation Engine</h2>
                    <p className="sim-sub">Adjust feature adoption levers to model conversion lift, transacting volume, and incremental revenue.</p>
                  </div>
                </div>
              </div>

              <div className="simulator-two-col">
                <div className="sliders-panel">
                  <h3 className="sliders-heading">
                    <Sliders size={16} />
                    <span>Adjust Growth Levers & Feature Adoption:</span>
                  </h3>

                  <div className="slider-group">
                    <div className="slider-label-row">
                      <span>Monthly Active Wishlist Users:</span>
                      <span className="slider-val-badge">{(activeWishlistUsers / 1000000).toFixed(1)}M Users</span>
                    </div>
                    <input
                      type="range"
                      min={5000000}
                      max={20000000}
                      step={500000}
                      value={activeWishlistUsers}
                      onChange={(e) => setActiveWishlistUsers(Number(e.target.value))}
                      className="custom-range-slider"
                    />
                  </div>

                  <div className="slider-group">
                    <div className="slider-label-row">
                      <span>Side-by-Side Comparison Studio Adoption:</span>
                      <span className="slider-val-badge text-pink">{compareAdoption}% Users</span>
                    </div>
                    <input
                      type="range"
                      min={10}
                      max={70}
                      step={1}
                      value={compareAdoption}
                      onChange={(e) => setCompareAdoption(Number(e.target.value))}
                      className="custom-range-slider"
                    />
                  </div>

                  <div className="slider-group">
                    <div className="slider-label-row">
                      <span>AI Outfit Matcher & Look Builder Adoption:</span>
                      <span className="slider-val-badge text-purple">{outfitAdoption}% Users</span>
                    </div>
                    <input
                      type="range"
                      min={5}
                      max={50}
                      step={1}
                      value={outfitAdoption}
                      onChange={(e) => setOutfitAdoption(Number(e.target.value))}
                      className="custom-range-slider"
                    />
                  </div>

                  <div className="slider-group">
                    <div className="slider-label-row">
                      <span>1-Tap WhatsApp Voting Card Adoption:</span>
                      <span className="slider-val-badge text-blue">{socialAdoption}% Users</span>
                    </div>
                    <input
                      type="range"
                      min={5}
                      max={40}
                      step={1}
                      value={socialAdoption}
                      onChange={(e) => setSocialAdoption(Number(e.target.value))}
                      className="custom-range-slider"
                    />
                  </div>

                  <div className="slider-group">
                    <div className="slider-label-row">
                      <span>Average Order Value (AOV):</span>
                      <span className="slider-val-badge">₹{avgOrderValue.toLocaleString()}</span>
                    </div>
                    <input
                      type="range"
                      min={1000}
                      max={3000}
                      step={50}
                      value={avgOrderValue}
                      onChange={(e) => setAvgOrderValue(Number(e.target.value))}
                      className="custom-range-slider"
                    />
                  </div>
                </div>

                <div className="sim-results-panel">
                  <h3 className="results-heading">
                    <Sparkles size={16} className="text-pink" />
                    <span>Simulated Business Impact (30-Day Cohort):</span>
                  </h3>

                  <div className="sim-kpi-grid">
                    <div className="sim-kpi-card highlight-card">
                      <span className="sim-kpi-label">Projected 30-Day Conversion</span>
                      <div className="sim-kpi-main-val text-pink">{targetConvRate}%</div>
                      <span className="sim-kpi-sub">+{totalLiftBps} bps lift from baseline ({baselineConvRate}%)</span>
                    </div>

                    <div className="sim-kpi-card">
                      <span className="sim-kpi-label">Incremental Transacting Users</span>
                      <div className="sim-kpi-main-val text-purple">+{incrementalBuyers.toLocaleString()}</div>
                      <span className="sim-kpi-sub">Total: {targetBuyers.toLocaleString()} converting users</span>
                    </div>

                    <div className="sim-kpi-card">
                      <span className="sim-kpi-label">Monthly Incremental GMV</span>
                      <div className="sim-kpi-main-val text-green">+₹{incrementalGMVCr} Cr</div>
                      <span className="sim-kpi-sub">100% Non-discounted margin intact</span>
                    </div>

                    <div className="sim-kpi-card">
                      <span className="sim-kpi-label">Return Cost Savings (Fit Clarity)</span>
                      <div className="sim-kpi-main-val text-blue">+₹{returnSavingsCr} Cr</div>
                      <span className="sim-kpi-sub">Via -600 bps reduction in sizing returns</span>
                    </div>
                  </div>

                  <div className="growth-summary-box">
                    <ShieldCheck size={18} className="text-green" />
                    <p>
                      <strong>Zero-Discount Mandate Validated:</strong> By solving comparison paralysis (+{((compareLift) * 100).toFixed(0)} bps) and outfit styling hesitation (+{((outfitLift) * 100).toFixed(0)} bps), Myntra captures <strong>+{incrementalBuyers.toLocaleString()} transacting buyers</strong> without spending ₹1 on promotional discounts.
                    </p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        )}

        {/* TAB 2: Problem Framing & RICE Prioritization */}
        {activeTab === 'RICE_PRIORITIZATION' && (
          <div className="discovery-section">
            <div className="simulator-section-card">
              <div className="sim-header">
                <div className="sim-title-row">
                  <Scale size={22} className="text-pink" />
                  <div>
                    <h2 className="sim-title">RICE Framework Solution Prioritization Matrix</h2>
                    <p className="sim-sub">
                      Mathematical evaluation: RICE Score = (Reach × Impact × Confidence) / Effort.
                    </p>
                  </div>
                </div>
              </div>

              <div className="category-table-wrapper">
                <table className="category-table">
                  <thead>
                    <tr>
                      <th>Rank</th>
                      <th>Solution Intervention</th>
                      <th>Strategic Pillar</th>
                      <th>Reach (Users)</th>
                      <th>Impact</th>
                      <th>Confidence</th>
                      <th>Effort</th>
                      <th>RICE Score</th>
                      <th>Status</th>
                    </tr>
                  </thead>
                  <tbody>
                    {sortedSolutions.map((sol, sIdx) => {
                      const riceScore = calculateRice(sol);
                      const isTop = sIdx < 3;
                      const isRejected = sol.id === 'sol_5';

                      return (
                        <tr key={sol.id}>
                          <td style={{ fontWeight: 800, color: isRejected ? '#6B7280' : '#FF3F6C' }}>
                            #{sIdx + 1}
                          </td>
                          <td>
                            <div className="cat-name-cell">{sol.name}</div>
                            <div className="friction-cell">{sol.description}</div>
                          </td>
                          <td>
                            <span className="share-pill">{sol.pillar}</span>
                          </td>
                          <td>{(sol.reach / 1000000).toFixed(1)}M</td>
                          <td>{sol.impact}x</td>
                          <td>{(sol.confidence * 100).toFixed(0)}%</td>
                          <td>{sol.effort} mo</td>
                          <td>
                            <span className={`conv-pill ${isRejected ? 'text-muted' : ''}`}>
                              {riceScore}
                            </span>
                          </td>
                          <td>
                            {isRejected ? (
                              <span className="return-badge risk-med">Rejected (Margin Risk)</span>
                            ) : isTop ? (
                              <span className="return-badge risk-low">MVP Priority</span>
                            ) : (
                              <span className="return-badge">Phase 2</span>
                            )}
                          </td>
                        </tr>
                      );
                    })}
                  </tbody>
                </table>
              </div>
            </div>
          </div>
        )}

        {/* TAB 3: Success Metrics & Amplitude Event Schema */}
        {activeTab === 'SUCCESS_METRICS' && (
          <div className="discovery-section">
            <div className="simulator-section-card">
              <div className="sim-header">
                <div className="sim-title-row">
                  <Activity size={22} className="text-pink" />
                  <div>
                    <h2 className="sim-title">Metrics Hierarchy & Amplitude Event Schema</h2>
                    <p className="sim-sub">Comprehensive measurement dictionary for North Star, leading indicators, and tracking properties.</p>
                  </div>
                </div>
              </div>

              <div className="category-table-wrapper">
                <table className="category-table">
                  <thead>
                    <tr>
                      <th>Hierarchy</th>
                      <th>Metric Name</th>
                      <th>Baseline &rarr; Target</th>
                      <th>Mathematical Definition</th>
                    </tr>
                  </thead>
                  <tbody>
                    {METRICS_TABLE.map((m, idx) => (
                      <tr key={idx}>
                        <td><span className="share-pill">{m.category}</span></td>
                        <td><strong className="cat-name-cell">{m.name}</strong></td>
                        <td><span className="conv-pill">{m.baseline} &rarr; {m.target}</span></td>
                        <td className="friction-cell">{m.formula}</td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>

              <h3 style={{ marginTop: '2rem', marginBottom: '1rem', fontSize: '1.1rem', fontWeight: 800 }}>
                Amplitude / Mixpanel Event Tracking Dictionary:
              </h3>
              <div className="category-table-wrapper">
                <table className="category-table">
                  <thead>
                    <tr>
                      <th>Event Name</th>
                      <th>Trigger Condition</th>
                      <th>Tracked Properties</th>
                    </tr>
                  </thead>
                  <tbody>
                    {TRACKING_EVENTS.map((evt, idx) => (
                      <tr key={idx}>
                        <td><code style={{ color: '#FF3F6C', fontWeight: 700 }}>{evt.eventName}</code></td>
                        <td className="friction-cell">{evt.trigger}</td>
                        <td>
                          <div style={{ display: 'flex', gap: '0.35rem', flexWrap: 'wrap' }}>
                            {evt.properties.map((p, pIdx) => (
                              <span key={pIdx} className="spec-chip">{p}</span>
                            ))}
                          </div>
                        </td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            </div>
          </div>
        )}

        {/* TAB 4: Rollout Guardrails & Risk Mitigation */}
        {activeTab === 'RISKS_GUARDRAILS' && (
          <div className="discovery-section">
            <div className="simulator-section-card">
              <div className="sim-header">
                <div className="sim-title-row">
                  <ShieldAlert size={22} className="text-pink" />
                  <div>
                    <h2 className="sim-title">Pre-Mortem Risk Analysis & Phased Canary Rollout</h2>
                    <p className="sim-sub">Comprehensive failure mode mitigation and canary release safeguards.</p>
                  </div>
                </div>
              </div>

              <div className="category-table-wrapper">
                <table className="category-table">
                  <thead>
                    <tr>
                      <th>Failure Mode</th>
                      <th>Severity</th>
                      <th>Mitigation Strategy</th>
                      <th>Trigger / Guardrail</th>
                    </tr>
                  </thead>
                  <tbody>
                    {RISKS_DATA.map((risk, idx) => (
                      <tr key={idx}>
                        <td><strong className="cat-name-cell">{risk.risk}</strong></td>
                        <td>
                          <span className={`return-badge ${risk.severity === 'High' ? 'risk-high' : 'risk-med'}`}>
                            {risk.severity} Severity
                          </span>
                        </td>
                        <td className="friction-cell">{risk.mitigation}</td>
                        <td style={{ color: '#34D399', fontWeight: 700 }}>{risk.guardrail}</td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}
