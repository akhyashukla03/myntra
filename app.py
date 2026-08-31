import streamlit as st
import pandas as pd
import plotly.express as px
import os
import random

# 1. Page Configuration
st.set_page_config(
    page_title="Myntra Wishlist Studio MVP Solution",
    page_icon="🛍️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom Styling for Authentic, Premium Myntra Website Design System
st.markdown("""
<style>
  @import url('https://fonts.googleapis.com/css2?family=Assistant:wght@400;600;700;800;900&display=swap');
  
  html, body, [class*="css"] {
    font-family: 'Assistant', -apple-system, BlinkMacSystemFont, sans-serif;
  }
  
  .stApp {
    background-color: #F5F5F6;
    color: #282C3F;
  }
  
  [data-testid="stSidebar"] {
    display: none !important;
  }

  /* Authentic Top Header Navigation Bar */
  .myntra-main-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background-color: #FFFFFF;
    border-bottom: 1px solid #EAEAEC;
    padding: 0.75rem 2.5rem;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
    margin-bottom: 1.5rem;
    position: sticky;
    top: 0;
    z-index: 999;
  }
  
  .myntra-logo-badge {
    background: linear-gradient(135deg, #FF3F6C 0%, #FF527B 100%);
    color: #FFFFFF;
    font-weight: 900;
    font-size: 1.75rem;
    width: 44px;
    height: 44px;
    border-radius: 10px;
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 0 4px 12px rgba(255, 63, 108, 0.35);
  }
  
  .myntra-brand-name {
    font-size: 1.6rem;
    font-weight: 900;
    color: #FF3F6C;
    letter-spacing: -0.5px;
    line-height: 1;
  }

  .myntra-brand-sub {
    font-size: 0.78rem;
    font-weight: 800;
    color: #535766;
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }

  /* White E-Commerce Section Card */
  .myntra-section-card {
    background-color: #FFFFFF;
    border: 1px solid #EAEAEC;
    border-radius: 12px;
    padding: 1.5rem;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.03);
    margin-bottom: 1.5rem;
  }
  
  .section-title-pink {
    font-size: 1.25rem;
    font-weight: 900;
    color: #FF3F6C;
    margin-bottom: 0.25rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
  }

  /* Product Card */
  .myntra-card-white {
    background-color: #FFFFFF;
    border: 1px solid #EAEAEC;
    border-radius: 8px;
    padding: 0.85rem;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
    margin-bottom: 1.25rem;
  }
  
  .prod-brand-text {
    font-size: 0.88rem;
    font-weight: 900;
    color: #282C3F;
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }

  .prod-title-text {
    font-size: 0.85rem;
    font-weight: 600;
    color: #535766;
    margin: 0.15rem 0 0.4rem 0;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }
  
  .price-row-box {
    display: flex;
    align-items: center;
    gap: 0.45rem;
    margin-bottom: 0.5rem;
  }
  
  .price-curr {
    font-size: 0.95rem;
    font-weight: 800;
    color: #282C3F;
  }
  
  .price-orig {
    font-size: 0.78rem;
    color: #7E818C;
    text-decoration: line-through;
  }
  
  .price-disc {
    font-size: 0.75rem;
    font-weight: 800;
    color: #FF905A;
  }

  .spec-badge-gsm {
    background-color: #F3E8FF;
    color: #7E22CE;
    font-size: 0.72rem;
    font-weight: 800;
    padding: 0.25rem 0.6rem;
    border-radius: 4px;
    display: inline-block;
  }
  
  .spec-badge-fit {
    background-color: #E6F4F1;
    color: #03A685;
    font-size: 0.72rem;
    font-weight: 800;
    padding: 0.25rem 0.6rem;
    border-radius: 4px;
    display: inline-block;
  }

  /* Native Mobile iPhone Device Frame Wrapper */
  .mobile-device-shell {
    max-width: 410px;
    margin: 1rem auto;
    background-color: #FFFFFF;
    border: 14px solid #282C3F;
    border-radius: 44px;
    padding: 1.1rem;
    box-shadow: 0 20px 50px rgba(0, 0, 0, 0.2);
    color: #282C3F;
  }

  .mobile-notch-strip {
    width: 130px;
    height: 18px;
    background-color: #282C3F;
    border-bottom-left-radius: 14px;
    border-bottom-right-radius: 14px;
    margin: -1.1rem auto 0.75rem auto;
  }

  .mobile-bottom-nav {
    display: flex;
    justify-content: space-around;
    align-items: center;
    border-top: 1px solid #EAEAEC;
    padding-top: 0.65rem;
    margin-top: 1rem;
    font-size: 0.72rem;
    font-weight: 800;
    color: #535766;
  }
</style>
""", unsafe_allow_html=True)

# Master Dataset (6 Authentic Myntra Wishlist Items)
PRODUCTS = [
    {
        "id": "p1", "name": "Heavyweight Streetwear Cargo Pants", "brand": "ROADSTER", "price": 1999, "mrp": 2499,
        "gsm": "240 GSM Heavyweight Cotton", "fit": "88% True to Size (Relaxed Fit)", "return": "12% Low Return Risk",
        "img": "https://images.unsplash.com/photo-1517445312882-bc9910d016b7?w=400", "cat": "Workwear"
    },
    {
        "id": "p2", "name": "Poplin Relaxed Fit Cargo Pants", "brand": "WROGN", "price": 1499, "mrp": 2999,
        "gsm": "160 GSM Lightweight Poplin", "fit": "64% Runs Small (Tight Waist)", "return": "28% High Sizing Variance",
        "img": "https://images.unsplash.com/photo-1541099649105-f69ad21f3246?w=400", "cat": "Workwear"
    },
    {
        "id": "p3", "name": "Structured Italian Linen Blazer", "brand": "MANGO", "price": 3490, "mrp": 4990,
        "gsm": "210 GSM Pure Linen", "fit": "92% True to Size (Tailored Fit)", "return": "9% Low Return Risk",
        "img": "https://images.unsplash.com/photo-1591047139829-d91aecb6caea?w=400", "cat": "Party"
    },
    {
        "id": "p4", "name": "Oversized Bio-Washed Graphic Tee", "brand": "H&M", "price": 899, "mrp": 1299,
        "gsm": "220 GSM Bio-Washed Cotton", "fit": "84% True to Size (Oversized)", "return": "10% Low Return Risk",
        "img": "https://images.unsplash.com/photo-1521572267360-ee0c2909d518?w=400", "cat": "Streetwear"
    },
    {
        "id": "p5", "name": "Classic Raw Denim Trucker Jacket", "brand": "LEVI'S", "price": 4299, "mrp": 5999,
        "gsm": "320 GSM Heavy Denim", "fit": "90% True to Size (Regular Fit)", "return": "11% Low Return Risk",
        "img": "https://images.unsplash.com/photo-1576995853123-5a10305d93c0?w=400", "cat": "Streetwear"
    },
    {
        "id": "p6", "name": "Slim Fit Stretch Cotton Chinos", "brand": "JACK & JONES", "price": 2199, "mrp": 2999,
        "gsm": "190 GSM Stretch Twill", "fit": "78% True to Size (Slim Fit)", "return": "15% Moderate Variance",
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

# Authentic Myntra Top Header Navigation
st.markdown("""
<div class="myntra-main-header">
    <div style="display:flex; align-items:center; gap:1rem;">
        <div class="myntra-logo-badge">M</div>
        <div>
            <div class="myntra-brand-name">myntra</div>
            <div class="myntra-brand-sub">Growth Lab • Wishlist Studio Solution</div>
        </div>
    </div>
    <div style="display:flex; align-items:center; gap:1.5rem;">
        <div style="background:#F5F5F6; border:1px solid #EAEAEC; border-radius:4px; padding:0.5rem 1rem; font-size:0.85rem; color:#696E79; width:300px;">
            🔍 Search products, specs & fabrics
        </div>
        <div style="display:flex; flex-direction:column; align-items:center; font-size:0.75rem; font-weight:800; color:#FF3F6C;">
            <span style="font-size:1.2rem;">🛍️</span>
            <span>Bag ({cart_count})</span>
        </div>
    </div>
</div>
""".format(cart_count=len(st.session_state.cart_items)), unsafe_allow_html=True)

# Top Device View Selector (Mobile App Frame vs Full Web Workspace Flow)
view_mode = st.radio(
    "Select Display View:",
    ["💻 Desktop Web Workspace View (Unified Multi-Feature Flow)", "📱 Mobile Smartphone App View (Interactive Native App Shell)"],
    horizontal=True
)

st.markdown("---")

# ==================== 1. DESKTOP WEB WORKSPACE (UNIFIED FLOW) ====================
if "Desktop" in view_mode:
    # KPI Banner
    st.markdown("""
    <div style="background:linear-gradient(135deg, #1E1B4B 0%, #0F172A 100%); color:#FFF; padding:1.25rem 2rem; border-radius:12px; margin-bottom:1.5rem; display:flex; justify-content:space-between; align-items:center;">
        <div>
            <h3 style="margin:0; font-weight:900; color:#FF3F6C;">Myntra Wishlist Studio Growth Engine</h3>
            <p style="margin:0.2rem 0 0 0; font-size:0.88rem; color:#CBD5E1;">Solving Wishlist Decision Stalls • Target: 30-Day Conversion 7.5% → 10.5% (+300bps) | Zero Discounts</p>
        </div>
        <div style="text-align:right;">
            <span style="background:#FF3F6C; color:#FFF; font-weight:900; padding:0.4rem 1rem; border-radius:9999px; font-size:0.85rem;">+₹18.81 Cr / mo Net Profit Unlock</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # UNIFIED SECTION 1: WISHLIST WARDROBE GRID
    st.markdown("""
    <div class="myntra-section-card">
        <div class="section-title-pink"><span>1. Saved Wardrobe Wishlist</span></div>
        <p style="color:#535766; font-size:0.88rem; margin-top:0;">Organize items by occasion, view fabric weight specs (GSM), and check items to compare side-by-side.</p>
    </div>
    """, unsafe_allow_html=True)

    smart_folder = st.selectbox(
        "Occasion Smart Folder Filter:",
        ["All Saved Items (6 items)", "Workwear (3 items)", "Streetwear (2 items)", "Party (1 item)"]
    )
    
    disp_prods = PRODUCTS
    if "Workwear" in smart_folder:
        disp_prods = [p for p in PRODUCTS if p["cat"] == "Workwear"]
    elif "Streetwear" in smart_folder:
        disp_prods = [p for p in PRODUCTS if p["cat"] == "Streetwear"]
    elif "Party" in smart_folder:
        disp_prods = [p for p in PRODUCTS if p["cat"] == "Party"]

    grid_cols = st.columns(3)
    for idx, p in enumerate(disp_prods):
        with grid_cols[idx % 3]:
            st.markdown(f"""
            <div class="myntra-card-white">
                <img src="{p['img']}" style="width:100%; height:200px; object-fit:cover; border-radius:6px; margin-bottom:0.5rem;" />
                <div class="prod-brand-text">{p['brand']}</div>
                <div class="prod-title-text">{p['name']}</div>
                <div class="price-row-box">
                    <span class="price-curr">Rs. {p['price']:,}</span>
                    <span class="price-orig">Rs. {p['mrp']:,}</span>
                    <span class="price-disc">({round(((p['mrp']-p['price'])/p['mrp'])*100)}% OFF)</span>
                </div>
                <div style="display:flex; gap:0.4rem; margin-bottom:0.5rem;">
                    <span class="spec-badge-gsm">{p['gsm']}</span>
                    <span class="spec-badge-fit">{p['fit']}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            is_chk = p["id"] in st.session_state.compared_ids
            if st.checkbox(f"Compare Item", value=is_chk, key=f"d_chk_{p['id']}"):
                if p["id"] not in st.session_state.compared_ids:
                    st.session_state.compared_ids.append(p["id"])
            else:
                if p["id"] in st.session_state.compared_ids:
                    st.session_state.compared_ids.remove(p["id"])
                    
            if st.button(f"Move '{p['brand']}' to Bag", key=f"d_bag_{p['id']}"):
                st.session_state.cart_items.append(p)
                st.success(f"✓ '{p['name']}' added to Bag!")

    # UNIFIED SECTION 2: SIDE-BY-SIDE SPEC COMPARISON MATRIX
    st.markdown("""
    <div class="myntra-section-card">
        <div class="section-title-pink"><span>2. Side-by-Side Spec & GSM Comparison Matrix</span></div>
        <p style="color:#535766; font-size:0.88rem; margin-top:0;">Direct side-by-side spec evaluation (240 GSM heavy vs 160 GSM light poplin, fit consensus score, return risk).</p>
    </div>
    """, unsafe_allow_html=True)

    selected_comps = [p for p in PRODUCTS if p["id"] in st.session_state.compared_ids]
    if len(selected_comps) >= 2:
        matrix_cols = st.columns(len(selected_comps))
        for idx, p in enumerate(selected_comps):
            with matrix_cols[idx]:
                st.image(p["img"], use_container_width=True)
                st.markdown(f"**{p['brand']} — {p['name']}**")
                st.info(f"**Fabric Weight:** {p['gsm']}")
                st.success(f"**Fit Consensus:** {p['fit']}")
                st.write(f"**Price:** Rs. {p['price']:,} (0% Discount)")
                st.warning(f"**Return Risk:** {p['return']}")
                if st.button(f"🛍️ Add '{p['brand']}' to Bag", key=f"comp_bag_{p['id']}"):
                    st.session_state.cart_items.append(p)
                    st.success(f"✓ '{p['name']}' added to Bag!")
    else:
        st.info("💡 Select at least 2 items in Section 1 above to compare side-by-side.")

    # UNIFIED SECTION 3: AI OUTFIT COORDINATOR
    st.markdown("""
    <div class="myntra-section-card">
        <div class="section-title-pink"><span>3. AI Coordinated Outfit Builder (+₹450 AOV Lift)</span></div>
        <p style="color:#535766; font-size:0.88rem; margin-top:0;">Generates complete 3-piece Friday outfits around any seed item, driving cross-category AOV expansion with zero discounts.</p>
    </div>
    """, unsafe_allow_html=True)

    d_seed = st.selectbox("Select Seed Wishlist Item for Outfit Pairing:", PRODUCTS, format_func=lambda x: f"{x['brand']} - {x['name']}")
    
    o_col1, o_col2 = st.columns(2)
    with o_col1:
        st.markdown("**Look 1: Casual Friday Ensemble**")
        st.write(f"• Seed Item: {d_seed['name']} (Rs. {d_seed['price']:,})")
        st.write("• Oversized Graphic Tee (Rs. 899)")
        st.write("• Vintage Canvas Sneakers (Rs. 1,499)")
        l1_tot = d_seed['price'] + 899 + 1499
        st.markdown(f"**Total Look Bundle:** Rs. {l1_tot:,} *(0% Margin Erosion)*")
        if st.button("🛍️ Move Complete Look 1 to Bag", key=f"look1_{d_seed['id']}"):
            st.session_state.cart_items.extend([d_seed, PRODUCTS[3]])
            st.success("✨ Complete Look 1 added to Bag! +₹450 AOV expansion logged.")

    with o_col2:
        st.markdown("**Look 2: Evening Smart Outfit**")
        st.write(f"• Seed Item: {d_seed['name']} (Rs. {d_seed['price']:,})")
        st.write("• Structured Linen Blazer (Rs. 3,490)")
        st.write("• Leather Loafers (Rs. 2,299)")
        l2_tot = d_seed['price'] + 3490 + 2299
        st.markdown(f"**Total Look Bundle:** Rs. {l2_tot:,} *(0% Margin Erosion)*")
        if st.button("🛍️ Move Complete Look 2 to Bag", key=f"look2_{d_seed['id']}"):
            st.session_state.cart_items.extend([d_seed, PRODUCTS[2]])
            st.success("✨ Complete Look 2 added to Bag! +₹450 AOV expansion logged.")

    # UNIFIED SECTION 4: 1-TAP WHATSAPP GROUP VOTING
    st.markdown("""
    <div class="myntra-section-card">
        <div class="section-title-pink"><span>4. 1-Tap WhatsApp Social Voting Micro-Card</span></div>
        <p style="color:#535766; font-size:0.88rem; margin-top:0;">Resolves 18-hour friend reply latency via instant group polling micro-card + 2s AI community consensus fallback.</p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("📱 Share Voting Micro-Card to WhatsApp Group", key="d_wa_btn"):
        st.session_state.wa_poll_active = True
        
    if st.session_state.wa_poll_active:
        st.info("💬 WhatsApp voting card generated for group polling!")
        st.success("⚡ Instant Fallback Active: **78% Community Consensus** Choice verified in 2 seconds.")

    # UNIFIED SECTION 5: SHOPPING BAG & ZERO-DISCOUNT CHECKOUT
    st.markdown("""
    <div class="myntra-section-card">
        <div class="section-title-pink"><span>5. Shopping Bag & Zero-Discount Order Checkout</span></div>
        <p style="color:#535766; font-size:0.88rem; margin-top:0;">Live bag summary tracking total order value, zero discount subsidies, and net gross profit unlock.</p>
    </div>
    """, unsafe_allow_html=True)

    df_bag = pd.DataFrame([
        {"Brand": item["brand"], "Item Name": item["name"], "Fabric Spec": item["gsm"], "Price": f"Rs. {item['price']:,}"}
        for item in st.session_state.cart_items
    ])
    st.table(df_bag)
    
    tot_val = sum(item["price"] for item in st.session_state.cart_items)
    st.markdown(f"### Total Order Price: **Rs. {tot_val:,}** *(Zero Discount Subsidies)*")
    
    if st.button("💳 Confirm 1-Tap Checkout Order"):
        order_num = f"MYN-2026-{random.randint(10000, 99999)}"
        st.balloons()
        st.success(f"🎉 Order {order_num} Confirmed! Total Paid: Rs. {tot_val:,}. Zero discount subsidies used!")

# ==================== 2. MOBILE SMARTPHONE APP INTERFACE ====================
else:
    st.markdown("### 📱 Native Myntra Mobile Smartphone App Interface")
    st.caption("Interactive 375pt × 812pt Native App Shell Architecture")
    
    # Phone Shell Container
    st.markdown("""
    <div class="mobile-device-shell">
        <div class="mobile-notch-strip"></div>
        <div style="display:flex; justify-content:space-between; font-size:0.75rem; font-weight:800; color:#535766; border-bottom:1px solid #EAEAEC; padding-bottom:0.4rem; margin-bottom:0.75rem;">
            <span>9:41 📶 5G</span>
            <span style="color:#FF3F6C; font-weight:900; font-size:0.95rem;">myntra</span>
            <span>🛍️ Bag ({cart_count})</span>
        </div>
        <div style="background:#E6F4F1; color:#03A685; padding:0.45rem 0.75rem; border-radius:6px; font-size:0.75rem; font-weight:800; display:flex; justify-content:space-between; margin-bottom:0.75rem;">
            <span>Folder: Workwear</span>
            <span>Spec Matrix Active</span>
        </div>
        <div class="mobile-bottom-nav">
            <span>🏠 Home</span>
            <span style="color:#FF3F6C; border-top:2px solid #FF3F6C;">✨ Studio</span>
            <span>💖 Wishlist</span>
            <span>🛍️ Bag ({cart_count})</span>
            <span>👤 Profile</span>
        </div>
    </div>
    """.format(cart_count=len(st.session_state.cart_items)), unsafe_allow_html=True)
    
    st.markdown("#### 1. Native Mobile Side-by-Side Spec Comparison")
    m_c1, m_c2 = st.columns(2)
    with m_c1:
        st.markdown("**Option A: Roadster Heavy Cargo**")
        st.image(PRODUCTS[0]["img"], use_container_width=True)
        st.markdown("<span class='spec-badge-gsm'>240 GSM Heavy Cotton</span>", unsafe_allow_html=True)
        st.markdown("<span class='spec-badge-fit'>Fit: 88% True to Size</span>", unsafe_allow_html=True)
        st.write(f"**Price:** Rs. {PRODUCTS[0]['price']:,}")
        if st.button("Add Option A to Bag", key="m_add_a"):
            st.session_state.cart_items.append(PRODUCTS[0])
            st.success("✓ Roadster added to Bag!")

    with m_c2:
        st.markdown("**Option B: Wrogn Poplin Cargo**")
        st.image(PRODUCTS[1]["img"], use_container_width=True)
        st.markdown("<span class='spec-badge-gsm'>160 GSM Light Poplin</span>", unsafe_allow_html=True)
        st.markdown("<span class='spec-badge-fit'>Fit: 64% Runs Small</span>", unsafe_allow_html=True)
        st.write(f"**Price:** Rs. {PRODUCTS[1]['price']:,}")
        if st.button("Add Option B to Bag", key="m_add_b"):
            st.session_state.cart_items.append(PRODUCTS[1])
            st.success("✓ Wrogn added to Bag!")

    st.markdown("---")
    
    # Mobile AI Look Builder
    st.markdown("#### 2. Native Mobile AI Look Coordinator")
    st.write("Pair **Roadster Cargo** (Rs. 1,999) with curated Friday complement pieces:")
    st.write("• Oversized Graphic Tee (Rs. 899)")
    st.write("• Vintage Canvas Sneakers (Rs. 1,499)")
    st.markdown("**Complete Look Total:** Rs. 4,397 *(0% Discount)*")
    if st.button("🛍️ Move 3-Piece Look to Mobile Bag", key="m_add_look"):
        st.session_state.cart_items.extend([PRODUCTS[0], PRODUCTS[3]])
        st.success("✨ Complete 3-Piece Look added to Bag!")

    st.markdown("---")
    
    # Mobile WhatsApp Voting
    st.markdown("#### 3. Native Mobile WhatsApp Voting Micro-Card")
    if st.button("📱 Share Voting Card to WhatsApp", key="m_wa_share"):
        st.session_state.wa_poll_active = True
        
    if st.session_state.wa_poll_active:
        st.info("💬 WhatsApp voting card generated!")
        st.success("⚡ Instant Fallback Active: **78% Community Consensus** Choice verified in 2 seconds.")

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
    m2.metric("Monthly Incremental GMV", f"Rs. {incremental_gmv:.2f} Cr", f"+Rs. {incremental_gmv*12:.1f} Cr / yr")
    m3.metric("Monthly Gross Profit Unlock", f"Rs. {monthly_gross_profit:.2f} Cr", f"At {margin}% Margin")
    m4.metric("Feature ROI", f"{roi:.0f}x ROI", f"Payback < {payback_days:.1f} Days")

    st.markdown("---")
    st.markdown("### Financial Sensitivity Matrix")
    df_sens_table = pd.DataFrame([
        {"Scenario": "Base Case (100% Target Lift)", "Lift (bps)": "+300 bps", "Monthly Profit": f"Rs. {monthly_gross_profit:.2f} Cr", "Annual Value": f"Rs. {annual_gross_profit:.1f} Cr", "Feature ROI": f"{roi:.0f}x", "Payback": f"{payback_days:.1f} Days"},
        {"Scenario": "Conservative Case (75% Lift)", "Lift (bps)": f"+{int(target_lift_bps*0.75)} bps", "Monthly Profit": f"Rs. {monthly_gross_profit*0.75:.2f} Cr", "Annual Value": f"Rs. {annual_gross_profit*0.75:.1f} Cr", "Feature ROI": f"{roi*0.75:.0f}x", "Payback": f"{payback_days/0.75:.1f} Days"},
        {"Scenario": "Stress-Test Case (50% Lift)", "Lift (bps)": f"+{int(target_lift_bps*0.50)} bps", "Monthly Profit": f"Rs. {monthly_gross_profit*0.50:.2f} Cr", "Annual Value": f"Rs. {annual_gross_profit*0.50:.1f} Cr", "Feature ROI": f"{roi*0.50:.0f}x", "Payback": f"{payback_days/0.50:.1f} Days"},
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
