import streamlit as st
import pandas as pd
import plotly.express as px
import os

# 1. Page Configuration
st.set_page_config(
    page_title="Myntra Growth Lab | Wishlist Conversion Engine",
    page_icon="🛍️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom Styling for Streamlit App
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
  
  /* Hide sidebar if collapsed */
  [data-testid="stSidebar"] {
    display: none !important;
  }
  
  /* Brand Top Banner */
  .brand-header-box {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background: linear-gradient(135deg, #1E1B4B 0%, #0F172A 100%);
    border: 1px solid rgba(255, 63, 108, 0.3);
    padding: 1rem 1.75rem;
    border-radius: 16px;
    margin-bottom: 1.25rem;
  }
  
  .brand-logo-main {
    font-size: 1.8rem;
    font-weight: 900;
    color: #FF3F6C;
    letter-spacing: -0.8px;
  }
  
  .brand-subtitle-badge {
    background: #2D0A4E;
    color: #FFFFFF;
    font-size: 0.72rem;
    font-weight: 800;
    padding: 0.3rem 0.85rem;
    border-radius: 9999px;
    text-transform: uppercase;
  }

  /* Smartphone Mockup Container */
  .phone-mockup-wrapper {
    max-width: 440px;
    margin: 1rem auto;
    background-color: #0A0D14;
    border: 14px solid #1E293B;
    border-radius: 40px;
    padding: 1.25rem;
    box-shadow: 0 25px 60px rgba(0, 0, 0, 0.7);
    color: #FFFFFF;
  }
  
  .phone-header-strip {
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1px solid rgba(255, 255, 255, 0.1);
    padding-bottom: 0.5rem;
    margin-bottom: 0.75rem;
  }

  .badge-purple {
    background-color: #2D0A4E;
    color: #FFFFFF;
    font-size: 0.72rem;
    font-weight: 800;
    padding: 0.25rem 0.65rem;
    border-radius: 6px;
  }
  
  .badge-pink {
    background-color: rgba(255, 63, 108, 0.15);
    color: #FF3F6C;
    font-size: 0.72rem;
    font-weight: 800;
    padding: 0.25rem 0.65rem;
    border-radius: 6px;
  }
</style>
""", unsafe_allow_html=True)

# Helper function to check for image files
def get_image_path(filename):
    paths = [
        filename,
        os.path.join("myntra-growth-app", "public", filename),
        os.path.join("public", filename)
    ]
    for p in paths:
        if os.path.exists(p):
            return p
    return None

# Brand Top Header
st.markdown("""
<div class="brand-header-box">
    <div>
        <span class="brand-logo-main">myntra</span>
        <span style="font-size:1.25rem; font-weight:800; color:#FFFFFF; margin-left:0.5rem;">Growth Lab</span>
        <div style="font-size:0.85rem; color:#CBD5E1; margin-top:0.2rem;">
            Wishlist Conversion Engine — Target: 30-Day Conversion 7.5% → 10.5% (+300bps) | Zero Discounts
        </div>
    </div>
    <div>
        <span class="brand-subtitle-badge">+₹18.81 Cr / mo Profit Lift</span>
    </div>
</div>
""", unsafe_allow_html=True)

# Top Native Streamlit Navigation Tabs
tab_mvp, tab_nlp, tab_metrics, tab_figma = st.tabs([
    "🛍️ Wishlist Studio MVP Solution",
    "🔬 AI Review NLP Discovery Engine (20,250 Corpus)",
    "📊 Financial & Metric Sensitivity Simulator",
    "🎨 Figma Mobile App Design System & Wireframes"
])

# Initialize session state for interactive bag cart
if 'cart_count' not in st.session_state:
    st.session_state.cart_count = 1
if 'toast_msg' not in st.session_state:
    st.session_state.toast_msg = ''

# TAB 1: WISHLIST STUDIO MVP SOLUTION
with tab_mvp:
    st.title("🛍️ Wishlist Studio MVP Prototype")
    st.caption("High-Intent Shortlist Workspace • Resolves Spec Ambiguity, Styling Doubt & Friend Latency")
    
    # View Mode Radio Options (Mobile vs Desktop)
    mvp_view_mode = st.radio(
        "Select Interface View Option:",
        ["📱 Mobile Smartphone App View (iOS / Android)", "💻 Desktop Web Workspace View"],
        horizontal=True
    )
    
    st.markdown("---")

    # Product Dataset Definition
    prod_a = {
        "id": "p1", "name": "Heavy Streetwear Cargo Pants", "brand": "Roadster", "price": 1999, "mrp": 2499,
        "gsm": "240 GSM Heavyweight Cotton Twill", "fit": "88% True to Size (Relaxed Fit)", "return": "12% Low Returns",
        "img": "https://images.unsplash.com/photo-1517445312882-bc9910d016b7?w=400"
    }
    prod_b = {
        "id": "p2", "name": "Poplin Relaxed Cargo Pants", "brand": "Wrong", "price": 1499, "mrp": 2999,
        "gsm": "160 GSM Lightweight Poplin", "fit": "64% Runs Small (Tight Waist)", "return": "28% High Sizing Variance",
        "img": "https://images.unsplash.com/photo-1541099649105-f69ad21f3246?w=400"
    }

    # MOBILE APP VIEW MODE
    if "Mobile" in mvp_view_mode:
        st.markdown("<h3 style='text-align:center; color:#FF3F6C;'>📱 Native Myntra Mobile App Interface</h3>", unsafe_allow_html=True)
        st.caption("Formated inside native 375pt × 812pt Smartphone Frame Architecture")
        
        col_m1, col_m2, col_m3 = st.columns([0.4, 2.2, 0.4])
        with col_m2:
            st.markdown(f"""
            <div class="phone-mockup-wrapper">
                <div class="phone-header-strip">
                    <span style="font-size:0.75rem; color:#94A3B8;">9:41 📶 5G</span>
                    <span style="font-size:1.1rem; font-weight:900; color:#FF3F6C;">myntra</span>
                    <span style="font-size:0.75rem; color:#94A3B8;">🛍️ Bag ({st.session_state.cart_count})</span>
                </div>
                <div style="background-color:#1E293B; padding:0.45rem 0.75rem; border-radius:8px; font-size:0.78rem; font-weight:700; margin-bottom:0.75rem; display:flex; justify-content:space-between;">
                    <span>Folder: Workwear</span>
                    <span style="color:#FF3F6C;">Spec Matrix Active</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            # Show high-resolution Figma mockup if present
            mock_img = get_image_path("myntra_mobile_spec_matrix.jpg")
            if mock_img:
                st.image(mock_img, caption="Mobile Spec Matrix Screenshot (240 GSM vs 160 GSM)", use_container_width=True)
                
            st.markdown("#### 1. Side-by-Side Spec & GSM Matrix")
            m_col1, m_col2 = st.columns(2)
            with m_col1:
                st.write(f"**{prod_a['name']}**")
                st.image(prod_a['img'], use_container_width=True)
                st.markdown("<span class='badge-purple'>240 GSM Heavy Cotton</span>", unsafe_allow_html=True)
                st.caption(f"Fit: {prod_a['fit']}")
                st.write(f"**Price:** ₹{prod_a['price']}")
                if st.button("Move Option A to Bag", key="m_add_a"):
                    st.session_state.cart_count += 1
                    st.success("✓ Option A added to Bag!")

            with m_col2:
                st.write(f"**{prod_b['name']}**")
                st.image(prod_b['img'], use_container_width=True)
                st.markdown("<span class='badge-pink'>160 GSM Light Poplin</span>", unsafe_allow_html=True)
                st.caption(f"Fit: {prod_b['fit']}")
                st.write(f"**Price:** ₹{prod_b['price']}")
                if st.button("Move Option B to Bag", key="m_add_b"):
                    st.session_state.cart_count += 1
                    st.success("✓ Option B added to Bag!")

            st.markdown("---")
            st.markdown("#### 2. AI Coordinated Look Builder (+₹450 AOV)")
            st.write("Pair selected Heavy Cargo (₹1,999) with curated Friday complement pieces:")
            st.write("• Oversized Boxy Tee (₹899)")
            st.write("• Vintage Canvas Sneakers (₹1,499)")
            st.markdown("**Total Look Bundle Price:** ₹4,397 (0% Discount)")
            if st.button("🛍️ Move 3-Piece Look to Bag (Mobile)", key="m_bundle"):
                st.session_state.cart_count += 3
                st.success("✨ Complete 3-Piece Friday Look added to Bag! +₹450 AOV logged.")

            st.markdown("---")
            st.markdown("#### 3. 1-Tap WhatsApp Voting Card")
            if st.button("📱 Share Poll to WhatsApp (Mobile)", key="m_wa_share"):
                st.info("WhatsApp poll card sent to group!")
                st.success("Instant Fallback Triggered: **78% Community Consensus** in 2 seconds.")

    # DESKTOP WEB WORKSPACE VIEW MODE
    else:
        st.markdown("<h3 style='color:#FF3F6C;'>💻 Myntra Wishlist Studio — Desktop Web Workspace</h3>", unsafe_allow_html=True)
        
        folder = st.selectbox("Occasion Smart Folder Filter:", ["All Saved Items (38)", "Workwear (12)", "Streetwear (18)", "Party (8)"])
        
        st.markdown("### 1. Side-by-Side Spec & GSM Matrix")
        
        d_c1, d_c2 = st.columns(2)
        with d_c1:
            st.subheader(f"Option A: {prod_a['name']}")
            st.image(prod_a['img'], width=240)
            st.markdown("<span class='badge-purple'>240 GSM Heavyweight Cotton</span>", unsafe_allow_html=True)
            st.write(f"**Verified Fit Consensus:** {prod_a['fit']}")
            st.write(f"**Price:** ₹{prod_a['price']} (MRP: ₹{prod_a['mrp']})")
            st.write(f"**Return Risk:** {prod_a['return']}")
            if st.button("🛍️ Move Option A to Bag", key="d_add_a"):
                st.session_state.cart_count += 1
                st.success("✓ Option A added to Bag!")

        with d_c2:
            st.subheader(f"Option B: {prod_b['name']}")
            st.image(prod_b['img'], width=240)
            st.markdown("<span class='badge-pink'>160 GSM Lightweight Poplin</span>", unsafe_allow_html=True)
            st.write(f"**Verified Fit Consensus:** {prod_b['fit']}")
            st.write(f"**Price:** ₹{prod_b['price']} (MRP: ₹{prod_b['mrp']})")
            st.write(f"**Return Risk:** {prod_b['return']}")
            if st.button("🛍️ Move Option B to Bag", key="d_add_b"):
                st.session_state.cart_count += 1
                st.success("✓ Option B added to Bag!")

        st.markdown("---")
        st.markdown("### 2. AI Coordinated Look Builder (+₹450 AOV Expansion)")
        st.write("Pair selected Heavy Cargo (₹1,999) with curated complement pieces:")
        st.write("• Oversized Boxy Tee (₹899)")
        st.write("• Vintage Canvas Sneakers (₹1,499)")
        st.markdown("**Total Look Bundle Price:** ₹4,397 (0% Margin Erosion)")
        if st.button("🛍️ Move Complete 3-Piece Look to Bag", key="d_bundle"):
            st.session_state.cart_count += 3
            st.success("✨ Complete 3-Piece Look added to Bag! +₹450 AOV expansion logged.")

        st.markdown("---")
        st.markdown("### 3. 1-Tap WhatsApp Voting Micro-Card")
        if st.button("📱 Share Voting Card to WhatsApp", key="d_wa_share"):
            st.info("WhatsApp micro-card generated! Link created for group polling.")
            st.success("Instant Fallback Triggered: **78% Community Choice** verified in 2 seconds.")

# TAB 2: AI REVIEW NLP DISCOVERY ENGINE
with tab_nlp:
    st.title("🔬 AI Review NLP Discovery Engine")
    st.caption("Corpus: Sourced 20,250 Verified Buyer Reviews Across Top 5 Apparel Categories")
    
    query = st.text_input("Enter Product Keyword or Friction Query:", "fabric thickness cargos sizing")
    
    if query:
        st.write(f"Parsing NLP Corpus for query: **'{query}'**...")
        
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

# TAB 3: FINANCIAL & METRIC SIMULATOR
with tab_metrics:
    st.title("📊 Financial & Metric Sensitivity Simulator")
    st.caption("Interactive Opportunity Sizing & Unit Economics Stress-Test Model")
    
    col_l1, col_l2 = st.columns(2)
    with col_l1:
        mau = st.slider("Active Wishlist MAU:", 5000000, 15000000, 10000000, 1000000)
        baseline_conv = st.slider("Baseline 30-Day Conversion Rate (%):", 5.0, 10.0, 7.5, 0.5)
        target_lift_bps = st.slider("Target Conversion Lift (bps):", 50, 400, 300, 25)
    with col_l2:
        aov = st.slider("Average Order Value (AOV in ₹):", 1200, 2500, 1650, 50)
        margin = st.slider("Platform Gross Margin (%):", 30, 50, 38, 1)
        infra_cost_monthly = st.slider("Monthly Tech Infra Cost (₹ Lakh):", 5.0, 20.0, 8.5, 0.5)
        
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

# TAB 4: FIGMA DESIGN SYSTEM & WIREFRAMES
with tab_figma:
    st.title("🎨 Figma Mobile App Design System & Wireframes")
    st.caption("Component Tokens, Mobile Smartphone Layout Specs & Figma Guidelines")
    
    mock_img = get_image_path("myntra_mobile_spec_matrix.jpg")
    if mock_img:
        st.image(mock_img, caption="Figma Mobile UI Screen: Wishlist Side-by-Side Spec Matrix (240 GSM vs 160 GSM)", width=420)
    else:
        st.info("Mobile Spec Matrix UI Mockup ready.")

    st.markdown("---")
    st.markdown("### Design System Color Tokens")
    
    fc1, fc2, fc3, fc4 = st.columns(4)
    with fc1:
        st.markdown("**`brand-myntra-pink`**")
        st.markdown("<div style='background-color:#FF3F6C; height:50px; border-radius:8px;'></div>", unsafe_allow_html=True)
        st.caption("#FF3F6C • Primary CTA")
    with fc2:
        st.markdown("**`brand-deep-purple`**")
        st.markdown("<div style='background-color:#2D0A4E; height:50px; border-radius:8px;'></div>", unsafe_allow_html=True)
        st.caption("#2D0A4E • Pill Banners")
    with fc3:
        st.markdown("**`accent-indigo-glow`**")
        st.markdown("<div style='background-color:#4F46E5; height:50px; border-radius:8px;'></div>", unsafe_allow_html=True)
        st.caption("#4F46E5 • Subtitles & AOV")
    with fc4:
        st.markdown("**`status-emerald-green`**")
        st.markdown("<div style='background-color:#10B981; height:50px; border-radius:8px;'></div>", unsafe_allow_html=True)
        st.caption("#10B981 • Fit Consensus")

    st.markdown("---")
    st.markdown("### Complete Figma Design Document")
    st.markdown("View full design specification file: [`FIGMA_DESIGN_SYSTEM.md`](https://github.com/akhyashukla03/myntra/blob/main/FIGMA_DESIGN_SYSTEM.md)")
