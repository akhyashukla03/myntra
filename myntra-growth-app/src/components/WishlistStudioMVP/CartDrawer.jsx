import React from 'react';
import { ShoppingBag, X, Trash2, ShieldCheck, ArrowRight, Sparkles, CheckCircle2 } from 'lucide-react';

export default function CartDrawer({ isOpen, onClose, cartItems, onRemoveItem, onProceedToCheckout }) {
  if (!isOpen) return null;

  const totalAmount = cartItems.reduce((acc, item) => acc + (item.price || item.lookTotal || 0), 0);
  const totalOriginal = cartItems.reduce((acc, item) => acc + (item.originalPrice || (item.price ? item.price * 1.5 : item.lookTotal * 1.3)), 0);
  const savings = Math.round(totalOriginal - totalAmount);

  return (
    <div className="modal-overlay" onClick={onClose}>
      <div
        className="modal-content-card"
        style={{ maxWidth: '540px', padding: '1.75rem' }}
        onClick={(e) => e.stopPropagation()}
      >
        {/* Header */}
        <div className="modal-header">
          <div className="modal-title-row">
            <ShoppingBag size={20} className="text-pink" />
            <h3>Your Shopping Bag ({cartItems.length} {cartItems.length === 1 ? 'Item' : 'Items'})</h3>
          </div>
          <button className="modal-close-btn" onClick={onClose}>
            <X size={18} />
          </button>
        </div>

        {/* Empty State */}
        {cartItems.length === 0 ? (
          <div style={{ textAlign: 'center', padding: '3rem 1rem' }}>
            <ShoppingBag size={48} style={{ color: '#64748B', marginBottom: '1rem', opacity: 0.5 }} />
            <h4 style={{ fontSize: '1.1rem', fontWeight: 800, marginBottom: '0.5rem' }}>Your Bag is Empty</h4>
            <p style={{ fontSize: '0.88rem', color: '#94A3B8' }}>
              Add items from your Wishlist Grid or generate complete looks in the AI Outfit Matcher!
            </p>
          </div>
        ) : (
          <div style={{ display: 'flex', flexDirection: 'column', gap: '1.25rem' }}>
            {/* Items List */}
            <div style={{ display: 'flex', flexDirection: 'column', gap: '0.85rem', maxHeight: '360px', overflowY: 'auto' }}>
              {cartItems.map((item, idx) => (
                <div
                  key={idx}
                  style={{
                    display: 'flex',
                    alignItems: 'center',
                    gap: '1rem',
                    background: 'rgba(255, 255, 255, 0.03)',
                    border: '1px solid rgba(255, 255, 255, 0.08)',
                    borderRadius: '12px',
                    padding: '0.85rem 1rem'
                  }}
                >
                  <img
                    src={item.image || 'https://images.unsplash.com/photo-1542272604-780c96856592?w=200'}
                    alt={item.name || item.lookName}
                    style={{ width: '56px', height: '68px', objectFit: 'cover', borderRadius: '6px', flexShrink: 0 }}
                  />

                  <div style={{ flex: 1, minWidth: 0 }}>
                    {item.isBundle && (
                      <span
                        style={{
                          fontSize: '0.68rem',
                          fontWeight: 800,
                          color: '#C084FC',
                          background: 'rgba(139, 92, 246, 0.15)',
                          padding: '0.15rem 0.45rem',
                          borderRadius: '4px',
                          display: 'inline-block',
                          marginBottom: '0.2rem'
                        }}
                      >
                        ✨ AI COORDINATED 3-PIECE LOOK
                      </span>
                    )}
                    <h5
                      style={{
                        fontSize: '0.88rem',
                        fontWeight: 700,
                        color: '#FFF',
                        whiteSpace: 'nowrap',
                        overflow: 'hidden',
                        textOverflow: 'ellipsis'
                      }}
                    >
                      {item.name || item.lookName}
                    </h5>
                    <div style={{ fontSize: '0.78rem', color: '#94A3B8', marginTop: '0.15rem' }}>
                      {item.brand ? `${item.brand} • ` : ''}Qty: 1
                    </div>
                    <div style={{ fontSize: '0.95rem', fontWeight: 800, color: '#FF3F6C', marginTop: '0.25rem' }}>
                      ₹{(item.price || item.lookTotal || 0).toLocaleString()}
                    </div>
                  </div>

                  <button
                    onClick={() => onRemoveItem(idx)}
                    style={{
                      background: 'rgba(239, 68, 68, 0.1)',
                      border: '1px solid rgba(239, 68, 68, 0.25)',
                      color: '#F87171',
                      borderRadius: '8px',
                      padding: '0.45rem',
                      cursor: 'pointer'
                    }}
                    title="Remove item"
                  >
                    <Trash2 size={15} />
                  </button>
                </div>
              ))}
            </div>

            {/* Price Breakdown */}
            <div
              style={{
                background: 'rgba(0, 0, 0, 0.3)',
                border: '1px solid rgba(255, 255, 255, 0.08)',
                borderRadius: '12px',
                padding: '1.1rem',
                display: 'flex',
                flexDirection: 'column',
                gap: '0.5rem'
              }}
            >
              <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '0.85rem', color: '#94A3B8' }}>
                <span>Total MRP:</span>
                <span style={{ textDecoration: 'line-through' }}>₹{totalOriginal.toLocaleString()}</span>
              </div>
              <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '0.85rem', color: '#34D399' }}>
                <span>Direct Brand Price Discount:</span>
                <span>-₹{savings.toLocaleString()}</span>
              </div>
              <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '0.85rem', color: '#94A3B8' }}>
                <span>Delivery Fee:</span>
                <span style={{ color: '#34D399', fontWeight: 700 }}>FREE (Express)</span>
              </div>
              <div
                style={{
                  display: 'flex',
                  justifyContent: 'space-between',
                  fontSize: '1.1rem',
                  fontWeight: 900,
                  color: '#FFF',
                  borderTop: '1px solid rgba(255, 255, 255, 0.1)',
                  paddingTop: '0.65rem',
                  marginTop: '0.25rem'
                }}
              >
                <span>Total Amount:</span>
                <span style={{ color: '#FF3F6C' }}>₹{totalAmount.toLocaleString()}</span>
              </div>
            </div>

            {/* Fit Guarantee Badge */}
            <div
              style={{
                display: 'flex',
                alignItems: 'center',
                gap: '0.65rem',
                background: 'rgba(16, 185, 129, 0.08)',
                border: '1px solid rgba(16, 185, 129, 0.25)',
                borderRadius: '8px',
                padding: '0.75rem 1rem',
                fontSize: '0.82rem',
                color: '#E2E8F0'
              }}
            >
              <ShieldCheck size={18} style={{ color: '#34D399', flexShrink: 0 }} />
              <span>
                <strong>Zero-Risk Fit Guarantee:</strong> Backed by Verified Fit Consensus & free 14-day doorstep exchange.
              </span>
            </div>

            {/* Checkout CTA */}
            <button
              className="add-to-bag-btn"
              style={{ padding: '0.85rem', fontSize: '0.95rem' }}
              onClick={onProceedToCheckout}
            >
              <span>Proceed to 1-Tap Checkout</span>
              <ArrowRight size={16} />
            </button>
          </div>
        )}
      </div>
    </div>
  );
}
