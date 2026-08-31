# Myntra Wishlist Studio — Figma Design System & Mobile UI Specification
**Project:** Myntra Growth Lab — Non-Discounted Wishlist Conversion Engine  
**Figma Component Library Version:** 2.4.0 (Mobile iOS / Android + Web Desktop UI)  
**Live Application URL:** https://myntra-growth-lab.vercel.app  
**Streamlit App URL:** https://myntranlmvp.streamlit.app  

---

## 1. Executive Design Vision

Myntra Wishlist Studio transforms passive saved item lists into an interactive decision studio. The design system is engineered around **Confidence-Driven Commerce**, providing inline spec clarity (Fabric GSM, Fit Consensus) and AI styling without distracting discount popups or banner noise.

---

## 2. Color Token Architecture

| Token Name | Hex Code | Usage & Context |
| :--- | :---: | :--- |
| **`brand-myntra-pink`** | `#FF3F6C` | Primary Action CTA, Active Badges, Logo |
| **`brand-deep-purple`** | `#2D0A4E` | Category Pill Headers, Top Stage Trackers |
| **`neutral-dark-navy`** | `#0A0D14` | Smartphone Mockup Background, Status Bar |
| **`neutral-card-bg`** | `#FFFFFF` | Primary Content Cards, Spec Comparison Cells |
| **`accent-indigo-glow`** | `#4F46E5` | Secondary Metrics, AOV Lift Callouts |
| **`status-emerald-green`** | `#10B981` | Fit Consensus High Confidence, Low Return Badges |
| **`status-amber-gold`** | `#F59E0B` | Sizing Variance Warnings, Circuit Breaker Indicators |

---

## 3. Mobile Smartphone App Layout Specifications (375px × 812px Frame)

### 3.1 Screen Frame Architecture (iOS 17 / Android 14 Frame)
- **Viewport Dimensions:** 375pt width × 812pt height (19.5:9 ratio).
- **Status Bar Height:** 44pt with battery, signal, and time indicators.
- **Top Navigation Bar:** 56pt sticky header containing Back Arrow, Search Input (`Search Myntra...`), Shopping Bag Icon, and User Profile.
- **Bottom Navigation Bar:** 64pt fixed tab bar featuring `Home`, `Categories`, `New`, `Studio`, `Account`, and `Wishlist Bag`.

### 3.2 Mobile Feature Component 1: Side-by-Side Spec & GSM Matrix
- **Header:** Sticky sub-header `WISHLIST — Comparison (2 items selected)`.
- **Product Card Column Width:** 168pt each (2-column layout).
- **Fabric Weight Row:** Highlights `Heavyweight 240 GSM` (Primary) vs `Lightweight 160 GSM` (Alternative).
- **Fit Consensus Histogram:** Visual 5-bar distribution chart displaying verified customer feedback (`88% True to Size`).
- **Buyer Photo Switcher:** Toggle pill switching between `Studio Model Photo` and `Real Buyer Photo`.
- **CTA Buttons:** Full-width 40pt high `ADD TO BAG` buttons in `#FF3F6C`.

### 3.3 Mobile Feature Component 2: AI Coordinated Outfit Coordinator
- **Layout:** Vertical card stack displaying the primary saved item paired with 2 complementary accessories/garments.
- **Outfits Offered:** `Casual Friday Look`, `Smart Evening Look`, `Weekend Streetwear`.
- **Bundle Price Card:** Shows combined item total (e.g. ₹4,397) with `0% Discount / Full Margin` badge.
- **Action Button:** 44pt high `#FF3F6C` button reading `🛍️ MOVE COMPLETE LOOK TO BAG (+₹450 AOV)`.

### 3.4 Mobile Feature Component 3: 1-Tap WhatsApp Social Voting Micro-Card
- **Card Schema:** Compact 320pt × 180pt card styled like a WhatsApp chat bubble.
- **Content:** Thumbnail images of Option A vs Option B with voting buttons `[ Vote A ]` and `[ Vote B ]`.
- **Instant AI Fallback:** 2-second timeout badge showing `⚡ 78% Community Consensus Choice` when friend reply is delayed.

---

## 4. Desktop Web Dashboard Layout Specifications (1440px Canvas)

- **Grid System:** 12-column layout, 24px gutters, 80px margins.
- **Sidebar Navigation:** 240px fixed left sidebar with brand logo, portal tab links, and live financial metrics.
- **Main Workspace:** 1120px fluid content container housing the Spec Comparison Grid, Outfit Matcher, and Sentiment Analytics charts.

---

## 5. Summary of Figma Component Assets Created
1. `Figma_Frame_Mobile_Wishlist_Spec_Matrix` (375 × 812)
2. `Figma_Frame_Mobile_AI_Outfit_Coordinator` (375 × 812)
3. `Figma_Frame_Mobile_WhatsApp_Voting_Card` (320 × 180)
4. `Figma_Frame_Desktop_Wishlist_Studio_Workspace` (1440 × 900)
