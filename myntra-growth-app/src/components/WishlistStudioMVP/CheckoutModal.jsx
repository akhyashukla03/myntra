import React, { useState } from 'react';
import { CheckCircle2, X, MapPin, CreditCard, Smartphone, Truck, Sparkles, ShoppingBag } from 'lucide-react';

export default function CheckoutModal({ isOpen, onClose, cartItems, onOrderComplete }) {
  const [selectedAddress, setSelectedAddress] = useState('home');
  const [selectedPayment, setSelectedPayment] = useState('upi');
  const [isPlacing, setIsPlacing] = useState(false);
  const [orderSuccess, setOrderSuccess] = useState(false);
  const [orderId, setOrderId] = useState('');

  if (!isOpen) return null;

  const totalAmount = cartItems.reduce((acc, item) => acc + (item.price || item.lookTotal || 0), 0);

  const handlePlaceOrder = () => {
    setIsPlacing(true);
    setTimeout(() => {
      const genId = 'MYN-' + Math.floor(100000 + Math.random() * 900000);
      setOrderId(genId);
      setIsPlacing(false);
      setOrderSuccess(true);
      if (onOrderComplete) onOrderComplete(genId);
    }, 1200);
  };

  return (
    <div className="modal-overlay" onClick={onClose}>
      <div
        className="modal-content-card"
        style={{ maxWidth: '580px', padding: '2rem' }}
        onClick={(e) => e.stopPropagation()}
      >
        {!orderSuccess ? (
          <div style={{ display: 'flex', flexDirection: 'column', gap: '1.5rem' }}>
            {/* Header */}
            <div className="modal-header">
              <div className="modal-title-row">
                <Truck size={22} className="text-pink" />
                <h3>1-Tap Express Checkout</h3>
              </div>
              <button className="modal-close-btn" onClick={onClose}>
                <X size={18} />
              </button>
            </div>

            {/* Address Selection */}
            <div>
              <label style={{ fontSize: '0.8rem', fontWeight: 800, color: '#94A3B8', textTransform: 'uppercase', display: 'block', marginBottom: '0.65rem' }}>
                1. Delivery Address:
              </label>
              <div style={{ display: 'flex', flexDirection: 'column', gap: '0.65rem' }}>
                <div
                  onClick={() => setSelectedAddress('home')}
                  style={{
                    display: 'flex',
                    alignItems: 'center',
                    gap: '0.75rem',
                    padding: '0.85rem 1rem',
                    borderRadius: '10px',
                    border: `1.5px solid ${selectedAddress === 'home' ? '#FF3F6C' : 'rgba(255,255,255,0.08)'}`,
                    background: selectedAddress === 'home' ? 'rgba(255,63,108,0.08)' : 'rgba(255,255,255,0.02)',
                    cursor: 'pointer'
                  }}
                >
                  <MapPin size={18} style={{ color: selectedAddress === 'home' ? '#FF3F6C' : '#94A3B8' }} />
                  <div>
                    <div style={{ fontSize: '0.88rem', fontWeight: 800, color: '#FFF' }}>
                      Home (Default) • Valued Shopper
                    </div>
                    <div style={{ fontSize: '0.78rem', color: '#94A3B8' }}>
                      #402, Skyline Residency, 12th Main, Indiranagar, Bengaluru - 560038
                    </div>
                  </div>
                </div>

                <div
                  onClick={() => setSelectedAddress('office')}
                  style={{
                    display: 'flex',
                    alignItems: 'center',
                    gap: '0.75rem',
                    padding: '0.85rem 1rem',
                    borderRadius: '10px',
                    border: `1.5px solid ${selectedAddress === 'office' ? '#FF3F6C' : 'rgba(255,255,255,0.08)'}`,
                    background: selectedAddress === 'office' ? 'rgba(255,63,108,0.08)' : 'rgba(255,255,255,0.02)',
                    cursor: 'pointer'
                  }}
                >
                  <MapPin size={18} style={{ color: selectedAddress === 'office' ? '#FF3F6C' : '#94A3B8' }} />
                  <div>
                    <div style={{ fontSize: '0.88rem', fontWeight: 800, color: '#FFF' }}>
                      Office • Whitefield Tech Park
                    </div>
                    <div style={{ fontSize: '0.78rem', color: '#94A3B8' }}>
                      Tower B, 4th Floor, EPIP Zone, Bengaluru - 560066
                    </div>
                  </div>
                </div>
              </div>
            </div>

            {/* Payment Method */}
            <div>
              <label style={{ fontSize: '0.8rem', fontWeight: 800, color: '#94A3B8', textTransform: 'uppercase', display: 'block', marginBottom: '0.65rem' }}>
                2. Select Payment Method:
              </label>
              <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '0.65rem' }}>
                <div
                  onClick={() => setSelectedPayment('upi')}
                  style={{
                    display: 'flex',
                    alignItems: 'center',
                    gap: '0.65rem',
                    padding: '0.85rem',
                    borderRadius: '10px',
                    border: `1.5px solid ${selectedPayment === 'upi' ? '#FF3F6C' : 'rgba(255,255,255,0.08)'}`,
                    background: selectedPayment === 'upi' ? 'rgba(255,63,108,0.08)' : 'rgba(255,255,255,0.02)',
                    cursor: 'pointer'
                  }}
                >
                  <Smartphone size={18} style={{ color: selectedPayment === 'upi' ? '#FF3F6C' : '#94A3B8' }} />
                  <div>
                    <div style={{ fontSize: '0.85rem', fontWeight: 800, color: '#FFF' }}>Google Pay / UPI</div>
                    <div style={{ fontSize: '0.72rem', color: '#34D399' }}>Instant 1-Tap</div>
                  </div>
                </div>

                <div
                  onClick={() => setSelectedPayment('card')}
                  style={{
                    display: 'flex',
                    alignItems: 'center',
                    gap: '0.65rem',
                    padding: '0.85rem',
                    borderRadius: '10px',
                    border: `1.5px solid ${selectedPayment === 'card' ? '#FF3F6C' : 'rgba(255,255,255,0.08)'}`,
                    background: selectedPayment === 'card' ? 'rgba(255,63,108,0.08)' : 'rgba(255,255,255,0.02)',
                    cursor: 'pointer'
                  }}
                >
                  <CreditCard size={18} style={{ color: selectedPayment === 'card' ? '#FF3F6C' : '#94A3B8' }} />
                  <div>
                    <div style={{ fontSize: '0.85rem', fontWeight: 800, color: '#FFF' }}>Credit / Debit Card</div>
                    <div style={{ fontSize: '0.72rem', color: '#94A3B8' }}>HDFC •• 4912</div>
                  </div>
                </div>
              </div>
            </div>

            {/* Total Summary */}
            <div
              style={{
                display: 'flex',
                justifyContent: 'space-between',
                alignItems: 'center',
                background: 'rgba(0,0,0,0.4)',
                border: '1px solid rgba(255,255,255,0.08)',
                borderRadius: '10px',
                padding: '0.9rem 1.25rem'
              }}
            >
              <div>
                <span style={{ fontSize: '0.78rem', color: '#94A3B8' }}>Total Payable ({cartItems.length} items):</span>
                <div style={{ fontSize: '1.35rem', fontWeight: 900, color: '#FF3F6C' }}>
                  ₹{totalAmount.toLocaleString()}
                </div>
              </div>

              <span style={{ fontSize: '0.75rem', fontWeight: 800, color: '#34D399', background: 'rgba(16,185,129,0.1)', padding: '0.3rem 0.65rem', borderRadius: '6px' }}>
                Zero-Discount Intact
              </span>
            </div>

            {/* Place Order CTA */}
            <button
              className="add-to-bag-btn"
              style={{ padding: '0.95rem', fontSize: '1rem' }}
              onClick={handlePlaceOrder}
              disabled={isPlacing}
            >
              {isPlacing ? (
                <span>Securing Order on Myntra...</span>
              ) : (
                <span>Pay ₹{totalAmount.toLocaleString()} & Place Order</span>
              )}
            </button>
          </div>
        ) : (
          /* Order Confirmation Screen */
          <div style={{ textAlign: 'center', padding: '1.5rem 0', display: 'flex', flexDirection: 'column', alignItems: 'center', gap: '1.25rem' }}>
            <div
              style={{
                width: '72px',
                height: '72px',
                borderRadius: '50%',
                background: 'rgba(16, 185, 129, 0.15)',
                border: '2px solid #10B981',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                boxShadow: '0 0 24px rgba(16, 185, 129, 0.3)'
              }}
            >
              <CheckCircle2 size={40} color="#10B981" />
            </div>

            <div>
              <span style={{ fontSize: '0.75rem', fontWeight: 800, color: '#34D399', textTransform: 'uppercase', letterSpacing: '0.5px' }}>
                Conversion Journey Complete
              </span>
              <h2 style={{ fontSize: '1.65rem', fontWeight: 900, color: '#FFF', marginTop: '0.25rem' }}>
                Order Confirmed! 🎉
              </h2>
              <p style={{ fontSize: '0.9rem', color: '#94A3B8', marginTop: '0.35rem' }}>
                Order ID: <strong style={{ color: '#FFF' }}>{orderId}</strong> • Estimated Delivery: <strong style={{ color: '#34D399' }}>Tomorrow by 2:00 PM</strong>
              </p>
            </div>

            <div
              style={{
                background: 'rgba(255, 255, 255, 0.03)',
                border: '1px solid rgba(255, 255, 255, 0.08)',
                borderRadius: '12px',
                padding: '1.1rem',
                width: '100%',
                textAlign: 'left'
              }}
            >
              <div style={{ fontSize: '0.8rem', fontWeight: 800, color: '#94A3B8', textTransform: 'uppercase', marginBottom: '0.5rem' }}>
                Growth Metric Impact of This Order:
              </div>
              <ul style={{ listStyle: 'none', display: 'flex', flexDirection: 'column', gap: '0.4rem', fontSize: '0.85rem', color: '#E2E8F0' }}>
                <li>✨ <strong>Zero Margin Dilution:</strong> Paid full non-discounted price (100% GMV captured).</li>
                <li>🎯 <strong>Resolved Dwell Latency:</strong> Converted from dormant wishlist item to purchase in &lt; 2 minutes.</li>
                <li>🛡️ <strong>Verified Fit Confidence:</strong> -600 bps return probability protection active.</li>
              </ul>
            </div>

            <button
              className="add-to-bag-btn"
              style={{ width: '100%', padding: '0.8rem' }}
              onClick={onClose}
            >
              <span>Back to Wishlist Studio</span>
            </button>
          </div>
        )}
      </div>
    </div>
  );
}
