import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# 1. Page Configuration & Title
st.set_page_config(
    page_title="Myntra Growth Lab | Wishlist Conversion Engine",
    page_icon="🛍️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS styling for Streamlit
st.markdown("""
<style>
  @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800;900&display=swap');
  html, body, [class*="css"] {
    font-family: 'Plus Jakarta Sans', sans-serif;
  }
  .stApp {
    background-color: #0A0D14;
    color: #F8FAFC;
  }
  
  /* Mobile Smartphone Frame Simulation */
  .mobile-phone-container {
    max-width: 410px;
    margin: 0 auto;
    background-color: #0A0D14;
    border: 12px solid #1E293B;
    border-radius: 36px;
    padding: 1rem;
    box-shadow: 0 20px 50px rgba(0, 0, 0, 0.6);
    color: #FFFFFF;
  }
  
  .mobile-header-bar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1px solid rgba(255, 255, 255, 0.1);
    padding-bottom: 0.5rem;
    margin-bottom: 0.75rem;
  }
  
  .mobile-brand-title {
    font-size: 1.1rem;
    font-weight: 900;
    color: #FF3F6C;
  }
  
  .spec-comparison-card {
    background-color: #FFFFFF;
    color: #0F172A;
    border-radius: 14px;
    padding: 1rem;
    margin-bottom: 1rem;
  }
  
  .badge-purple {
    background-color: #2D0A4E;
    color: #FFFFFF;
    font-size: 0.68rem;
    font-weight: 800;
    padding: 0.2rem 0.6rem;
    border-radius: 6px;
  }
  
  .badge-pink {
    background-color: rgba(255, 63, 108, 0.12);
    color: #FF3F6C;
    font-size: 0.68rem;
    font-weight: 800;
    padding: 0.2rem 0.6rem;
    border-radius: 6px;
  }
  
  /* Brand Badge */
  .myntra-brand-badge {
    font-size: 1.8rem;
    font-weight: 900;
    color: #FF3F6C;
    letter-spacing: -1.2px;
    text-align: right;
  }
</style>
""", unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.markdown("<h2 style='color:#FF3F6C;'>Myntra Growth Lab</h2>", unsafe_allow_html=True)
st.sidebar.markdown("### Wishlist Conversion Engine")

app_mode = st.sidebar.radio(
    "Select Navigation Portal:",
    [
        "🛍️ Wishlist Studio MVP (Mobile & Web Options)",
        "🔬 AI Review NLP Discovery Engine (20,250 Corpus)",
        "📊 Financial & Metric Sensitivity Simulator",
        "🎨 Figma Mobile App Design System & Wireframes"
    ]
)

st.sidebar.markdown("---")
st.sidebar.info("💡 **Capstone Growth Target:**\n30-Day Conversion 7.5% → 10.5% (+300bps) | Zero Discounts | +₹18.81 Cr/mo Profit")
st.sidebar.caption("📄 PowerPoint Deck uploaded separately as .pptx submission.")

# PORTAL 1: Wishlist Studio MVP Prototype (Mobile & Web Options)
if app_mode == "🛍️ Wishlist Studio MVP (Mobile & Web Options)":
    st.title("🛍️ Wishlist Studio MVP Prototype")
    st.caption("Live Interactive Prototype • High-Intent Shortlist Workspace")
    
    # Device Display Mode Switcher
    view_option = st.radio(
        "📱 Select View Mode Option:",
        ["📱 Mobile Smartphone App View (iOS / Android Myntra App)", "💻 Desktop Web App View"],
        horizontal=True
    )
    
    st.markdown("---")
    
    # MOBILE APP VIEW MODE
    if "Mobile" in view_option:
        st.markdown("<h3 style='text-align:center; color:#FF3F6C;'>📱 Myntra Wishlist Studio — Smartphone App View</h3>", unsafe_allow_html=True)
        st.caption("Simulating the native Myntra Mobile App wishlist evaluation workflow")
        
        # Phone Container Frame
        m_col1, m_col2, m_col3 = st.columns([0.5, 2.0, 0.5])
        with m_col2:
            st.markdown("""
            <div class="mobile-phone-container">
                <div class="mobile-header-bar">
                    <span style="font-size:0.75rem; color:#94A3B8;">9:41 📶 5G</span>
                    <span class="mobile-brand-title">myntra</span>
                    <span style="font-size:0.75rem; color:#94A3B8;">🛍️ Wishlist (38)</span>
                </div>
                <div style="background-color:#1E293B; padding:0.4rem 0.75rem; border-radius:8px; font-size:0.75rem; font-weight:700; margin-bottom:0.75rem; display:flex; justify-content:space-between;">
                    <span>Smart Folder: Workwear</span>
                    <span style="color:#FF3F6C;">Spec Matrix Active</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("#### 1. Side-by-Side Spec & GSM Matrix (Mobile)")
            
            # Mobile Product Comparison Columns
            mp1, mp2 = st.columns(2)
            with mp1:
                st.markdown("**Option A: Heavy Cargo**")
                st.image("https://images.unsplash.com/photo-1517445312882-bc9910d016b7?w=300", use_column_width=True)
                st.markdown("<span class='badge-purple'>240 GSM Heavy Cotton</span>", unsafe_allow_html=True)
                st.write("**Fit:** 88% True to Size")
                st.write("**Price:** ₹1,999 (0% Disc)")
                st.write("**Return:** 12% Low")
                if st.button("Add Option A to Bag", key="m_btn1"):
                    st.success("Option A added to bag!")
                    
            with mp2:
                st.markdown("**Option B: Poplin Cargo**")
                st.image("https://images.unsplash.com/photo-1541099649105-f69ad21f3246?w=300", use_column_width=True)
                st.markdown("<span class='badge-pink'>160 GSM Light Poplin</span>", unsafe_allow_html=True)
                st.write("**Fit:** 64% Runs Small")
                st.write("**Price:** ₹1,499 (0% Disc)")
                st.write("**Return:** 28% High Variance")
                if st.button("Add Option B to Bag", key="m_btn2"):
                    st.success("Option B added to bag!")

            st.markdown("---")
            st.markdown("#### 2. Mobile AI Look Builder (+₹450 AOV)")
            st.write("Pair selected Cargo with curated Friday complement pieces:")
            st.write("• Oversized Boxy Tee (₹899)")
            st.write("• Vintage Canvas Sneakers (₹1,499)")
            st.markdown("**Total Look Bundle:** ₹4,397")
            if st.button("🛍️ Move 3-Piece Look to Bag (Mobile)", key="m_look"):
                st.success("Complete Look moved to bag! +₹450 AOV expansion logged.")

            st.markdown("---")
            st.markdown("#### 3. Mobile WhatsApp Polling Card")
            if st.button("📱 Share Poll to WhatsApp (Mobile)", key="m_wa"):
                st.info("WhatsApp voting card sent to group!")
                st.success("Instant Fallback Triggered: **78% Community Consensus** in 2s.")

    # DESKTOP WEB VIEW MODE
    else:
        st.markdown("<h3 style='color:#FF3F6C;'>💻 Myntra Wishlist Studio — Desktop Web Workspace View</h3>", unsafe_allow_html=True)
        
        folder = st.selectbox("Occasion Smart Folder Filter:", ["All Saved Items (38)", "Workwear (12)", "Streetwear (18)", "Party (8)"])
        
        st.markdown("### 1. Side-by-Side Spec & GSM Comparison Matrix")
        
        c1, c2 = st.columns(2)
        with c1:
            st.subheader("Item 1: Heavy Streetwear Cargo")
            st.image("https://images.unsplash.com/photo-1517445312882-bc9910d016b7?w=400", width=220)
            st.write("**Fabric Weight:** 240 GSM Heavyweight Cotton")
            st.write("**Fit Consensus:** 88% True to Size")
            st.write("**Price:** ₹1,999 (Zero Discount)")
            st.write("**Return Rate:** 12% Low Returns")
            st.button("Compare Specs vs Item 2", key="w_btn1")
            
        with c2:
            st.subheader("Item 2: Poplin Relaxed Cargo")
            st.image("https://images.unsplash.com/photo-1541099649105-f69ad21f3246?w=400", width=220)
            st.write("**Fabric Weight:** 160 GSM Lightweight Poplin")
            st.write("**Fit Consensus:** 64% Runs Small")
            st.write("**Price:** ₹1,499 (Zero Discount)")
            st.write("**Return Rate:** 28% High Sizing Variance")
            st.button("Compare Specs vs Item 1", key="w_btn2")

        st.markdown("---")
        st.markdown("### 2. AI Coordinated Look Builder (+₹450 AOV Lift)")
        st.write("Pair selected Heavy Cargo (₹1,999) with curated complement pieces:")
        st.write("• Oversized Boxy Tee (₹899)")
        st.write("• Vintage Canvas Sneakers (₹1,499)")
        st.markdown("**Total Look Bundle Price:** ₹4,397 (0% Margin Dilution)")
        if st.button("🛍️ Move Complete 3-Piece Look to Bag"):
            st.success("Complete Friday Look moved to bag! +₹450 AOV expansion logged.")

        st.markdown("---")
        st.markdown("### 3. 1-Tap WhatsApp Voting Micro-Card")
        if st.button("📱 Share Voting Card to WhatsApp"):
            st.info("WhatsApp micro-card generated! Link created for group polling.")
            st.success("Instant Fallback Triggered: **78% Community Choice** verified in 2 seconds.")

# PORTAL 2: AI Review NLP Discovery Engine
elif app_mode == "🔬 AI Review NLP Discovery Engine (20,250 Corpus)":
    st.title("🔬 AI Review NLP Discovery Engine")
    st.caption("Corpus: Sourced 20,250 Verified Buyer Reviews Across Top 5 Apparel Categories")
    
    st.markdown("### Search & Synthesize Sentiment Clusters")
    query = st.text_input("Enter Product Keyword or Friction Query:", "fabric thickness cargos sizing")
    
    if query:
        st.write(f"Parsing NLP Corpus for query: **'{query}'**...")
        
        # Donut Chart for Sentiment Breakdown
        df_chart = pd.DataFrame({
            "Cluster": ["Positive Delights (Delivery/Variety)", "Neutral Feature Requests (GSM/Pairing)", "Negative Frictions (Sizing/Fabric Ambiguity)"],
            "Volume": [8100, 6075, 6075]
        })
        fig = px.pie(df_chart, values="Volume", names="Cluster", title="20,250 Review Sentiment Corpus Distribution", hole=0.4)
        st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("### Top Synthesized Barrier Buckets")
        st.warning("1. **Comparison Overload (35% NLP / 88.9% Survey):** Users save 3.8 alternatives per sub-category and stall due to hidden GSM weight.")
        st.warning("2. **Styling Isolation (28% NLP / 77.8% Survey):** Hesitation caused by uncertainty on how to pair standalone pieces.")
        st.warning("3. **WhatsApp Reply Latency (66.6% Survey):** Screenshot sharing causes 18-hour delay and loss of buying impulse.")

# PORTAL 3: Financial & Metric Sensitivity Simulator
elif app_mode == "📊 Financial & Metric Sensitivity Simulator":
    st.title("📊 Financial & Metric Sensitivity Simulator")
    st.caption("Interactive Opportunity Sizing & Unit Economics Stress-Test Model")
    
    st.markdown("### Adjust Key Growth Levers")
    col_l1, col_l2 = st.columns(2)
    with col_l1:
        mau = st.slider("Active Wishlist MAU:", 5000000, 15000000, 10000000, 1000000)
        baseline_conv = st.slider("Baseline 30-Day Conversion Rate (%):", 5.0, 10.0, 7.5, 0.5)
        target_lift_bps = st.slider("Target Conversion Lift (bps):", 50, 400, 300, 25)
    with col_l2:
        aov = st.slider("Average Order Value (AOV in ₹):", 1200, 2500, 1650, 50)
        margin = st.slider("Platform Gross Margin (%):", 30, 50, 38, 1)
        infra_cost_monthly = st.slider("Monthly Tech Infra Cost (₹ Lakh):", 5.0, 20.0, 8.5, 0.5)
        
    # Calculate Outputs
    target_conv = baseline_conv + (target_lift_bps / 100)
    baseline_revenue = (mau * (baseline_conv / 100) * aov) / 10000000
    target_revenue = (mau * (target_conv / 100) * aov) / 10000000
    incremental_gmv = target_revenue - baseline_revenue
    monthly_gross_profit = incremental_gmv * (margin / 100)
    annual_gross_profit = monthly_gross_profit * 12
    annual_infra = (infra_cost_monthly * 12) / 100
    roi = annual_gross_profit / annual_infra if annual_infra > 0 else 0
    payback_days = (infra_cost_monthly / monthly_gross_profit) * 30 if monthly_gross_profit > 0 else 0
    
    st.markdown("---")
    st.markdown("### Simulated Financial Impact")
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Target Conversion Rate", f"{target_conv:.2f}%", f"+{target_lift_bps} bps")
    m2.metric("Monthly Incremental GMV", f"₹{incremental_gmv:.2f} Cr", f"+₹{incremental_gmv*12:.1f} Cr / yr")
    m3.metric("Monthly Gross Profit Unlock", f"₹{monthly_gross_profit:.2f} Cr", f"At {margin}% Margin")
    m4.metric("Feature ROI", f"{roi:.0f}x ROI", f"Payback < {payback_days:.1f} Days")

    st.markdown("---")
    st.markdown("### Financial Sensitivity Matrix")
    df_sens_table = pd.DataFrame([
        {"Scenario": "Base Case (100% Target Lift)", "Lift (bps)": "+300 bps", "Monthly Profit": f"₹{monthly_gross_profit:.2f} Cr", "Annual Value": f"₹{annual_gross_profit:.1f} Cr", "Feature ROI": f"{roi:.0f}x", "Payback": f"{payback_days:.1f} Days"},
        {"Scenario": "Conservative Case (75% Lift)", "Lift (bps)": f"+{int(target_lift_bps*0.75)} bps", "Monthly Profit": f"₹{monthly_gross_profit*0.75:.2f} Cr", "Annual Value": f"₹{annual_gross_profit*0.75:.1f} Cr", "Feature ROI": f"{roi*0.75:.0f}x", "Payback": f"{payback_days/0.75:.1f} Days"},
        {"Scenario": "Stress-Test Case (50% Lift)", "Lift (bps)": f"+{int(target_lift_bps*0.50)} bps", "Monthly Profit": f"₹{monthly_gross_profit*0.50:.2f} Cr", "Annual Value": f"₹{annual_gross_profit*0.50:.1f} Cr", "Feature ROI": f"{roi*0.50:.0f}x", "Payback": f"{payback_days/0.50:.1f} Days"},
    ])
    st.table(df_sens_table)

# PORTAL 4: Figma Design System & Wireframes
else:
    st.title("🎨 Figma Mobile App Design System & Wireframes")
    st.caption("Component Tokens, Mobile Smartphone Layout Specs & Figma Guidelines")
    
    st.markdown("### 1. Mobile App UI Design Mockup (Side-by-Side Spec Matrix)")
    
    # Try displaying local generated image
    try:
        st.image("myntra-growth-app/public/myntra_mobile_spec_matrix.jpg", caption="Figma Mobile UI Screen: Wishlist Side-by-Side Spec Matrix (240 GSM vs 160 GSM)", width=380)
    except:
        st.info("Mobile Spec Matrix UI Mockup generated.")

    st.markdown("---")
    st.markdown("### 2. Design System Color Tokens")
    
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown("**`brand-myntra-pink`**")
        st.markdown("<div style='background-color:#FF3F6C; height:50px; border-radius:8px;'></div>", unsafe_allow_html=True)
        st.caption("#FF3F6C • Primary CTA")
    with c2:
        st.markdown("**`brand-deep-purple`**")
        st.markdown("<div style='background-color:#2D0A4E; height:50px; border-radius:8px;'></div>", unsafe_allow_html=True)
        st.caption("#2D0A4E • Pill Banners")
    with c3:
        st.markdown("**`accent-indigo-glow`**")
        st.markdown("<div style='background-color:#4F46E5; height:50px; border-radius:8px;'></div>", unsafe_allow_html=True)
        st.caption("#4F46E5 • Subtitles & AOV")
    with c4:
        st.markdown("**`status-emerald-green`**")
        st.markdown("<div style='background-color:#10B981; height:50px; border-radius:8px;'></div>", unsafe_allow_html=True)
        st.caption("#10B981 • Fit Consensus")

    st.markdown("---")
    st.markdown("### 3. Complete Figma Design Document")
    st.markdown("View full design specification file: [`FIGMA_DESIGN_SYSTEM.md`](https://github.com/akhyashukla03/myntra/blob/main/FIGMA_DESIGN_SYSTEM.md)")
