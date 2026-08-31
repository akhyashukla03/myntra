import React from 'react';
import { WISHLIST_COLLECTIONS } from '../../data/mockWishlistProducts';
import { Sparkles, Layers, Share2, Wand2, Columns3, ShoppingBag } from 'lucide-react';

export default function WishlistHeader({
  activeCollection,
  setActiveCollection,
  activeView,
  setActiveView,
  selectedForCompare,
  cartCount,
  onOpenCart,
  onOpenSocialModal,
}) {
  return (
    <div className="wishlist-header-card">
      <div className="wishlist-title-row">
        <div>
          <div className="wishlist-badge">
            <Sparkles size={14} className="text-pink" />
            <span>Myntra Wishlist Studio • Decision Workspace</span>
          </div>
          <h1 className="wishlist-main-title">My Saved Wardrobe ({WISHLIST_COLLECTIONS[0].count} Items)</h1>
          <p className="wishlist-sub">
            Organize by occasion, compare alternative shortlists side-by-side, generate AI outfits, or poll friends with 1 tap.
          </p>
        </div>

        {/* Action Toggle Pills & Shopping Bag */}
        <div className="studio-action-controls">
          <button
            className={`studio-toggle-btn ${activeView === 'GRID' ? 'active' : ''}`}
            onClick={() => setActiveView('GRID')}
          >
            <Layers size={16} />
            <span>Wishlist Grid</span>
          </button>

          <button
            className={`studio-toggle-btn ${activeView === 'COMPARE' ? 'active' : ''}`}
            onClick={() => setActiveView('COMPARE')}
          >
            <Columns3 size={16} />
            <span>Compare Studio ({selectedForCompare.length})</span>
          </button>

          <button
            className={`studio-toggle-btn ${activeView === 'OUTFITS' ? 'active' : ''}`}
            onClick={() => setActiveView('OUTFITS')}
          >
            <Wand2 size={16} />
            <span>AI Outfit Matcher</span>
          </button>

          <button className="studio-share-btn" onClick={onOpenSocialModal}>
            <Share2 size={16} />
            <span>Ask Friends</span>
          </button>

          {/* Glowing Shopping Bag Drawer CTA */}
          <button
            onClick={onOpenCart}
            style={{
              display: 'inline-flex',
              alignItems: 'center',
              gap: '0.45rem',
              background: 'linear-gradient(135deg, #FF3F6C, #FF6B4A)',
              color: '#FFF',
              border: 'none',
              borderRadius: '9999px',
              padding: '0.55rem 1.15rem',
              fontSize: '0.85rem',
              fontWeight: 800,
              cursor: 'pointer',
              boxShadow: '0 0 15px rgba(255, 63, 108, 0.35)',
              position: 'relative'
            }}
          >
            <ShoppingBag size={16} />
            <span>Bag ({cartCount})</span>
          </button>
        </div>
      </div>

      {/* Smart Occasion & Category Collections Filter Bar */}
      <div className="collections-bar">
        <span className="collections-label">Smart Occasions:</span>
        <div className="collections-scroll">
          {WISHLIST_COLLECTIONS.map((col) => (
            <button
              key={col.id}
              className={`collection-pill ${activeCollection === col.id ? 'active' : ''}`}
              onClick={() => setActiveCollection(col.id)}
            >
              <span>{col.name}</span>
              <span className="collection-count">{col.count}</span>
            </button>
          ))}
        </div>
      </div>
    </div>
  );
}
