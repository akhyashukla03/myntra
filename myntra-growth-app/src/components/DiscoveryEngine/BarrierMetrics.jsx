import React from 'react';
import { BARRIER_DISTRIBUTION, CATEGORY_DROPOFF, DISCOVERY_STATS } from '../../data/mockDiscoveryData';
import { BarChart3, TrendingDown, Clock, ShieldAlert, CheckCircle2 } from 'lucide-react';

export default function BarrierMetrics() {
  return (
    <div className="discovery-section">
      <div className="section-header">
        <div>
          <h2 className="section-title">Quantitative Barrier Quantification & Opportunity Mapping</h2>
          <p className="section-subtitle">
            Analyzing the relative impact of each purchase barrier across 24,850+ classified user touchpoints.
          </p>
        </div>
      </div>

      {/* Top Stat Cards */}
      <div className="stats-grid">
        <div className="stat-card">
          <div className="stat-icon-wrapper bg-pink-light">
            <BarChart3 className="text-pink" size={20} />
          </div>
          <div>
            <div className="stat-val">{DISCOVERY_STATS.totalAnalyzed}</div>
            <div className="stat-desc">Analyzed Customer Touchpoints</div>
          </div>
        </div>

        <div className="stat-card">
          <div className="stat-icon-wrapper bg-purple-light">
            <Clock className="text-purple" size={20} />
          </div>
          <div>
            <div className="stat-val">{DISCOVERY_STATS.avgWishlistDwellDays} Days</div>
            <div className="stat-desc">Average Wishlist Dwell Time</div>
          </div>
        </div>

        <div className="stat-card">
          <div className="stat-icon-wrapper bg-blue-light">
            <TrendingDown className="text-blue" size={20} />
          </div>
          <div>
            <div className="stat-val">{DISCOVERY_STATS.conversionDropoffPct}</div>
            <div className="stat-desc">30-Day Wishlist Inaction Rate</div>
          </div>
        </div>

        <div className="stat-card">
          <div className="stat-icon-wrapper bg-green-light">
            <ShieldAlert className="text-green" size={20} />
          </div>
          <div>
            <div className="stat-val">34%</div>
            <div className="stat-desc">Top Barrier: Comparison Paralysis</div>
          </div>
        </div>
      </div>

      {/* Main Charts Row */}
      <div className="charts-two-col">
        {/* Barrier Distribution Horizontal Bar Chart */}
        <div className="chart-card">
          <div className="chart-header">
            <h3 className="chart-title">Primary Non-Monetary Barriers to Purchase (%)</h3>
            <span className="chart-badge">N = 24,850 Touchpoints</span>
          </div>
          <p className="chart-desc">
            34% of users stall because they have saved multiple alternative items and cannot easily evaluate differences.
          </p>

          <div className="bars-list">
            {BARRIER_DISTRIBUTION.map((barrier, index) => (
              <div key={index} className="bar-item">
                <div className="bar-label-row">
                  <span className="bar-name">{barrier.name}</span>
                  <span className="bar-val-text" style={{ color: barrier.color }}>
                    {barrier.percentage}% ({barrier.count.toLocaleString()} mentions)
                  </span>
                </div>
                <div className="bar-track">
                  <div
                    className="bar-fill"
                    style={{
                      width: `${barrier.percentage * 2.5}%`,
                      backgroundColor: barrier.color,
                    }}
                  />
                </div>
                <div className="bar-footer-note">
                  Severity: <strong>{barrier.severity}</strong> • Primary Driver: {index === 0 ? 'Choice Overload' : index === 1 ? 'Outfit Coordination' : index === 2 ? 'Size Charts' : 'Studio Lighting'}
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* Category Drop-off & Conversion Matrix */}
        <div className="chart-card">
          <div className="chart-header">
            <h3 className="chart-title">Wishlist Volume vs Conversion by Category</h3>
            <span className="chart-badge">Category Performance</span>
          </div>
          <p className="chart-desc">
            Western Wear and Denim constitute 64% of all wishlisted items, yet suffer the lowest conversion rates due to styling and comparison doubt.
          </p>

          <div className="category-table-wrapper">
            <table className="category-table">
              <thead>
                <tr>
                  <th>Category</th>
                  <th>Wishlist Share</th>
                  <th>30-Day Conv.</th>
                  <th>Primary Friction Point</th>
                </tr>
              </thead>
              <tbody>
                {CATEGORY_DROPOFF.map((row, idx) => (
                  <tr key={idx}>
                    <td className="cat-name-cell">{row.category}</td>
                    <td>
                      <span className="share-pill">{row.wishlistShare}</span>
                    </td>
                    <td>
                      <span className="conv-pill">{row.conversionRate}</span>
                    </td>
                    <td className="friction-cell">{row.topFriction}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>

          <div className="insight-callout">
            <CheckCircle2 size={16} className="text-green" />
            <div>
              <strong>Key Growth Takeaway:</strong> Improving comparison and styling in Western Tops and Denim represents <strong>72% of the total revenue unlock</strong>.
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
