import streamlit as st
import pandas as pd
import plotly.express as px
import os
import random

# 1. Page Configuration
st.set_page_config(
    page_title="Myntra Growth Lab | Wishlist Conversion Engine",
    page_icon="🛍️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS Styling
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
  
  [data-testid="stSidebar"] {
    display: none !important;
  }
  
  .brand-header-box {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background: linear-gradient(135deg, #1E1B4B 0%, #0F172A 100%);
    border: 1px solid rgba(255, 63, 108, 0.35);
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
  
  .product-card-box {
    background: #121826;
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 12px;
    padding: 0.85rem;
    margin-bottom: 1rem;
  }
  
  .whatsapp-bubble {
    background-color: #075E54;
    color: #FFFFFF;
    border-radius: 14px;
    padding: 1rem;
    margin: 1rem 0;
    border-left: 4px solid #25D366;
  }
</style>
""", unsafe_allow_html=True)

# Master Products Dataset (6 Products)
PRODUCTS = [
    {
        "id": "p1", "name": "Heavy Streetwear Cargo Pants", "brand": "Roadster", "price": 1999, "mrp": 2499,
        "gsm": "240 GSM Heavyweight Cotton Twill", "fit": "88% True to Size (Relaxed Fit)", "return": "12% Low Returns",
        "img": "https://images.unsplash.com/photo-1517445312882-bc9910d016b7?w=400", "cat": "Workwear"
    },
    {
        "id": "p2", "name": "Poplin Relaxed Cargo Pants", "brand": "Wrong", "price": 1499, "mrp": 2999,
        "gsm": "160 GSM Lightweight Poplin", "fit": "64% Runs Small (Tight Waist)", "return": "28% High Sizing Variance",
        "img": "https://images.unsplash.com/photo-1541099649105-f69ad21f3246?w=400", "cat": "Workwear"
    },
    {
        "id": "p3", "name": "Structured Linen Blend Blazer", "brand": "Mango", "price": 3490, "mrp": 4990,
        "gsm": "210 GSM Pure Italian Linen", "fit": "92% True to Size (Tailored Fit)", "return": "9% Low Returns",
        "img": "https://images.unsplash.com/photo-1591047139829-d91aecb6caea?w=400", "cat": "Party"
    },
    {
        "id": "p4", "name": "Oversized Vintage Graphic Tee", "brand": "H&M", "price": 899, "mrp": 1299,
        "gsm": "220 GSM Bio-Washed Cotton", "fit": "84% True to Size (Oversized)", "return": "10% Low Returns",
        "img": "https://images.unsplash.com/photo-1521572267360-ee0c2909d518?w=400", "cat": "Streetwear"
    },
    {
        "id": "p5", "name": "Classic Raw Denim Trucker Jacket", "brand": "Levi's", "price": 4299, "mrp": 5999,
        "gsm": "320 GSM Heavy Rigid Denim", "fit": "90% True to Size (Regular Fit)", "return": "11% Low Returns",
        "img": "https://images.unsplash.com/photo-1576995853123-5a10305d93c0?w=400", "cat": "Streetwear"
    },
    {
        "id": "p6", "name": "Slim Fit Stretch Chino Trousers", "brand": "Jack & Jones", "price": 2199, "mrp": 2999,
        "gsm": "190 GSM Stretch Cotton Twill", "fit": "78% True to Size (Slim Fit)", "return": "15% Moderate Variance",
        "img": "https://images.unsplash.com/photo-1473966968600-fa801b869a1a?w=400", "cat": "Workwear"
    }
]

# Session State Initialization
if 'compared_ids' not in st.session_state:
    st.session_state.compared_ids = ["p1", "p2"]
if 'cart_items' not in st.session_state:
    st.session_state.cart_items = [PRODUCTS[0]]
if 'wa_poll_created' not in st.session_state:
    st.session_state.wa_poll_created = False
if 'wa_votes' not in st.session_state:
    st.session_state.wa_votes = {"Option A": 14, "Option B": 4}

# Top Header
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
        <span style="background:#2D0A4E; color:#FFF; font-size:0.75rem; font-weight:800; padding:0.35rem 0.85rem; border-radius:9999px;">
            🛍️ Shopping Bag: {cart_len} Items
        </span>
    </div>
</div>
""".format(cart_len=len(st.session_state.cart_items)), unsafe_allow_html=True)

# Top Navigation Tabs
tab_mvp, tab_nlp, tab_metrics, tab_figma = st.tabs([
    "🛍️ Wishlist Studio MVP Solution",
    "🔬 AI Review NLP Discovery Engine (20,250 Corpus)",
    "📊 Financial & Metric Sensitivity Simulator",
    "🎨 Figma Mobile App Design System & Wireframes"
])

# TAB 1: WISHLIST STUDIO MVP SOLUTION
with tab_mvp:
    st.title("🛍️ Wishlist Studio MVP Prototype")
    st.caption("Interactive Shortlist Workspace • Side-by-Side GSM Matrix • AI Outfit Builder • WhatsApp Friend Polling")
    
    # View Mode Option (Mobile vs Desktop)
    mvp_view = st.radio(
        "Select Display Interface:",
        ["📱 Mobile Smartphone App View (iOS / Android)", "💻 Desktop Web Workspace View"],
        horizontal=True
    )
    
    st.markdown("---")

    # Smart Occasion Category Filter
    category_filter = st.selectbox(
        "Filter Wishlist Items by Smart Occasion:",
        ["All Occasions (6 items)", "Workwear (3 items)", "Streetwear (2 items)", "Party (1 item)"]
    )
    
    filtered_products = PRODUCTS
    if "Workwear" in category_filter:
        filtered_products = [p for p in PRODUCTS if p["cat"] == "Workwear"]
    elif "Streetwear" in category_filter:
        filtered_products = [p for p in PRODUCTS if p["cat"] == "Streetwear"]
    elif "Party" in category_filter:
        filtered_products = [p for p in PRODUCTS if p["cat"] == "Party"]

    # MVP MODULE 1: PRODUCT GRID & COMPARISON SELECTOR
    st.subheader("1. Wishlist Items & Side-by-Side Comparison Selector")
    st.write(f"Select up to 4 items below to generate real-time Side-by-Side Spec & GSM Comparison Matrix:")
    
    # Grid of products
    cols = st.columns(3)
    for idx, prod in enumerate(filtered_products):
        with cols[idx % 3]:
            st.image(prod["img"], use_container_width=True)
            st.markdown(f"**{prod['brand']}** — {prod['name']}")
            st.write(f"**Price:** ₹{prod['price']:,} *(MRP: ₹{prod['mrp']:,})*")
            st.caption(f"Fabric: {prod['gsm']}")
            
            is_compared = prod["id"] in st.session_state.compared_ids
            if st.checkbox(f"Compare Item #{idx+1}", value=is_compared, key=f"chk_{prod['id']}"):
                if prod["id"] not in st.session_state.compared_ids:
                    st.session_state.compared_ids.append(prod["id"])
            else:
                if prod["id"] in st.session_state.compared_ids:
                    st.session_state.compared_ids.remove(prod["id"])
                    
            if st.button(f"Add to Bag", key=f"add_{prod['id']}"):
                st.session_state.cart_items.append(prod)
                st.success(f"✓ '{prod['name']}' added to Bag!")

    st.markdown("---")

    # MVP MODULE 2: SIDE-BY-SIDE SPEC MATRIX
    st.subheader("2. Live Side-by-Side Spec & GSM Comparison Matrix")
    
    compared_products = [p for p in PRODUCTS if p["id"] in st.session_state.compared_ids]
    if len(compared_products) >= 2:
        comp_cols = st.columns(len(compared_products))
        for idx, p in enumerate(compared_products):
            with comp_cols[idx]:
                st.image(p["img"], use_container_width=True)
                st.markdown(f"### {p['name']}")
                st.info(f"**Fabric Weight:** {p['gsm']}")
                st.success(f"**Fit Consensus:** {p['fit']}")
                st.write(f"**Price:** ₹{p['price']:,} (0% Discount)")
                st.warning(f"**Return Risk:** {p['return']}")
                if st.button(f"🛍️ Move to Bag", key=f"comp_bag_{p['id']}"):
                    st.session_state.cart_items.append(p)
                    st.success(f"✓ '{p['name']}' moved to bag!")
    else:
        st.info("💡 Select at least 2 items above to view side-by-side spec comparison matrix.")

    st.markdown("---")

    # MVP MODULE 3: AI OUTFIT COORDINATOR
    st.subheader("3. AI Coordinated Outfit Builder (+₹450 AOV Lift)")
    selected_base = st.selectbox(
        "Select Seed Item to Coordinate Outfits For:",
        PRODUCTS,
        format_func=lambda x: f"{x['brand']} — {x['name']} (₹{x['price']})"
    )
    
    st.write(f"Generated 3 Curated Friday Outfits for **{selected_base['name']}**:")
    
    o_c1, o_c2 = st.columns(2)
    with o_c1:
        st.markdown("**Look 1: Casual Friday Ensemble**")
        st.write(f"• Selected Item: {selected_base['name']} (₹{selected_base['price']})")
        st.write("• Oversized Boxy Tee (₹899)")
        st.write("• Vintage Canvas Sneakers (₹1,499)")
        bundle_total = selected_base['price'] + 899 + 1499
        st.markdown(f"**Total Bundle Price:** ₹{bundle_total:,} *(0% Margin Erosion)*")
        if st.button("🛍️ Move Complete Look 1 to Bag", key=f"look1_{selected_base['id']}"):
            st.session_state.cart_items.extend([selected_base, PRODUCTS[3]])
            st.success(f"✨ Complete 3-Piece Look added to Bag! +₹450 AOV expansion logged.")

    with o_c2:
        st.markdown("**Look 2: Evening Smart Casual**")
        st.write(f"• Selected Item: {selected_base['name']} (₹{selected_base['price']})")
        st.write("• Linen Blend Blazer (₹3,490)")
        st.write("• Leather Loafers (₹2,299)")
        bundle_total_2 = selected_base['price'] + 3490 + 2299
        st.markdown(f"**Total Bundle Price:** ₹{bundle_total_2:,} *(0% Margin Erosion)*")
        if st.button("🛍️ Move Complete Look 2 to Bag", key=f"look2_{selected_base['id']}"):
            st.session_state.cart_items.extend([selected_base, PRODUCTS[2]])
            st.success(f"✨ Complete Evening Look added to Bag! +₹450 AOV expansion logged.")

    st.markdown("---")

    # MVP MODULE 4: WHATSAPP SOCIAL VOTING CARD SIMULATOR
    st.subheader("4. 1-Tap WhatsApp Voting Micro-Card Simulator")
    
    poll_q = st.text_input("Enter WhatsApp Poll Question:", "Which cargos look better for Friday night?")
    if st.button("📱 Generate 1-Tap WhatsApp Voting Card"):
        st.session_state.wa_poll_created = True
        
    if st.session_state.wa_poll_created:
        st.markdown(f"""
        <div class="whatsapp-bubble">
            <div style="font-size:0.8rem; font-weight:800; color:#25D366; margin-bottom:0.3rem;">💬 WhatsApp Poll Created • Shared to Group</div>
            <div style="font-size:1.05rem; font-weight:900;">Question: "{poll_q}"</div>
        </div>
        """, unsafe_allow_html=True)
        
        wa1, wa2 = st.columns(2)
        with wa1:
            st.write(f"**Option A: {PRODUCTS[0]['name']}**")
            st.write(f"Votes: {st.session_state.wa_votes['Option A']} friends (78%)")
            if st.button("Vote Option A (+1 Vote)", key="vote_a"):
                st.session_state.wa_votes['Option A'] += 1
                
        with wa2:
            st.write(f"**Option B: {PRODUCTS[1]['name']}**")
            st.write(f"Votes: {st.session_state.wa_votes['Option B']} friends (22%)")
            if st.button("Vote Option B (+1 Vote)", key="vote_b"):
                st.session_state.wa_votes['Option B'] += 1
                
        st.success("⚡ Instant Fallback Active: **78% Community Consensus** Choice verified in 2 seconds.")

    st.markdown("---")

    # MVP MODULE 5: SHOPPING BAG DRAWER & CHECKOUT MODAL
    st.subheader("5. Shopping Bag & Zero-Discount Checkout")
    st.write(f"Currently **{len(st.session_state.cart_items)} Items** in Shopping Bag:")
    
    cart_df = pd.DataFrame([
        {"Item Name": item["name"], "Brand": item["brand"], "Price": f"₹{item['price']:,}", "Discount": "0% (Full Margin)"}
        for item in st.session_state.cart_items
    ])
    st.table(cart_df)
    
    total_cart_val = sum(item["price"] for item in st.session_state.cart_items)
    st.markdown(f"### Total Bag Price: **₹{total_cart_val:,}**")
    
    if st.button("💳 Proceed to 1-Tap Checkout"):
        order_id = f"MYN-2026-{random.randint(10000, 99999)}"
        st.balloons()
        st.success(f"🎉 Order {order_id} Confirmed! Total Paid: ₹{total_cart_val:,}. Zero discount subsidies used!")

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
