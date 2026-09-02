import os
import json

def create_svg_file(filepath, svg_content):
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(svg_content.strip())
    print(f"Created SVG: {filepath}")

# 1. Mobile App Screen 1: Spec Comparison Matrix (375 x 812)
svg_mobile_spec_matrix = """<svg width="375" height="812" viewBox="0 0 375 812" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bgGrad" x1="0" y1="0" x2="375" y2="812" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#0A0D14"/>
      <stop offset="100%" stop-color="#121826"/>
    </linearGradient>
    <linearGradient id="btnGrad" x1="0" y1="0" x2="150" y2="0" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#FF3F6C"/>
      <stop offset="100%" stop-color="#FF6B8B"/>
    </linearGradient>
    <filter id="shadow" x="-5" y="-5" width="385" height="822" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="10" stdDeviation="15" flood-color="#000000" flood-opacity="0.5"/>
    </filter>
  </defs>

  <!-- Background Canvas -->
  <rect width="375" height="812" rx="40" fill="url(#bgGrad)"/>

  <!-- Status Bar -->
  <text x="24" y="32" fill="#FFFFFF" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="14" font-weight="600">9:41</text>
  <path d="M315 23h18v10h-18z" fill="none" stroke="#FFFFFF" stroke-width="1" rx="2"/>
  <rect x="317" y="25" width="12" height="6" fill="#FFFFFF" rx="1"/>
  <path d="M295 28a4 4 0 0 1 4-4h.01a4 4 0 0 1 4 4v4a4 4 0 0 1-4 4H299a4 4 0 0 1-4-4v-4z" fill="#FFFFFF"/>

  <!-- App Header -->
  <rect x="0" y="44" width="375" height="56" fill="#121826" opacity="0.95"/>
  <text x="20" y="78" fill="#FF3F6C" font-family="-apple-system, sans-serif" font-size="20" font-weight="900" letter-spacing="-0.5">myntra</text>
  <rect x="90" y="60" width="190" height="34" rx="17" fill="#1E293B"/>
  <text x="105" y="82" fill="#64748B" font-family="sans-serif" font-size="12">Search Myntra...</text>
  <circle cx="340" cy="77" r="14" fill="#2D0A4E"/>
  <text x="334" y="82" fill="#FFFFFF" font-family="sans-serif" font-size="12" font-weight="bold">🛍️</text>

  <!-- Sub-Header: Wishlist Spec Matrix -->
  <rect x="0" y="100" width="375" height="40" fill="#2D0A4E"/>
  <text x="16" y="125" fill="#FFFFFF" font-family="sans-serif" font-size="13" font-weight="700">WISHLIST — Spec Comparison (2 Selected)</text>
  <rect x="290" y="108" width="68" height="24" rx="12" fill="#FF3F6C"/>
  <text x="298" y="124" fill="#FFFFFF" font-family="sans-serif" font-size="11" font-weight="800">240 GSM</text>

  <!-- Spec Grid Header -->
  <rect x="16" y="152" width="168" height="230" rx="12" fill="#FFFFFF"/>
  <rect x="191" y="152" width="168" height="230" rx="12" fill="#FFFFFF"/>

  <!-- Product 1 Image Placeholder & Badge -->
  <rect x="24" y="160" width="152" height="130" rx="8" fill="#F1F5F9"/>
  <text x="50" y="230" fill="#94A3B8" font-family="sans-serif" font-size="12">Heavy Cargo</text>
  <rect x="28" y="164" width="70" height="20" rx="4" fill="#2D0A4E"/>
  <text x="32" y="178" fill="#FFFFFF" font-family="sans-serif" font-size="9" font-weight="800">240 GSM HEAVY</text>

  <!-- Product 2 Image Placeholder & Badge -->
  <rect x="199" y="160" width="152" height="130" rx="8" fill="#F1F5F9"/>
  <text x="225" y="230" fill="#94A3B8" font-family="sans-serif" font-size="12">Slim Cargo</text>
  <rect x="203" y="164" width="70" height="20" rx="4" fill="#64748B"/>
  <text x="207" y="178" fill="#FFFFFF" font-family="sans-serif" font-size="9" font-weight="800">160 GSM LIGHT</text>

  <!-- Product Details Row 1 -->
  <text x="24" y="305" fill="#0A0D14" font-family="sans-serif" font-size="12" font-weight="800">Roadster Heavy Duty</text>
  <text x="24" y="322" fill="#FF3F6C" font-family="sans-serif" font-size="14" font-weight="900">₹1,999</text>
  <text x="199" y="305" fill="#0A0D14" font-family="sans-serif" font-size="12" font-weight="800">HIGHLANDER Slim Fit</text>
  <text x="199" y="322" fill="#FF3F6C" font-family="sans-serif" font-size="14" font-weight="900">₹1,499</text>

  <!-- Fit & Spec Comparison Rows -->
  <!-- Fit Score Card 1 -->
  <rect x="16" y="392" width="343" height="140" rx="12" fill="#1E293B"/>
  <text x="30" y="415" fill="#10B981" font-family="sans-serif" font-size="12" font-weight="800">✓ 88% TRUE TO SIZE CONSENSUS</text>
  <text x="30" y="432" fill="#94A3B8" font-family="sans-serif" font-size="11">Based on 1,420 verified buyer ratings (Low return friction)</text>
  
  <!-- Fit Histogram Bars -->
  <rect x="30" y="445" width="60" height="8" rx="4" fill="#10B981"/>
  <rect x="95" y="445" width="200" height="8" rx="4" fill="#334155"/>
  <text x="30" y="468" fill="#FFFFFF" font-family="sans-serif" font-size="11" font-weight="700">Fabric Stretch: 4-Way Micro Stretch (Zero Bagging)</text>

  <!-- Buyer Photo Switcher Pill -->
  <rect x="30" y="480" width="150" height="32" rx="16" fill="#2D0A4E"/>
  <text x="45" y="501" fill="#FFFFFF" font-family="sans-serif" font-size="11" font-weight="700">📸 Real Buyer Photos</text>
  <rect x="190" y="480" width="150" height="32" rx="16" fill="#334155"/>
  <text x="210" y="501" fill="#94A3B8" font-family="sans-serif" font-size="11" font-weight="600">Studio Model</text>

  <!-- Action CTA Buttons -->
  <rect x="16" y="545" width="168" height="44" rx="8" fill="url(#btnGrad)"/>
  <text x="50" y="572" fill="#FFFFFF" font-family="sans-serif" font-size="13" font-weight="800">ADD TO BAG</text>

  <rect x="191" y="545" width="168" height="44" rx="8" fill="#334155"/>
  <text x="225" y="572" fill="#FFFFFF" font-family="sans-serif" font-size="13" font-weight="800">ADD TO BAG</text>

  <!-- WhatsApp Micro Voting Preview Banner -->
  <rect x="16" y="602" width="343" height="70" rx="12" fill="#054740"/>
  <text x="30" y="625" fill="#25D366" font-family="sans-serif" font-size="12" font-weight="800">💬 ASK FRIENDS ON WHATSAPP</text>
  <text x="30" y="642" fill="#E2E8F0" font-family="sans-serif" font-size="11">Generate 1-Tap micro-poll card with instant fallback</text>
  <rect x="250" y="620" width="95" height="32" rx="6" fill="#25D366"/>
  <text x="262" y="641" fill="#FFFFFF" font-family="sans-serif" font-size="11" font-weight="800">Share Poll</text>

  <!-- Bottom Navigation Bar -->
  <rect x="0" y="738" width="375" height="74" fill="#0A0D14" stroke="#1E293B" stroke-width="1"/>
  <text x="30" y="775" fill="#94A3B8" font-family="sans-serif" font-size="11">Home</text>
  <text x="100" y="775" fill="#94A3B8" font-family="sans-serif" font-size="11">Categories</text>
  <text x="175" y="775" fill="#FF3F6C" font-family="sans-serif" font-size="12" font-weight="bold">Studio</text>
  <text x="250" y="775" fill="#94A3B8" font-family="sans-serif" font-size="11">Wishlist</text>
  <text x="315" y="775" fill="#94A3B8" font-family="sans-serif" font-size="11">Profile</text>
</svg>"""


# 2. Mobile App Screen 2: AI Outfit Coordinator (375 x 812)
svg_mobile_ai_outfit = """<svg width="375" height="812" viewBox="0 0 375 812" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bgGrad2" x1="0" y1="0" x2="375" y2="812" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#0A0D14"/>
      <stop offset="100%" stop-color="#1E1B4B"/>
    </linearGradient>
    <linearGradient id="aiGrad" x1="0" y1="0" x2="343" y2="0" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#4F46E5"/>
      <stop offset="100%" stop-color="#818CF8"/>
    </linearGradient>
  </defs>

  <rect width="375" height="812" rx="40" fill="url(#bgGrad2)"/>

  <!-- Status Bar -->
  <text x="24" y="32" fill="#FFFFFF" font-family="-apple-system, sans-serif" font-size="14" font-weight="600">9:41</text>

  <!-- Header -->
  <rect x="0" y="44" width="375" height="56" fill="#0A0D14" opacity="0.9"/>
  <text x="20" y="78" fill="#FF3F6C" font-family="sans-serif" font-size="20" font-weight="900">myntra</text>
  <text x="140" y="77" fill="#FFFFFF" font-family="sans-serif" font-size="15" font-weight="700">AI Look Builder</text>

  <!-- Banner -->
  <rect x="16" y="110" width="343" height="48" rx="10" fill="url(#aiGrad)"/>
  <text x="30" y="138" fill="#FFFFFF" font-family="sans-serif" font-size="13" font-weight="800">✨ AI Coordinated Look Generator (+₹450 AOV Lift)</text>

  <!-- Selected Item Header Card -->
  <rect x="16" y="170" width="343" height="110" rx="12" fill="#1E293B"/>
  <rect x="28" y="180" width="70" height="90" rx="6" fill="#334155"/>
  <text x="45" y="230" fill="#94A3B8" font-family="sans-serif" font-size="10">Bomber</text>
  <text x="110" y="200" fill="#818CF8" font-family="sans-serif" font-size="11" font-weight="800">ANCHOR ITEM FROM WISHLIST</text>
  <text x="110" y="220" fill="#FFFFFF" font-family="sans-serif" font-size="14" font-weight="800">Olive Heavy Bomber Jacket</text>
  <text x="110" y="240" fill="#FF3F6C" font-family="sans-serif" font-size="15" font-weight="900">₹2,499</text>
  <rect x="110" y="250" width="110" height="18" rx="4" fill="#2D0A4E"/>
  <text x="116" y="263" fill="#FFFFFF" font-family="sans-serif" font-size="9" font-weight="700">Fabric: 280 GSM Canvas</text>

  <!-- AI Outfit Look Cards Carousel -->
  <text x="16" y="305" fill="#FFFFFF" font-family="sans-serif" font-size="14" font-weight="800">Suggested Complete Outfits</text>

  <!-- Look 1 Card -->
  <rect x="16" y="320" width="343" height="230" rx="14" fill="#121826" stroke="#4F46E5" stroke-width="1.5"/>
  <rect x="28" y="332" width="130" height="22" rx="11" fill="#4F46E5"/>
  <text x="40" y="347" fill="#FFFFFF" font-family="sans-serif" font-size="11" font-weight="800">Look #1: Streetwear Casual</text>

  <!-- 3 Paired Items Gallery -->
  <rect x="28" y="365" width="95" height="100" rx="8" fill="#1E293B"/>
  <text x="35" y="420" fill="#94A3B8" font-family="sans-serif" font-size="9">Heavy Tee ₹899</text>
  <rect x="136" y="365" width="95" height="100" rx="8" fill="#1E293B"/>
  <text x="144" y="420" fill="#94A3B8" font-family="sans-serif" font-size="9">Relaxed Denim ₹1,999</text>
  <rect x="244" y="365" width="95" height="100" rx="8" fill="#1E293B"/>
  <text x="250" y="420" fill="#94A3B8" font-family="sans-serif" font-size="9">High Sneakers ₹2,499</text>

  <!-- Bundle Price Summary -->
  <text x="28" y="490" fill="#CBD5E1" font-family="sans-serif" font-size="12">Total Bundle Value (4 Items):</text>
  <text x="28" y="512" fill="#FFFFFF" font-family="sans-serif" font-size="18" font-weight="900">₹7,896</text>
  <rect x="120" y="496" width="100" height="20" rx="4" fill="#10B981"/>
  <text x="126" y="510" fill="#FFFFFF" font-family="sans-serif" font-size="10" font-weight="800">0% Discount / Full Margin</text>

  <!-- 1-Tap Add Look Button -->
  <rect x="16" y="565" width="343" height="48" rx="10" fill="#FF3F6C"/>
  <text x="75" y="594" fill="#FFFFFF" font-family="sans-serif" font-size="13" font-weight="900">🛍️ MOVE ENTIRE LOOK TO BAG (+₹450 AOV)</text>

  <!-- Strategic Guardrail Note -->
  <rect x="16" y="625" width="343" height="85" rx="12" fill="#0A0D14" stroke="#334155" stroke-width="1"/>
  <text x="28" y="648" fill="#10B981" font-family="sans-serif" font-size="11" font-weight="800">🛡️ AI STYLING GUARDRAILS ACTIVE</text>
  <text x="28" y="666" fill="#94A3B8" font-family="sans-serif" font-size="11">Color harmony & seasonal specs auto-verified against catalog graph.</text>
  <text x="28" y="682" fill="#94A3B8" font-family="sans-serif" font-size="11">Eliminates styling hesitation without discounting.</text>

  <!-- Bottom Nav -->
  <rect x="0" y="738" width="375" height="74" fill="#0A0D14" stroke="#1E293B" stroke-width="1"/>
  <text x="175" y="775" fill="#FF3F6C" font-family="sans-serif" font-size="12" font-weight="bold">Studio</text>
</svg>"""


# 3. Mobile App Screen 3: WhatsApp Peer Voting Card (375 x 812)
svg_mobile_whatsapp = """<svg width="375" height="812" viewBox="0 0 375 812" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="waGrad" x1="0" y1="0" x2="375" y2="812" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#0B141A"/>
      <stop offset="100%" stop-color="#111B21"/>
    </linearGradient>
  </defs>

  <rect width="375" height="812" rx="40" fill="url(#waGrad)"/>
  
  <!-- Status bar -->
  <text x="24" y="32" fill="#FFFFFF" font-family="sans-serif" font-size="14" font-weight="600">9:41</text>

  <!-- WhatsApp Header -->
  <rect x="0" y="44" width="375" height="56" fill="#202C33"/>
  <circle cx="36" cy="72" r="18" fill="#00A884"/>
  <text x="30" y="77" fill="#FFFFFF" font-family="sans-serif" font-size="14" font-weight="bold">F</text>
  <text x="65" y="68" fill="#E9EDEF" font-family="sans-serif" font-size="15" font-weight="700">Fashion Squad (4)</text>
  <text x="65" y="84" fill="#8696A0" font-family="sans-serif" font-size="11">Ananya, Rahul, Sneha, You</text>

  <!-- Chat Bubble with Micro Poll Card -->
  <rect x="16" y="120" width="343" height="420" rx="12" fill="#202C33"/>
  
  <!-- Myntra Header in Card -->
  <rect x="28" y="132" width="319" height="36" rx="6" fill="#111B21"/>
  <text x="40" y="155" fill="#FF3F6C" font-family="sans-serif" font-size="13" font-weight="900">myntra wishlist studio</text>
  <text x="220" y="154" fill="#8696A0" font-family="sans-serif" font-size="10">Help me decide! 👇</text>

  <!-- Poll Question -->
  <text x="28" y="190" fill="#E9EDEF" font-family="sans-serif" font-size="13" font-weight="800">Which jacket should I buy for Friday night?</text>

  <!-- Option A Card -->
  <rect x="28" y="205" width="319" height="100" rx="8" fill="#111B21" stroke="#00A884" stroke-width="1"/>
  <rect x="36" y="213" width="70" height="84" rx="6" fill="#2A3942"/>
  <text x="50" y="260" fill="#8696A0" font-family="sans-serif" font-size="9">Option A</text>
  <text x="115" y="232" fill="#E9EDEF" font-family="sans-serif" font-size="12" font-weight="700">Option A: Olive Canvas Bomber</text>
  <text x="115" y="250" fill="#FF3F6C" font-family="sans-serif" font-size="13" font-weight="800">₹2,499 (280 GSM)</text>
  <rect x="115" y="262" width="130" height="24" rx="12" fill="#00A884"/>
  <text x="135" y="278" fill="#FFFFFF" font-family="sans-serif" font-size="11" font-weight="800">Vote Option A (3 votes)</text>

  <!-- Option B Card -->
  <rect x="28" y="315" width="319" height="100" rx="8" fill="#111B21"/>
  <rect x="36" y="323" width="70" height="84" rx="6" fill="#2A3942"/>
  <text x="50" y="370" fill="#8696A0" font-family="sans-serif" font-size="9">Option B</text>
  <text x="115" y="342" fill="#E9EDEF" font-family="sans-serif" font-size="12" font-weight="700">Option B: Black Denim Trucker</text>
  <text x="115" y="360" fill="#FF3F6C" font-family="sans-serif" font-size="13" font-weight="800">₹1,999 (210 GSM)</text>
  <rect x="115" y="372" width="130" height="24" rx="12" fill="#2A3942"/>
  <text x="140" y="388" fill="#E9EDEF" font-family="sans-serif" font-size="11" font-weight="600">Vote Option B (1 vote)</text>

  <!-- Instant AI Fallback Badge -->
  <rect x="28" y="425" width="319" height="40" rx="6" fill="#2D0A4E"/>
  <text x="40" y="444" fill="#FF3F6C" font-family="sans-serif" font-size="11" font-weight="800">⚡ 2s AI FALLBACK BACKUP ACTIVE</text>
  <text x="40" y="457" fill="#E2E8F0" font-family="sans-serif" font-size="10">Community consensus choice: Option A (78% agreement)</text>

  <!-- Time stamp -->
  <text x="310" y="530" fill="#8696A0" font-family="sans-serif" font-size="10">9:42 AM</text>
</svg>"""


# 4. Mobile App Screen 4: Wishlist Studio Home & Collections (375 x 812)
svg_mobile_home = """<svg width="375" height="812" viewBox="0 0 375 812" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="homeGrad" x1="0" y1="0" x2="375" y2="812" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#0A0D14"/>
      <stop offset="100%" stop-color="#1E293B"/>
    </linearGradient>
  </defs>

  <rect width="375" height="812" rx="40" fill="url(#homeGrad)"/>

  <!-- Status Bar -->
  <text x="24" y="32" fill="#FFFFFF" font-family="sans-serif" font-size="14" font-weight="600">9:41</text>

  <!-- Header -->
  <rect x="0" y="44" width="375" height="56" fill="#0A0D14"/>
  <text x="20" y="78" fill="#FF3F6C" font-family="sans-serif" font-size="20" font-weight="900">myntra</text>
  <text x="120" y="77" fill="#FFFFFF" font-family="sans-serif" font-size="15" font-weight="700">Wishlist Studio</text>
  <rect x="290" y="60" width="70" height="28" rx="14" fill="#2D0A4E"/>
  <text x="302" y="78" fill="#FFFFFF" font-family="sans-serif" font-size="11" font-weight="800">Bag (3)</text>

  <!-- Occasion Pills Scroll Horizontal -->
  <text x="16" y="125" fill="#94A3B8" font-family="sans-serif" font-size="12" font-weight="700">SMART OCCASION COLLECTIONS</text>
  <rect x="16" y="135" width="110" height="32" rx="16" fill="#FF3F6C"/>
  <text x="28" y="156" fill="#FFFFFF" font-family="sans-serif" font-size="11" font-weight="800">Workwear (5)</text>

  <rect x="134" y="135" width="110" height="32" rx="16" fill="#1E293B"/>
  <text x="146" y="156" fill="#94A3B8" font-family="sans-serif" font-size="11" font-weight="700">Streetwear (4)</text>

  <rect x="252" y="135" width="110" height="32" rx="16" fill="#1E293B"/>
  <text x="264" y="156" fill="#94A3B8" font-family="sans-serif" font-size="11" font-weight="700">Party Night (3)</text>

  <!-- Saved Items Grid -->
  <rect x="16" y="185" width="168" height="240" rx="12" fill="#121826" stroke="#334155" stroke-width="1"/>
  <rect x="24" y="193" width="152" height="140" rx="8" fill="#1E293B"/>
  <text x="32" y="350" fill="#FFFFFF" font-family="sans-serif" font-size="12" font-weight="700">Roadster Cargo</text>
  <text x="32" y="368" fill="#FF3F6C" font-family="sans-serif" font-size="13" font-weight="800">₹1,999</text>
  <rect x="32" y="380" width="136" height="32" rx="6" fill="#FF3F6C"/>
  <text x="55" y="401" fill="#FFFFFF" font-family="sans-serif" font-size="11" font-weight="800">Move to Bag</text>

  <rect x="191" y="185" width="168" height="240" rx="12" fill="#121826" stroke="#334155" stroke-width="1"/>
  <rect x="199" y="193" width="152" height="140" rx="8" fill="#1E293B"/>
  <text x="207" y="350" fill="#FFFFFF" font-family="sans-serif" font-size="12" font-weight="700">HIGHLANDER Shirt</text>
  <text x="207" y="368" fill="#FF3F6C" font-family="sans-serif" font-size="13" font-weight="800">₹1,499</text>
  <rect x="207" y="380" width="136" height="32" rx="6" fill="#FF3F6C"/>
  <text x="230" y="401" fill="#FFFFFF" font-family="sans-serif" font-size="11" font-weight="800">Move to Bag</text>

  <!-- Bottom Nav -->
  <rect x="0" y="738" width="375" height="74" fill="#0A0D14" stroke="#1E293B" stroke-width="1"/>
  <text x="175" y="775" fill="#FF3F6C" font-family="sans-serif" font-size="12" font-weight="bold">Studio</text>
</svg>"""


# 5. Desktop Web Workspace Screen (1440 x 900)
svg_desktop_web = """<svg width="1440" height="900" viewBox="0 0 1440 900" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="webGrad" x1="0" y1="0" x2="1440" y2="900" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#0A0D14"/>
      <stop offset="100%" stop-color="#121826"/>
    </linearGradient>
    <linearGradient id="pinkGrad" x1="0" y1="0" x2="200" y2="0" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#FF3F6C"/>
      <stop offset="100%" stop-color="#FF6B8B"/>
    </linearGradient>
  </defs>

  <rect width="1440" height="900" fill="url(#webGrad)"/>

  <!-- Top Navigation Header Bar -->
  <rect x="0" y="0" width="1440" height="70" fill="#121826" stroke="#1E293B" stroke-width="1"/>
  <text x="40" y="44" fill="#FF3F6C" font-family="sans-serif" font-size="24" font-weight="900" letter-spacing="-1">myntra</text>
  <text x="145" y="42" fill="#FFFFFF" font-family="sans-serif" font-size="16" font-weight="800">Growth Lab — Wishlist Studio</text>

  <rect x="420" y="18" width="500" height="36" rx="18" fill="#1E293B"/>
  <text x="440" y="41" fill="#64748B" font-family="sans-serif" font-size="13">Search products, categories or comparison specs...</text>

  <rect x="1240" y="16" width="160" height="38" rx="8" fill="url(#pinkGrad)"/>
  <text x="1265" y="40" fill="#FFFFFF" font-family="sans-serif" font-size="13" font-weight="800">🛍️ Shopping Bag (3)</text>

  <!-- Left Sidebar Navigation -->
  <rect x="0" y="70" width="240" height="830" fill="#0A0D14" stroke="#1E293B" stroke-width="1"/>
  <rect x="20" y="95" width="200" height="40" rx="8" fill="#2D0A4E"/>
  <text x="50" y="120" fill="#FFFFFF" font-family="sans-serif" font-size="13" font-weight="800">🛍️ Wishlist Studio MVP</text>

  <rect x="20" y="150" width="200" height="40" rx="8" fill="transparent"/>
  <text x="50" y="175" fill="#94A3B8" font-family="sans-serif" font-size="13" font-weight="600">📊 User Research & NLP</text>

  <rect x="20" y="205" width="200" height="40" rx="8" fill="transparent"/>
  <text x="50" y="230" fill="#94A3B8" font-family="sans-serif" font-size="13" font-weight="600">📈 Strategy & Metrics</text>

  <!-- Financial KPI Metrics Widget in Sidebar -->
  <rect x="20" y="680" width="200" height="190" rx="10" fill="#1E293B"/>
  <text x="32" y="705" fill="#FF3F6C" font-family="sans-serif" font-size="11" font-weight="800">TARGET LIFT IMPACT</text>
  <text x="32" y="730" fill="#FFFFFF" font-family="sans-serif" font-size="20" font-weight="900">+300 bps</text>
  <text x="32" y="748" fill="#94A3B8" font-family="sans-serif" font-size="11">Conv: 7.5% → 10.5%</text>

  <text x="32" y="778" fill="#10B981" font-family="sans-serif" font-size="16" font-weight="800">+₹49.5 Cr / mo</text>
  <text x="32" y="794" fill="#94A3B8" font-family="sans-serif" font-size="11">Incremental GMV Lift</text>

  <text x="32" y="824" fill="#818CF8" font-family="sans-serif" font-size="14" font-weight="800">221x Feature ROI</text>
  <text x="32" y="840" fill="#94A3B8" font-family="sans-serif" font-size="11">Payback Period &lt; 4 Days</text>

  <!-- Main Content Area: Side-by-Side Comparison Grid Workspace -->
  <rect x="270" y="95" width="1130" height="775" rx="16" fill="#121826" stroke="#1E293B" stroke-width="1"/>

  <!-- Module Header Bar -->
  <text x="300" y="135" fill="#FFFFFF" font-family="sans-serif" font-size="20" font-weight="800">Side-by-Side Spec &amp; Fabric GSM Comparison Studio</text>
  <text x="300" y="156" fill="#94A3B8" font-family="sans-serif" font-size="13">Inline evaluation studio eliminating choice overload without price discounts</text>

  <!-- Spec Comparison Table Header -->
  <rect x="300" y="180" width="1070" height="40" rx="8" fill="#1E293B"/>
  <text x="320" y="205" fill="#94A3B8" font-family="sans-serif" font-size="12" font-weight="700">SPECIFICATION DIMENSION</text>
  <text x="560" y="205" fill="#FFFFFF" font-family="sans-serif" font-size="12" font-weight="800">PRODUCT #1: Heavy Duty Cargo</text>
  <text x="840" y="205" fill="#FFFFFF" font-family="sans-serif" font-size="12" font-weight="800">PRODUCT #2: Slim Stretch Cargo</text>
  <text x="1120" y="205" fill="#FFFFFF" font-family="sans-serif" font-size="12" font-weight="800">PRODUCT #3: Oversized Utility</text>

  <!-- Row 1: Fabric GSM Weight -->
  <rect x="300" y="230" width="1070" height="55" fill="#0A0D14" stroke="#1E293B" stroke-width="1"/>
  <text x="320" y="262" fill="#E2E8F0" font-family="sans-serif" font-size="13" font-weight="700">Fabric GSM Weight</text>

  <rect x="560" y="242" width="120" height="30" rx="6" fill="#2D0A4E"/>
  <text x="575" y="262" fill="#FFFFFF" font-family="sans-serif" font-size="12" font-weight="800">240 GSM (Heavy)</text>

  <rect x="840" y="242" width="120" height="30" rx="6" fill="#334155"/>
  <text x="855" y="262" fill="#CBD5E1" font-family="sans-serif" font-size="12" font-weight="600">160 GSM (Light)</text>

  <rect x="1120" y="242" width="120" height="30" rx="6" fill="#2D0A4E"/>
  <text x="1135" y="262" fill="#FFFFFF" font-family="sans-serif" font-size="12" font-weight="800">220 GSM (Heavy)</text>

  <!-- Row 2: Fit Score & Consensus -->
  <rect x="300" y="285" width="1070" height="55" fill="#121826" stroke="#1E293B" stroke-width="1"/>
  <text x="320" y="317" fill="#E2E8F0" font-family="sans-serif" font-size="13" font-weight="700">Fit Rating Consensus</text>
  <text x="560" y="317" fill="#10B981" font-family="sans-serif" font-size="13" font-weight="800">✓ 88% True to Size</text>
  <text x="840" y="317" fill="#F59E0B" font-family="sans-serif" font-size="13" font-weight="800">⚠️ 62% Slim Variance</text>
  <text x="1120" y="317" fill="#10B981" font-family="sans-serif" font-size="13" font-weight="800">✓ 91% True to Size</text>

  <!-- Row 3: Price & Action -->
  <rect x="300" y="340" width="1070" height="70" fill="#0A0D14" stroke="#1E293B" stroke-width="1"/>
  <text x="320" y="380" fill="#E2E8F0" font-family="sans-serif" font-size="13" font-weight="700">Price &amp; Action</text>

  <text x="560" y="368" fill="#FF3F6C" font-family="sans-serif" font-size="16" font-weight="900">₹1,999</text>
  <rect x="560" y="378" width="130" height="26" rx="6" fill="#FF3F6C"/>
  <text x="580" y="395" fill="#FFFFFF" font-family="sans-serif" font-size="11" font-weight="800">Choose This One</text>

  <text x="840" y="368" fill="#FF3F6C" font-family="sans-serif" font-size="16" font-weight="900">₹1,499</text>
  <rect x="840" y="378" width="130" height="26" rx="6" fill="#334155"/>
  <text x="860" y="395" fill="#FFFFFF" font-family="sans-serif" font-size="11" font-weight="800">Choose This One</text>

  <text x="1120" y="368" fill="#FF3F6C" font-family="sans-serif" font-size="16" font-weight="900">₹2,299</text>
  <rect x="1120" y="378" width="130" height="26" rx="6" fill="#334155"/>
  <text x="1140" y="395" fill="#FFFFFF" font-family="sans-serif" font-size="11" font-weight="800">Choose This One</text>

  <!-- Bottom Workspace Widgets: AI Outfit Matcher Preview & Social WhatsApp Link -->
  <rect x="300" y="440" width="520" height="390" rx="12" fill="#1E293B"/>
  <text x="320" y="475" fill="#4F46E5" font-family="sans-serif" font-size="16" font-weight="800">✨ AI Outfit Matcher &amp; Visualizer (+₹450 AOV Lift)</text>
  <text x="320" y="495" fill="#94A3B8" font-family="sans-serif" font-size="12">Coordinates selected Wishlist item with complementary catalog pieces</text>
  <rect x="320" y="515" width="480" height="220" rx="8" fill="#121826"/>
  <text x="340" y="550" fill="#FFFFFF" font-family="sans-serif" font-size="13" font-weight="800">Curated Outfit: Weekend Streetwear Look</text>
  <rect x="320" y="750" width="480" height="44" rx="8" fill="url(#pinkGrad)"/>
  <text x="460" y="777" fill="#FFFFFF" font-family="sans-serif" font-size="13" font-weight="800">🛍️ MOVE ENTIRE LOOK TO BAG</text>

  <rect x="850" y="440" width="520" height="390" rx="12" fill="#054740"/>
  <text x="870" y="475" fill="#25D366" font-family="sans-serif" font-size="16" font-weight="800">💬 1-Tap WhatsApp Social Voting Link</text>
  <text x="870" y="495" fill="#E2E8F0" font-family="sans-serif" font-size="12">Generates shareable peer voting micro-card with 2s AI fallback</text>
  <rect x="870" y="515" width="480" height="220" rx="8" fill="#111B21"/>
  <text x="890" y="550" fill="#E9EDEF" font-family="sans-serif" font-size="13" font-weight="700">Live Vote Tally: Option A (75%) vs Option B (25%)</text>
  <rect x="870" y="750" width="480" height="44" rx="8" fill="#25D366"/>
  <text x="1000" y="777" fill="#FFFFFF" font-family="sans-serif" font-size="13" font-weight="800">🚀 Share Micro-Poll to WhatsApp</text>
</svg>"""


# 6. Figma Design Tokens Schema (JSON)
figma_tokens = {
  "name": "Myntra Wishlist Studio Figma Design System",
  "version": "2.4.0",
  "colorTokens": {
    "brand-myntra-pink": "#FF3F6C",
    "brand-deep-purple": "#2D0A4E",
    "neutral-dark-navy": "#0A0D14",
    "neutral-card-bg": "#FFFFFF",
    "accent-indigo-glow": "#4F46E5",
    "status-emerald-green": "#10B981",
    "status-amber-gold": "#F59E0B"
  },
  "frames": [
    { "name": "01_Figma_Mobile_Spec_Comparison_Matrix.svg", "dimensions": "375x812", "type": "Mobile iOS/Android Frame" },
    { "name": "02_Figma_Mobile_AI_Outfit_Coordinator.svg", "dimensions": "375x812", "type": "Mobile iOS/Android Frame" },
    { "name": "03_Figma_Mobile_WhatsApp_Voting_Card.svg", "dimensions": "375x812", "type": "Mobile Micro Card" },
    { "name": "04_Figma_Mobile_Wishlist_Studio_Home.svg", "dimensions": "375x812", "type": "Mobile Wishlist Home" },
    { "name": "05_Figma_Desktop_Web_Wishlist_Studio.svg", "dimensions": "1440x900", "type": "Desktop Web Workspace" }
  ]
}

def main():
    target_dir = os.path.join(os.getcwd(), 'figma_design_assets')
    os.makedirs(target_dir, exist_ok=True)
    
    create_svg_file(os.path.join(target_dir, '01_Figma_Mobile_Spec_Comparison_Matrix.svg'), svg_mobile_spec_matrix)
    create_svg_file(os.path.join(target_dir, '02_Figma_Mobile_AI_Outfit_Coordinator.svg'), svg_mobile_ai_outfit)
    create_svg_file(os.path.join(target_dir, '03_Figma_Mobile_WhatsApp_Voting_Card.svg'), svg_mobile_whatsapp)
    create_svg_file(os.path.join(target_dir, '04_Figma_Mobile_Wishlist_Studio_Home.svg'), svg_mobile_home)
    create_svg_file(os.path.join(target_dir, '05_Figma_Desktop_Web_Wishlist_Studio.svg'), svg_desktop_web)
    
    with open(os.path.join(target_dir, '06_Figma_Design_Tokens.json'), 'w', encoding='utf-8') as f:
        json.dump(figma_tokens, f, indent=2)
    print("Figma design tokens created successfully.")

if __name__ == '__main__':
    main()
