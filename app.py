import streamlit as st
import pandas as pd
import plotly.express as px
import os
import json
import random

# ==========================================
# 1. Page Configuration & Custom CSS
# ==========================================
st.set_page_config(
    page_title="Myntra Growth Lab — Wishlist Conversion Engine",
    page_icon="🛍️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Premium Myntra Custom Styling System
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

  /* Myntra Sticky Header Nav */
  .myntra-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background-color: #FFFFFF;
    border-bottom: 1px solid #EAEAEC;
    padding: 0.75rem 2.5rem;
    box-shadow: 0 4px 12px rgba(0,0,0,0.04);
    margin-bottom: 1rem;
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
    font-size: 1.5rem;
    font-weight: 900;
    color: #FF3F6C;
    letter-spacing: -0.5px;
    line-height: 1;
  }

  .myntra-sub-text {
    font-size: 0.75rem;
    font-weight: 800;
    color: #535766;
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }

  /* Stat Card */
  .stat-card-box {
    background: #FFFFFF;
    border: 1px solid #EAEAEC;
    border-radius: 10px;
    padding: 1rem 1.25rem;
    box-shadow: 0 2px 8px rgba(0,0,0,0.03);
    margin-bottom: 1rem;
  }
  .stat-val {
    font-size: 1.8rem;
    font-weight: 900;
    color: #FF3F6C;
  }
  .stat-lbl {
    font-size: 0.85rem;
    font-weight: 800;
    color: #282C3F;
  }
  .stat-sub {
    font-size: 0.75rem;
    color: #7E818C;
  }

  /* Product Card */
  .myntra-card-white {
    background-color: #FFFFFF;
    border: 1px solid #EAEAEC;
    border-radius: 10px;
    padding: 1rem;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
    margin-bottom: 1rem;
    height: 100%;
  }
  
  .prod-brand-text {
    font-size: 0.88rem;
    font-weight: 900;
    color: #282C3F;
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }

  .prod-title-text {
    font-size: 0.82rem;
    font-weight: 600;
    color: #535766;
    margin: 0.2rem 0 0.4rem 0;
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
    padding: 0.25rem 0.55rem;
    border-radius: 4px;
    display: inline-block;
  }
  
  .spec-badge-fit {
    background-color: #E6F4F1;
    color: #03A685;
    font-size: 0.72rem;
    font-weight: 800;
    padding: 0.25rem 0.55rem;
    border-radius: 4px;
    display: inline-block;
  }

  .spec-badge-risk {
    background-color: #FEF3C7;
    color: #D97706;
    font-size: 0.72rem;
    font-weight: 800;
    padding: 0.25rem 0.55rem;
    border-radius: 4px;
    display: inline-block;
  }

  /* Native Mobile iPhone Device Frame Wrapper */
  .mobile-device-shell {
    max-width: 390px;
    margin: 1rem auto;
    background-color: #FFFFFF;
    border: 14px solid #1F2937;
    border-radius: 44px;
    padding: 1rem;
    box-shadow: 0 25px 60px rgba(0, 0, 0, 0.25);
    color: #282C3F;
  }

  .mobile-notch-strip {
    width: 120px;
    height: 18px;
    background-color: #1F2937;
    border-bottom-left-radius: 12px;
    border-bottom-right-radius: 12px;
    margin: -1rem auto 0.75rem auto;
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

  .wa-card-box {
    background: #E7FCE8;
    border: 1px solid #25D366;
    border-radius: 12px;
    padding: 0.85rem;
    margin-top: 0.75rem;
  }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 2. Master Wishlist Dataset (12 Products)
# ==========================================
WISHLIST_PRODUCTS = [
    {
        "id": "prod-01",
        "name": "Roadster Relaxed Fit 6-Pocket Baggy Cargo Pants",
        "brand": "Roadster",
        "category": "STREETWEAR",
        "price": 1399,
        "originalPrice": 2799,
        "rating": 4.2,
        "fabric": "100% Heavy Twill Cotton (280 GSM)",
        "fitScore": "91% Say True to Size (Baggy Cut)",
        "returnRisk": "Low (12% Return Rate)",
        "color": "Olive Green",
        "image": "https://images.unsplash.com/photo-1624378439575-d8705ad7ae80?w=600&auto=format&fit=crop&q=80"
    },
    {
        "id": "prod-02",
        "name": "Highlander Men Wide Leg Relaxed Cotton Cargo Trousers",
        "brand": "Highlander",
        "category": "STREETWEAR",
        "price": 1199,
        "originalPrice": 2499,
        "rating": 4.0,
        "fabric": "Cotton Poly Blend (210 GSM)",
        "fitScore": "78% Say Runs Slightly Long",
        "returnRisk": "Medium (19% Return Rate)",
        "color": "Pitch Black",
        "image": "https://images.unsplash.com/photo-1506630448388-4e683c67ddb0?w=600&auto=format&fit=crop&q=80"
    },
    {
        "id": "prod-03",
        "name": "Levi's Men 568 Loose Straight Fit Vintage Wash Jeans",
        "brand": "Levi's",
        "category": "STREETWEAR",
        "price": 2699,
        "originalPrice": 4599,
        "rating": 4.5,
        "fabric": "100% Rigid Denim (13.5 oz / 380 GSM)",
        "fitScore": "96% Say True to Size (Classic Straight)",
        "returnRisk": "Very Low (6% Return Rate)",
        "color": "Light Vintage Indigo",
        "image": "https://images.unsplash.com/photo-1541099649105-f69ad21f3246?w=600&auto=format&fit=crop&q=80"
    },
    {
        "id": "prod-04",
        "name": "H&M Men Boxy Fit Heavyweight Graphic Hoodie",
        "brand": "H&M",
        "category": "STREETWEAR",
        "price": 1999,
        "originalPrice": 2999,
        "rating": 4.4,
        "fabric": "80% Cotton / 20% Fleece (340 GSM)",
        "fitScore": "88% Say True to Size (Boxy Drop Shoulder)",
        "returnRisk": "Low (9% Return Rate)",
        "color": "Washed Charcoal",
        "image": "https://images.unsplash.com/photo-1556905055-8f358a7a47b2?w=600&auto=format&fit=crop&q=80"
    },
    {
        "id": "prod-05",
        "name": "MANGO Structured Pure Linen Single-Breasted Blazer",
        "brand": "MANGO",
        "category": "WORKWEAR",
        "price": 4490,
        "originalPrice": 6990,
        "rating": 4.6,
        "fabric": "100% Normandy Linen (220 GSM)",
        "fitScore": "93% Say True to Size (Tailored Slim)",
        "returnRisk": "Very Low (8% Return Rate)",
        "color": "Beige Sand",
        "image": "https://images.unsplash.com/photo-1591047139829-d91aecb6caea?w=600&auto=format&fit=crop&q=80"
    },
    {
        "id": "prod-06",
        "name": "Jack & Jones Men Slim Fit Stretch Twill Formal Chinos",
        "brand": "Jack & Jones",
        "category": "WORKWEAR",
        "price": 1899,
        "originalPrice": 3299,
        "rating": 4.1,
        "fabric": "98% Cotton 2% Elastane (240 GSM)",
        "fitScore": "82% Say Runs Slightly Tight at Waist",
        "returnRisk": "Medium (16% Return Rate)",
        "color": "Navy Blue",
        "image": "https://images.unsplash.com/photo-1473966968600-fa801b869a1a?w=600&auto=format&fit=crop&q=80"
    },
    {
        "id": "prod-07",
        "name": "Rare Rabbit Men Oxford Cotton Button-Down Shirt",
        "brand": "Rare Rabbit",
        "category": "WORKWEAR",
        "price": 2299,
        "originalPrice": 3999,
        "rating": 4.3,
        "fabric": "100% Fine Oxford Weave Cotton (180 GSM)",
        "fitScore": "90% Say True to Size (Structured Regular)",
        "returnRisk": "Low (11% Return Rate)",
        "color": "Crisp Light Blue",
        "image": "https://images.unsplash.com/photo-1602810318383-e386cc2a3ccf?w=600&auto=format&fit=crop&q=80"
    },
    {
        "id": "prod-08",
        "name": "Puma Rebound Retro High-Top Chunky Sneakers",
        "brand": "Puma",
        "category": "FOOTWEAR",
        "price": 3499,
        "originalPrice": 5999,
        "rating": 4.4,
        "fabric": "Genuine Leather Upper & Cushioned Rubber Sole",
        "fitScore": "89% Say True to Size",
        "returnRisk": "Low (10% Return Rate)",
        "color": "White / High-Risk Red",
        "image": "https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=600&auto=format&fit=crop&q=80"
    },
    {
        "id": "prod-09",
        "name": "Nike Court Vision Low-Top Leather Sneakers",
        "brand": "Nike",
        "category": "FOOTWEAR",
        "price": 4295,
        "originalPrice": 5495,
        "rating": 4.7,
        "fabric": "Synthetic & Genuine Leather Mix",
        "fitScore": "94% Say True to Size",
        "returnRisk": "Very Low (5% Return Rate)",
        "color": "Triple White",
        "image": "https://images.unsplash.com/photo-1595950653106-6c9ebd614d3a?w=600&auto=format&fit=crop&q=80"
    },
    {
        "id": "prod-10",
        "name": "Red Tape Men Chunky Lug-Sole Chelsea Boots",
        "brand": "Red Tape",
        "category": "FOOTWEAR",
        "price": 2299,
        "originalPrice": 5299,
        "rating": 4.1,
        "fabric": "Faux Leather & Heavy Rubber Grip Sole",
        "fitScore": "75% Say Runs 1 Size Large",
        "returnRisk": "High (24% Return Rate)",
        "color": "Matte Black",
        "image": "https://images.unsplash.com/photo-1608256246200-53e635b5b65f?w=600&auto=format&fit=crop&q=80"
    },
    {
        "id": "prod-11",
        "name": "Zara Metallic Sheen Party Slip Dress",
        "brand": "Zara",
        "category": "WEEKEND",
        "price": 3290,
        "originalPrice": 4990,
        "rating": 4.5,
        "fabric": "Satin Poly Blend with Metallic Sheen",
        "fitScore": "92% Say Slim Bodycon Fit",
        "returnRisk": "Medium (14% Return Rate)",
        "color": "Midnight Champagne",
        "image": "https://images.unsplash.com/photo-1539109136881-3be0616acf4b?w=600&auto=format&fit=crop&q=80"
    },
    {
        "id": "prod-12",
        "name": "Urbanic Velvet Oversized Evening Kimono Blazer",
        "brand": "Urbanic",
        "category": "WEEKEND",
        "price": 2490,
        "originalPrice": 3990,
        "rating": 4.2,
        "fabric": "Plush Soft Velvet (300 GSM)",
        "fitScore": "87% Say Relaxed Oversized Fit",
        "returnRisk": "Low (10% Return Rate)",
        "color": "Deep Emerald Green",
        "image": "https://images.unsplash.com/photo-1515886657613-9f3515b0c78f?w=600&auto=format&fit=crop&q=80"
    }
]

# ==========================================
# 3. Session State Initialization
# ==========================================
if 'cart_items' not in st.session_state:
    st.session_state.cart_items = [WISHLIST_PRODUCTS[0]]
if 'compared_ids' not in st.session_state:
    st.session_state.compared_ids = ["prod-01", "prod-02", "prod-03"]
if 'wa_poll_active' not in st.session_state:
    st.session_state.wa_poll_active = False

# ==========================================
# 4. Top Header & Navigation System
# ==========================================
cart_count = len(st.session_state.cart_items)

st.markdown(f"""
<div class="myntra-header">
    <div class="myntra-logo-box">
        <div class="myntra-m-badge">M</div>
        <div>
            <div class="myntra-title-text">Myntra Growth Lab</div>
            <div class="myntra-sub-text">Wishlist Conversion Engine • Solution Architecture</div>
        </div>
    </div>
    <div style="display:flex; align-items:center; gap:1.5rem;">
        <div style="background:#F5F5F6; border:1px solid #EAEAEC; border-radius:6px; padding:0.45rem 1rem; font-size:0.85rem; color:#696E79; width:260px;">
            🔍 Search products, specs & fabrics
        </div>
        <div style="display:flex; align-items:center; gap:0.5rem; background:#FFF0F4; border:1px solid #FF3F6C; border-radius:6px; padding:0.45rem 0.85rem; font-size:0.85rem; font-weight:800; color:#FF3F6C;">
            <span>🛍️ Bag ({cart_count})</span>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Main Navigation Module Selector (Matching React HeaderNav)
main_module = st.radio(
    "Select Growth Lab Module:",
    [
        "🛍️ Wishlist Studio MVP",
        "👥 User Research & Insights",
        "📈 Growth Strategy & Metrics"
    ],
    horizontal=True,
    key="main_nav_radio"
)

st.markdown("<hr style='margin:0.5rem 0 1.5rem 0; border:0; border-top:1px solid #EAEAEC;'>", unsafe_allow_html=True)

# ==========================================
# 5. Shopping Bag Expander (Drawer Equivalent)
# ==========================================
with st.sidebar:
    st.markdown("### 🛍️ Shopping Bag")
    if len(st.session_state.cart_items) == 0:
        st.info("Your bag is currently empty.")
    else:
        tot_val = sum(item["price"] for item in st.session_state.cart_items)
        for idx, item in enumerate(st.session_state.cart_items):
            st.markdown(f"**{idx+1}. {item['brand']}** — {item['name'][:30]}...")
            st.caption(f"Price: Rs. {item['price']:,} | {item.get('fabric', 'Cotton')[:25]}")
        st.markdown("---")
        st.markdown(f"#### Total Payable: **Rs. {tot_val:,}**")
        st.caption("✨ Zero Discount Subsidies Used")
        if st.button("💳 1-Tap Checkout"):
            order_num = f"MYN-2026-{random.randint(10000, 99999)}"
            st.balloons()
            st.success(f"🎉 Order {order_num} Confirmed! Total Paid: Rs. {tot_val:,}.")

# ==========================================
# MODULE 1: WISHLIST STUDIO MVP
# ==========================================
if "Wishlist Studio MVP" in main_module:
    st.markdown("<h2 style='color:#FF3F6C; font-weight:900; margin-bottom:0;'>Wishlist Studio MVP Solution</h2>", unsafe_allow_html=True)
    st.caption("End-to-End Prototype transforming dormant bookmarks into zero-discount checkout conversions.")

    mvp_tab = st.radio(
        "Select Wishlist Studio Sub-View:",
        [
            "📁 Saved Wishlist Grid",
            "⚖️ Side-by-Side Spec Matrix",
            "🎨 AI Outfit Coordinator",
            "📱 Native Mobile App Simulator",
            "🎨 Figma Design Assets & Tokens"
        ],
        horizontal=True,
        key="mvp_tab_radio"
    )

    st.markdown("<hr style='margin:0.75rem 0 1.25rem 0; border:0; border-top:1px solid #EAEAEC;'>", unsafe_allow_html=True)

    # ----------------------------------------------------
    # SUB-VIEW 1: SAVED WISHLIST GRID
    # ----------------------------------------------------
    if "Wishlist Grid" in mvp_tab:
        st.markdown("### 📁 Saved Wishlist Wardrobe")
        st.caption("Organized into Smart Occasion Folders with fabric GSM weight pills & fit consensus scores.")

        col_cat, col_info = st.columns([1, 2])
        with col_cat:
            cat_filter = st.selectbox(
                "Filter Smart Occasion Folder:",
                ["ALL", "STREETWEAR", "WORKWEAR", "FOOTWEAR", "WEEKEND"]
            )

        filtered_prods = [p for p in WISHLIST_PRODUCTS if cat_filter == "ALL" or p["category"] == cat_filter]

        grid_cols = st.columns(3)
        for idx, p in enumerate(filtered_prods):
            with grid_cols[idx % 3]:
                st.markdown(f"""
                <div class="myntra-card-white">
                    <img src="{p['image']}" style="width:100%; height:220px; object-fit:cover; border-radius:8px; margin-bottom:0.6rem;" />
                    <div class="prod-brand-text">{p['brand']}</div>
                    <div class="prod-title-text">{p['name']}</div>
                    <div class="price-row-box">
                        <span class="price-curr">Rs. {p['price']:,}</span>
                        <span class="price-orig">Rs. {p['originalPrice']:,}</span>
                        <span class="price-disc">({round(((p['originalPrice']-p['price'])/p['originalPrice'])*100)}% OFF)</span>
                    </div>
                    <div style="display:flex; flex-wrap:wrap; gap:0.35rem; margin-bottom:0.6rem;">
                        <span class="spec-badge-gsm">{p['fabric'][:25]}</span>
                        <span class="spec-badge-fit">{p['fitScore'][:22]}</span>
                    </div>
                </div>
                """, unsafe_allow_html=True)

                is_checked = p["id"] in st.session_state.compared_ids
                if st.checkbox(f"Compare item", value=is_checked, key=f"grid_chk_{p['id']}"):
                    if p["id"] not in st.session_state.compared_ids:
                        if len(st.session_state.compared_ids) >= 4:
                            st.warning("Maximum 4 items can be compared at once.")
                        else:
                            st.session_state.compared_ids.append(p["id"])
                else:
                    if p["id"] in st.session_state.compared_ids:
                        st.session_state.compared_ids.remove(p["id"])

                if st.button(f"Move to Bag", key=f"grid_bag_{p['id']}", use_container_width=True):
                    st.session_state.cart_items.append(p)
                    st.success(f"✓ '{p['brand']}' added to Bag!")

    # ----------------------------------------------------
    # SUB-VIEW 2: SIDE-BY-SIDE SPEC MATRIX
    # ----------------------------------------------------
    elif "Spec Matrix" in mvp_tab:
        st.markdown("### ⚖️ Side-by-Side Spec & GSM Comparison Matrix")
        st.caption("Resolving fabric weight & fit ambiguity side-by-side without toggling tabs.")

        selected_prods = [p for p in WISHLIST_PRODUCTS if p["id"] in st.session_state.compared_ids]

        if len(selected_prods) < 2:
            st.info("💡 Select at least 2 items in the Wishlist Grid tab to compare side-by-side.")
        else:
            m_cols = st.columns(len(selected_prods))
            for idx, p in enumerate(selected_prods):
                with m_cols[idx]:
                    st.image(p["image"], use_container_width=True)
                    st.markdown(f"### {p['brand']}")
                    st.markdown(f"**{p['name']}**")
                    st.markdown(f"**Price:** Rs. {p['price']:,} *(MRP: Rs. {p['originalPrice']:,})*")
                    st.info(f"**Fabric Spec:** {p['fabric']}")
                    st.success(f"**Verified Fit Score:** {p['fitScore']}")
                    st.warning(f"**Return Risk Rating:** {p['returnRisk']}")
                    st.write(f"**Color Variant:** {p['color']}")

                    if st.button(f"🛍️ Select & Add '{p['brand']}' to Bag", key=f"matrix_add_{p['id']}", use_container_width=True):
                        st.session_state.cart_items.append(p)
                        st.success(f"✓ '{p['name']}' added to Bag!")

    # ----------------------------------------------------
    # SUB-VIEW 3: AI OUTFIT COORDINATOR
    # ----------------------------------------------------
    elif "Outfit Coordinator" in mvp_tab:
        st.markdown("### 🎨 AI Outfit Coordinator & Style Matcher (+₹450 AOV Lift)")
        st.caption("Curating complete 3-piece ensembles around seed wishlist items to eliminate styling hesitation.")

        seed_item = st.selectbox(
            "Select Seed Wishlist Item for AI Outfit Pairing:",
            WISHLIST_PRODUCTS,
            format_func=lambda x: f"{x['brand']} — {x['name']} (Rs. {x['price']:,})"
        )

        st.markdown("---")

        o_c1, o_c2 = st.columns(2)

        with o_c1:
            st.markdown("#### 🌟 Look 1: Urban Street Ensemble")
            st.image(seed_item["image"], width=220)
            st.markdown(f"1. **Anchor Piece:** {seed_item['name']} — **Rs. {seed_item['price']:,}**")
            st.markdown("2. **Top Complement:** Highlander Oversized Graphic Tee — **Rs. 699**")
            st.markdown("3. **Footwear Complement:** Puma Rebound Retro Sneakers — **Rs. 3,499**")
            look1_total = seed_item['price'] + 699 + 3499
            st.markdown(f"#### Total Look Bundle: **Rs. {look1_total:,}** *(0% Discount Subsidy)*")
            st.caption("✨ +₹450 Margin Lift via Cross-Category Add")
            if st.button("🛍️ Add Complete Look 1 to Bag", key=f"outfit_l1_{seed_item['id']}", use_container_width=True):
                st.session_state.cart_items.extend([seed_item, WISHLIST_PRODUCTS[7]])
                st.success("✨ Complete Look 1 added to Bag! +₹450 AOV logged.")

        with o_c2:
            st.markdown("#### 👔 Look 2: Evening Smart Outfit")
            st.image(seed_item["image"], width=220)
            st.markdown(f"1. **Anchor Piece:** {seed_item['name']} — **Rs. {seed_item['price']:,}**")
            st.markdown("2. **Outerwear Complement:** MANGO Linen Blazer — **Rs. 4,490**")
            st.markdown("3. **Footwear Complement:** Red Tape Leather Boots — **Rs. 2,299**")
            look2_total = seed_item['price'] + 4490 + 2299
            st.markdown(f"#### Total Look Bundle: **Rs. {look2_total:,}** *(0% Discount Subsidy)*")
            st.caption("✨ +₹450 Margin Lift via Cross-Category Add")
            if st.button("🛍️ Add Complete Look 2 to Bag", key=f"outfit_l2_{seed_item['id']}", use_container_width=True):
                st.session_state.cart_items.extend([seed_item, WISHLIST_PRODUCTS[4]])
                st.success("✨ Complete Look 2 added to Bag! +₹450 AOV logged.")

    # ----------------------------------------------------
    # SUB-VIEW 4: NATIVE MOBILE APP SIMULATOR
    # ----------------------------------------------------
    elif "Mobile App Simulator" in mvp_tab:
        st.markdown("### 📱 Native Myntra Smartphone App Simulator")
        st.caption("Interactive 375pt × 812pt Smartphone Screen Experience.")

        st.markdown(f"""
        <div class="mobile-device-shell">
            <div class="mobile-notch-strip"></div>
            <div style="display:flex; justify-content:space-between; font-size:0.75rem; font-weight:800; color:#535766; border-bottom:1px solid #EAEAEC; padding-bottom:0.4rem; margin-bottom:0.75rem;">
                <span>9:41 📶 5G</span>
                <span style="color:#FF3F6C; font-weight:900; font-size:0.95rem;">myntra</span>
                <span>🛍️ Bag ({cart_count})</span>
            </div>
            <div style="background:#FFF0F4; color:#FF3F6C; padding:0.45rem 0.75rem; border-radius:6px; font-size:0.78rem; font-weight:800; display:flex; justify-content:space-between; margin-bottom:0.75rem;">
                <span>Folder: Saved Streetwear</span>
                <span>Matrix & Voting Active</span>
            </div>
            <div class="mobile-bottom-nav">
                <span>🏠 Home</span>
                <span style="color:#FF3F6C; border-top:2px solid #FF3F6C;">✨ Studio</span>
                <span>💖 Wishlist</span>
                <span>🛍️ Bag ({cart_count})</span>
                <span>👤 Profile</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("#### 1-Tap WhatsApp Voting Micro-Card Simulation")
        st.caption("Resolving 18-hour friend reply latency via instant group polling + 2s AI community consensus fallback.")

        if st.button("📱 Share Voting Card to WhatsApp Group", key="mobile_wa_btn"):
            st.session_state.wa_poll_active = True

        if st.session_state.wa_poll_active:
            st.markdown("""
            <div class="wa-card-box">
                <div style="font-size:0.85rem; font-weight:900; color:#1E3A8A;">💬 WhatsApp Poll Live: "Help me pick for Friday night!"</div>
                <div style="font-size:0.78rem; color:#374151; margin:0.3rem 0;">Option A: Roadster Baggy Cargo (Rs. 1,399) — <b>6 votes (67%)</b></div>
                <div style="font-size:0.78rem; color:#374151;">Option B: Highlander Wide Leg Cargo (Rs. 1,199) — <b>3 votes (33%)</b></div>
                <div style="background:#FFFFFF; border-radius:6px; padding:0.4rem; margin-top:0.5rem; font-size:0.75rem; font-weight:800; color:#03A685;">
                    ⚡ 2s Instant AI Fallback Active: Verified 91% True to Size consensus for Option A!
                </div>
            </div>
            """, unsafe_allow_html=True)

    # ----------------------------------------------------
    # SUB-VIEW 5: FIGMA DESIGN ASSETS & TOKENS
    # ----------------------------------------------------
    elif "Figma Design Assets" in mvp_tab:
        st.markdown("### 🎨 Figma Design Assets & Design Tokens")
        st.caption("Generated SVG mockups & JSON Design Tokens for Myntra Wishlist Studio.")

        figma_dir = "figma_design_assets"
        if os.path.exists(figma_dir):
            svg_files = [f for f in os.listdir(figma_dir) if f.endswith(".svg")]
            json_file = os.path.join(figma_dir, "06_Figma_Design_Tokens.json")

            for svg in svg_files:
                svg_path = os.path.join(figma_dir, svg)
                st.markdown(f"#### 📄 {svg}")
                with open(svg_path, "r", encoding="utf-8") as f:
                    svg_content = f.read()
                st.image(svg_path, use_container_width=True)

            if os.path.exists(json_file):
                st.markdown("#### 🔤 Design Tokens (`06_Figma_Design_Tokens.json`)")
                with open(json_file, "r", encoding="utf-8") as f:
                    tokens = json.load(f)
                st.json(tokens)

# ==========================================
# MODULE 2: USER RESEARCH & INSIGHTS
# ==========================================
elif "User Research & Insights" in main_module:
    st.markdown("<h2 style='color:#FF3F6C; font-weight:900; margin-bottom:0;'>User Research & Insights Studio</h2>", unsafe_allow_html=True)
    st.caption("Synthesizing live survey responses, App Store sentiment analysis, and core shopper friction heatmaps.")

    # Top Key Metric Cards
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown("""
        <div class="stat-card-box">
            <div class="stat-val">100%</div>
            <div class="stat-lbl">Primary Shoppers</div>
            <div class="stat-sub">Shop primarily on Myntra</div>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown("""
        <div class="stat-card-box">
            <div class="stat-val">66.7%</div>
            <div class="stat-lbl">Wishlist Inaction</div>
            <div class="stat-sub">Items saved & forgotten for months</div>
        </div>
        """, unsafe_allow_html=True)
    with c3:
        st.markdown("""
        <div class="stat-card-box">
            <div class="stat-val">88.9%</div>
            <div class="stat-lbl">Comparison Friction</div>
            <div class="stat-sub">Toggle tabs repeatedly or drop off</div>
        </div>
        """, unsafe_allow_html=True)
    with c4:
        st.markdown("""
        <div class="stat-card-box">
            <div class="stat-val">100%</div>
            <div class="stat-lbl">Matrix Demand</div>
            <div class="stat-sub">Rated side-by-side matrix highly</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("### 📊 Live Shopper Survey Breakdown (9 Verified Respondents)")
    
    q_data = pd.DataFrame([
        {"Friction Point": "Dormant Wishlist (Forgotten for months)", "Percentage": 66.7},
        {"Friction Point": "Comparison Dilemma (2-3 options saved)", "Percentage": 44.4},
        {"Friction Point": "Styling Doubt (Unsure how to style)", "Percentage": 33.3},
        {"Friction Point": "Fit & Return Friction (Unsure about sizing)", "Percentage": 22.2},
        {"Friction Point": "Fabric Realism (Hard to tell real texture)", "Percentage": 22.2}
    ])
    
    fig = px.bar(
        q_data,
        x="Percentage",
        y="Friction Point",
        orientation="h",
        color_discrete_sequence=["#FF3F6C"],
        title="Top Friction Reasons for Abandoning Wishlisted Items"
    )
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("### 💬 Qualitative Shopper Quotes")
    st.info('🗣️ **"I save 20 items on Myntra during sales, but I end up buying nothing because I get confused comparing fabric thickness and fitting between 3 cargo pants."** — *Respondent #4*')
    st.info('🗣️ **"I take screenshots of blazers and send them on WhatsApp. By the time my friend replies 18 hours later, I lose interest."** — *Respondent #7*')

# ==========================================
# MODULE 3: GROWTH STRATEGY & METRICS
# ==========================================
elif "Growth Strategy & Metrics" in main_module:
    st.markdown("<h2 style='color:#FF3F6C; font-weight:900; margin-bottom:0;'>Growth Strategy & Decision Modeling</h2>", unsafe_allow_html=True)
    st.caption("Unit economics simulator, conversion rate lift modeling, and guardrails matrix.")

    st.markdown("### 🧮 Interactive Metric Tree & GMV Simulator")
    
    s_col1, s_col2 = st.columns(2)
    with s_col1:
        wishlist_users = st.slider("Active Wishlist Users (Monthly)", 1000000, 20000000, 10000000, step=1000000)
        compare_adoption = st.slider("Spec Matrix Adoption Rate (%)", 10, 80, 35)
        outfit_adoption = st.slider("AI Outfit Matcher Adoption Rate (%)", 5, 50, 24)
    with s_col2:
        social_adoption = st.slider("WhatsApp Voting Adoption Rate (%)", 5, 40, 18)
        avg_order_val = st.slider("Average Order Value (AOV in Rs.)", 1000, 3000, 1650, step=50)

    # Unit economics calculations
    base_cr = 7.5
    lift_cr = (compare_adoption * 0.04) + (outfit_adoption * 0.03) + (social_adoption * 0.02)
    target_cr = base_cr + lift_cr
    
    base_buyers = int(wishlist_users * (base_cr / 100))
    target_buyers = int(wishlist_users * (target_cr / 100))
    inc_buyers = target_buyers - base_buyers
    inc_gmv_cr = round((inc_buyers * avg_order_val) / 10000000, 2)
    return_savings = round((inc_buyers * 0.06 * 450) / 10000000, 2)

    st.markdown("---")
    
    m1, m2, m3, m4 = st.columns(4)
    with m1:
        st.metric("Baseline Conversion", f"{base_cr}%")
    with m2:
        st.metric("Projected Conversion", f"{target_cr:.2f}%", delta=f"+{lift_cr:.2f}%")
    with m3:
        st.metric("Incremental Buyers", f"{inc_buyers:,}")
    with m4:
        st.metric("Incremental GMV Lift", f"₹ {inc_gmv_cr} Cr")

    st.success(f"✨ **Return Rate Savings:** Reduced size variance returns yields **₹ {return_savings} Cr** in annual logistics savings.")

    st.markdown("---")

    st.markdown("### 📋 Guardrails & Risk Mitigation Matrix")
    guardrails_df = pd.DataFrame([
        {"Risk Factor": "Fabric GSM Accuracy Risk", "Mitigation Strategy": "Verified supplier spec ingestion & customer GSM validation tags", "Status": "Active Guardrail"},
        {"Risk Factor": "WhatsApp Spam Vulnerability", "Mitigation Strategy": "Rate limiting (max 3 micro-cards/day) & 2s instant AI fallback", "Status": "Active Guardrail"},
        {"Risk Factor": "Margin Erosion Risk", "Mitigation Strategy": "Strict 0% discount subsidy rule; bundle discounts capped at +₹450 AOV lift", "Status": "Active Guardrail"}
    ])
    st.table(guardrails_df)
