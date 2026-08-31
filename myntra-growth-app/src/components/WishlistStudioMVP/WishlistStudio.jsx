import React, { useState } from 'react';
import { WISHLIST_PRODUCTS } from '../../data/mockWishlistProducts';
import WishlistHeader from './WishlistHeader';
import ComparisonGrid from './ComparisonGrid';
import OutfitMatcher from './OutfitMatcher';
import SocialShareModal from './SocialShareModal';
import CartDrawer from './CartDrawer';
import CheckoutModal from './CheckoutModal';
import { Star, ShoppingBag, Plus, Check, Columns3, Wand2, Share2, Heart, Smartphone, Monitor } from 'lucide-react';

export default function WishlistStudio() {
  const [activeCollection, setActiveCollection] = useState('ALL');
  const [activeView, setActiveView] = useState('GRID'); // 'GRID', 'COMPARE', 'OUTFITS'
  const [deviceMode, setDeviceMode] = useState('DESKTOP'); // 'DESKTOP' or 'MOBILE'
  const [selectedForCompare, setSelectedForCompare] = useState(['prod-01', 'prod-02', 'prod-03']);
  const [selectedForOutfit, setSelectedForOutfit] = useState(WISHLIST_PRODUCTS[0]);
  const [isSocialModalOpen, setIsSocialModalOpen] = useState(false);
  const [isCartOpen, setIsCartOpen] = useState(false);
  const [isCheckoutOpen, setIsCheckoutOpen] = useState(false);
  const [toastMessage, setToastMessage] = useState('');

  // Live persistent cart state
  const [cartItems, setCartItems] = useState([
    WISHLIST_PRODUCTS[0]
  ]);

  // Filter products by collection
  const filteredProducts = WISHLIST_PRODUCTS.filter((p) => {
    if (activeCollection === 'ALL') return true;
    return p.category === activeCollection;
  });

  const handleToggleCompare = (productId) => {
    setSelectedForCompare((prev) => {
      if (prev.includes(productId)) {
        return prev.filter((id) => id !== productId);
      } else {
        if (prev.length >= 4) {
          showToast('You can compare a maximum of 4 items at once.');
          return prev;
        }
        return [...prev, productId];
      }
    });
  };

  const handleMoveToBag = (product) => {
    setCartItems((prev) => [...prev, product]);
    showToast(`✓ "${product.name}" added to your Bag!`);
  };

  const handleAddLookToBag = (bundle) => {
    setCartItems((prev) => [...prev, bundle]);
    showToast(`✨ Complete 4-Piece Look added to your Bag!`);
    setIsCartOpen(true);
  };

  const handleRemoveFromCart = (index) => {
    setCartItems((prev) => prev.filter((_, i) => i !== index));
    showToast(`Item removed from Shopping Bag.`);
  };

  const handleLaunchOutfitMatcher = (product) => {
    setSelectedForOutfit(product);
    setActiveView('OUTFITS');
  };

  const showToast = (msg) => {
    setToastMessage(msg);
    setTimeout(() => setToastMessage(''), 3500);
  };

  return (
    <div className="module-container">
      {/* View Mode Switcher Header Bar */}
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', background: '#121826', border: '1px solid rgba(255,255,255,0.08)', padding: '0.65rem 1.25rem', borderRadius: '12px', marginBottom: '1.25rem' }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '0.65rem' }}>
          <span style={{ fontSize: '0.85rem', fontWeight: '800', color: '#F8FAFC' }}>📱 MVP Display Options:</span>
          <span style={{ fontSize: '0.75rem', color: '#94A3B8' }}>Select interface mode to simulate Myntra Mobile App or Desktop Workspace</span>
        </div>

        <div style={{ display: 'flex', gap: '0.5rem' }}>
          <button
            onClick={() => setDeviceMode('DESKTOP')}
            style={{
              background: deviceMode === 'DESKTOP' ? '#4F46E5' : 'rgba(255,255,255,0.05)',
              color: '#FFFFFF', border: 'none', padding: '0.4rem 0.85rem', borderRadius: '6px', cursor: 'pointer', fontWeight: '700', fontSize: '0.78rem', display: 'flex', alignItems: 'center', gap: '0.35rem'
            }}
          >
            <Monitor size={15} />
            <span>💻 Web Workspace</span>
          </button>

          <button
            onClick={() => setDeviceMode('MOBILE')}
            style={{
              background: deviceMode === 'MOBILE' ? '#FF3F6C' : 'rgba(255,255,255,0.05)',
              color: '#FFFFFF', border: 'none', padding: '0.4rem 0.85rem', borderRadius: '6px', cursor: 'pointer', fontWeight: '700', fontSize: '0.78rem', display: 'flex', alignItems: 'center', gap: '0.35rem'
            }}
          >
            <Smartphone size={15} />
            <span>📱 Mobile App Frame</span>
          </button>
        </div>
      </div>

      {/* RENDER MOBILE SMARTPHONE FRAME VIEW IF SELECTED */}
      {deviceMode === 'MOBILE' ? (
        <div style={{ maxWidth: '420px', margin: '0 auto', background: '#0A0D14', border: '12px solid #1E293B', borderRadius: '36px', padding: '1.25rem', boxShadow: '0 25px 60px rgba(0,0,0,0.6)', color: '#FFF' }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', borderBottom: '1px solid rgba(255,255,255,0.1)', paddingBottom: '0.5rem', marginBottom: '0.75rem' }}>
            <span style={{ fontSize: '0.75rem', color: '#94A3B8' }}>9:41 📶 5G</span>
            <span style={{ fontSize: '1.1rem', fontWeight: '900', color: '#FF3F6C' }}>myntra</span>
            <button onClick={() => setIsCartOpen(true)} style={{ background: '#2D0A4E', color: '#FFF', border: 'none', padding: '0.2rem 0.6rem', borderRadius: '6px', fontSize: '0.75rem', fontWeight: '800', cursor: 'pointer' }}>
              🛍️ Bag ({cartItems.length})
            </button>
          </div>

          <div style={{ background: '#1E293B', padding: '0.45rem 0.75rem', borderRadius: '8px', fontSize: '0.78rem', fontWeight: '700', marginBottom: '0.85rem', display: 'flex', justifyContent: 'space-between' }}>
            <span>Smart Folder: Workwear</span>
            <span style={{ color: '#FF3F6C' }}>Spec Matrix Active</span>
          </div>

          {/* Interactive Mobile Comparison Showcase */}
          <div style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
            <h4 style={{ fontSize: '0.85rem', fontWeight: '800', color: '#FF3F6C', margin: 0 }}>Side-by-Side Spec & GSM Matrix</h4>
            
            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '0.65rem' }}>
              {WISHLIST_PRODUCTS.slice(0, 2).map((p) => (
                <div key={p.id} style={{ background: '#121826', border: '1px solid rgba(255,255,255,0.1)', borderRadius: '10px', padding: '0.65rem', display: 'flex', flexDirection: 'column', gap: '0.35rem' }}>
                  <img src={p.image} alt={p.name} style={{ width: '100%', height: '120px', objectFit: 'cover', borderRadius: '6px' }} />
                  <span style={{ fontSize: '0.72rem', fontWeight: '800', color: '#F8FAFC' }}>{p.name}</span>
                  <span style={{ background: p.id === 'prod-01' ? '#2D0A4E' : 'rgba(255,63,108,0.2)', color: p.id === 'prod-01' ? '#FFF' : '#FF3F6C', fontSize: '0.65rem', fontWeight: '800', padding: '0.15rem 0.4rem', borderRadius: '4px', alignSelf: 'flex-start' }}>
                    {p.fabric.split('(')[0]}
                  </span>
                  <span style={{ fontSize: '0.68rem', color: '#CBD5E1' }}>Fit: {p.fitScore.split('(')[0]}</span>
                  <span style={{ fontSize: '0.78rem', fontWeight: '900', color: '#FF3F6C' }}>₹{p.price.toLocaleString()}</span>
                  <button
                    onClick={() => handleMoveToBag(p)}
                    style={{ background: '#FF3F6C', color: '#FFF', border: 'none', padding: '0.35rem', borderRadius: '6px', fontSize: '0.72rem', fontWeight: '800', cursor: 'pointer', marginTop: '0.25rem' }}
                  >
                    Add to Bag
                  </button>
                </div>
              ))}
            </div>

            <div style={{ background: '#121826', border: '1px solid rgba(255,255,255,0.1)', borderRadius: '10px', padding: '0.75rem', marginTop: '0.5rem' }}>
              <h4 style={{ fontSize: '0.82rem', fontWeight: '800', color: '#4F46E5', margin: '0 0 0.35rem 0' }}>✨ AI Coordinated Look (+₹450 AOV)</h4>
              <p style={{ fontSize: '0.72rem', color: '#CBD5E1', margin: '0 0 0.5rem 0' }}>Heavy Cargo (₹1,999) + Oversized Tee (₹899) + Canvas Sneakers (₹1,499) = ₹4,397</p>
              <button
                onClick={() => handleAddLookToBag(WISHLIST_PRODUCTS[0])}
                style={{ background: 'linear-gradient(135deg, #4F46E5, #818CF8)', color: '#FFF', border: 'none', width: '100%', padding: '0.45rem', borderRadius: '6px', fontSize: '0.75rem', fontWeight: '800', cursor: 'pointer' }}
              >
                Move 3-Piece Look to Bag
              </button>
            </div>

            <button
              onClick={() => setIsSocialModalOpen(true)}
              style={{ background: 'rgba(255,255,255,0.08)', border: '1px solid rgba(255,255,255,0.15)', color: '#FFF', padding: '0.5rem', borderRadius: '8px', fontSize: '0.75rem', fontWeight: '700', cursor: 'pointer', display: 'flex', alignItems: 'center', justifyContent: 'center', gap: '0.35rem' }}
            >
              <Share2 size={14} />
              <span>Ask Friends on WhatsApp</span>
            </button>
          </div>
        </div>
      ) : (
        /* RENDER DESKTOP WEB WORKSPACE VIEW */
        <>
          {/* Header & Occasion Bar */}
          <WishlistHeader
            activeCollection={activeCollection}
            setActiveCollection={setActiveCollection}
            activeView={activeView}
            setActiveView={setActiveView}
            selectedForCompare={selectedForCompare}
            cartCount={cartItems.length}
            onOpenCart={() => setIsCartOpen(true)}
            onOpenSocialModal={() => setIsSocialModalOpen(true)}
          />

          {/* Main View Area */}
          <div className="studio-main-content">
            {activeView === 'GRID' && (
              <div className="wishlist-grid-view">
                {/* Quick action helper bar */}
                <div className="grid-helper-bar">
                  <span>
                    Select items to compare side-by-side ({selectedForCompare.length}/4 selected) • Showing {filteredProducts.length} items
                  </span>
                  <div style={{ display: 'flex', gap: '0.65rem' }}>
                    {selectedForCompare.length >= 2 && (
                      <button
                        className="open-compare-bar-btn"
                        onClick={() => setActiveView('COMPARE')}
                      >
                        <Columns3 size={15} />
                        <span>Launch Comparison ({selectedForCompare.length} items)</span>
                      </button>
                    )}
                    <button
                      className="open-compare-bar-btn"
                      style={{ background: 'rgba(255,255,255,0.1)' }}
                      onClick={() => setIsCartOpen(true)}
                    >
                      <ShoppingBag size={15} />
                      <span>View Bag ({cartItems.length})</span>
                    </button>
                  </div>
                </div>

                <div className="product-cards-grid">
                  {filteredProducts.map((prod) => {
                    const isSelected = selectedForCompare.includes(prod.id);

                    return (
                      <div key={prod.id} className="product-card-item">
                        <div className="prod-img-wrapper">
                          <img src={prod.image} alt={prod.name} className="product-card-img" />
                          <button className="wishlist-heart-btn" title="Saved in Wishlist">
                            <Heart size={16} fill="#FF3F6C" color="#FF3F6C" />
                          </button>

                          <div className="compare-checkbox-pill" onClick={() => handleToggleCompare(prod.id)}>
                            <div className={`checkbox-box ${isSelected ? 'checked' : ''}`}>
                              {isSelected && <Check size={12} />}
                            </div>
                            <span>Compare</span>
                          </div>
                        </div>

                        <div className="prod-card-body">
                          <span className="prod-brand">{prod.brand}</span>
                          <h4 className="prod-name">{prod.name}</h4>

                          <div className="prod-price-row">
                            <span className="prod-price">₹{prod.price.toLocaleString()}</span>
                            <span className="prod-mrp">₹{prod.originalPrice.toLocaleString()}</span>
                            <span className="prod-discount-pill">
                              {Math.round(((prod.originalPrice - prod.price) / prod.originalPrice) * 100)}% OFF
                            </span>
                          </div>

                          {/* Studio Micro Signals */}
                          <div className="prod-spec-row">
                            <span className="spec-chip highlight-fabric">{prod.fabric.split('(')[0]}</span>
                            <span className="spec-chip highlight-fit">{prod.fitScore.split('(')[0]}</span>
                          </div>

                          {/* Card Action Buttons */}
                          <div className="prod-actions-row">
                            <button
                              className="add-to-bag-btn"
                              onClick={() => handleMoveToBag(prod)}
                            >
                              <ShoppingBag size={14} />
                              <span>Move to Bag</span>
                            </button>

                            <button
                              className="choose-btn"
                              style={{ width: 'auto', padding: '0.65rem 0.85rem' }}
                              title="Generate AI Outfit Looks with this item"
                              onClick={() => handleLaunchOutfitMatcher(prod)}
                            >
                              <Wand2 size={15} />
                            </button>
                          </div>
                        </div>
                      </div>
                    );
                  })}
                </div>
              </div>
            )}

            {activeView === 'COMPARE' && (
              <ComparisonGrid
                products={WISHLIST_PRODUCTS}
                selectedForCompare={selectedForCompare}
                onToggleCompare={handleToggleCompare}
                onMoveToBag={handleMoveToBag}
              />
            )}

            {activeView === 'OUTFITS' && (
              <OutfitMatcher
                products={WISHLIST_PRODUCTS}
                initialProduct={selectedForOutfit}
                onAddLookToBag={handleAddLookToBag}
                showToast={showToast}
              />
            )}
          </div>
        </>
      )}

      {/* Shopping Bag Drawer Modal */}
      <CartDrawer
        isOpen={isCartOpen}
        onClose={() => setIsCartOpen(false)}
        cartItems={cartItems}
        onRemoveItem={handleRemoveFromCart}
        onProceedToCheckout={() => {
          setIsCartOpen(false);
          setIsCheckoutOpen(true);
        }}
      />

      {/* 1-Tap Checkout Modal */}
      <CheckoutModal
        isOpen={isCheckoutOpen}
        onClose={() => setIsCheckoutOpen(false)}
        cartItems={cartItems}
        onOrderComplete={(orderId) => {
          setCartItems([]);
          showToast(`🎉 Order ${orderId} confirmed successfully!`);
        }}
      />

      {/* Social WhatsApp Modal */}
      <SocialShareModal
        isOpen={isSocialModalOpen}
        onClose={() => setIsSocialModalOpen(false)}
        products={WISHLIST_PRODUCTS.slice(0, 2)}
      />

      {/* Floating Toast Notification */}
      {toastMessage && (
        <div className="custom-toast">
          {toastMessage}
        </div>
      )}
    </div>
  );
}
