import React, { useState } from 'react';
import HeaderNav from './components/Navigation/HeaderNav';
import WishlistStudio from './components/WishlistStudioMVP/WishlistStudio';
import UserResearchStudio from './components/UserResearch/UserResearchStudio';
import ProblemStrategyStudio from './components/ProblemStrategy/ProblemStrategyStudio';

export default function App() {
  // Default landing view is Wishlist Studio MVP
  const [activeModule, setActiveModule] = useState('MVP');

  return (
    <div className="app-root">
      <HeaderNav activeModule={activeModule} setActiveModule={setActiveModule} />

      <main className="app-main-content">
        {/* 1. Primary Prototype Solution */}
        {activeModule === 'MVP' && <WishlistStudio />}

        {/* 2. Consolidated User Research & AI Discovery */}
        {activeModule === 'RESEARCH' && <UserResearchStudio />}

        {/* 3. Consolidated Growth Strategy, Metric Tree & Guardrails */}
        {activeModule === 'STRATEGY' && <ProblemStrategyStudio />}
      </main>
    </div>
  );
}
