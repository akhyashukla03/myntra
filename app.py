import streamlit as st
import pandas as pd
import plotly.express as px
import os
import random

# 1. Page Configuration (Streamlit Collapsed Sidebar)
st.set_page_config(
    page_title="Myntra Wishlist Studio MVP",
    page_icon="🛍️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom Styling for Authentic Myntra Look & Feel
st.markdown("""
<style>
  @import url('https://fonts.googleapis.com/css2?family=Assistant:wght@400;600;700;800&display=swap');
  
  html, body, [class*="css"] {
    font-family: 'Assistant', sans-serif;
  }
  
  .stApp {
    background-color: #0F1117;
    color: #FFFFFF;
  }
  
  /* Hide sidebar */
  [data-testid="stSidebar"] {
    display: none !important;
  }

  /* Authentic Myntra Top Header Bar */
  .myntra-header-bar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background-color: #181B26;
    border-bottom: 2px solid #FF3F6C;
    padding: 0.85rem 2rem;
    border-radius: 12px;
    margin-bottom: 1.5rem;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.4);
  }
  
  .myntra-logo-box {
    display: flex;
    align-items: center;
    gap: 0.75rem;
  }
  
  .myntra-m-badge {
    background: linear-gradient(135deg, #FF3F6C 0%, #FF527B 100%);
    color: #FFFFFF;
    font-weight: 900;
    font-size: 1.6rem;
    width: 42px;
    height: 42px;
    border-radius: 10px;
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 0 4px 12px rgba(255, 63, 108, 0.4);
  }
  
  .myntra-logo-text {
    font-size: 1.8rem;
    font-weight: 900;
    color: #FF3F6C;
    letter-spacing: -0.5px;
  }

  .myntra-tagline-text {
    font-size: 0.85rem;
    color: #94A3B8;
    font-weight: 700;
  }
  
  .myntra-nav-right {
    display: flex;
    align-items: center;
    gap: 1rem;
  }
  
  .myntra-bag-btn {
    background: #FF3F6C;
    color: #FFFFFF;
    font-weight: 800;
    padding: 0.45rem 1.15rem;
    border-radius: 8px;
    font-size: 0.85rem;
    border: none;
  }

  /* Native Mobile iPhone Device Wrapper */
  .mobile-phone-frame {
    max-width: 390px;
    margin: 1rem auto;
    background-color: #121520;
    border: 12px solid #232838;
    border-radius: 44px;
    padding: 1.1rem;
    box-shadow: 0 25px 50px rgba(0, 0, 0, 0.8);
    position: relative;
  }

  .mobile-notch {
    width: 130px;
    height: 18px;
    background-color: #232838;
    border-bottom-left-radius: 14px;
    border-bottom-right-radius: 14px;
    margin: -1.1rem auto 0.75rem auto;
  }

  .mobile-status-strip {
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 0.72rem;
    font-weight: 800;
    color: #94A3B8;
    margin-bottom: 0.65rem;
    border-bottom: 1px solid rgba(255, 255, 255, 0.08);
    padding-bottom: 0.4rem;
  }
  
  /* Authentic Myntra Product Card */
  .myntra-prod-card {
    background-color: #181B26;
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 12px;
    padding: 0.75rem;
    margin-bottom: 1rem;
  }
  
  .myntra-brand-title {
    font-size: 0.75rem;
    font-weight: 900;
    color: #94A3B8;
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }
  
  .myntra-prod-name {
    font-size: 0.88rem;
    font-weight: 700;
    color: #FFFFFF;
    margin: 0.15rem 0 0.4rem 0;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }
  
  .myntra-price-row {
    display: flex;
    align-items: center;
    gap: 0.45rem;
    margin-bottom: 0.4rem;
  }
  
  .price-current {
    font-size: 0.95rem;
    font-weight: 800;
    color: #FFFFFF;
  }
  
  .price-mrp {
    font-size: 0.78rem;
    color: #64748B;
    text-decoration: line-through;
  }
  
  .price-discount {
    font-size: 0.72rem;
    font-weight: 800;
    color: #FF527B;
  }

  .gsm-chip {
    background-color: #2D0A4E;
    color: #D8B4FE;
    font-size: 0.68rem;
    font-weight: 800;
    padding: 0.2rem 0.5rem;
    border-radius: 6px;
    display: inline-block;
  }
  
  .fit-chip {
    background-color: rgba(3, 166, 133, 0.15);
    color: #03A685;
    font-size: 0.68rem;
    font-weight: 800;
    padding: 0.2rem 0.5rem;
    border-radius: 6px;
    display: inline-block;
  }
</style>
""", unsafe_allow_html=True)

# Master Dataset (6 Authentic Myntra Wishlist Items)
PRODUCTS = [
    {
        "id": "p1", "name": "Heavy Streetwear Cargo Pants", "brand": "ROADSTER", "price": 1999, "mrp": 2499,
        "gsm": "240 GSM Heavy Cotton Twill", "fit": "88% True to Size", "return": "12% Low Returns",
        "img": "https://images.unsplash.com/photo-1517445312882-bc9910d016b7?w=400", "cat": "Workwear"
    },
    {
        "id": "p2", "name": "Poplin Relaxed Cargo Pants", "brand": "WROGN", "price": 1499, "mrp": 2999,
        "gsm": "160 GSM Light Poplin", "fit": "64% Runs Small", "return": "28% High Sizing Variance",
        "img": "https://images.unsplash.com/photo-1541099649105-f69ad21f3246?w=400", "cat": "Workwear"
    },
    {
        "id": "p3", "name": "Structured Linen Blend Blazer", "brand": "MANGO", "price": 3490, "mrp": 4990,
        "gsm": "210 GSM Pure Italian Linen", "fit": "92% True to Size", "return": "9% Low Returns",
        "img": "https://images.unsplash.com/photo-1591047139829-d91aecb6caea?w=400", "cat": "Party"
    },
    {
        "id": "p4", "name": "Oversized Graphic Cotton Tee", "brand": "H&M", "price": 899, "mrp": 1299,
        "gsm": "220 GSM Bio-Washed Cotton", "fit": "84% True to Size", "return": "10% Low Returns",
        "img": "https://images.unsplash.com/photo-1521572267360-ee0c2909d518?w=400", "cat": "Streetwear"
    },
    {
        "id": "p5", "name": "Classic Raw Denim Jacket", "brand": "LEVI'S", "price": 4299, "mrp": 5999,
        "gsm": "320 GSM Rigid Denim", "fit": "90% True to Size", "return": "11% Low Returns",
        "img": "https://images.unsplash.com/photo-1576995853123-5a10305d93c0?w=400", "cat": "Streetwear"
    },
    {
        "id": "p6", "name": "Slim Fit Stretch Chinos", "brand": "JACK & JONES", "price": 2199, "mrp": 2999,
        "gsm": "190 GSM Cotton Twill", "fit": "78% True to Size", "return": "15% Moderate Variance",
        "img": "https://images.unsplash.com/photo-1473966968600-fa801b869a1a?w=400", "cat": "Workwear"
    }
]

# Session State Initialization
if 'cart_items' not in st.session_state:
    st.session_state.cart_items = [PRODUCTS[0]]
if 'compared_ids' not in st.session_state:
    st.session_state.compared_ids = ["p1", "p2"]
if 'wa_poll_active' not in st.session_state:
    st.session_state.wa_poll_active = False

# Authentic Myntra Header Banner
st.markdown("""
<div class="myntra-header-bar">
    <div class="myntra-logo-box">
        <div class="myntra-m-badge">M</div>
        <div>
            <span class="myntra-logo-text">myntra</span>
            <span style="font-weight:800; font-size:1.1rem; color:#FFF; margin-left:0.4rem;">Growth Lab</span>
            <div class="myntra-tagline-text">Wishlist Conversion Engine • Target: 7.5% → 10.5% (+300bps) | +₹18.81 Cr/mo Profit</div>
        </div>
    </div>
    <div class="myntra-nav-right">
        <div style="background:#2D0A4E; padding:0.4rem 0.85rem; border-radius:8px; font-weight:800; font-size:0.82rem; color:#D8B4FE;">
            🛍️ Shopping Bag ({cart_count})
        </div>
    </div>
</div>
""".format(cart_count=len(st.session_state.cart_items)), unsafe_allow_html=True)

# Top Navigation Tabs
tab_mvp, tab_nlp, tab_metrics, tab_figma = st.tabs([
    "🛍️ Wishlist Studio MVP (Mobile & Web Modes)",
    "🔬 AI Review NLP Discovery Engine (20,250 Corpus)",
    "📊 Financial & Metric Sensitivity Simulator",
    "🎨 Figma Mobile App Design System & Specs"
])

# TAB 1: WISHLIST STUDIO MVP
with tab_mvp:
    st.title("🛍️ Myntra Wishlist Studio MVP Solution")
    st.caption("Resolves Wishlist Stalls via Side-by-Side Spec Comparison, AI Outfits & 1-Tap WhatsApp Polling")
    
    # Interface Display Toggle
    view_mode = st.radio(
        "Select Experience Mode:",
        ["📱 Mobile Smartphone App View (iOS / Android)", "💻 Desktop Web Workspace View"],
        horizontal=True
    )
    
    st.markdown("---")

    # ==================== MOBILE SMARTPHONE APP VIEW MODE ====================
    if "Mobile" in view_mode:
        st.markdown("<h3 style='text-align:center; color:#FF3F6C;'>📱 Native Myntra Mobile App Simulator</h3>", unsafe_allow_html=True)
        st.caption("Interactive 375pt × 812pt Smartphone Frame — Click any button inside the phone frame below to test live!")
        
        # Phone Container
        st.markdown("""
        <div class="mobile-phone-frame">
            <div class="mobile-notch"></div>
            <div class="mobile-status-strip">
                <span>9:41 📶 5G</span>
                <span style="color:#FF3F6C; font-size:0.95rem; font-weight:900;">myntra</span>
                <span>🛍️ Bag ({cart_count})</span>
            </div>
            <div style="background:#181B26; padding:0.4rem 0.65rem; border-radius:8px; font-size:0.75rem; font-weight:800; display:flex; justify-content:space-between; margin-bottom:0.75rem; border:1px solid rgba(255,255,255,0.08);">
                <span>📁 Smart Folder: Workwear</span>
                <span style="color:#FF3F6C;">Spec Matrix Active</span>
            </div>
        </div>
        """.format(cart_count=len(st.session_state.cart_items)), unsafe_allow_html=True)
        
        # Interactive Mobile Controls
        m_col1, m_col2 = st.columns(2)
        with m_col1:
            st.markdown("#### 1. Mobile Item Selection")
            m_sel_a = st.selectbox("Option A Product:", PRODUCTS, format_func=lambda x: f"{x['brand']} - {x['name']}")
            st.image(m_sel_a["img"], use_container_width=True)
            st.markdown(f"<span class='gsm-chip'>{m_sel_a['gsm']}</span>", unsafe_allow_html=True)
            st.markdown(f"<span class='fit-chip'>Fit: {m_sel_a['fit']}</span>", unsafe_allow_html=True)
            st.write(f"**Price:** ₹{m_sel_a['price']:,}")
            if st.button(f"Add Option A to Bag", key="m_bag_a"):
                st.session_state.cart_items.append(m_sel_a)
                st.success(f"✓ {m_sel_a['brand']} added to Bag!")

        with m_col2:
            st.markdown("#### 2. Alternative Item")
            m_sel_b = st.selectbox("Option B Product:", [p for p in PRODUCTS if p["id"] != m_sel_a["id"]], format_func=lambda x: f"{x['brand']} - {x['name']}")
            st.image(m_sel_b["img"], use_container_width=True)
            st.markdown(f"<span class='gsm-chip'>{m_sel_b['gsm']}</span>", unsafe_allow_html=True)
            st.markdown(f"<span class='fit-chip'>Fit: {m_sel_b['fit']}</span>", unsafe_allow_html=True)
            st.write(f"**Price:** ₹{m_sel_b['price']:,}")
            if st.button(f"Add Option B to Bag", key="m_bag_b"):
                st.session_state.cart_items.append(m_sel_b)
                st.success(f"✓ {m_sel_b['brand']} added to Bag!")

        st.markdown("---")
        
        # Mobile AI Look Builder
        st.markdown("#### 3. Mobile AI Outfit Coordinator (+₹450 AOV Lift)")
        st.write(f"Pair **{m_sel_a['name']}** (₹{m_sel_a['price']:,}) with curated Friday complement pieces:")
        st.write("• Oversized Graphic Tee (₹899)")
        st.write("• Vintage Canvas Sneakers (₹1,499)")
        look_total = m_sel_a['price'] + 899 + 1499
        st.markdown(f"**Complete Look Bundle Total:** ₹{look_total:,} *(0% Discount)*")
        if st.button("🛍️ Add Complete 3-Piece Look to Mobile Bag", key="m_add_look"):
            st.session_state.cart_items.extend([m_sel_a, PRODUCTS[3]])
            st.success("✨ Complete 3-Piece Look added to Bag! +₹450 AOV logged.")

        st.markdown("---")
        
        # Mobile WhatsApp Voting Card
        st.markdown("#### 4. Mobile 1-Tap WhatsApp Friend Polling")
        if st.button("📱 Share Voting Card to WhatsApp", key="m_wa_poll"):
            st.session_state.wa_poll_active = True
            
        if st.session_state.wa_poll_active:
            st.info("💬 WhatsApp poll card generated for group!")
            st.success("⚡ Instant Fallback Active: **78% Community Choice** Choice verified in 2 seconds.")

    # ==================== DESKTOP WEB WORKSPACE VIEW MODE ====================
    else:
        st.markdown("<h3 style='color:#FF3F6C;'>💻 Myntra Wishlist Studio — Desktop Web Workspace</h3>", unsafe_allow_html=True)
        
        # Smart Folder Filter
        f_cat = st.selectbox("Occasion Smart Folder:", ["All Occasions (6 items)", "Workwear (3 items)", "Streetwear (2 items)", "Party (1 item)"])
        
        # Filter products
        disp_prods = PRODUCTS
        if "Workwear" in f_cat:
            disp_prods = [p for p in PRODUCTS if p["cat"] == "Workwear"]
        elif "Streetwear" in f_cat:
            disp_prods = [p for p in PRODUCTS if p["cat"] == "Streetwear"]
        elif "Party" in f_cat:
            disp_prods = [p for p in PRODUCTS if p["cat"] == "Party"]

        st.markdown("### 1. Wishlist Product Cards & Comparison Selector")
        d_cols = st.columns(3)
        for idx, p in enumerate(disp_prods):
            with d_cols[idx % 3]:
                st.image(p["img"], use_container_width=True)
                st.markdown(f"<div class='myntra-brand-title'>{p['brand']}</div>", unsafe_allow_html=True)
                st.markdown(f"<div class='myntra-prod-name'>{p['name']}</div>", unsafe_allow_html=True)
                st.markdown(f"""
                <div class="myntra-price-row">
                    <span class="price-current">₹{p['price']:,}</span>
                    <span class="price-mrp">₹{p['mrp']:,}</span>
                    <span class="price-discount">{round(((p['mrp']-p['price'])/p['mrp'])*100)}% OFF</span>
                </div>
                """, unsafe_allow_html=True)
                st.markdown(f"<span class='gsm-chip'>{p['gsm']}</span>", unsafe_allow_html=True)
                st.markdown(f"<span class='fit-chip'>{p['fit']}</span>", unsafe_allow_html=True)
                
                is_chk = p["id"] in st.session_state.compared_ids
                if st.checkbox(f"Compare Item", value=is_chk, key=f"d_chk_{p['id']}"):
                    if p["id"] not in st.session_state.compared_ids:
                        st.session_state.compared_ids.append(p["id"])
                else:
                    if p["id"] in st.session_state.compared_ids:
                        st.session_state.compared_ids.remove(p["id"])
                        
                if st.button(f"Move to Bag", key=f"d_bag_{p['id']}"):
                    st.session_state.cart_items.append(p)
                    st.success(f"✓ '{p['name']}' added to Bag!")

        st.markdown("---")

        # Side-by-Side Comparison Matrix
        st.markdown("### 2. Live Side-by-Side Spec & GSM Comparison Matrix")
        selected_comps = [p for p in PRODUCTS if p["id"] in st.session_state.compared_ids]
        
        if len(selected_comps) >= 2:
            matrix_cols = st.columns(len(selected_comps))
            for idx, p in enumerate(selected_comps):
                with matrix_cols[idx]:
                    st.image(p["img"], use_container_width=True)
                    st.markdown(f"**{p['brand']} — {p['name']}**")
                    st.info(f"**Fabric Weight:** {p['gsm']}")
                    st.success(f"**Fit Consensus:** {p['fit']}")
                    st.write(f"**Price:** ₹{p['price']:,}")
                    st.warning(f"**Return Risk:** {p['return']}")
                    if st.button(f"🛍️ Select & Move to Bag", key=f"d_comp_add_{p['id']}"):
                        st.session_state.cart_items.append(p)
                        st.success(f"✓ '{p['name']}' added to Bag!")
        else:
            st.info("💡 Select at least 2 items above to generate side-by-side spec matrix.")

        st.markdown("---")

        # AI Coordinated Outfits
        st.markdown("### 3. AI Coordinated Look Builder (+₹450 AOV Lift)")
        d_seed = st.selectbox("Select Seed Wishlist Item:", PRODUCTS, format_func=lambda x: f"{x['brand']} - {x['name']}")
        
        c_look1, c_look2 = st.columns(2)
        with c_look1:
            st.markdown("**Look 1: Casual Friday Look**")
            st.write(f"• Seed Piece: {d_seed['name']} (₹{d_seed['price']:,})")
            st.write("• Oversized Graphic Tee (₹899)")
            st.write("• Vintage Canvas Sneakers (₹1,499)")
            l1_tot = d_seed['price'] + 899 + 1499
            st.markdown(f"**Total Bundle:** ₹{l1_tot:,} *(0% Discount)*")
            if st.button("🛍️ Move Complete Look 1 to Bag", key=f"d_look1_{d_seed['id']}"):
                st.session_state.cart_items.extend([d_seed, PRODUCTS[3]])
                st.success("✨ Complete Look 1 added to Bag!")

        with c_look2:
            st.markdown("**Look 2: Smart Evening Outfit**")
            st.write(f"• Seed Piece: {d_seed['name']} (₹{d_seed['price']:,})")
            st.write("• Linen Blend Blazer (₹3,490)")
            st.write("• Leather Loafers (₹2,299)")
            l2_tot = d_seed['price'] + 3490 + 2299
            st.markdown(f"**Total Bundle:** ₹{l2_tot:,} *(0% Discount)*")
            if st.button("🛍️ Move Complete Look 2 to Bag", key=f"d_look2_{d_seed['id']}"):
                st.session_state.cart_items.extend([d_seed, PRODUCTS[2]])
                st.success("✨ Complete Look 2 added to Bag!")

        st.markdown("---")

        # 1-Tap WhatsApp Voting Card
        st.markdown("### 4. 1-Tap WhatsApp Social Voting Card")
        if st.button("📱 Share Polling Micro-Card to WhatsApp", key="d_wa_share"):
            st.info("WhatsApp micro-card generated for group polling!")
            st.success("⚡ Instant Fallback Triggered: **78% Community Consensus** Choice verified in 2 seconds.")

    st.markdown("---")

    # Shopping Bag Drawer Summary
    st.subheader("🛍️ Shopping Bag & Zero-Discount Checkout Summary")
    st.write(f"Items currently in Shopping Bag: **{len(st.session_state.cart_items)} Items**")
    
    df_bag = pd.DataFrame([
        {"Brand": item["brand"], "Item Name": item["name"], "Fabric Spec": item["gsm"], "Price": f"₹{item['price']:,}"}
        for item in st.session_state.cart_items
    ])
    st.table(df_bag)
    
    tot_val = sum(item["price"] for item in st.session_state.cart_items)
    st.markdown(f"### Total Order Value: **₹{tot_val:,}** *(0% Discount Subsidy)*")
    
    if st.button("💳 Proceed to 1-Tap Order Confirmation"):
        order_num = f"MYN-2026-{random.randint(10000, 99999)}"
        st.balloons()
        st.success(f"🎉 Order {order_num} Confirmed! Total Paid: ₹{tot_val:,}. Zero discount subsidies used!")

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

# TAB 4: FIGMA DESIGN SYSTEM & SPECS
with tab_figma:
    st.title("🎨 Figma Mobile App Design System & Wireframes")
    st.caption("Component Tokens, Mobile Smartphone Layout Specs & Figma Guidelines")
    
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
