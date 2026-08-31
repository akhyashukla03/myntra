import React from 'react';
import { ShoppingBag, Users, TrendingUp, Presentation } from 'lucide-react';

export default function HeaderNav({ activeModule, setActiveModule }) {
  return (
    <header className="app-header">
      <div className="brand-section">
        <div className="logo-badge">M</div>
        <div>
          <div className="brand-title">Myntra Growth Lab</div>
          <div className="brand-subtitle">Wishlist Conversion Engine</div>
        </div>
      </div>

      <nav className="main-nav">
        {/* 1. Primary MVP Prototype Solution */}
        <button
          className={`nav-link ${activeModule === 'MVP' ? 'active' : ''}`}
          onClick={() => setActiveModule('MVP')}
        >
          <ShoppingBag size={16} />
          <span>Wishlist Studio MVP</span>
        </button>

        {/* 2. Consolidated User Research & AI Discovery */}
        <button
          className={`nav-link ${activeModule === 'RESEARCH' ? 'active' : ''}`}
          onClick={() => setActiveModule('RESEARCH')}
        >
          <Users size={16} />
          <span>User Research & Insights</span>
        </button>

        {/* 3. Consolidated Growth Strategy & Decision Modeling */}
        <button
          className={`nav-link ${activeModule === 'STRATEGY' ? 'active' : ''}`}
          onClick={() => setActiveModule('STRATEGY')}
        >
          <TrendingUp size={16} />
          <span>Growth Strategy & Metrics</span>
        </button>

        {/* 4. 10-Slide Pitch Deck */}
        <button
          className={`nav-link ${activeModule === 'DECK' ? 'active' : ''}`}
          onClick={() => setActiveModule('DECK')}
        >
          <Presentation size={16} />
          <span>📝 10-Slide Deck</span>
        </button>
      </nav>
    </header>
  );
}
