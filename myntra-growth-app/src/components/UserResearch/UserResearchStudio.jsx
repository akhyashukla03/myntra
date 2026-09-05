import React, { useState } from 'react';
import { Users, FileSpreadsheet, CheckCircle2, Copy, BarChart3, HelpCircle, MessageCircle, Sparkles, TrendingUp, Bot, Quote, Check } from 'lucide-react';
import { GOOGLE_FORMS_SURVEY_SCHEMA, USER_INTERVIEWS, LIVE_SURVEY_SUMMARY } from '../../data/userResearchData';
import AIQueryConsole from '../DiscoveryEngine/AIQueryConsole';
import BarrierMetrics from '../DiscoveryEngine/BarrierMetrics';

export default function UserResearchStudio() {
  const [activeTab, setActiveTab] = useState('LIVE_SURVEY'); // 'LIVE_SURVEY', 'INTERVIEWS', 'AI_DISCOVERY', 'SCHEMA'
  const [copied, setCopied] = useState(false);
  const [selectedPersona, setSelectedPersona] = useState(USER_INTERVIEWS[0]);

  const copyMarkdownSchema = () => {
    let md = `# ${GOOGLE_FORMS_SURVEY_SCHEMA.title}\n\n${GOOGLE_FORMS_SURVEY_SCHEMA.description}\n\n`;
    GOOGLE_FORMS_SURVEY_SCHEMA.sections.forEach(sec => {
      md += `## ${sec.sectionTitle}\n\n`;
      sec.questions.forEach((q) => {
        md += `### ${q.question}\n`;
        if (q.options) {
          q.options.forEach(opt => {
            md += `- [ ] ${opt}\n`;
          });
        } else if (q.type === 'scale') {
          md += `*Scale ${q.scaleMin} (${q.scaleMinLabel}) to ${q.scaleMax} (${q.scaleMaxLabel})*\n`;
        } else {
          md += `*Paragraph / Short Text*\n`;
        }
        md += `\n`;
      });
    });

    navigator.clipboard.writeText(md);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  return (
    <div className="module-container">
      {/* Hero Banner */}
      <div className="discovery-hero-banner">
        <div className="hero-content">
          <div className="hero-badge">
            <Users size={14} className="text-pink" />
            <span>Primary User Research & Discovery Suite</span>
          </div>
          <h1 className="hero-title">Live Survey Data (N=25 Responses) & 6 Deep-Dive Interviews</h1>
          <p className="hero-subtitle">
            Triangulating live quantitative survey findings (N=25) with 6 in-depth qualitative user interviews and 24,850+ scraped review touchpoints.
          </p>
        </div>

        {/* 4 Clean Sub-Tabs */}
        <div className="hero-nav-tabs">
          <button
            className={`hero-tab-btn ${activeTab === 'LIVE_SURVEY' ? 'active' : ''}`}
            onClick={() => setActiveTab('LIVE_SURVEY')}
          >
            <BarChart3 size={16} />
            <span>1. Survey Data & Breakdown (25 Responses)</span>
          </button>
          <button
            className={`hero-tab-btn ${activeTab === 'INTERVIEWS' ? 'active' : ''}`}
            onClick={() => setActiveTab('INTERVIEWS')}
          >
            <MessageCircle size={16} />
            <span>2. 6 In-Depth User Interviews</span>
          </button>
          <button
            className={`hero-tab-btn ${activeTab === 'AI_DISCOVERY' ? 'active' : ''}`}
            onClick={() => setActiveTab('AI_DISCOVERY')}
          >
            <Bot size={16} />
            <span>3. AI Review Intelligence (24k+ Corpus)</span>
          </button>
          <button
            className={`hero-tab-btn ${activeTab === 'SCHEMA' ? 'active' : ''}`}
            onClick={() => setActiveTab('SCHEMA')}
          >
            <HelpCircle size={16} />
            <span>4. Form Questionnaire Schema</span>
          </button>
        </div>
      </div>

      <div className="discovery-tab-content">
        {/* TAB 1: LIVE SURVEY DATA & BREAKDOWN */}
        {activeTab === 'LIVE_SURVEY' && (
          <div className="discovery-section">
            {/* Top Key Metrics Grid */}
            <div className="discovery-kpi-grid">
              {LIVE_SURVEY_SUMMARY.keyMetrics.map((km, idx) => (
                <div key={idx} className="kpi-card">
                  <span className="kpi-label">{km.label}</span>
                  <div className="kpi-value text-pink">{km.val}</div>
                  <span className="kpi-subtext">{km.sub}</span>
                </div>
              ))}
            </div>

            {/* Question by Question Distribution Cards */}
            <div className="simulator-section-card" style={{ marginTop: '2rem' }}>
              <div className="sim-header">
                <div className="sim-title-row">
                  <Sparkles size={22} className="text-pink" />
                  <div>
                    <h2 className="sim-title">Detailed Survey Question Distributions (N = 25)</h2>
                    <p className="sim-sub">Aggregated responses proving that non-monetary cognitive friction (comparison & styling) drives wishlist drop-offs.</p>
                  </div>
                </div>
              </div>

              <div className="charts-two-col">
                {LIVE_SURVEY_SUMMARY.questionBreakdown.map((qb, qIdx) => (
                  <div key={qIdx} className="chart-card">
                    <div className="chart-header">
                      <h3 className="chart-title" style={{ fontSize: '0.95rem' }}>
                        <span className="text-pink" style={{ marginRight: '0.5rem' }}>{qb.qNum}:</span>
                        {qb.question}
                      </h3>
                    </div>

                    {qb.distribution && (
                      <div className="bars-list" style={{ marginTop: '0.75rem' }}>
                        {qb.distribution.map((dist, dIdx) => (
                          <div key={dIdx} className="dist-row">
                            <div className="dist-label-row">
                              <span className="dist-label-text">{dist.option}</span>
                              <span className="dist-val-text">{dist.percentage}% ({dist.count})</span>
                            </div>
                            <div className="bar-track">
                              <div
                                className="bar-fill"
                                style={{
                                  width: `${dist.percentage}%`,
                                  background: dIdx === 0 ? 'linear-gradient(90deg, #FF3F6C, #FF6B4A)' : 'rgba(255,255,255,0.2)'
                                }}
                              />
                            </div>
                          </div>
                        ))}
                      </div>
                    )}

                    {qb.verbatims && (
                      <div style={{ display: 'flex', flexDirection: 'column', gap: '0.5rem', marginTop: '0.75rem' }}>
                        {qb.verbatims.map((vb, vIdx) => (
                          <div key={vIdx} className="key-quote-box">
                            <p className="quote-text">"{vb}"</p>
                          </div>
                        ))}
                      </div>
                    )}
                  </div>
                ))}
              </div>
            </div>
          </div>
        )}

        {/* TAB 2: 6 IN-DEPTH INTERVIEWS */}
        {activeTab === 'INTERVIEWS' && (
          <div className="discovery-section">
            <div className="interviews-layout">
              {/* Left Column: Persona Selector */}
              <div className="persona-selector-col">
                <h3 style={{ fontSize: '1rem', fontWeight: 800, marginBottom: '0.5rem', color: '#CBD5E1' }}>
                  Select Interviewee ({USER_INTERVIEWS.length} Participants):
                </h3>
                {USER_INTERVIEWS.map((user) => (
                  <div
                    key={user.id}
                    className={`persona-nav-card ${selectedPersona.id === user.id ? 'active' : ''}`}
                    onClick={() => setSelectedPersona(user)}
                  >
                    <div className="persona-avatar-wrap">
                      <div className="persona-avatar">{user.name.charAt(0)}</div>
                      <div>
                        <div className="persona-name">{user.name}, {user.age}</div>
                        <div className="persona-city">{user.city} • {user.occupation}</div>
                      </div>
                    </div>
                    <span className="persona-badge-pill">{user.primaryCategory}</span>
                  </div>
                ))}
              </div>

              {/* Right Column: Persona Deep-Dive Transcript Card */}
              <div className="persona-detail-card">
                <div className="persona-detail-header">
                  <div>
                    <h2 className="detail-name">{selectedPersona.name} ({selectedPersona.primaryCategory})</h2>
                    <div className="detail-meta">
                      {selectedPersona.age} Years • {selectedPersona.occupation} • {selectedPersona.city} • Saved Items: {selectedPersona.wishlistSize}
                    </div>
                  </div>
                </div>

                <div className="key-quote-box">
                  <span className="quote-label">Direct Verbatim Quote:</span>
                  <p className="quote-text" style={{ fontSize: '0.95rem' }}>"{selectedPersona.verbatimQuote}"</p>
                </div>

                <div className="action-point" style={{ marginTop: '1.25rem' }}>
                  <span className="point-number">1</span>
                  <div>
                    <strong>Core Purchase Blocker:</strong> {selectedPersona.corePainPoint}
                  </div>
                </div>

                <div className="action-point">
                  <span className="point-number">2</span>
                  <div>
                    <strong>Current Workaround:</strong> {selectedPersona.currentWorkaround}
                  </div>
                </div>

                <div className="action-point">
                  <span className="point-number">3</span>
                  <div>
                    <strong>Reaction to Wishlist Studio:</strong> {selectedPersona.solutionFeedback}
                  </div>
                </div>
              </div>
            </div>
          </div>
        )}

        {/* TAB 3: AI REVIEW INTELLIGENCE (24k+ REVIEWS) */}
        {activeTab === 'AI_DISCOVERY' && (
          <div className="discovery-section">
            <AIQueryConsole />
            <div style={{ marginTop: '2rem' }}>
              <BarrierMetrics />
            </div>
          </div>
        )}

        {/* TAB 4: FORM QUESTIONNAIRE SCHEMA */}
        {activeTab === 'SCHEMA' && (
          <div className="discovery-section">
            <div className="section-header">
              <div>
                <h2 className="section-title">Standardized Google Form Survey Schema</h2>
                <p className="section-subtitle">22-Question instrument deployed to fashion shoppers to isolate non-monetary conversion blockers.</p>
              </div>
              <button className="copy-schema-btn" onClick={copyMarkdownSchema}>
                {copied ? <CheckCircle2 size={16} className="text-green" /> : <Copy size={16} />}
                <span>{copied ? 'Copied Markdown!' : 'Copy Survey Schema (Markdown)'}</span>
              </button>
            </div>

            <div className="schema-sections-list">
              {GOOGLE_FORMS_SURVEY_SCHEMA.sections.map((sec, sIdx) => (
                <div key={sIdx} className="schema-section-card">
                  <h3 className="section-block-title">{sec.sectionTitle}</h3>
                  <div className="questions-list">
                    {sec.questions.map((q, qIdx) => (
                      <div key={qIdx} className="question-item-card">
                        <div className="q-title-row">
                          <span className="q-badge">Q{qIdx + 1}</span>
                          <span className="q-text">{q.question}</span>
                        </div>
                        {q.options && (
                          <ul className="q-options-list">
                            {q.options.map((opt, oIdx) => (
                              <li key={oIdx} className="q-option-pill">{opt}</li>
                            ))}
                          </ul>
                        )}
                        {q.type === 'scale' && (
                          <div className="q-scale-indicator">
                            Scale {q.scaleMin} ({q.scaleMinLabel}) &rarr; {q.scaleMax} ({q.scaleMaxLabel})
                          </div>
                        )}
                      </div>
                    ))}
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
