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
  BarChart3,
  Users,
  Target,
  FileSpreadsheet
} from 'lucide-react';

export default function SlideDeckViewer() {
  const [currentSlideIdx, setCurrentSlideIdx] = useState(0);
  const [viewMode, setViewMode] = useState('single'); // 'single' or 'all'
  const [deckTheme, setDeckTheme] = useState('light');
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
    // SLIDE 1: Strategic Brief + 5-Step Unit Economics Waterfall
    if (s.slideNumber === 1 && s.midCard && s.midCard.bullets) {
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

          {/* Card 2: Mid 5-Step Waterfall Column */}
          <div className="slide-evidence-card financial-waterfall-card">
            <div className="evidence-card-header">
              <span className="evidence-card-title">{s.midCard.title}</span>
            </div>
            <div className="evidence-card-body">
              <ul className="evidence-bullets">
                {s.midCard.bullets.map((bullet, idx) => (
                  <li key={idx} className="evidence-bullet-item">
                    <span className="bullet-dot" style={{ color: '#03A685' }}>▶</span>
                    <div className="bullet-text-wrapper">
                      <strong style={{ color: '#FF3F6C' }}>{bullet.bold}</strong> {bullet.text}
                    </div>
                  </li>
                ))}
              </ul>
            </div>
          </div>

          {/* Card 3: Phone Mockup */}
          <div className="slide-phone-mockup-wrapper">
            <div className="smartphone-device-frame">
              <div className="smartphone-notch">
                <div className="speaker-earpiece"></div>
                <div className="camera-dot"></div>
              </div>
              <div className="smartphone-screen figma-screen-view">
                {s.figmaSvg ? (
                  <img src={s.figmaSvg} alt={s.phoneMockup.screenName} className="figma-phone-screen-svg" />
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
                  </div>
                )}
              </div>
            </div>
          </div>
        </div>
      );
    }

    // SLIDE 2: Hypothesis + Funnel + Competitor Teardown
    if (s.slideNumber === 2 && s.competitorTeardown) {
      return (
        <div style={{ display: 'grid', gridTemplateColumns: '1.1fr 1fr', gap: '1rem' }}>
          <div style={{ display: 'flex', flexDirection: 'column', gap: '0.8rem' }}>
            <div className="slide-evidence-card">
              <div className="evidence-card-header">
                <span className="evidence-card-title">💡 THE CORE HYPOTHESIS</span>
              </div>
              <div className="evidence-card-body" style={{ fontSize: '0.85rem', lineHeight: '1.4' }}>
                {s.hypothesisBox}
              </div>
            </div>
            <div className="slide-evidence-card">
              <div className="evidence-card-header">
                <span className="evidence-card-title">🌐 GLOBAL & DOMESTIC COMPETITOR TEARDOWN</span>
              </div>
              <div className="evidence-card-body">
                <ul className="evidence-bullets">
                  {s.competitorTeardown.map((comp, cIdx) => (
                    <li key={cIdx} className="evidence-bullet-item">
                      <span className="bullet-dot">•</span>
                      <div className="bullet-text-wrapper">
                        <strong style={{ color: comp.platform.includes('Myntra') ? '#FF3F6C' : 'inherit' }}>{comp.platform}:</strong> {comp.feature}
                      </div>
                    </li>
                  ))}
                </ul>
              </div>
            </div>
          </div>

          <div style={{ display: 'flex', flexDirection: 'column', gap: '0.8rem' }}>
            <div className="slide-evidence-card">
              <div className="evidence-card-header">
                <span className="evidence-card-title">🔄 CURRENT DISCOVERY FLOW (THE GRAVEYARD LOOP)</span>
              </div>
              <div className="evidence-card-body" style={{ display: 'grid', gridTemplateColumns: 'repeat(2, 1fr)', gap: '0.5rem' }}>
                {s.discoveryFunnel.map((step, sIdx) => (
                  <div key={sIdx} style={{ background: '#FFF0F4', border: '1px solid #FFC2D1', borderRadius: '6px', padding: '0.4rem' }}>
                    <div style={{ fontSize: '0.75rem', fontWeight: 700, color: '#FF3F6C' }}>{step.step}</div>
                    <div style={{ fontSize: '0.7rem', color: '#535766' }}>{step.desc}</div>
                  </div>
                ))}
              </div>
            </div>
            <div className="slide-evidence-card">
              <div className="evidence-card-header">
                <span className="evidence-card-title">⚠️ CORE CUSTOMER FRICTIONS</span>
              </div>
              <div className="evidence-card-body">
                <ul className="evidence-bullets">
                  {s.frictionCards.map((fric, fIdx) => (
                    <li key={fIdx} className="evidence-bullet-item">
                      <span className="bullet-dot">•</span>
                      <div className="bullet-text-wrapper">
                        <strong>{fric.title}:</strong> {fric.desc}
                      </div>
                    </li>
                  ))}
                </ul>
              </div>
            </div>
          </div>
        </div>
      );
    }

    // SLIDE 3: Research & Thinking Evolution Narrative Layout
    if (s.slideNumber === 3) {
      return (
        <div className="slide-varied-layout research-evolution-layout">
          {s.evolutionNarrative && (
            <div className="slide-evidence-card" style={{ marginBottom: '0.8rem', background: '#FFF0F4', borderColor: '#FFC2D1' }}>
              <div className="evidence-card-header">
                <span className="evidence-card-title">🔄 STRATEGIC THINKING EVOLUTION PIVOT</span>
              </div>
              <div className="evidence-card-body" style={{ fontSize: '0.82rem', lineHeight: '1.4' }}>
                <div><strong>Initial Hypothesis:</strong> {s.evolutionNarrative.initialHypothesis}</div>
                <div style={{ marginTop: '0.3rem', color: '#FF3F6C' }}><strong>Discovery Finding:</strong> {s.evolutionNarrative.dataFinding}</div>
                <div style={{ marginTop: '0.3rem', color: '#03A685' }}><strong>Strategic Pivot:</strong> {s.evolutionNarrative.strategicPivot}</div>
              </div>
            </div>
          )}

          <div className="discovery-section">
            <div className="section-header-row">
              <h3 className="section-subtitle-pill">💬 NLP QUERIES & SYNTHESIS</h3>
              <a href="https://myntra-growth-lab.vercel.app" target="_blank" rel="noreferrer" className="live-discovery-link">
                <ExternalLink size={12} />
                <span>Test Live Discovery Engine</span>
              </a>
            </div>
            <div className="workflow-flow-grid" style={{ gridTemplateColumns: 'repeat(3, 1fr)' }}>
              {s.nlpPrompts && s.nlpPrompts.map((wf, wIdx) => (
                <div key={wIdx} className="workflow-step-card">
                  <div className="wf-title">{wf.q}</div>
                  <div className="wf-detail">{wf.ans}</div>
                </div>
              ))}
            </div>
          </div>
        </div>
      );
    }

    // SLIDE 4: 4-Quadrant Target Canvas
    if (s.slideNumber === 4 && s.quadrants) {
      return (
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(2, 1fr)', gap: '0.8rem' }}>
          {s.quadrants.map((q, qIdx) => (
            <div key={qIdx} className="slide-evidence-card">
              <div className="evidence-card-header">
                <span className="evidence-card-title">{q.icon} {q.title}</span>
              </div>
              <div className="evidence-card-body">
                <ul className="evidence-bullets">
                  {q.bullets.map((b, bIdx) => (
                    <li key={bIdx} className="evidence-bullet-item">
                      <span className="bullet-dot">•</span>
                      <div className="bullet-text-wrapper">
                        <strong>{b.bold}</strong> {b.text}
                      </div>
                    </li>
                  ))}
                </ul>
              </div>
            </div>
          ))}
        </div>
      );
    }

    // SLIDE 5: 2x3 Qualitative User Research Grid
    if (s.slideNumber === 5 && s.userCards) {
      return (
        <div>
          <div style={{ background: '#FFF0F4', border: '1px solid #FFC2D1', borderRadius: '6px', padding: '0.4rem 0.8rem', marginBottom: '0.6rem', fontSize: '0.8rem', fontWeight: 600, color: '#FF3F6C' }}>
            📋 {s.researchMethodology}
          </div>
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: '0.6rem' }}>
            {s.userCards.map((user, uIdx) => (
              <div key={uIdx} className="slide-evidence-card" style={{ padding: '0.6rem' }}>
                <div style={{ fontSize: '0.85rem', fontWeight: 700, color: '#FF3F6C', marginBottom: '0.2rem' }}>
                  👤 {user.id} ({user.demographics})
                </div>
                <div style={{ fontSize: '0.78rem', fontStyle: 'italic', color: '#282C3F', margin: '0.3rem 0', padding: '0.3rem', background: '#F8F9FA', borderRadius: '4px', borderLeft: '3px solid #FF3F6C' }}>
                  "{user.quote}"
                </div>
                <div style={{ fontSize: '0.76rem', fontWeight: 600, color: '#03A685' }}>
                  {user.insight}
                </div>
              </div>
            ))}
          </div>
        </div>
      );
    }

    // SLIDE 6: 5 PM Questions
    if (s.slideNumber === 6 && s.pmQuestions) {
      return (
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: '0.6rem' }}>
          {s.pmQuestions.map((pm, pIdx) => (
            <div key={pIdx} className="slide-evidence-card" style={{ gridColumn: pIdx >= 3 ? 'span 1' : 'span 1' }}>
              <div className="evidence-card-header">
                <span className="evidence-card-title">{pm.qNum}: {pm.q}</span>
              </div>
              <div className="evidence-card-body" style={{ fontSize: '0.78rem', lineHeight: '1.35' }}>
                {pm.ans && <div>{pm.ans}</div>}
                {pm.customerValue && (
                  <div>
                    <div style={{ marginBottom: '0.2rem' }}><strong>Customer Value:</strong> {pm.customerValue}</div>
                    <div style={{ color: '#03A685' }}><strong>Business Value:</strong> {pm.businessValue}</div>
                  </div>
                )}
              </div>
            </div>
          ))}
        </div>
      );
    }

    // SLIDE 7: Principles & RICE Matrix Table
    if (s.slideNumber === 7 && s.riceTable) {
      return (
        <div style={{ display: 'flex', flexDirection: 'column', gap: '0.8rem' }}>
          <div className="slide-evidence-card" style={{ background: '#FFF0F4', borderColor: '#FFC2D1' }}>
            <div className="evidence-card-header">
              <span className="evidence-card-title">✨ 3 CORE PRODUCT DESIGN PRINCIPLES</span>
            </div>
            <div className="evidence-card-body" style={{ display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: '0.6rem' }}>
              {s.principles.map((pr, prIdx) => (
                <div key={prIdx}>
                  <strong style={{ color: '#FF3F6C' }}>{pr.title}:</strong>
                  <p style={{ fontSize: '0.78rem', margin: 0, color: '#282C3F' }}>{pr.desc}</p>
                </div>
              ))}
            </div>
          </div>

          <div className="slide-evidence-card">
            <div className="evidence-card-header">
              <span className="evidence-card-title">📊 QUANTITATIVE RICE PRIORITIZATION MATRIX</span>
            </div>
            <div className="evidence-card-body">
              <div style={{ display: 'flex', flexDirection: 'column', gap: '0.5rem' }}>
                {s.riceTable.map((row, rIdx) => (
                  <div key={rIdx} style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', padding: '0.5rem', background: row.verdict.includes('Winner') ? '#FFF0F4' : '#F8F9FA', borderRadius: '6px', border: row.verdict.includes('Winner') ? '1px solid #FFC2D1' : '1px solid #EAEAEC' }}>
                    <div>
                      <strong style={{ color: row.verdict.includes('Winner') ? '#FF3F6C' : 'inherit' }}>{row.solution}:</strong> {row.desc}
                    </div>
                    <div style={{ display: 'flex', gap: '0.8rem', alignItems: 'center', fontSize: '0.8rem' }}>
                      <span style={{ color: '#535766' }}>Reach: {row.reach} | Impact: {row.impact} | Conf: {row.confidence} | Effort: {row.effort}</span>
                      <strong style={{ color: '#FF3F6C' }}>Score: {row.score}</strong>
                      <span style={{ fontWeight: 600, color: row.verdict.includes('Winner') ? '#03A685' : '#888' }}>[{row.verdict}]</span>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          </div>
        </div>
      );
    }

    // SLIDE 8: Architecture & Live MVP Showcase
    if (s.slideNumber === 8 && s.pipeline) {
      return (
        <div style={{ display: 'flex', flexDirection: 'column', gap: '0.8rem' }}>
          <div className="slide-evidence-card">
            <div className="evidence-card-header">
              <span className="evidence-card-title">🏗️ 4-STEP TECHNICAL ARCHITECTURE PIPELINE (LATENCY &lt;180ms)</span>
            </div>
            <div className="evidence-card-body" style={{ display: 'grid', gridTemplateColumns: 'repeat(4, 1fr)', gap: '0.5rem' }}>
              {s.pipeline.map((pip, pIdx) => (
                <div key={pIdx} style={{ background: '#F8F9FA', border: '1px solid #EAEAEC', borderRadius: '6px', padding: '0.5rem' }}>
                  <div style={{ fontSize: '0.8rem', fontWeight: 700, color: '#FF3F6C' }}>{pip.step}</div>
                  <div style={{ fontSize: '0.74rem', color: '#535766' }}>{pip.desc}</div>
                </div>
              ))}
            </div>
          </div>

          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: '0.6rem' }}>
            {s.mvpFeatures.map((mvp, mIdx) => (
              <div key={mIdx} className="slide-evidence-card">
                <div className="evidence-card-header">
                  <span className="evidence-card-title">📱 {mvp.title}</span>
                </div>
                <div className="evidence-card-body" style={{ fontSize: '0.78rem' }}>
                  {mvp.desc}
                </div>
              </div>
            ))}
          </div>
        </div>
      );
    }

    // SLIDE 9: Success Metrics Hierarchy & RCT Experiment
    if (s.slideNumber === 9 && s.metricsTable) {
      return (
        <div style={{ display: 'grid', gridTemplateColumns: '1.2fr 1fr', gap: '0.8rem' }}>
          <div className="slide-evidence-card">
            <div className="evidence-card-header">
              <span className="evidence-card-title">🎯 SUCCESS METRICS HIERARCHY (WITH SOURCED BASELINES)</span>
            </div>
            <div className="evidence-card-body" style={{ display: 'flex', flexDirection: 'column', gap: '0.4rem' }}>
              {s.metricsTable.map((row, rIdx) => (
                <div key={rIdx} style={{ padding: '0.4rem 0.6rem', background: '#F8F9FA', borderRadius: '6px', borderLeft: '3px solid #FF3F6C' }}>
                  <div style={{ fontSize: '0.8rem', fontWeight: 700, color: '#FF3F6C' }}>[{row.type}] {row.kpi}</div>
                  <div style={{ fontSize: '0.76rem', color: '#03A685', fontWeight: 600 }}>{row.target}</div>
                  <div style={{ fontSize: '0.72rem', color: '#535766' }}>Goal: {row.goal}</div>
                </div>
              ))}
            </div>
          </div>

          <div className="slide-evidence-card" style={{ background: '#FFF0F4', borderColor: '#FFC2D1' }}>
            <div className="evidence-card-header">
              <span className="evidence-card-title">🧪 200,000-USER RCT A/B TESTING DESIGN</span>
            </div>
            <div className="evidence-card-body">
              <ul className="evidence-bullets">
                {s.experimentDesign.map((item, eIdx) => (
                  <li key={eIdx} className="evidence-bullet-item">
                    <span className="bullet-dot">•</span>
                    <div className="bullet-text-wrapper">
                      <strong>{item.bold}</strong> {item.text}
                    </div>
                  </li>
                ))}
              </ul>
            </div>
          </div>
        </div>
      );
    }

    // SLIDE 10: Risk Mitigations & 3-Phase GTM Rollout
    if (s.slideNumber === 10 && s.pitfalls) {
      return (
        <div style={{ display: 'flex', flexDirection: 'column', gap: '0.8rem' }}>
          <div className="slide-evidence-card">
            <div className="evidence-card-header">
              <span className="evidence-card-title">⚠️ PITFALLS & RISK MITIGATION MATRIX</span>
            </div>
            <div className="evidence-card-body" style={{ display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: '0.6rem' }}>
              {s.pitfalls.map((pit, pIdx) => (
                <div key={pIdx} style={{ background: '#F8F9FA', borderRadius: '6px', padding: '0.5rem', border: '1px solid #EAEAEC' }}>
                  <div style={{ fontSize: '0.82rem', fontWeight: 700, color: '#FF3F6C' }}>{pit.title}</div>
                  <div style={{ fontSize: '0.76rem', color: '#535766', margin: '0.2rem 0' }}><strong>Risk:</strong> {pit.pitfall}</div>
                  <div style={{ fontSize: '0.76rem', color: '#03A685' }}><strong>Mitigation:</strong> {pit.mitigation}</div>
                </div>
              ))}
            </div>
          </div>

          <div className="slide-evidence-card" style={{ background: '#FFF0F4', borderColor: '#FFC2D1' }}>
            <div className="evidence-card-header">
              <span className="evidence-card-title">🚀 3-PHASE ROLLOUT ROADMAP & GATES</span>
            </div>
            <div className="evidence-card-body" style={{ display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: '0.6rem' }}>
              {s.rolloutPhases.map((ph, phIdx) => (
                <div key={phIdx} style={{ background: '#FFFFFF', borderRadius: '6px', padding: '0.5rem', border: '1px solid #FFC2D1' }}>
                  <div style={{ fontSize: '0.82rem', fontWeight: 700, color: '#FF3F6C' }}>{ph.phase}</div>
                  <div style={{ fontSize: '0.74rem', color: '#535766' }}><strong>Target:</strong> {ph.target}</div>
                  <div style={{ fontSize: '0.74rem', color: '#535766' }}><strong>Scope:</strong> {ph.scope}</div>
                  <div style={{ fontSize: '0.74rem', color: '#03A685', fontWeight: 600 }}><strong>Gate:</strong> {ph.gate}</div>
                </div>
              ))}
            </div>
          </div>
        </div>
      );
    }

    // Default Fallback
    return null;
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
        {s.bottomBanner && (
          <div className="slide-bottom-synthesis-card">
            <div className="synthesis-header-label">
              <Sparkles size={13} className="text-pink" />
              <span>{s.bottomBanner.title}</span>
            </div>
            <div className="synthesis-text-body">
              {s.bottomBanner.text}
            </div>
          </div>
        )}
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

            {/* Live Figma Canvas Link */}
            <a
              href="https://www.figma.com/design/EtSP7uuOBjzS2b5uA8qaml/Myntra-MVP-NL?node-id=1-2&t=ljtykPy7ulKHE6Kr-1"
              target="_blank"
              rel="noreferrer"
              className="deck-nav-btn figma-btn"
              title="Open Official Live Figma Canvas"
            >
              <ExternalLink size={14} />
              <span>Figma Canvas</span>
            </a>

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
