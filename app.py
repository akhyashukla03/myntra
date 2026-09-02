import streamlit as st
import pandas as pd
import plotly.express as px
import os
import random

# 1. Page Configuration
st.set_page_config(
    page_title="Myntra Wishlist Studio — End-to-End Shopper Journey",
    page_icon="🛍️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS Styling for Authentic Myntra E-Commerce Web Experience
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

  /* Myntra Top Sticky Navigation Header */
  .myntra-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background-color: #FFFFFF;
    border-bottom: 1px solid #EAEAEC;
    padding: 0.75rem 2.5rem;
    box-shadow: 0 4px 12px rgba(0,0,0,0.04);
    margin-bottom: 1.5rem;
    position: sticky;
    top: 0;
    z-index: 999;
  }
  
  .myntra-logo-box {
    display: flex;
    align-items: center;
    gap: 1rem;
  }
  
  .myntra-m-badge {
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
  
  .myntra-title-text {
    font-size: 1.6rem;
    font-weight: 900;
    color: #FF3F6C;
    letter-spacing: -0.5px;
    line-height: 1;
  }

  .myntra-sub-text {
    font-size: 0.78rem;
    font-weight: 800;
    color: #535766;
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }

  /* User Journey Banner Steps */
  .journey-stepper-bar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background: #FFFFFF;
    border: 1px solid #EAEAEC;
    border-radius: 12px;
    padding: 1rem 1.5rem;
    margin-bottom: 1.5rem;
    box-shadow: 0 2px 8px rgba(0,0,0,0.03);
  }
  
  .step-pill {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    font-size: 0.85rem;
    font-weight: 800;
    color: #535766;
  }
  
  .step-pill.active {
    color: #FF3F6C;
  }
  
  .step-num {
    background: #F5F5F6;
    color: #535766;
    width: 26px;
    height: 26px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 0.78rem;
  }
  
  .step-pill.active .step-num {
    background: #FF3F6C;
    color: #FFFFFF;
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

# Myntra Top Header Navigation
st.markdown("""
<div class="myntra-header">
    <div class="myntra-logo-box">
        <div class="myntra-m-badge">M</div>
        <div>
            <div class="myntra-title-text">myntra</div>
            <div class="myntra-sub-text">Wishlist Conversion Engine • Shopper Journey</div>
        </div>
    </div>
    <div style="display:flex; align-items:center; gap:1.5rem;">
        <div style="background:#F5F5F6; border:1px solid #EAEAEC; border-radius:4px; padding:0.45rem 1rem; font-size:0.85rem; color:#696E79; width:280px;">
            🔍 Search products, specs & fabrics
        </div>
        <div style="display:flex; flex-direction:column; align-items:center; font-size:0.75rem; font-weight:800; color:#FF3F6C;">
            <span style="font-size:1.2rem;">🛍️</span>
            <span>Bag ({cart_count})</span>
        </div>
    </div>
</div>
""".format(cart_count=len(st.session_state.cart_items)), unsafe_allow_html=True)

# Device View Selector
view_mode = st.radio(
    "Select Experience Journey Mode:",
    ["💻 Myntra Web Application Journey (Full Off-White Web Flow)", "📱 Myntra Native Mobile App Journey (375pt × 812pt Smartphone App)"],
    horizontal=True
)

st.markdown("---")

# ==================== 1. WEB APPLICATION JOURNEY ====================
if "Web" in view_mode:
    # Journey Stepper Header Bar
    st.markdown("""
    <div class="journey-stepper-bar">
        <div class="step-pill active"><span class="step-num">1</span><span>Wishlist Wardrobe</span></div>
        <span style="color:#CBD5E1;">➔</span>
        <div class="step-pill active"><span class="step-num">2</span><span>Spec Comparison</span></div>
        <span style="color:#CBD5E1;">➔</span>
        <div class="step-pill active"><span class="step-num">3</span><span>AI Outfit Builder</span></div>
        <span style="color:#CBD5E1;">➔</span>
        <div class="step-pill active"><span class="step-num">4</span><span>WhatsApp Polling</span></div>
        <span style="color:#CBD5E1;">➔</span>
        <div class="step-pill active"><span class="step-num">5</span><span>Bag & Checkout</span></div>
    </div>
    """, unsafe_allow_html=True)

    # STEP 1: WISHLIST WARDROBE DISCOVERY
    st.markdown("<h3 style='color:#FF3F6C; font-weight:900;'>Step 1: Saved Wardrobe Wishlist</h3>", unsafe_allow_html=True)
    st.caption("Organized into Smart Folders with visible fabric GSM weight pills & fit consensus scores")
    
    smart_folder = st.selectbox(
        "Filter Wishlist Items by Smart Occasion Folder:",
        ["All Saved Items (6 items)", "Workwear (3 items)", "Streetwear (2 items)", "Party (1 item)"]
    )
    
    disp_prods = PRODUCTS
    if "Workwear" in smart_folder:
        disp_prods = [p for p in PRODUCTS if p["cat"] == "Workwear"]
    elif "Streetwear" in smart_folder:
        disp_prods = [p for p in PRODUCTS if p["cat"] == "Streetwear"]
    elif "Party" in smart_folder:
        disp_prods = [p for p in PRODUCTS if p["cat"] == "Party"]

    g_cols = st.columns(3)
    for idx, p in enumerate(disp_prods):
        with g_cols[idx % 3]:
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
            if st.checkbox(f"Select for Side-by-Side Comparison", value=is_chk, key=f"w_chk_{p['id']}"):
                if p["id"] not in st.session_state.compared_ids:
                    st.session_state.compared_ids.append(p["id"])
            else:
                if p["id"] in st.session_state.compared_ids:
                    st.session_state.compared_ids.remove(p["id"])
                    
            if st.button(f"Move '{p['brand']}' to Bag", key=f"w_add_{p['id']}"):
                st.session_state.cart_items.append(p)
                st.success(f"✓ '{p['name']}' added to Bag!")

    st.markdown("---")

    # STEP 2: SIDE-BY-SIDE SPEC MATRIX
    st.markdown("<h3 style='color:#FF3F6C; font-weight:900;'>Step 2: Side-by-Side Spec & GSM Comparison Sheet</h3>", unsafe_allow_html=True)
    st.caption("Resolving fabric & fit ambiguity side-by-side (240 GSM heavy vs 160 GSM light poplin)")
    
    selected_comps = [p for p in PRODUCTS if p["id"] in st.session_state.compared_ids]
    if len(selected_comps) >= 2:
        matrix_cols = st.columns(len(selected_comps))
        for idx, p in enumerate(selected_comps):
            with matrix_cols[idx]:
                st.image(p["img"], use_container_width=True)
                st.markdown(f"**{p['brand']} — {p['name']}**")
                st.info(f"**Fabric Spec:** {p['gsm']}")
                st.success(f"**Fit Consensus:** {p['fit']}")
                st.write(f"**Price:** Rs. {p['price']:,} (0% Discount)")
                st.warning(f"**Return Risk:** {p['return']}")
                if st.button(f"🛍️ Select & Add '{p['brand']}' to Bag", key=f"comp_bag_{p['id']}"):
                    st.session_state.cart_items.append(p)
                    st.success(f"✓ '{p['name']}' added to Bag!")
    else:
        st.info("💡 Select at least 2 items in Step 1 above to compare side-by-side.")

    st.markdown("---")

    # STEP 3: AI OUTFIT BUILDER
    st.markdown("<h3 style='color:#FF3F6C; font-weight:900;'>Step 3: AI Style Assistant & Outfit Matcher (+₹450 AOV Lift)</h3>", unsafe_allow_html=True)
    st.caption("Generating complete 3-piece Friday outfits around any seed item with zero discounts")
    
    d_seed = st.selectbox("Select Seed Wishlist Item for Outfit Pairing:", PRODUCTS, format_func=lambda x: f"{x['brand']} - {x['name']}")
    
    o_c1, o_c2 = st.columns(2)
    with o_c1:
        st.markdown("**Look 1: Casual Friday Ensemble**")
        st.write(f"• Seed Piece: {d_seed['name']} (Rs. {d_seed['price']:,})")
        st.write("• Oversized Graphic Tee (Rs. 899)")
        st.write("• Vintage Canvas Sneakers (Rs. 1,499)")
        l1_tot = d_seed['price'] + 899 + 1499
        st.markdown(f"**Total Look Bundle:** Rs. {l1_tot:,} *(0% Margin Erosion)*")
        if st.button("🛍️ Move Complete Look 1 to Bag", key=f"d_look1_{d_seed['id']}"):
            st.session_state.cart_items.extend([d_seed, PRODUCTS[3]])
            st.success("✨ Complete Look 1 added to Bag! +₹450 AOV logged.")

    with o_c2:
        st.markdown("**Look 2: Evening Smart Outfit**")
        st.write(f"• Seed Piece: {d_seed['name']} (Rs. {d_seed['price']:,})")
        st.write("• Structured Linen Blazer (Rs. 3,490)")
        st.write("• Leather Loafers (Rs. 2,299)")
        l2_tot = d_seed['price'] + 3490 + 2299
        st.markdown(f"**Total Look Bundle:** Rs. {l2_tot:,} *(0% Margin Erosion)*")
        if st.button("🛍️ Move Complete Look 2 to Bag", key=f"d_look2_{d_seed['id']}"):
            st.session_state.cart_items.extend([d_seed, PRODUCTS[2]])
            st.success("✨ Complete Look 2 added to Bag! +₹450 AOV logged.")

    st.markdown("---")

    # STEP 4: WHATSAPP SOCIAL VOTING
    st.markdown("<h3 style='color:#FF3F6C; font-weight:900;'>Step 4: 1-Tap WhatsApp Social Voting Micro-Card</h3>", unsafe_allow_html=True)
    st.caption("Resolving 18-hour friend reply latency via instant group polling micro-card + 2s AI community consensus fallback")
    
    if st.button("📱 Share Voting Micro-Card to WhatsApp Group", key="w_wa_share"):
        st.session_state.wa_poll_active = True
        
    if st.session_state.wa_poll_active:
        st.info("💬 WhatsApp voting micro-card generated!")
        st.success("⚡ Instant Fallback Active: **78% Community Consensus** Choice verified in 2 seconds.")

    st.markdown("---")

    # STEP 5: SHOPPING BAG & CHECKOUT
    st.markdown("<h3 style='color:#FF3F6C; font-weight:900;'>Step 5: Shopping Bag & 1-Tap Zero-Discount Checkout</h3>", unsafe_allow_html=True)
    st.caption("Order breakdown tracking total paid, zero discount subsidies used, and profit unlock")
    
    df_bag = pd.DataFrame([
        {"Brand": item["brand"], "Item Name": item["name"], "Fabric Spec": item["gsm"], "Price": f"Rs. {item['price']:,}"}
        for item in st.session_state.cart_items
    ])
    st.table(df_bag)
    
    tot_val = sum(item["price"] for item in st.session_state.cart_items)
    st.markdown(f"### Total Order Price: **Rs. {tot_val:,}** *(0% Discount Subsidies)*")
    
    if st.button("💳 Confirm 1-Tap Checkout Order"):
        order_num = f"MYN-2026-{random.randint(10000, 99999)}"
        st.balloons()
        st.success(f"🎉 Order {order_num} Confirmed! Total Paid: Rs. {tot_val:,}. Zero discount subsidies used!")

# ==================== 2. MOBILE SMARTPHONE APP JOURNEY ====================
else:
    st.markdown("### 📱 Native Myntra Mobile Smartphone App Journey")
    st.caption("Interactive 375pt × 812pt Mobile Screen Architecture")
    
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
