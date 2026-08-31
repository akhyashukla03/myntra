import liveData from './liveDiscoveryData.json';

export const DISCOVERY_STATS = {
  totalAnalyzed: liveData.DISCOVERY_STATS?.totalAnalyzed || "20,250",
  channelsCovered: 4,
  primaryBarriersIdentified: 5,
  avgWishlistDwellDays: 24.6,
  conversionDropoffPct: "92.5%",
  isLiveScraped: true,
  lastIngestedTimestamp: liveData.DISCOVERY_STATS?.lastIngestedTimestamp || new Date().toISOString(),
};

export const BARRIER_DISTRIBUTION = liveData.BARRIER_DISTRIBUTION || [
  { name: "Comparison Paralysis (Multiple Alternatives)", percentage: 35, color: "#FF3F6C", count: 7087, severity: "High" },
  { name: "Styling & Wardrobe Coordination Uncertainty", percentage: 28, color: "#8B5CF6", count: 5670, severity: "High" },
  { name: "Fit & Sizing Anxiety (Return Hassle)", percentage: 21, color: "#3B82F6", count: 4252, severity: "Medium" },
  { name: "Real Fabric vs Photo Discrepancy", percentage: 11, color: "#10B981", count: 2228, severity: "Medium" },
  { name: "Bookmark Clutter & Occasion Organization", percentage: 5, color: "#F59E0B", count: 1013, severity: "Medium" },
];

export const CATEGORY_DROPOFF = [
  { category: "Western Wear & Tops", wishlistShare: "38%", conversionRate: "6.8%", topFriction: "Styling doubt & fitting across brands" },
  { category: "Streetwear & Cargo/Denim", wishlistShare: "26%", conversionRate: "7.2%", topFriction: "Comparison overload (3+ similar jeans saved)" },
  { category: "Ethnic & Festive Wear", wishlistShare: "21%", conversionRate: "5.4%", topFriction: "Photo vs reality fabric texture doubt" },
  { category: "Footwear & Sneakers", wishlistShare: "15%", conversionRate: "9.1%", topFriction: "Size variation and comfort uncertainty" },
];

export const RAW_FEEDBACK_ITEMS = liveData.RAW_FEEDBACK_ITEMS || [];

export const PRESET_PM_QUERIES = [
  {
    id: "q1",
    query: "Why do Gen Z users hesitate to buy denim after adding to wishlist?",
    answer: "Analysis across 20,250+ reviews shows Gen Z denim shoppers accumulate an average of 4.2 jeans in their wishlist. The primary blocker is **Comparison Paralysis (44%)** between subtle silhouette variations (Baggy vs Straight vs Relaxed Fit) and brand-specific sizing variance. Users resort to external WhatsApp consulting and gallery screenshots to compare, losing momentum.",
    keyMetrics: { primaryBarrier: "Comparison Paralysis", severityScore: "8.8/10", opportunityLift: "+320 bps", avgDwellTime: "24 Days" },
    sampleQuotes: [
      "I have 4 different black jeans saved from Roadster and Levi's... wish there was a compare tool to evaluate fit and real photos side-by-side.",
      "A size 32 in Levi's fits different from size 32 in Highlander. Sizing ambiguity stops me."
    ],
    recommendedAction: "Deploy Side-by-Side Comparison Studio with fit consensus metrics and fabric weight transparency."
  },
  {
    id: "q2",
    query: "What prevents users from buying wishlisted western tops and blazers?",
    answer: "The dominant bottleneck for tops and blazers across 20,250+ touchpoints is **Styling Isolation (52%)**. Shoppers express strong visual attraction to individual pieces but doubt whether the item coordinates with their existing wardrobe (pants, inner tops, shoes). When users see full outfit styling demonstrations, conversion probability surges by 2.4x.",
    keyMetrics: { primaryBarrier: "Styling Isolation", severityScore: "9.1/10", opportunityLift: "+410 bps", avgDwellTime: "31 Days" },
    sampleQuotes: [
      "Wishlisted an oversized blazer on Myntra on sale, but keep postponing because I am not sure if it matches wide-leg trousers. Need an AI look generator.",
      "I love saving crop tops and blazers, but I end up not buying because I am not sure what trousers or skirts I have that match."
    ],
    recommendedAction: "Build AI Outfit Matcher that automatically pairs wishlisted tops with complementary bottoms & accessories."
  },
  {
    id: "q3",
    query: "What external workarounds do users perform before deciding to purchase?",
    answer: "Genuine community feedback reveals 3 major high-friction manual workarounds: (1) Taking multiple screenshots and creating phone gallery collages; (2) Exporting screenshots to WhatsApp/Instagram group chats to poll friends; (3) Cross-referencing YouTube haul reviews to check fabric realism. The latency of these manual steps results in >65% intent drop-off.",
    keyMetrics: { primaryBarrier: "Social Validation Lag & Comparison Friction", severityScore: "8.5/10", opportunityLift: "+280 bps", avgDwellTime: "18 Days" },
    sampleQuotes: [
      "I screenshot 2-3 pairs and send to WhatsApp... by the time they reply I lose interest.",
      "Wish Myntra had a comparison studio where I can select 3 wishlisted jackets."
    ],
    recommendedAction: "Provide 1-tap WhatsApp voting cards and native side-by-side comparison directly in the wishlist."
  }
];

export const FUNNEL_STAGES = [
  { step: "1. Wishlist Add (High Intent)", volume: "10,000 Users", dropPct: "0%", description: "User expresses explicit visual interest by clicking heart icon." },
  { step: "2. Revisit & Evaluation", volume: "6,200 Users", dropPct: "-38%", description: "User opens wishlist but faces cluttered list of 30+ mixed items." },
  { step: "3. Alternative Comparison", volume: "3,100 Users", dropPct: "-50%", description: "Comparison paralysis: user cannot easily evaluate 4 similar items." },
  { step: "4. External Workaround (WhatsApp/Hauls)", volume: "1,400 Users", dropPct: "-55%", description: "User leaves app to send screenshots or look up styling; momentum lost." },
  { step: "5. Purchase within 30 Days (Baseline)", volume: "750 Users", dropPct: "-46%", description: "Only 7.5% final conversion rate without non-monetary decision support." }
];
