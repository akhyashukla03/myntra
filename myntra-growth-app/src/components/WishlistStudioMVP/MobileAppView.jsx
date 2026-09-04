import React, { useState } from 'react';
import { Share2, ShoppingBag, Wand2, Columns3, Check, Star, Sparkles, Heart, Home, Search, User } from 'lucide-react';

export default function MobileAppView({
  products,
  cartItems,
  onMoveToBag,
  onAddLookToBag,
  onOpenSocialModal,
  onOpenCart,
  onRemoveFromCart,
  onProceedToCheckout
}) {
  const [mobileTab, setMobileTab] = useState('MATRIX'); // 'HOME', 'MATRIX', 'OUTFITS', 'POLL', 'BAG'
  const [selectedFolder, setSelectedFolder] = useState('ALL');
  const [buyerPhotoActive, setBuyerPhotoActive] = useState(false);

  // Interactive WhatsApp Poll Vote State
  const [votes, setVotes] = useState({ optionA: 3, optionB: 1 });
  const [userVoted, setUserVoted] = useState(null);

  // Filter products by selected folder
  const filteredProducts = products.filter((p) => {
    if (selectedFolder === 'ALL') return true;
    return p.category === selectedFolder;
  });

  const handleVote = (option) => {
    if (userVoted === option) return;
    setVotes((prev) => {
      const updated = { ...prev };
      if (userVoted) {
        updated[userVoted === 'optionA' ? 'optionA' : 'optionB'] -= 1;
      }
      updated[option] += 1;
      return updated;
    });
    setUserVoted(option);
  };

  const totalVotes = votes.optionA + votes.optionB;
  const percentA = Math.round((votes.optionA / totalVotes) * 100);
  const percentB = Math.round((votes.optionB / totalVotes) * 100);

  return (
    <div
      className="mobile-app-container"
      style={{
        maxWidth: '420px',
        height: '750px',
        width: '100%',
        boxSizing: 'border-box',
        margin: '0 auto',
        background: '#0A0D14',
        border: '12px solid #1E293B',
        borderRadius: '40px',
        padding: '1rem 1rem 0.5rem 1rem',
        boxShadow: '0 25px 60px rgba(0,0,0,0.7)',
        color: '#FFF',
        fontFamily: '-apple-system, BlinkMacSystemFont, sans-serif',
        display: 'flex',
        flexDirection: 'column',
        overflow: 'hidden'
      }}
    >
      {/* 1. FIXED TOP PHONE HEADER (Status Bar + Folders + Tabs) */}
      <div style={{ flexShrink: 0, width: '100%' }}>
        {/* iOS / Android Smartphone Status Bar */}
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', paddingBottom: '0.4rem', borderBottom: '1px solid rgba(255,255,255,0.08)', marginBottom: '0.65rem', width: '100%' }}>
          <span style={{ fontSize: '0.75rem', fontWeight: '700', color: '#F8FAFC' }}>9:41 📶 5G</span>
          <span style={{ fontSize: '1.15rem', fontWeight: '900', color: '#FF3F6C', letterSpacing: '-0.5px' }}>myntra</span>
          <button onClick={() => setMobileTab('BAG')} style={{ background: mobileTab === 'BAG' ? '#FF3F6C' : '#2D0A4E', color: '#FFF', border: '1px solid rgba(255,63,108,0.4)', padding: '0.2rem 0.5rem', borderRadius: '12px', fontSize: '0.7rem', fontWeight: '800', cursor: 'pointer', display: 'flex', alignItems: 'center', gap: '0.25rem', whiteSpace: 'nowrap' }}>
            <ShoppingBag size={12} />
            <span>Bag ({cartItems.length})</span>
          </button>
        </div>

        {/* Smart Occasion Header Folder Filter Bar */}
        <div style={{ marginBottom: '0.65rem', width: '100%', overflow: 'hidden' }}>
          <div style={{ fontSize: '0.68rem', fontWeight: '800', color: '#94A3B8', marginBottom: '0.35rem', letterSpacing: '0.5px' }}>
            📁 SMART OCCASION FOLDERS
          </div>
          <div style={{ display: 'flex', gap: '0.35rem', overflowX: 'auto', paddingBottom: '0.25rem', width: '100%' }}>
            {[
              { id: 'ALL', label: `All Saved (${products.length})` },
              { id: 'STREETWEAR', label: 'Streetwear (4)' },
              { id: 'WORKWEAR', label: 'Workwear (3)' },
              { id: 'FOOTWEAR', label: 'Footwear (3)' },
              { id: 'WEEKEND', label: 'Party Outfits (2)' }
            ].map((folder) => (
              <button
                key={folder.id}
                onClick={() => setSelectedFolder(folder.id)}
                style={{
                  background: selectedFolder === folder.id ? '#FF3F6C' : 'rgba(255,255,255,0.08)',
                  color: '#FFF', border: 'none', padding: '0.25rem 0.6rem', borderRadius: '12px', fontSize: '0.68rem', fontWeight: '700', whiteSpace: 'nowrap', cursor: 'pointer', flexShrink: 0
                }}
              >
                {folder.label}
              </button>
            ))}
          </div>
        </div>

        {/* Internal Mobile Feature Navigation Tabs */}
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(3, minmax(0, 1fr))', gap: '0.35rem', marginBottom: '0.75rem', width: '100%' }}>
          <button
            onClick={() => setMobileTab('MATRIX')}
            style={{
              background: mobileTab === 'MATRIX' ? '#FF3F6C' : 'rgba(255,255,255,0.06)',
              color: '#FFF', border: 'none', padding: '0.4rem 0.2rem', borderRadius: '6px', fontSize: '0.68rem', fontWeight: '800', cursor: 'pointer', display: 'flex', alignItems: 'center', justifyContent: 'center', gap: '0.2rem', minWidth: 0, overflow: 'hidden'
            }}
          >
            <Columns3 size={12} />
            <span style={{ whiteSpace: 'nowrap', overflow: 'hidden', textOverflow: 'ellipsis' }}>Spec Matrix</span>
          </button>

          <button
            onClick={() => setMobileTab('OUTFITS')}
            style={{
              background: mobileTab === 'OUTFITS' ? '#4F46E5' : 'rgba(255,255,255,0.06)',
              color: '#FFF', border: 'none', padding: '0.4rem 0.2rem', borderRadius: '6px', fontSize: '0.68rem', fontWeight: '800', cursor: 'pointer', display: 'flex', alignItems: 'center', justifyContent: 'center', gap: '0.2rem', minWidth: 0, overflow: 'hidden'
            }}
          >
            <Wand2 size={12} />
            <span style={{ whiteSpace: 'nowrap', overflow: 'hidden', textOverflow: 'ellipsis' }}>AI Looks</span>
          </button>

          <button
            onClick={() => setMobileTab('POLL')}
            style={{
              background: mobileTab === 'POLL' ? '#054740' : 'rgba(255,255,255,0.06)',
              color: mobileTab === 'POLL' ? '#25D366' : '#FFF', border: 'none', padding: '0.4rem 0.2rem', borderRadius: '6px', fontSize: '0.68rem', fontWeight: '800', cursor: 'pointer', display: 'flex', alignItems: 'center', justifyContent: 'center', gap: '0.2rem', minWidth: 0, overflow: 'hidden'
            }}
          >
            <Share2 size={12} />
            <span style={{ whiteSpace: 'nowrap', overflow: 'hidden', textOverflow: 'ellipsis' }}>WhatsApp Poll</span>
          </button>
        </div>
      </div>

      {/* 2. SCROLLABLE PHONE SCREEN BODY (INTERNAL VERTICAL SCROLL) */}
      <div
        className="mobile-scrollable-body"
        style={{
          flex: 1,
          overflowY: 'auto',
          paddingRight: '0.25rem',
          display: 'flex',
          flexDirection: 'column',
          gap: '0.75rem',
          width: '100%',
          boxSizing: 'border-box'
        }}
      >
        {/* A. SIDE-BY-SIDE SPEC MATRIX MOBILE VIEW */}
        {mobileTab === 'MATRIX' && (
          <div style={{ display: 'flex', flexDirection: 'column', gap: '0.75rem', width: '100%' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', width: '100%' }}>
              <h4 style={{ fontSize: '0.78rem', fontWeight: '800', color: '#FF3F6C', margin: 0, whiteSpace: 'nowrap', overflow: 'hidden', textOverflow: 'ellipsis' }}>Side-by-Side Spec Matrix</h4>
              <button
                onClick={() => setBuyerPhotoActive(!buyerPhotoActive)}
                style={{ background: buyerPhotoActive ? '#2D0A4E' : 'rgba(255,255,255,0.1)', color: '#FFF', border: 'none', padding: '0.2rem 0.45rem', borderRadius: '12px', fontSize: '0.62rem', fontWeight: '800', cursor: 'pointer', whiteSpace: 'nowrap', flexShrink: 0 }}
              >
                {buyerPhotoActive ? '📸 Buyer Photos' : '🖼️ Studio Photos'}
              </button>
            </div>

            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(2, minmax(0, 1fr))', gap: '0.5rem', width: '100%' }}>
              {filteredProducts.slice(0, 4).map((p) => (
                <div key={p.id} style={{ background: '#121826', border: '1px solid rgba(255,255,255,0.12)', borderRadius: '12px', padding: '0.5rem', display: 'flex', flexDirection: 'column', gap: '0.35rem', minWidth: 0, overflow: 'hidden', boxSizing: 'border-box' }}>
                  <div style={{ position: 'relative', width: '100%' }}>
                    <img src={p.image} alt={p.name} style={{ width: '100%', height: '115px', objectFit: 'cover', borderRadius: '8px' }} />
                    <span style={{ position: 'absolute', top: '4px', left: '4px', background: p.id === 'prod-01' ? '#2D0A4E' : '#334155', color: '#FFF', fontSize: '0.58rem', fontWeight: '800', padding: '0.15rem 0.35rem', borderRadius: '4px', maxWidth: '90%', whiteSpace: 'nowrap', overflow: 'hidden', textOverflow: 'ellipsis' }}>
                      {p.fabric.split('(')[0]}
                    </span>
                  </div>

                  <span style={{ fontSize: '0.72rem', fontWeight: '800', color: '#F8FAFC', whiteSpace: 'nowrap', overflow: 'hidden', textOverflow: 'ellipsis', width: '100%' }}>{p.name}</span>
                  <span style={{ fontSize: '0.65rem', color: '#10B981', fontWeight: '700', whiteSpace: 'nowrap', overflow: 'hidden', textOverflow: 'ellipsis' }}>✓ Fit: {p.fitScore.split('(')[0]}</span>
                  
                  <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginTop: '0.15rem', width: '100%' }}>
                    <span style={{ fontSize: '0.82rem', fontWeight: '900', color: '#FF3F6C' }}>₹{p.price.toLocaleString()}</span>
                    <span style={{ fontSize: '0.62rem', color: '#94A3B8', textDecoration: 'line-through' }}>₹{p.originalPrice.toLocaleString()}</span>
                  </div>

                  <button
                    onClick={() => onMoveToBag(p)}
                    style={{ background: '#FF3F6C', color: '#FFF', border: 'none', padding: '0.35rem', borderRadius: '6px', fontSize: '0.7rem', fontWeight: '800', cursor: 'pointer', marginTop: '0.2rem', display: 'flex', alignItems: 'center', justifyContent: 'center', gap: '0.2rem', width: '100%' }}
                  >
                    <ShoppingBag size={11} />
                    <span>Add to Bag</span>
                  </button>
                </div>
              ))}
            </div>

            {/* Sizing & Return Friction Rating Card */}
            <div style={{ background: '#1E293B', padding: '0.6rem', borderRadius: '10px', fontSize: '0.7rem', width: '100%', boxSizing: 'border-box' }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '0.35rem', width: '100%' }}>
                <span style={{ color: '#10B981', fontWeight: '800', fontSize: '0.68rem' }}>✓ 88% TRUE TO SIZE</span>
                <span style={{ background: '#10B981', color: '#FFF', fontSize: '0.58rem', padding: '0.1rem 0.35rem', borderRadius: '4px', fontWeight: '800', flexShrink: 0 }}>Low Return Risk</span>
              </div>
              <div style={{ display: 'flex', height: '6px', borderRadius: '3px', overflow: 'hidden', marginBottom: '0.35rem', width: '100%' }}>
                <div style={{ width: '88%', background: '#10B981' }} title="True to size: 88%"></div>
                <div style={{ width: '8%', background: '#F59E0B' }} title="Runs small: 8%"></div>
                <div style={{ width: '4%', background: '#EF4444' }} title="Runs large: 4%"></div>
              </div>
              <span style={{ color: '#94A3B8', fontSize: '0.65rem' }}>Verified across 1,420 buyer reviews. Sizing return friction &lt; 18%.</span>
            </div>
          </div>
        )}

        {/* B. AI OUTFIT MATCHERS MOBILE VIEW */}
        {mobileTab === 'OUTFITS' && (
          <div style={{ display: 'flex', flexDirection: 'column', gap: '0.75rem', width: '100%' }}>
            <div style={{ background: 'linear-gradient(135deg, #4F46E5, #818CF8)', padding: '0.6rem', borderRadius: '10px', width: '100%', boxSizing: 'border-box' }}>
              <span style={{ fontSize: '0.78rem', fontWeight: '800', color: '#FFF', display: 'block' }}>✨ AI Coordinated Look Generator</span>
              <span style={{ fontSize: '0.65rem', color: '#E0E7FF', display: 'block', marginTop: '0.15rem' }}>Coordinates wishlisted item with complementary wardrobe pieces (+₹450 AOV Lift)</span>
            </div>

            {/* Look 1 */}
            <div style={{ background: '#121826', border: '1px solid #4F46E5', borderRadius: '12px', padding: '0.65rem', width: '100%', boxSizing: 'border-box' }}>
              <span style={{ fontSize: '0.72rem', fontWeight: '800', color: '#818CF8', display: 'block', marginBottom: '0.4rem', whiteSpace: 'nowrap', overflow: 'hidden', textOverflow: 'ellipsis' }}>Look #1: Casual Weekend Streetwear</span>
              
              <div style={{ display: 'grid', gridTemplateColumns: 'repeat(3, minmax(0, 1fr))', gap: '0.35rem', marginBottom: '0.5rem', width: '100%' }}>
                {products.slice(0, 3).map((item, idx) => (
                  <div key={idx} style={{ background: '#1E293B', padding: '0.3rem', borderRadius: '6px', textAlign: 'center', minWidth: 0, overflow: 'hidden', boxSizing: 'border-box' }}>
                    <img src={item.image} alt={item.name} style={{ width: '100%', height: '55px', objectFit: 'cover', borderRadius: '4px', marginBottom: '0.2rem' }} />
                    <span style={{ fontSize: '0.58rem', color: '#CBD5E1', display: 'block', whiteSpace: 'nowrap', overflow: 'hidden', textOverflow: 'ellipsis', width: '100%' }}>{item.name}</span>
                  </div>
                ))}
              </div>

              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginTop: '0.4rem', borderTop: '1px solid rgba(255,255,255,0.08)', paddingTop: '0.4rem', width: '100%' }}>
                <div>
                  <span style={{ fontSize: '0.6rem', color: '#CBD5E1', display: 'block' }}>Bundle Total:</span>
                  <span style={{ fontSize: '0.85rem', fontWeight: '900', color: '#FFF' }}>₹5,497</span>
                </div>
                <button
                  onClick={() => onAddLookToBag(products[0])}
                  style={{ background: '#4F46E5', color: '#FFF', border: 'none', padding: '0.4rem 0.65rem', borderRadius: '6px', fontSize: '0.7rem', fontWeight: '800', cursor: 'pointer', whiteSpace: 'nowrap', flexShrink: 0 }}
                >
                  Move Look to Bag
                </button>
              </div>
            </div>

            {/* Look 2 */}
            <div style={{ background: '#121826', border: '1px solid rgba(255,255,255,0.1)', borderRadius: '12px', padding: '0.65rem', width: '100%', boxSizing: 'border-box' }}>
              <span style={{ fontSize: '0.72rem', fontWeight: '800', color: '#F8FAFC', display: 'block', marginBottom: '0.4rem', whiteSpace: 'nowrap', overflow: 'hidden', textOverflow: 'ellipsis' }}>Look #2: Smart Executive Office Fit</span>
              
              <div style={{ display: 'grid', gridTemplateColumns: 'repeat(3, minmax(0, 1fr))', gap: '0.35rem', marginBottom: '0.5rem', width: '100%' }}>
                {products.slice(4, 7).map((item, idx) => (
                  <div key={idx} style={{ background: '#1E293B', padding: '0.3rem', borderRadius: '6px', textAlign: 'center', minWidth: 0, overflow: 'hidden', boxSizing: 'border-box' }}>
                    <img src={item.image} alt={item.name} style={{ width: '100%', height: '55px', objectFit: 'cover', borderRadius: '4px', marginBottom: '0.2rem' }} />
                    <span style={{ fontSize: '0.58rem', color: '#CBD5E1', display: 'block', whiteSpace: 'nowrap', overflow: 'hidden', textOverflow: 'ellipsis', width: '100%' }}>{item.name}</span>
                  </div>
                ))}
              </div>

              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginTop: '0.4rem', borderTop: '1px solid rgba(255,255,255,0.08)', paddingTop: '0.4rem', width: '100%' }}>
                <div>
                  <span style={{ fontSize: '0.6rem', color: '#CBD5E1', display: 'block' }}>Bundle Total:</span>
                  <span style={{ fontSize: '0.85rem', fontWeight: '900', color: '#FFF' }}>₹11,579</span>
                </div>
                <button
                  onClick={() => onAddLookToBag(products[4])}
                  style={{ background: '#4F46E5', color: '#FFF', border: 'none', padding: '0.4rem 0.65rem', borderRadius: '6px', fontSize: '0.7rem', fontWeight: '800', cursor: 'pointer', whiteSpace: 'nowrap', flexShrink: 0 }}
                >
                  Move Look to Bag
                </button>
              </div>
            </div>
          </div>
        )}

        {/* C. WHATSAPP PEER VOTING MOBILE VIEW */}
        {mobileTab === 'POLL' && (
          <div style={{ display: 'flex', flexDirection: 'column', gap: '0.75rem', width: '100%' }}>
            <div style={{ background: '#054740', padding: '0.6rem', borderRadius: '10px', width: '100%', boxSizing: 'border-box' }}>
              <span style={{ fontSize: '0.78rem', fontWeight: '800', color: '#25D366', display: 'block' }}>💬 WhatsApp Peer Micro-Voting Card</span>
              <span style={{ fontSize: '0.65rem', color: '#E2E8F0', display: 'block', marginTop: '0.15rem' }}>1-Tap friend polling eliminating buying delay without discounts.</span>
            </div>

            <div style={{ background: '#111B21', border: '1px solid #25D366', borderRadius: '12px', padding: '0.65rem', width: '100%', boxSizing: 'border-box' }}>
              <div style={{ fontSize: '0.72rem', fontWeight: '800', color: '#FF3F6C', marginBottom: '0.35rem' }}>myntra wishlist poll</div>
              <div style={{ fontSize: '0.7rem', color: '#E9EDEF', fontWeight: '700', marginBottom: '0.5rem' }}>"Which jacket should I buy for Friday night?"</div>

              <div style={{ display: 'flex', flexDirection: 'column', gap: '0.45rem', width: '100%' }}>
                <div style={{ background: '#202C33', padding: '0.45rem', borderRadius: '8px', border: userVoted === 'optionA' ? '1px solid #00A884' : '1px solid transparent', width: '100%', boxSizing: 'border-box' }}>
                  <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '0.2rem', width: '100%' }}>
                    <span style={{ fontSize: '0.68rem', color: '#FFF', fontWeight: '700', whiteSpace: 'nowrap', overflow: 'hidden', textOverflow: 'ellipsis' }}>Option A: Heavy Canvas (240 GSM)</span>
                    <button
                      onClick={() => handleVote('optionA')}
                      style={{ background: userVoted === 'optionA' ? '#00A884' : '#2A3942', color: '#FFF', border: 'none', padding: '0.18rem 0.45rem', borderRadius: '4px', fontSize: '0.62rem', fontWeight: '800', cursor: 'pointer', flexShrink: 0 }}
                    >
                      {userVoted === 'optionA' ? '✓ Voted' : 'Vote A'}
                    </button>
                  </div>
                  <div style={{ display: 'flex', alignItems: 'center', gap: '0.4rem', width: '100%' }}>
                    <div style={{ flex: 1, background: '#111B21', height: '6px', borderRadius: '3px', overflow: 'hidden' }}>
                      <div style={{ width: `${percentA}%`, background: '#00A884', height: '100%' }}></div>
                    </div>
                    <span style={{ fontSize: '0.62rem', color: '#00A884', fontWeight: '800', flexShrink: 0 }}>{percentA}% ({votes.optionA})</span>
                  </div>
                </div>

                <div style={{ background: '#202C33', padding: '0.45rem', borderRadius: '8px', border: userVoted === 'optionB' ? '1px solid #00A884' : '1px solid transparent', width: '100%', boxSizing: 'border-box' }}>
                  <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '0.2rem', width: '100%' }}>
                    <span style={{ fontSize: '0.68rem', color: '#CBD5E1', fontWeight: '600', whiteSpace: 'nowrap', overflow: 'hidden', textOverflow: 'ellipsis' }}>Option B: Light Denim (160 GSM)</span>
                    <button
                      onClick={() => handleVote('optionB')}
                      style={{ background: userVoted === 'optionB' ? '#00A884' : '#2A3942', color: '#FFF', border: 'none', padding: '0.18rem 0.45rem', borderRadius: '4px', fontSize: '0.62rem', fontWeight: '800', cursor: 'pointer', flexShrink: 0 }}
                    >
                      {userVoted === 'optionB' ? '✓ Voted' : 'Vote B'}
                    </button>
                  </div>
                  <div style={{ display: 'flex', alignItems: 'center', gap: '0.4rem', width: '100%' }}>
                    <div style={{ flex: 1, background: '#111B21', height: '6px', borderRadius: '3px', overflow: 'hidden' }}>
                      <div style={{ width: `${percentB}%`, background: '#334155', height: '100%' }}></div>
                    </div>
                    <span style={{ fontSize: '0.62rem', color: '#94A3B8', fontWeight: '700', flexShrink: 0 }}>{percentB}% ({votes.optionB})</span>
                  </div>
                </div>
              </div>

              <div style={{ background: '#2D0A4E', padding: '0.4rem', borderRadius: '6px', marginTop: '0.5rem', fontSize: '0.62rem', color: '#E0E7FF', width: '100%', boxSizing: 'border-box' }}>
                ⚡ 2s AI Fallback Backup: Community agreement favors Option A (78% consensus).
              </div>

              <button
                onClick={onOpenSocialModal}
                style={{ background: '#25D366', color: '#FFF', border: 'none', width: '100%', padding: '0.4rem', borderRadius: '6px', fontSize: '0.7rem', fontWeight: '800', cursor: 'pointer', marginTop: '0.55rem', display: 'flex', alignItems: 'center', justifyContent: 'center', gap: '0.25rem' }}
              >
                <Share2 size={12} />
                <span>Share Poll Link to WhatsApp</span>
              </button>
            </div>
          </div>
        )}

        {/* E. SHOPPING BAG MOBILE VIEW (IN-APP SCREEN) */}
        {mobileTab === 'BAG' && (
          <div style={{ display: 'flex', flexDirection: 'column', gap: '0.75rem', width: '100%' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', width: '100%' }}>
              <h4 style={{ fontSize: '0.82rem', fontWeight: '800', color: '#FF3F6C', margin: 0, display: 'flex', alignItems: 'center', gap: '0.3rem' }}>
                <ShoppingBag size={15} />
                <span>My Shopping Bag ({cartItems.length})</span>
              </h4>
              {cartItems.length > 0 && (
                <span style={{ fontSize: '0.62rem', color: '#10B981', fontWeight: '800', background: 'rgba(16,185,129,0.12)', padding: '0.15rem 0.4rem', borderRadius: '4px' }}>
                  ⚡ Free Express Delivery
                </span>
              )}
            </div>

            {cartItems.length === 0 ? (
              <div style={{ textAlign: 'center', padding: '2.5rem 1rem', background: '#121826', borderRadius: '12px', border: '1px solid rgba(255,255,255,0.08)' }}>
                <ShoppingBag size={36} style={{ color: '#64748B', marginBottom: '0.5rem', opacity: 0.5 }} />
                <div style={{ fontSize: '0.85rem', fontWeight: '800', color: '#F8FAFC', marginBottom: '0.25rem' }}>Your Bag is empty</div>
                <div style={{ fontSize: '0.7rem', color: '#94A3B8' }}>Add items from Spec Matrix or AI Looks to see complete order breakdown</div>
              </div>
            ) : (
              <div style={{ display: 'flex', flexDirection: 'column', gap: '0.65rem', width: '100%' }}>
                {/* Cart Items List */}
                {cartItems.map((item, idx) => (
                  <div key={idx} style={{ background: '#121826', border: '1px solid rgba(255,255,255,0.1)', borderRadius: '10px', padding: '0.5rem', display: 'flex', gap: '0.6rem', alignItems: 'center' }}>
                    <img src={item.image || (item.items && item.items[0]?.image) || 'https://images.unsplash.com/photo-1542272604-780c96856592?w=200'} alt={item.name || item.lookName} style={{ width: '48px', height: '60px', objectFit: 'cover', borderRadius: '6px', flexShrink: 0 }} />
                    <div style={{ flex: 1, minWidth: 0 }}>
                      {item.isBundle && (
                        <span style={{ fontSize: '0.58rem', fontWeight: '800', color: '#C084FC', background: 'rgba(139, 92, 246, 0.2)', padding: '0.1rem 0.3rem', borderRadius: '3px', display: 'inline-block', marginBottom: '0.15rem' }}>
                          ✨ AI 4-PIECE LOOK
                        </span>
                      )}
                      <div style={{ fontSize: '0.72rem', fontWeight: '800', color: '#F8FAFC', whiteSpace: 'nowrap', overflow: 'hidden', textOverflow: 'ellipsis' }}>
                        {item.name || item.lookName}
                      </div>
                      <div style={{ fontSize: '0.62rem', color: '#94A3B8' }}>
                        Qty: 1 • Size: M
                      </div>
                      <div style={{ fontSize: '0.82rem', fontWeight: '900', color: '#FF3F6C', marginTop: '0.15rem' }}>
                        ₹{(item.price || item.lookTotal || 0).toLocaleString()}
                      </div>
                    </div>
                    {onRemoveFromCart && (
                      <button
                        onClick={() => onRemoveFromCart(idx)}
                        style={{ background: 'rgba(239,68,68,0.15)', border: 'none', color: '#F87171', borderRadius: '6px', padding: '0.35rem', cursor: 'pointer', flexShrink: 0, fontSize: '0.7rem' }}
                        title="Remove item"
                      >
                        🗑️
                      </button>
                    )}
                  </div>
                ))}

                {/* Price Summary Card */}
                <div style={{ background: '#1E293B', border: '1px solid rgba(255,255,255,0.08)', borderRadius: '10px', padding: '0.6rem', fontSize: '0.68rem', display: 'flex', flexDirection: 'column', gap: '0.3rem' }}>
                  <div style={{ display: 'flex', justifyContent: 'space-between', color: '#94A3B8' }}>
                    <span>Total MRP:</span>
                    <span style={{ textDecoration: 'line-through' }}>₹{(cartItems.reduce((acc, item) => acc + (item.originalPrice || (item.price ? Math.round(item.price * 1.4) : Math.round(item.lookTotal * 1.3))), 0)).toLocaleString()}</span>
                  </div>
                  <div style={{ display: 'flex', justifyContent: 'space-between', color: '#10B981' }}>
                    <span>Direct Brand Discount:</span>
                    <span>-₹{(cartItems.reduce((acc, item) => acc + ((item.originalPrice || (item.price ? Math.round(item.price * 1.4) : Math.round(item.lookTotal * 1.3))) - (item.price || item.lookTotal || 0)), 0)).toLocaleString()}</span>
                  </div>
                  <div style={{ display: 'flex', justifyContent: 'space-between', color: '#94A3B8' }}>
                    <span>Convenience & Delivery:</span>
                    <span style={{ color: '#10B981', fontWeight: '700' }}>FREE</span>
                  </div>
                  <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '0.82rem', fontWeight: '900', color: '#FFF', borderTop: '1px solid rgba(255,255,255,0.1)', paddingTop: '0.35rem', marginTop: '0.15rem' }}>
                    <span>Total Payable:</span>
                    <span style={{ color: '#FF3F6C' }}>₹{(cartItems.reduce((acc, item) => acc + (item.price || item.lookTotal || 0), 0)).toLocaleString()}</span>
                  </div>
                </div>

                {/* Zero-Risk Guarantee */}
                <div style={{ background: 'rgba(16,185,129,0.08)', border: '1px solid rgba(16,185,129,0.25)', borderRadius: '8px', padding: '0.45rem', fontSize: '0.62rem', color: '#E2E8F0', display: 'flex', alignItems: 'center', gap: '0.35rem' }}>
                  <span style={{ fontSize: '0.85rem' }}>🛡️</span>
                  <span><strong>Zero-Risk Guarantee:</strong> 14-day exchange backed by fit consensus.</span>
                </div>

                {/* 1-Tap Checkout Button */}
                <button
                  onClick={() => onProceedToCheckout && onProceedToCheckout()}
                  style={{ background: '#FF3F6C', color: '#FFF', border: 'none', padding: '0.55rem', borderRadius: '8px', fontSize: '0.75rem', fontWeight: '800', cursor: 'pointer', width: '100%', display: 'flex', alignItems: 'center', justifyContent: 'center', gap: '0.35rem', boxShadow: '0 4px 12px rgba(255,63,108,0.35)' }}
                >
                  <span>Proceed to 1-Tap Checkout</span>
                  <span>➔</span>
                </button>
              </div>
            )}
          </div>
        )}
      </div>

      {/* 3. FIXED BOTTOM PHONE NAVIGATION BAR */}
      <div style={{ flexShrink: 0, display: 'grid', gridTemplateColumns: 'repeat(5, minmax(0, 1fr))', padding: '0.5rem 0 0.15rem 0', borderTop: '1px solid rgba(255,255,255,0.1)', marginTop: '0.5rem', textAlign: 'center', fontSize: '0.6rem', color: '#94A3B8', width: '100%' }}>
        <div onClick={() => setMobileTab('HOME')} style={{ cursor: 'pointer', color: mobileTab === 'HOME' ? '#FF3F6C' : '#94A3B8', fontWeight: mobileTab === 'HOME' ? '800' : 'normal', minWidth: 0, overflow: 'hidden', whiteSpace: 'nowrap' }}>
          🏠 Home
        </div>
        <div onClick={() => setMobileTab('MATRIX')} style={{ cursor: 'pointer', color: mobileTab === 'MATRIX' ? '#FF3F6C' : '#94A3B8', fontWeight: mobileTab === 'MATRIX' ? '800' : 'normal', minWidth: 0, overflow: 'hidden', whiteSpace: 'nowrap' }}>
          📊 Specs
        </div>
        <div onClick={() => setMobileTab('OUTFITS')} style={{ cursor: 'pointer', color: mobileTab === 'OUTFITS' ? '#FF3F6C' : '#94A3B8', fontWeight: mobileTab === 'OUTFITS' ? '800' : 'normal', minWidth: 0, overflow: 'hidden', whiteSpace: 'nowrap' }}>
          🛍️ Studio
        </div>
        <div onClick={() => setMobileTab('POLL')} style={{ cursor: 'pointer', color: mobileTab === 'POLL' ? '#FF3F6C' : '#94A3B8', fontWeight: mobileTab === 'POLL' ? '800' : 'normal', minWidth: 0, overflow: 'hidden', whiteSpace: 'nowrap' }}>
          💬 Poll
        </div>
        <div onClick={() => setMobileTab('BAG')} style={{ cursor: 'pointer', color: mobileTab === 'BAG' ? '#FF3F6C' : '#94A3B8', fontWeight: mobileTab === 'BAG' ? '800' : 'normal', minWidth: 0, overflow: 'hidden', whiteSpace: 'nowrap' }}>
          🛍️ Bag ({cartItems.length})
        </div>
      </div>
    </div>
  );
}
