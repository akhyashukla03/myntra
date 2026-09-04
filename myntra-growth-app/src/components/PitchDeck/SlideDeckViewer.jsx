import React, { useState, useEffect } from 'react';
import { SLIDE_DECK_DATA, SLIDE_TRACKS } from '../../data/slideDeckData';
import { 
  ChevronLeft, 
  ChevronRight, 
  Presentation, 
  Printer, 
  Layers, 
  Sparkles,
  ExternalLink,
  Smartphone,
  CheckCircle2,
  Sun,
  Moon,
  TrendingUp,
  ShieldCheck,
  Zap,
  ArrowRight,
  Sliders,
  Database,
  BarChart3
} from 'lucide-react';

export default function SlideDeckViewer() {
  const [currentSlideIdx, setCurrentSlideIdx] = useState(0);
  const [viewMode, setViewMode] = useState('single'); // 'single' or 'all'
  const [deckTheme, setDeckTheme] = useState('light'); // 'light' (Original Zepto style) or 'dark'
  const slide = SLIDE_DECK_DATA[currentSlideIdx];

  const handleNext = () => {
    if (currentSlideIdx < SLIDE_DECK_DATA.length - 1) {
      setCurrentSlideIdx((prev) => prev + 1);
    }
  };

  const handlePrev = () => {
    if (currentSlideIdx > 0) {
      setCurrentSlideIdx((prev) => prev - 1);
    }
  };

  // Keyboard navigation
  useEffect(() => {
    const handleKeyDown = (e) => {
      if (viewMode !== 'single') return;
      if (e.key === 'ArrowRight' || e.key === 'Space') {
        e.preventDefault();
        handleNext();
      } else if (e.key === 'ArrowLeft') {
        e.preventDefault();
        handlePrev();
      }
    };
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [currentSlideIdx, viewMode]);

  // Render varied visual slide layouts based on slide number
  const renderSlideContent = (s) => {
    // SLIDE 3: Research & Thinking Evolution Narrative Layout
    if (s.slideNumber === 3) {
      return (
        <div className="slide-varied-layout research-evolution-layout">
          {/* Thinking Evolution Timeline */}
          <div className="evolution-section">
            <h3 className="section-subtitle-pill">🧠 STRATEGIC THINKING EVOLUTION NARRATIVE</h3>
            <div className="evolution-grid">
              {s.thinkingEvolution.map((item, idx) => (
                <div key={idx} className="evolution-step-card">
                  <div className="step-badge">{item.stage}</div>
                  <p className="step-desc">{item.desc}</p>
                </div>
              ))}
            </div>
          </div>

          {/* AI Discovery Workflow */}
          <div className="discovery-section">
            <div className="section-header-row">
              <h3 className="section-subtitle-pill">🔬 AI DISCOVERY PIPELINE WORKFLOW</h3>
              <a href="https://myntra-growth-lab.vercel.app" target="_blank" rel="noreferrer" className="live-discovery-link">
                <ExternalLink size={12} />
                <span>Test Live Discovery Engine</span>
              </a>
            </div>
            <div className="workflow-flow-grid">
              {s.discoveryWorkflow.map((wf, wIdx) => (
                <div key={wIdx} className="workflow-step-card">
                  <div className="wf-title">{wf.step}</div>
                  <div className="wf-detail">{wf.detail}</div>
                </div>
              ))}
            </div>
          </div>
        </div>
      );
    }

    // SLIDE 5: Financial Waterfall & Sensitivity Stress-Testing Layout
    if (s.slideNumber === 5) {
      return (
        <div className="slide-varied-layout financial-sensitivity-layout">
          <div className="financial-grid-wrapper">
            {/* Financial Ledger Breakdown */}
            <div className="ledger-card-wrapper">
              <h3 className="section-subtitle-pill">📊 BOTTOM-UP FINANCIAL WATERFALL</h3>
              <div className="waterfall-list">
                {s.financialWaterfall.map((item, fIdx) => (
                  <div key={fIdx} className="waterfall-row">
                    <div className="wf-metric-info">
                      <span className="wf-metric-name">{item.metric}</span>
                      <span className="wf-metric-detail">{item.detail}</span>
                    </div>
                    <span className="wf-metric-val">{item.val}</span>
                  </div>
                ))}
              </div>
            </div>

            {/* Sensitivity Stress-Testing Scenarios */}
            <div className="sensitivity-card-wrapper">
              <h3 className="section-subtitle-pill">🛡️ SENSITIVITY STRESS-TESTING SCENARIOS</h3>
              <div className="sensitivity-table">
                <div className="sens-table-header">
                  <span>Scenario</span>
                  <span>Lift</span>
                  <span>Profit/Mo</span>
                  <span>ROI</span>
                  <span>Payback</span>
                </div>
                {s.sensitivityTable.map((sens, sIdx) => (
                  <div key={sIdx} className={`sens-table-row ${sIdx === 0 ? 'base-case' : sIdx === 2 ? 'stress-case' : ''}`}>
                    <span className="sens-scen-name">{sens.scenario}</span>
                    <span>{sens.convLift}</span>
                    <span>{sens.monthlyProfit}</span>
                    <span className="sens-roi-val">{sens.featureRoi}</span>
                    <span>{sens.payback}</span>
                  </div>
                ))}
              </div>
              <div className="sensitivity-note-box">
                <strong>Stress-Test Proof:</strong> Even under a 50% target drop (+150 bps lift), annual value exceeds ₹117 Cr at a 110x ROI with payback under 8 days.
              </div>
            </div>
          </div>
        </div>
    // SLIDE 7: MVP Showcase (Wireframe Cards & Deployed Product Visuals)
    if (s.slideNumber === 7) {
      return (
        <div className="slide-varied-layout mvp-showcase-layout">
          <div className="showcase-header-tag">
            <span>🚀 LIVE DEPLOYED PRODUCT SHOWCASE & INTERACTIVE MVP MODULES</span>
            <a href="https://myntra-growth-lab.vercel.app" target="_blank" rel="noreferrer" className="mvp-live-btn">
              <ExternalLink size={13} />
              <span>Launch Live Prototype (https://myntra-growth-lab.vercel.app)</span>
            </a>
          </div>

          <div className="mvp-wireframes-grid">
            {s.mvpWireframes.map((wf, mIdx) => (
              <div key={mIdx} className="wireframe-card">
                <div className="wf-card-top">
                  <span className="wf-feature-title">{wf.feature}</span>
                  <span className="wf-badge">{wf.badge}</span>
                </div>
                
                {/* Embedded High-Fidelity Figma SVG Screen */}
                <div className="wireframe-mock-ui figma-embed-container">
                  {wf.figmaSvg ? (
                    <img 
                      src={wf.figmaSvg} 
                      alt={wf.feature} 
                      className="figma-showcase-svg-img" 
                    />
                  ) : (
                    <>
                      <div className="ui-header-strip">{wf.uiBox.header}</div>
                      <div className="ui-columns">
                        <div className="ui-col col-primary">{wf.uiBox.col1}</div>
                        <div className="ui-col col-secondary">{wf.uiBox.col2}</div>
                      </div>
                    </>
                  )}
                </div>

                <div className="wf-impact-value">
                  <Zap size={14} className="text-pink" />
                  <span>{wf.value}</span>
                </div>
              </div>
            ))}
          </div>
        </div>
      );
    }

    // SLIDE 8: User Emotion Journey & System Architecture Layout
    if (s.slideNumber === 8) {
      return (
        <div className="slide-varied-layout architecture-journey-layout">
          {/* User Emotion State Transition Flow */}
          <div className="journey-flow-wrapper">
            <h3 className="section-subtitle-pill">📱 USER EMOTIONAL STATE TRANSITION MAP (4 STAGES)</h3>
            <div className="emotion-stages-grid">
              {s.userEmotionJourney.map((stg, eIdx) => (
                <div key={eIdx} className="emotion-stage-card">
                  <div className="stage-header-title">{stg.stage}</div>
                  <div className="stage-emotion-badge">{stg.emotion}</div>
                  <div className="stage-trigger">{stg.trigger}</div>
                  <div className="stage-tech-resolver">{stg.techResolver}</div>
                </div>
              ))}
            </div>
          </div>

          {/* 4-Layer System Stack Table & Desktop Workspace */}
          <div className="system-stack-wrapper">
            <h3 className="section-subtitle-pill">⚙️ 4-LAYER TECHNICAL SYSTEM STACK & DESKTOP WORKSPACE</h3>
            <div className="system-arch-visual-split">
              <div className="system-stack-grid">
                {s.systemArchitectureLayers.map((layer, lIdx) => (
                  <div key={lIdx} className="stack-layer-card">
                    <div className="layer-name">{layer.layer}</div>
                    <div className="layer-tech">{layer.tech}</div>
                    <div className="layer-sla">{layer.latency}</div>
                  </div>
                ))}
              </div>
              {s.figmaSvg && (
                <div className="desktop-figma-preview-box">
                  <img 
                    src={s.figmaSvg} 
                    alt="Desktop Web Workspace" 
                    className="figma-desktop-workspace-img"
                  />
                </div>
              )}
            </div>
          </div>
        </div>
      );
    }

    // SLIDE 9: Visual Metric Tree & A/B Experiment Design Layout
    if (s.slideNumber === 9) {
      return (
        <div className="slide-varied-layout metrics-experiment-layout">
          {/* Visual Metric Tree */}
          <div className="metric-tree-wrapper">
            <h3 className="section-subtitle-pill">🌳 VISUAL METRIC HIERARCHY TREE</h3>
            <div className="tree-nodes-list">
              {s.metricTree.map((node, nIdx) => (
                <div key={nIdx} className={`tree-node-card level-${nIdx}`}>
                  <div className="node-level-tag">{node.level}</div>
                  <div className="node-metric-name">{node.name}</div>
                  <div className="node-values-row">
                    <span className="base-val">{node.baseline}</span>
                    <ArrowRight size={12} />
                    <span className="target-val">{node.target}</span>
                  </div>
                </div>
              ))}
            </div>
          </div>

          {/* A/B Experimentation Setup */}
          <div className="ab-setup-wrapper">
            <h3 className="section-subtitle-pill">🧪 200,000-USER RANDOMIZED CONTROLLED TRIAL (RCT)</h3>
            <div className="ab-params-grid">
              {s.abExperimentation.map((ab, aIdx) => (
                <div key={aIdx} className="ab-param-card">
                  <span className="ab-param-label">{ab.param}</span>
                  <span className="ab-param-val">{ab.val}</span>
                </div>
              ))}
            </div>
          </div>
        </div>
      );
    }

    // Standard 3-Column Layout for Slides 1, 2, 4, 6, 10
    return (
      <div className="slide-body-grid">
        {/* Card 1: Left Strategic Column */}
        <div className="slide-evidence-card">
          <div className="evidence-card-header">
            <span className="evidence-card-title">{s.leftCard.title}</span>
          </div>
          <div className="evidence-card-body">
            <ul className="evidence-bullets">
              {s.leftCard.bullets.map((bullet, idx) => (
                <li key={idx} className="evidence-bullet-item">
                  <span className="bullet-dot">•</span>
                  <div className="bullet-text-wrapper">
                    <strong>{bullet.bold}</strong> {bullet.text}
                  </div>
                </li>
              ))}
            </ul>
          </div>
        </div>

        {/* Card 2: Mid Analytical Column */}
        <div className="slide-evidence-card">
          <div className="evidence-card-header">
            <span className="evidence-card-title">{s.midCard.title}</span>
          </div>
          <div className="evidence-card-body">
            <ul className="evidence-bullets">
              {s.midCard.bullets.map((bullet, idx) => (
                <li key={idx} className="evidence-bullet-item">
                  <span className="bullet-dot">•</span>
                  <div className="bullet-text-wrapper">
                    <strong>{bullet.bold}</strong> {bullet.text}
                  </div>
                </li>
              ))}
            </ul>
          </div>
        </div>

        {/* Card 3: Right Smartphone Device Mockup with Figma Embed */}
        <div className="slide-phone-mockup-wrapper">
          <div className="smartphone-device-frame">
            <div className="smartphone-notch">
              <div className="speaker-earpiece"></div>
              <div className="camera-dot"></div>
            </div>

            <div className="smartphone-screen figma-screen-view">
              {s.figmaSvg ? (
                <img 
                  src={s.figmaSvg} 
                  alt={s.phoneMockup.screenName} 
                  className="figma-phone-screen-svg" 
                />
              ) : (
                <div className="phone-screen-content">
                  <div className="screen-title-banner">
                    <Smartphone size={12} className="screen-icon" />
                    <span>{s.phoneMockup.screenName}</span>
                  </div>

                  <div className="phone-metrics-list">
                    {s.phoneMockup.items.map((item, mIdx) => (
                      <div key={mIdx} className="phone-metric-row">
                        <span className="phone-metric-label">{item.label}</span>
                        <span className="phone-metric-val">{item.val}</span>
                      </div>
                    ))}
                  </div>

                  <div className="phone-action-box">
                    <button className="phone-cta-btn">
                      <span>{s.phoneMockup.ctaText}</span>
                    </button>
                  </div>
                </div>
              )}

              <div className="smartphone-bottom-indicator"></div>
            </div>
          </div>
        </div>
      </div>
    );
  };

  // Render individual slide canvas
  const renderSlideCanvas = (s, isPrint = false) => {
    return (
      <div 
        key={s.slideNumber} 
        className={`zepto-slide-canvas ${deckTheme === 'dark' ? 'dark-canvas' : 'light-canvas'} ${isPrint ? 'print-page' : ''}`}
      >
        {/* 1. Top Category Pill Banner */}
        <div className="slide-top-banner-row">
          <div className="category-streak-pill">
            <span>{s.topBanner}</span>
          </div>
        </div>

        {/* 2. Slide Main Header & Brand Section */}
        <div className="slide-main-header-row">
          <div className="slide-title-block">
            <h1 className="slide-takeaway-title">{s.title}</h1>
            <p className="slide-takeaway-subtitle">{s.subtitle}</p>
          </div>
          <div className="slide-brand-logo">
            <span className="brand-myntra-text">myntra</span>
          </div>
        </div>

        {/* 3. Slide Content Area (Varied Layouts) */}
        {renderSlideContent(s)}

        {/* 4. Bottom Horizontal Synthesis Banner */}
        <div className="slide-bottom-synthesis-card">
          <div className="synthesis-header-label">
            <Sparkles size={13} className="text-pink" />
            <span>{s.bottomBanner.title}</span>
          </div>
          <div className="synthesis-text-body">
            {s.bottomBanner.text}
          </div>
        </div>
      </div>
    );
  };

  return (
    <div className="module-container slide-deck-module">
      <div className="deck-viewer-container">
        
        {/* Top Floating Control Bar & Slide Track Bar */}
        <div className="deck-controls-bar no-print">
          <div className="deck-meta">
            <div className="deck-pill">
              <Presentation size={15} className="text-pink" />
              <span>Top Fellow Executive Pitch Deck (10 Slides)</span>
            </div>

            {/* 10-Track Stage Selector Buttons */}
            <div className="top-track-ribbon">
              {SLIDE_TRACKS.map((trackName, tIdx) => (
                <button
                  key={trackName}
                  className={`top-track-btn ${tIdx === currentSlideIdx ? 'active-track' : ''}`}
                  onClick={() => setCurrentSlideIdx(tIdx)}
                >
                  #{tIdx + 1} {trackName}
                </button>
              ))}
            </div>
          </div>

          <div className="deck-btn-group">
            {/* Theme Toggle */}
            <button
              className="deck-nav-btn"
              onClick={() => setDeckTheme(deckTheme === 'light' ? 'dark' : 'light')}
              title="Toggle Light / Dark Presentation Canvas"
            >
              {deckTheme === 'light' ? <Moon size={15} /> : <Sun size={15} />}
              <span>{deckTheme === 'light' ? 'Dark Canvas' : 'Light Canvas'}</span>
            </button>

            {/* View Mode Toggle */}
            <button
              className={`deck-nav-btn ${viewMode === 'all' ? 'active' : ''}`}
              onClick={() => setViewMode(viewMode === 'single' ? 'all' : 'single')}
              title="Toggle all 10 slides overview"
            >
              <Layers size={15} />
              <span>{viewMode === 'single' ? 'View All 10 Slides' : 'Single Slide Focus'}</span>
            </button>

            {/* Print / PDF Export */}
            <button
              className="deck-nav-btn"
              onClick={() => window.print()}
              title="Print or Save Presentation as PDF"
            >
              <Printer size={15} />
              <span>Print / Save PDF</span>
            </button>

            {viewMode === 'single' && (
              <>
                <button
                  className="deck-nav-btn"
                  onClick={handlePrev}
                  disabled={currentSlideIdx === 0}
                  title="Previous Slide (Left Arrow)"
                >
                  <ChevronLeft size={18} />
                  <span>Prev</span>
                </button>

                <span className="deck-counter-badge">
                  {slide.slideNumber} / {SLIDE_DECK_DATA.length} ({slide.track})
                </span>

                <button
                  className="deck-nav-btn"
                  onClick={handleNext}
                  disabled={currentSlideIdx === SLIDE_DECK_DATA.length - 1}
                  title="Next Slide (Right Arrow)"
                >
                  <span>Next</span>
                  <ChevronRight size={18} />
                </button>
              </>
            )}
          </div>
        </div>

        {/* Slide Canvas Viewport */}
        {viewMode === 'single' ? (
          renderSlideCanvas(slide)
        ) : (
          <div className="all-slides-stack-container">
            {SLIDE_DECK_DATA.map((s) => renderSlideCanvas(s, true))}
          </div>
        )}

      </div>
    </div>
  );
}
