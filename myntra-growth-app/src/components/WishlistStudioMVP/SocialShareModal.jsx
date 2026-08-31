import React, { useState } from 'react';
import { Share2, CheckCircle2, MessageCircle, ThumbsUp, X, Sparkles, Copy } from 'lucide-react';

export default function SocialShareModal({ products, isOpen, onClose }) {
  const [copied, setCopied] = useState(false);
  const [votes, setVotes] = useState({ itemA: 5, itemB: 2, skip: 1 });
  const [hasVoted, setHasVoted] = useState(false);

  if (!isOpen) return null;

  const itemA = products[0];
  const itemB = products[1];

  const handleVote = (choice) => {
    if (hasVoted) return;
    setVotes((prev) => ({ ...prev, [choice]: prev[choice] + 1 }));
    setHasVoted(true);
  };

  const handleCopyLink = () => {
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  const totalVotes = votes.itemA + votes.itemB + votes.skip;
  const pctA = Math.round((votes.itemA / totalVotes) * 100);
  const pctB = Math.round((votes.itemB / totalVotes) * 100);

  return (
    <div className="modal-overlay" onClick={onClose}>
      <div className="modal-content-card" onClick={(e) => e.stopPropagation()}>
        <div className="modal-header">
          <div className="modal-title-row">
            <MessageCircle size={20} className="text-green" />
            <h3>Ask Friends: 1-Tap WhatsApp Voting Card</h3>
          </div>
          <button className="modal-close-btn" onClick={onClose}>
            <X size={18} />
          </button>
        </div>

        <p className="modal-sub">
          Share a live voting preview card directly to your WhatsApp groups. Friends can vote in 1 tap without installing the app.
        </p>

        {/* WhatsApp Preview Card */}
        <div className="whatsapp-preview-box">
          <div className="wa-header">
            <span className="wa-badge">WhatsApp Voting Link Preview</span>
            <span className="wa-status">🔴 {totalVotes} Friends Voted</span>
          </div>

          <div className="wa-items-compare-row">
            {/* Option A */}
            <div className={`wa-option-card ${votes.itemA > votes.itemB ? 'winner' : ''}`}>
              <span className="wa-opt-label">Option A</span>
              <img src={itemA.image} alt={itemA.name} className="wa-img" />
              <div className="wa-name">{itemA.name}</div>
              <div className="wa-price">₹{itemA.price}</div>
              <div className="wa-vote-bar">
                <div className="wa-vote-fill" style={{ width: `${pctA}%` }}></div>
              </div>
              <span className="wa-vote-pct">{pctA}% ({votes.itemA} votes)</span>
              <button
                className="wa-vote-btn"
                onClick={() => handleVote('itemA')}
                disabled={hasVoted}
              >
                <ThumbsUp size={13} />
                <span>Vote Option A</span>
              </button>
            </div>

            <div className="wa-vs-pill">VS</div>

            {/* Option B */}
            <div className={`wa-option-card ${votes.itemB > votes.itemA ? 'winner' : ''}`}>
              <span className="wa-opt-label">Option B</span>
              <img src={itemB.image} alt={itemB.name} className="wa-img" />
              <div className="wa-name">{itemB.name}</div>
              <div className="wa-price">₹{itemB.price}</div>
              <div className="wa-vote-bar">
                <div className="wa-vote-fill" style={{ width: `${pctB}%` }}></div>
              </div>
              <span className="wa-vote-pct">{pctB}% ({votes.itemB} votes)</span>
              <button
                className="wa-vote-btn"
                onClick={() => handleVote('itemB')}
                disabled={hasVoted}
              >
                <ThumbsUp size={13} />
                <span>Vote Option B</span>
              </button>
            </div>
          </div>

          {/* Friend Comments Simulation */}
          <div className="wa-comments-stream">
            <span className="stream-label">Live Friend Feed:</span>
            <div className="comment-bubble">
              <strong>Pooja K.:</strong> "Definitely Option A! The twill fabric is way more structured."
            </div>
            <div className="comment-bubble">
              <strong>Rahul M.:</strong> "Option A matches your white sneakers."
            </div>
          </div>
        </div>

        {/* Share Action Footer */}
        <div className="modal-footer-actions">
          <button className="copy-link-btn" onClick={handleCopyLink}>
            <Copy size={16} />
            <span>{copied ? 'Link Copied to Clipboard!' : 'Copy Voting Link'}</span>
          </button>
          <button className="share-whatsapp-btn" onClick={handleCopyLink}>
            <Share2 size={16} />
            <span>Share to WhatsApp Group</span>
          </button>
        </div>
      </div>
    </div>
  );
}
