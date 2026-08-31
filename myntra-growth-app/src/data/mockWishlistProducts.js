// Realistic Wishlist Product Catalog for Myntra Wishlist Studio MVP

export const WISHLIST_COLLECTIONS = [
  { id: 'ALL', name: 'All Saved Items', count: 12 },
  { id: 'STREETWEAR', name: 'Streetwear & Denim', count: 4, occasion: 'Casual & College' },
  { id: 'WORKWEAR', name: 'Office & Blazers', count: 3, occasion: 'Work & Meetings' },
  { id: 'FOOTWEAR', name: 'Sneakers & Shoes', count: 3, occasion: 'Daily Casual' },
  { id: 'WEEKEND', name: 'Weekend Party Outfits', count: 2, occasion: 'Night Out' },
];

export const WISHLIST_PRODUCTS = [
  // 1. Streetwear & Denim Group
  {
    id: 'prod-01',
    name: 'Roadster Relaxed Fit 6-Pocket Baggy Cargo Pants',
    brand: 'Roadster',
    category: 'STREETWEAR',
    price: 1399,
    originalPrice: 2799,
    rating: 4.2,
    ratingCount: 3820,
    image: 'https://images.unsplash.com/photo-1624378439575-d8705ad7ae80?w=600&auto=format&fit=crop&q=80',
    customerImages: [
      'https://images.unsplash.com/photo-1517445312882-bc9910d016b7?w=400&auto=format&fit=crop&q=80',
      'https://images.unsplash.com/photo-1509631179647-0177331693ae?w=400&auto=format&fit=crop&q=80'
    ],
    fabric: '100% Heavy Twill Cotton (280 GSM)',
    fitScore: '91% Say True to Size (Baggy Cut)',
    returnRisk: 'Low (12% Return Rate)',
    color: 'Olive Green',
    keyPros: 'Durable heavyweight fabric, deep cargo pockets, fade-resistant wash',
    daysInWishlist: 18,
    outfitSuggestions: [
      {
        lookName: 'Urban Street Casual',
        description: 'Pair with an oversized white graphic tee, chunky retro sneakers, and a crossbody sling bag.',
        top: 'Highlander Oversized White Graphic Tee (₹699)',
        shoes: 'Puma Rebound Retro High-Tops (₹3,499)',
        accessory: 'Urban Monkey Matte Black Sling (₹1,199)',
        lookTotal: 6796,
      },
      {
        lookName: 'Monochrome Street Fit',
        description: 'Layer with a black cropped bomber jacket and chunky combat boots for a sharp street silhouette.',
        top: 'H&M Boxy Fit Black T-Shirt (₹799)',
        shoes: 'Red Tape Chunky Black Boots (₹2,299)',
        accessory: 'Stainless Steel Curb Chain (₹499)',
        lookTotal: 4996,
      }
    ]
  },
  {
    id: 'prod-02',
    name: 'Highlander Men Wide Leg Relaxed Cotton Cargo Trousers',
    brand: 'Highlander',
    category: 'STREETWEAR',
    price: 1199,
    originalPrice: 2499,
    rating: 4.0,
    ratingCount: 2150,
    image: 'https://images.unsplash.com/photo-1506630448388-4e683c67ddb0?w=600&auto=format&fit=crop&q=80',
    customerImages: [
      'https://images.unsplash.com/photo-1517445312882-bc9910d016b7?w=400&auto=format&fit=crop&q=80',
      'https://images.unsplash.com/photo-1552374196-1ab2a1c593e8?w=400&auto=format&fit=crop&q=80'
    ],
    fabric: 'Cotton Poly Blend (210 GSM)',
    fitScore: '78% Say Runs Slightly Long',
    returnRisk: 'Medium (19% Return Rate)',
    color: 'Pitch Black',
    keyPros: 'Lightweight breathable feel, elastic waistband, casual streetwear vibe',
    daysInWishlist: 24,
    outfitSuggestions: [
      {
        lookName: 'Minimalist Monochrome',
        description: 'Style with an off-white boxy tee and low-top minimalist court sneakers.',
        top: 'Mast & Harbour Raw Hem Tee (₹599)',
        shoes: 'HRX Minimalist White Sneakers (₹1,499)',
        accessory: 'Silver Signet Ring Set (₹399)',
        lookTotal: 3696,
      }
    ]
  },
  {
    id: 'prod-03',
    name: "Levi's Men 568 Loose Straight Fit Vintage Wash Jeans",
    brand: "Levi's",
    category: 'STREETWEAR',
    price: 2699,
    originalPrice: 4599,
    rating: 4.5,
    ratingCount: 5410,
    image: 'https://images.unsplash.com/photo-1541099649105-f69ad21f3246?w=600&auto=format&fit=crop&q=80',
    customerImages: [
      'https://images.unsplash.com/photo-1512436991641-6745cdb1723f?w=400&auto=format&fit=crop&q=80',
      'https://images.unsplash.com/photo-1506152983158-b4a74a01c721?w=400&auto=format&fit=crop&q=80'
    ],
    fabric: '100% Rigid Denim (13.5 oz / 380 GSM)',
    fitScore: '96% Say True to Size (Classic Vintage Straight)',
    returnRisk: 'Very Low (6% Return Rate)',
    color: 'Light Vintage Indigo',
    keyPros: 'Authentic 90s denim drape, premium durability, zero color bleed',
    daysInWishlist: 31,
    outfitSuggestions: [
      {
        lookName: '90s Retro Aesthetic',
        description: 'Pair with a relaxed waffle knit polo and vintage brown leather loafers.',
        top: 'Mango Man Ribbed Knit Polo (₹1,990)',
        shoes: 'Bata Heritage Leather Loafers (₹2,799)',
        accessory: 'Tortoiseshell Sunglasses (₹899)',
        lookTotal: 8387,
      }
    ]
  },
  {
    id: 'prod-04',
    name: 'Freakins Raw Hem Baggy Skater Cargo Denim',
    brand: 'Freakins',
    category: 'STREETWEAR',
    price: 1899,
    originalPrice: 3299,
    rating: 4.1,
    ratingCount: 1420,
    image: 'https://images.unsplash.com/photo-1582552938357-32b906df40cb?w=600&auto=format&fit=crop&q=80',
    customerImages: [
      'https://images.unsplash.com/photo-1517445312882-bc9910d016b7?w=400&auto=format&fit=crop&q=80'
    ],
    fabric: 'Cotton Denim (300 GSM)',
    fitScore: '84% Say Runs Generously Oversized',
    returnRisk: 'Medium (16% Return Rate)',
    color: 'Washed Charcoal Grey',
    keyPros: 'Distressed raw edge hems, extra wide skater cut',
    daysInWishlist: 12,
    outfitSuggestions: [
      {
        lookName: 'Skater Drip',
        description: 'Style with a boxy zip-up hoodie and high-top skate shoes.',
        top: 'Urbanic Washed Zip-Up Hoodie (₹1,690)',
        shoes: 'Vans Old Skool Classics (₹4,499)',
        accessory: 'Silver Beaded Chain (₹449)',
        lookTotal: 8537,
      }
    ]
  },

  // 2. Workwear & Blazers Group
  {
    id: 'prod-05',
    name: 'Mango Single-Breasted Tailored Structured Blazer',
    brand: 'Mango',
    category: 'WORKWEAR',
    price: 3990,
    originalPrice: 6990,
    rating: 4.6,
    ratingCount: 1240,
    image: 'https://images.unsplash.com/photo-1591047139829-d91aecb6caea?w=600&auto=format&fit=crop&q=80',
    customerImages: [
      'https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=400&auto=format&fit=crop&q=80'
    ],
    fabric: 'Viscose Blend with Breathable Satin Lining (310 GSM)',
    fitScore: '94% Say Tailored Fit / True to Size',
    returnRisk: 'Very Low (7% Return Rate)',
    color: 'Lilac Pastel',
    keyPros: 'Wrinkle-resistant fabric, structured padded shoulders, luxury horn buttons',
    daysInWishlist: 27,
    outfitSuggestions: [
      {
        lookName: 'Executive Power Pastel',
        description: 'Pair with high-waist off-white wide trousers, a silk camisole, and pointed nude pumps.',
        top: 'H&M Satin Cami Top (₹999)',
        shoes: 'Metro Pointed Toe Nude Pumps (₹2,490)',
        accessory: 'Minimalist Gold Layered Necklace (₹599)',
        lookTotal: 8078,
      },
      {
        lookName: 'Friday Night Smart Casual',
        description: 'Dress it down with straight vintage blue denim, a ribbed white tank, and minimal kitten heels.',
        top: 'Mango Ribbed Tank Top (₹890)',
        shoes: 'Zudio Kitten Heel Mules (₹1,299)',
        accessory: 'Structured Shoulder Bag (₹1,699)',
        lookTotal: 7878,
      }
    ]
  },
  {
    id: 'prod-06',
    name: 'H&M Oversized Double-Breasted Linen Blend Jacket',
    brand: 'H&M',
    category: 'WORKWEAR',
    price: 2999,
    originalPrice: 4999,
    rating: 4.3,
    ratingCount: 3180,
    image: 'https://images.unsplash.com/photo-1594938298603-c8148c4dae35?w=600&auto=format&fit=crop&q=80',
    customerImages: [
      'https://images.unsplash.com/photo-1584273143981-41c073dfe8f8?w=400&auto=format&fit=crop&q=80',
      'https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=400&auto=format&fit=crop&q=80'
    ],
    fabric: '55% Linen 45% Cotton (220 GSM)',
    fitScore: '82% Say Relaxed Oversized Fit',
    returnRisk: 'Low (11% Return Rate)',
    color: 'Oatmeal Beige',
    keyPros: 'Ultra-breathable summer linen, natural texture, relaxed silhouette',
    daysInWishlist: 15,
    outfitSuggestions: [
      {
        lookName: 'Summer Boardroom Casual',
        description: 'Match with pleated linen trousers and tan leather slides for effortless chic.',
        top: 'Zara Pleated Beige Trousers (₹2,990)',
        shoes: 'Bata Tan Leather Slides (₹1,499)',
        accessory: 'Woven Straw Tote Bag (₹1,299)',
        lookTotal: 8787,
      }
    ]
  },
  {
    id: 'prod-07',
    name: 'Zara Tailored Wool-Blend Crop Blazer with Lapels',
    brand: 'Zara',
    category: 'WORKWEAR',
    price: 4590,
    originalPrice: 5990,
    rating: 4.4,
    ratingCount: 890,
    image: 'https://images.unsplash.com/photo-1539109136881-3be0616acf4b?w=600&auto=format&fit=crop&q=80',
    customerImages: [
      'https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=400&auto=format&fit=crop&q=80'
    ],
    fabric: 'Wool Poly Elastane Blend (340 GSM)',
    fitScore: '89% Say True to Size (Cropped Length)',
    returnRisk: 'Low (9% Return Rate)',
    color: 'Charcoal Houndstooth',
    keyPros: 'Modern cropped waistline, high thermal retention, sharp shoulder contour',
    daysInWishlist: 22,
    outfitSuggestions: [
      {
        lookName: 'High-Fashion Tailoring',
        description: 'Pair with ultra high-waist palazzo trousers and chunky platform oxfords.',
        top: 'Zara High-Waist Wide Pants (₹3,290)',
        shoes: 'Aldo Platform Oxfords (₹4,999)',
        accessory: 'Silver Buckle Belt (₹799)',
        lookTotal: 13678,
      }
    ]
  },

  // 3. Footwear & Sneakers Group
  {
    id: 'prod-08',
    name: 'Puma Unisex Rebound V6 Low Retro Sneakers',
    brand: 'Puma',
    category: 'FOOTWEAR',
    price: 2499,
    originalPrice: 4999,
    rating: 4.4,
    ratingCount: 8430,
    image: 'https://images.unsplash.com/photo-1549298916-b41d501d3772?w=600&auto=format&fit=crop&q=80',
    customerImages: [
      'https://images.unsplash.com/photo-1525966222134-fcfa99b8ae77?w=400&auto=format&fit=crop&q=80'
    ],
    fabric: 'Synthetic Leather with SoftFoam+ Cushioning',
    fitScore: '92% Say True to Size',
    returnRisk: 'Very Low (5% Return Rate)',
    color: 'Puma White / Forest Green',
    keyPros: 'Superior all-day insole cushioning, durable cupsole, easy wipe clean',
    daysInWishlist: 19,
    outfitSuggestions: [
      {
        lookName: 'Daily College Essential',
        description: 'Match with relaxed light wash jeans and an oversized hoodie.',
        top: 'Roadster Heavyweight Grey Hoodie (₹1,299)',
        shoes: 'Included',
        accessory: 'Canvas Backpack (₹1,499)',
        lookTotal: 5297,
      }
    ]
  },
  {
    id: 'prod-09',
    name: 'Red Tape Men Off-White Walking Lifestyle Sneakers',
    brand: 'Red Tape',
    category: 'FOOTWEAR',
    price: 1399,
    originalPrice: 5699,
    rating: 4.1,
    ratingCount: 12900,
    image: 'https://images.unsplash.com/photo-1560769629-975ec94e6a86?w=600&auto=format&fit=crop&q=80',
    customerImages: [
      'https://images.unsplash.com/photo-1595950653106-6c9ebd614d3a?w=400&auto=format&fit=crop&q=80'
    ],
    fabric: 'Mesh PU Upper with EVA Outsole',
    fitScore: '74% Say Order 1 Size Up',
    returnRisk: 'High (22% Return Rate due to sizing variation)',
    color: 'Off-White / Beige',
    keyPros: 'Extremely lightweight, high arch support',
    daysInWishlist: 29,
    outfitSuggestions: [
      {
        lookName: 'Athleisure Run',
        description: 'Style with black tapered joggers and a breathable athletic tee.',
        top: 'HRX Dri-Fit Running Tee (₹599)',
        shoes: 'Included',
        accessory: 'Sports Cap (₹499)',
        lookTotal: 2497,
      }
    ]
  },
  {
    id: 'prod-10',
    name: 'Nike Men Court Vision Low Next Nature Sneakers',
    brand: 'Nike',
    category: 'FOOTWEAR',
    price: 4995,
    originalPrice: 4995,
    rating: 4.7,
    ratingCount: 6810,
    image: 'https://images.unsplash.com/photo-1597045566677-8cf032ed6634?w=600&auto=format&fit=crop&q=80',
    customerImages: [
      'https://images.unsplash.com/photo-1584735935682-2f2b69dff9d2?w=400&auto=format&fit=crop&q=80'
    ],
    fabric: 'Recycled Synthetic Leather Upper',
    fitScore: '95% Say True to Size (Slightly Snug Fit)',
    returnRisk: 'Very Low (4% Return Rate)',
    color: 'Triple White',
    keyPros: 'Iconic 80s basketball silhouette, premium stitched overlays, zero flex crease',
    daysInWishlist: 35,
    outfitSuggestions: [
      {
        lookName: 'Clean Street Minimalist',
        description: 'Pair with relaxed black chinos and an oversized denim overshirt.',
        top: 'Levi’s Denim Trucker Overshirt (₹3,299)',
        shoes: 'Included',
        accessory: 'Silver Mesh Watch (₹2,499)',
        lookTotal: 10793,
      }
    ]
  },

  // 4. Weekend Party Outfits Group
  {
    id: 'prod-11',
    name: 'Urbanic Velvet Cowl Neck Emerald Bodycon Party Dress',
    brand: 'Urbanic',
    category: 'WEEKEND',
    price: 2190,
    originalPrice: 3490,
    rating: 4.5,
    ratingCount: 1840,
    image: 'https://images.unsplash.com/photo-1566174053879-31528523f8ae?w=600&auto=format&fit=crop&q=80',
    customerImages: [
      'https://images.unsplash.com/photo-1515886657613-9f3515b0c78f?w=400&auto=format&fit=crop&q=80'
    ],
    fabric: 'Premium Stretch Plush Velvet (290 GSM)',
    fitScore: '93% Say Body-Hugging Stretch Fit',
    returnRisk: 'Low (8% Return Rate)',
    color: 'Emerald Jewel Green',
    keyPros: 'Lustrous velvet drape, flattering cowl neckline, side slit ease',
    daysInWishlist: 8,
    outfitSuggestions: [
      {
        lookName: 'Glam Night Out',
        description: 'Pair with strappy metallic stiletto heels and a sparkling crystal clutch.',
        top: 'Included (Velvet Dress)',
        shoes: 'Catwalk Metallic Gold Stilettos (₹2,699)',
        accessory: 'Crystal Embellished Minaudiere Clutch (₹1,899)',
        lookTotal: 6788,
      }
    ]
  },
  {
    id: 'prod-12',
    name: 'Rare Rabbit Textured Silk Blend Cuban Collar Shirt',
    brand: 'Rare Rabbit',
    category: 'WEEKEND',
    price: 3499,
    originalPrice: 4999,
    rating: 4.6,
    ratingCount: 970,
    image: 'https://images.unsplash.com/photo-1602810318383-e386cc2a3ccf?w=600&auto=format&fit=crop&q=80',
    customerImages: [
      'https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?w=400&auto=format&fit=crop&q=80'
    ],
    fabric: 'Silk-Modal Slub Blend (180 GSM)',
    fitScore: '90% Say True to Size (Relaxed Resort Fit)',
    returnRisk: 'Low (6% Return Rate)',
    color: 'Champagne Ivory',
    keyPros: 'Ultra-luxurious handfeel, natural sheen, relaxed camp collar',
    daysInWishlist: 14,
    outfitSuggestions: [
      {
        lookName: 'Rooftop Cocktail Party',
        description: 'Pair with tailored black pleated trousers and Belgian leather loafers.',
        top: 'Included (Silk Shirt)',
        shoes: 'Aldo Belgian Suede Loafers (₹5,999)',
        accessory: 'Minimalist Chronograph Leather Watch (₹3,499)',
        lookTotal: 12997,
      }
    ]
  }
];
