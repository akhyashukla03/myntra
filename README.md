# Myntra Wishlist Studio — Non-Discounted Conversion Engine
### *Product Management & Growth Capstone Project (10-Slide Pitch Deck + Deployed Streamlit/React App)*

[![Live Streamlit App](https://img.shields.io/badge/Live_Streamlit_App-Streamlit_Cloud-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://myntra-growth-lab.streamlit.app)
[![Live Deployed Prototype](https://img.shields.io/badge/Live_React_MVP-Vercel_Deploy-000000?style=for-the-badge&logo=vercel&logoColor=white)](https://myntra-growth-lab.vercel.app)
[![PowerPoint Deck](https://img.shields.io/badge/Executive_Deck-16:9_PowerPoint-B7472A?style=for-the-badge&logo=microsoftpowerpoint&logoColor=white)](./Myntra_Wishlist_Studio_10_Slide_Deck.pptx)
[![Python 3.11](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![React 18](https://img.shields.io/badge/React-18.2.0-61DAFB?style=for-the-badge&logo=react&logoColor=black)](https://reactjs.org)

---

## 📌 Executive Summary

**Myntra Wishlist Studio** is a trust-led growth engine designed to convert high-intent, dormant wishlisted items into completed purchases without offering any margin-eroding discount coupons or promotional subsidies. 

### 🎯 Key Outcomes & Impact
* **North Star Target:** Lift 30-day Wishlist-to-Purchase Conversion Rate from **7.5% to 10.5% (+300 bps)** in 12 months.
* **Volume Delta:** Unlocks **+300,000 incremental buyers / month** at an Average Order Value (AOV) of **₹1,650**.
* **Monthly GMV Expansion:** **+₹49.5 Cr / month** incremental GMV (+₹594 Cr / year).
* **Net Gross Profit Lift:** **+₹18.81 Cr / month** (at 38% platform gross margin).
* **Logistics Savings:** **+₹73.5 Lakh / month** saved by reducing sizing returns from 24% to ≤18%.
* **Unit Economics ROI:** **221x Feature ROI** (annual net value of ₹234.5 Cr vs tech infra cost of ₹1.02 Cr/year) with a payback period under **4 days**.

---

## 🛠️ Repository Architecture & Deliverables

```
├── app.py                                  # Master Streamlit Web App (Deck, MVP, NLP Engine, Financial Simulator)
├── generate_pptx.py                        # Python script generating 16:9 PowerPoint presentation
├── data_pptx.py                            # Structured slide dataset for PPTX generator
├── Myntra_Wishlist_Studio_10_Slide_Deck.pptx# Executive 10-Slide PowerPoint Presentation
├── COMPREHENSIVE_PROBLEM_AND_MVP_SOLUTION_REVIEW.md # Self-contained PM Master Review Document
├── requirements.txt                        # Python dependencies for Streamlit Cloud deployment
├── .gitignore                              # Git ignore rules for Node, Python, and build outputs
├── LICENSE                                 # MIT Open-Source License
├── myntra-growth-app/                      # Full React 18 + Vite Web Application
│   ├── src/
│   │   ├── components/
│   │   │   ├── PitchDeck/SlideDeckViewer.jsx # Interactive 16:9 Slide Canvas Viewer
│   │   │   ├── WishlistStudioMVP/           # Side-by-Side Spec Matrix, AI Looks, WhatsApp Polling
│   │   │   ├── DiscoveryEngine/            # 20,250 Review NLP Sentiment Clustering Console
│   │   │   └── GrowthSimulator/            # Financial & Metric Sensitivity Calculator
│   │   └── data/slideDeckData.js           # Master slide deck dataset
└── plans/                                  # Modular Strategy & Technical Specs (01_ to 08_)
```

---

## 🚀 Quick Start & Local Execution

### 1. Launch Interactive Streamlit App
Make sure Python 3.11+ is installed, then run:

```bash
# Install Python dependencies
pip install -r requirements.txt

# Launch Streamlit Application
streamlit run app.py
```
> Access local Streamlit dashboard at: `http://localhost:8501`

### 2. Launch React MVP Application
```bash
cd myntra-growth-app

# Install Node dependencies
npm install

# Start Vite Development Server
npm run dev
```
> Access local React application at: `http://localhost:5173`

### 3. Regenerate PowerPoint (`.pptx`) Presentation
```bash
python generate_pptx.py
```
> Generates `Myntra_Wishlist_Studio_10_Slide_Deck.pptx` in the root folder.

---

## 🌐 One-Click Public Cloud Deployment

### Deploying to Streamlit Community Cloud (Free)
1. Fork or push this repository to **GitHub**.
2. Go to **[share.streamlit.io](https://share.streamlit.io)** and log in with GitHub.
3. Click **"New App"** → Select your repository → Set **Main file path** to `app.py`.
4. Click **Deploy!** (App goes live at `https://myntra-growth-lab.streamlit.app`).

### Deploying to Vercel (React Frontend)
1. Install Vercel CLI: `npm i -g vercel`.
2. Navigate to `myntra-growth-app/` and run `vercel`.
3. Select default settings to publish live at `https://myntra-growth-lab.vercel.app`.

---

## 📊 10-Slide Deck Overview (Zepto Capstone Layout)

| Slide | Track | Core Theme & Executive Focus |
| :---: | :--- | :--- |
| **1** | **Context** | Strategic brief, PM scope, zero-discount mandate, +₹18.81 Cr/mo profit model. |
| **2** | **Market** | Evaluation blind spots, choice paralysis, 35% fabric GSM ambiguity, WhatsApp delay. |
| **3** | **Research** | **Thinking Evolution Narrative**: Hypothesis → 20,250 Review NLP → N=9 Interview Pivot. |
| **4** | **Insights** | Gen-Z & Millennial persona (Ananya & Rahul), authentic interview verbatims, JTBD framework. |
| **5** | **Canvas** | **Financial Sensitivity Matrix**: Base Case (221x ROI) vs 50% Stress Test (110x ROI). |
| **6** | **Ideation** | Proprietary Spec Knowledge Graph moat vs copiable promo coupons; 3 RICE Horizons. |
| **7** | **MVP** | **Interactive Wireframe Showcase**: Side-by-Side Spec Matrix, AI Outfits, WhatsApp Polling. |
| **8** | **Architecture** | **4-Stage User Emotion Journey** (Confused → Confident) + 4-Layer System Stack SLAs. |
| **9** | **Metrics** | **Visual Metric Hierarchy Tree** + 200,000-User Randomized Controlled Trial (RCT) setup. |
| **10** | **GTM** | 4-Phase GTM rollout roadmap + 60-second automated circuit breaker safeguards. |

---

## 🛡️ Operational Guardrails & Automated Circuit Breakers

* **Return Rate Guardrail:** If product returns spike above **> 24%** over a 72-hour window, the feature flag automatically rolls back the comparison matrix.
* **API Latency Guardrail:** If p95 API response time exceeds **> 800ms** for 15 minutes, styling queries fall back to static pre-computed look caches.
* **Primary Adoption Safeguard:** If Spec Matrix adoption falls below **< 15% at Day 30**, attribute comparison rules trigger an automated redesign.

---

## 📜 License
This project is licensed under the MIT License — see the [LICENSE](./LICENSE) file for details.
