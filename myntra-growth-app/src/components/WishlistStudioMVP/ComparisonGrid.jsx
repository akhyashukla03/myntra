import React, { useState } from 'react';
import { Check, Star, ShieldCheck, Shirt, AlertCircle, ShoppingBag, Plus, X, Image } from 'lucide-react';

export default function ComparisonGrid({
  products,
  selectedForCompare,
  onToggleCompare,
  onMoveToBag,
}) {
  const [activePhotoIdx, setActivePhotoIdx] = useState({});

  const compareList = products.filter((p) => selectedForCompare.includes(p.id));

  const handleCyclePhoto = (prodId, numPhotos) => {
    setActivePhotoIdx((prev) => ({
      ...prev,
      [prodId]: ((prev[prodId] || 0) + 1) % numPhotos,
    }));
  };

  return (
    <div className="comparison-studio-container">
      <div className="compare-top-banner">
        <div>
          <h2 className="compare-title">Side-by-Side Fashion Comparison Studio</h2>
          <p className="compare-sub">
            Evaluating {compareList.length} shortlisted items across fit consensus, fabric weight (GSM), real user photos, and return risk.
          </p>
        </div>
        <div className="compare-hint-pill">
          <span>Tip: Click 'Cycle Customer Photos' to inspect unfiltered real reviews</span>
        </div>
      </div>

      {compareList.length === 0 ? (
        <div className="empty-compare-state">
          <AlertCircle size={40} className="text-pink" />
          <h3>No Items Selected for Comparison</h3>
          <p>Select 2 to 4 wishlisted items from the grid below to compare them side-by-side.</p>
        </div>
      ) : (
        <div className="compare-matrix-scroll">
          <div className="compare-columns-grid" style={{ gridTemplateColumns: `repeat(${compareList.length}, minmax(320px, 1fr))` }}>
            {compareList.map((prod) => {
              const currentImgIdx = activePhotoIdx[prod.id] || 0;
              const allImages = [prod.image, ...(prod.customerImages || [])];

              return (
                <div key={prod.id} className="compare-product-col">
                  {/* Remove button */}
                  <button
                    className="remove-compare-btn"
                    onClick={() => onToggleCompare(prod.id)}
                    title="Remove from comparison"
                  >
                    <X size={14} />
                  </button>

                  {/* Image Card with Real Photo Switcher */}
                  <div className="compare-img-box">
                    <img
                      src={allImages[currentImgIdx]}
                      alt={prod.name}
                      className="compare-product-img"
                    />
                    <div className="img-type-badge">
                      {currentImgIdx === 0 ? 'Studio Photo' : `Customer Photo #${currentImgIdx}`}
                    </div>
                    {allImages.length > 1 && (
                      <button
                        className="cycle-photo-btn"
                        onClick={() => handleCyclePhoto(prod.id, allImages.length)}
                      >
                        <Image size={13} />
                        <span>Cycle Photos ({currentImgIdx + 1}/{allImages.length})</span>
                      </button>
                    )}
                  </div>

                  {/* Product Metadata */}
                  <div className="compare-prod-info">
                    <span className="compare-brand">{prod.brand}</span>
                    <h3 className="compare-name">{prod.name}</h3>

                    <div className="compare-price-row">
                      <span className="curr-price">₹{prod.price.toLocaleString()}</span>
                      <span className="orig-price">₹{prod.originalPrice.toLocaleString()}</span>
                      <span className="rating-pill">
                        <Star size={12} fill="#F59E0B" color="#F59E0B" /> {prod.rating} ({prod.ratingCount})
                      </span>
                    </div>
                  </div>

                  {/* Comparative Specs Matrix */}
                  <div className="spec-rows-list">
                    <div className="spec-row-item">
                      <div className="spec-label">
                        <Shirt size={14} className="text-pink" />
                        <span>Fabric & Weight (GSM):</span>
                      </div>
                      <div className="spec-value highlight-fabric">{prod.fabric}</div>
                    </div>

                    <div className="spec-row-item">
                      <div className="spec-label">
                        <Check size={14} className="text-purple" />
                        <span>Verified Fit Rating:</span>
                      </div>
                      <div className="spec-value highlight-fit">{prod.fitScore}</div>
                    </div>

                    <div className="spec-row-item">
                      <div className="spec-label">
                        <ShieldCheck size={14} className="text-green" />
                        <span>Return Risk:</span>
                      </div>
                      <div className={`spec-value return-badge ${prod.returnRisk.includes('Low') ? 'risk-low' : 'risk-med'}`}>
                        {prod.returnRisk}
                      </div>
                    </div>

                    <div className="spec-row-item">
                      <div className="spec-label">
                        <span>Key Customer Consensus:</span>
                      </div>
                      <div className="spec-value-small">{prod.keyPros}</div>
                    </div>
                  </div>

                  {/* Decision Action CTA */}
                  <div className="compare-cta-box">
                    <button
                      className="choose-btn"
                      onClick={() => onMoveToBag(prod)}
                    >
                      <ShoppingBag size={16} />
                      <span>Choose This & Move to Bag</span>
                    </button>
                  </div>
                </div>
              );
            })}
          </div>
        </div>
      )}
    </div>
  );
}
