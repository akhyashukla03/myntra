// Neutral, Blinded User Research Dataset: Live Survey Data (25 Responses), Questionnaire & Qualitative Transcripts

export const LIVE_SURVEY_SUMMARY = {
  totalResponses: 25,
  collectionDate: "August 2026",
  source: "Online Fashion Shopping & Browsing Habits Survey (Google Forms - 25 Responses)",
  keyMetrics: [
    { label: "Myntra Primary Shoppers", val: "100%", sub: "25/25 respondents shop on Myntra (92% exclusive, 8% multi-app)" },
    { label: "Wishlist Inaction Rate", val: "76.0%", sub: "19/25 respondents report saved items forgotten for weeks/months" },
    { label: "Manual Comparison Friction", val: "92.0%", sub: "23/25 toggle tabs, compare phone screenshots, or drop off" },
    { label: "Screenshot & WhatsApp Sharing", val: "80.0%", sub: "20/25 regularly seek peer validation before buying" },
    { label: "AI Outfit Matcher Demand", val: "80.0%", sub: "20/25 rated 4/5 or 5/5 usefulness for 1-tap complete looks" },
    { label: "Side-by-Side Matrix Demand", val: "100%", sub: "25/25 rated 3/5 or higher; 72% rated 4/5 or 5/5" }
  ],
  questionBreakdown: [
    {
      qNum: "Q1",
      question: "Which fashion apps or websites do you browse or shop on most frequently?",
      distribution: [
        { option: "Myntra (Exclusive)", count: 23, percentage: 92.0 },
        { option: "Myntra + Ajio", count: 1, percentage: 4.0 },
        { option: "Myntra + Nykaa Fashion", count: 1, percentage: 4.0 }
      ]
    },
    {
      qNum: "Q2",
      question: "Roughly how many saved/wishlisted items do you currently have across your favorite fashion apps?",
      distribution: [
        { option: "15 - 40 items", count: 13, percentage: 52.0 },
        { option: "Under 15 items (I keep it clean)", count: 7, percentage: 28.0 },
        { option: "40 - 100 items", count: 5, percentage: 20.0 }
      ]
    },
    {
      qNum: "Q3",
      question: "What typically happens to items you save to your wishlist/bookmarks?",
      distribution: [
        { option: "I buy a few, but most stay saved and forgotten for weeks/months (Dormant)", count: 19, percentage: 76.0 },
        { option: "I wait to see if prices drop during sales", count: 4, percentage: 16.0 },
        { option: "I buy most of them within a few days", count: 2, percentage: 8.0 }
      ]
    },
    {
      qNum: "Q4",
      question: "When you really like a piece of clothing/footwear but STOP short of buying it, what are the top reasons?",
      distribution: [
        { option: "Comparison dilemma: 2-3 similar options saved and can't figure out which is better", count: 14, percentage: 56.0 },
        { option: "Fabric realism: Photos look studio-lit, hard to tell real fabric thickness/GSM", count: 10, percentage: 40.0 },
        { option: "Styling doubt: Love the piece, but unsure how to style with existing wardrobe", count: 9, percentage: 36.0 },
        { option: "Fit & return friction: Unsure about brand sizing and don't want return hassle", count: 8, percentage: 32.0 },
        { option: "Casual window shopping / waiting for upcoming occasion", count: 9, percentage: 36.0 }
      ]
    },
    {
      qNum: "Q5",
      question: "When stuck choosing between 2 or 3 similar items, what is your usual process?",
      distribution: [
        { option: "Toggle between multiple product tabs/pages repeatedly", count: 11, percentage: 44.0 },
        { option: "Share screenshots with friends on WhatsApp/Instagram for advice", count: 7, percentage: 28.0 },
        { option: "Take screenshots and compare them in phone gallery", count: 5, percentage: 20.0 },
        { option: "Get overwhelmed and abandon buying altogether", count: 2, percentage: 8.0 }
      ]
    },
    {
      qNum: "Q6",
      question: "How often do you screenshot apparel items and send them to friends/family for second opinions?",
      distribution: [
        { option: "Frequently (Almost every major outfit purchase)", count: 12, percentage: 48.0 },
        { option: "Occasionally (Only for party wear, blazers, or expensive items)", count: 8, percentage: 32.0 },
        { option: "Never (I decide 100% on my own)", count: 5, percentage: 20.0 }
      ]
    },
    {
      qNum: "Q7",
      question: "How helpful would a side-by-side spec comparison be? (fabric GSM, verified fit, customer photos)",
      distribution: [
        { option: "Score 5 (Extremely Helpful)", count: 8, percentage: 32.0 },
        { option: "Score 4 (Very Helpful)", count: 10, percentage: 40.0 },
        { option: "Score 3 (Moderately Helpful)", count: 7, percentage: 28.0 }
      ]
    },
    {
      qNum: "Q8",
      question: "How helpful would automated outfit pairing recommendations be? (showing 2-3 complete coordinated looks)",
      distribution: [
        { option: "Score 5 (Extremely Helpful)", count: 6, percentage: 24.0 },
        { option: "Score 4 (Very Helpful)", count: 14, percentage: 56.0 },
        { option: "Score 3 (Moderately Helpful)", count: 4, percentage: 16.0 },
        { option: "Score 2 (Slightly Helpful)", count: 1, percentage: 4.0 }
      ]
    },
    {
      qNum: "Q9",
      question: "How likely would you be to use a quick 1-tap poll link for friends to vote Option A vs B?",
      distribution: [
        { option: "Score 5 (Very Likely / Top Box)", count: 8, percentage: 32.0 },
        { option: "Score 4 (Likely)", count: 5, percentage: 20.0 },
        { option: "Score 3 (Neutral)", count: 6, percentage: 24.0 },
        { option: "Score 2 (Unlikely)", count: 3, percentage: 12.0 },
        { option: "Score 1 (Very Unlikely)", count: 3, percentage: 12.0 }
      ]
    },
    {
      qNum: "Q10",
      question: "What is one thing that currently frustrates you most when shopping for clothes online?",
      verbatims: [
        "Studio lighting makes cheap synthetic fabrics look like thick cotton. Hard to know real GSM without buying.",
        "Sizing is completely different between Roadster and Levi's. Medium in one is tight, in another it's oversized.",
        "Sending 6 photos to friends on WhatsApp and waiting all day for them to reply is tiring. Need faster group feedback.",
        "Toggling between 4 tabs on mobile app is so frustrating. I just want to compare measurements side by side.",
        "Wishlist lacks smart outfit bundles. I want to buy a complete look in one tap.",
        "Cannot tell GSM weight or drape stiffness from model photos alone. Need customer drape photos."
      ]
    },
    {
      qNum: "Q11",
      question: "Follow-up 10-Minute User Interview Opt-in",
      distribution: [
        { option: "Maybe later", count: 11, percentage: 44.0 },
        { option: "Yes, happy to help!", count: 8, percentage: 32.0 },
        { option: "No, thanks", count: 6, percentage: 24.0 }
      ]
    }
  ]
};

export const GOOGLE_FORMS_SURVEY_SCHEMA = {
  title: "Online Fashion Shopping & Browsing Habits Survey (2026)",
  description: "A quick 3-minute study on how fashion shoppers browse, bookmark, and evaluate apparel online across fashion platforms (Myntra, Ajio, Zara, Nykaa, etc.). Responses are confidential.",
  sections: [
    {
      sectionTitle: "Section 1: General Shopping & Bookmarking Habits",
      questions: [
        {
          id: "q1",
          question: "Which fashion apps or websites do you browse or shop on most frequently?",
          type: "multiple_choice",
          options: ["Myntra", "Ajio / Ajio Luxe", "Zara / H&M / Uniqlo", "Nykaa Fashion / Tata CliQ", "Other fashion apps"],
          required: true
        },
        {
          id: "q2",
          question: "Roughly how many saved/wishlisted items do you currently have across your favorite fashion apps?",
          type: "multiple_choice",
          options: ["Under 15 items (I keep it clean)", "15 - 40 items", "40 - 100 items", "100+ items (A massive bookmark collection)"],
          required: true
        },
        {
          id: "q3",
          question: "What typically happens to items you save to your wishlist/bookmarks?",
          type: "multiple_choice",
          options: [
            "I buy most of them within a few days",
            "I buy a few, but most stay saved and forgotten for weeks/months",
            "I use it purely as a moodboard / style inspiration gallery",
            "I wait to see if prices drop during sales"
          ],
          required: true
        }
      ]
    },
    {
      sectionTitle: "Section 2: Decision Making & Purchase Hesitations",
      questions: [
        {
          id: "q4",
          question: "When you really like a piece of clothing/footwear but STOP short of buying it, what are the top reasons? (Select up to 2)",
          type: "multiple_choice",
          options: [
            "Comparison dilemma: I have 2-3 similar options saved and can't figure out which is better",
            "Styling doubt: I love the piece, but I'm not sure how to style it with clothes I already own",
            "Fit & return friction: Unsure about brand sizing and don't want the hassle of returning",
            "Fabric realism: Photos look studio-lit, hard to tell real fabric thickness/texture",
            "Just casual window shopping / waiting for an upcoming occasion"
          ],
          required: true
        },
        {
          id: "q5",
          question: "When you are stuck choosing between 2 or 3 similar items (e.g., 3 jackets or 2 pairs of sneakers), what is your usual process?",
          type: "multiple_choice",
          options: [
            "I toggle between multiple product tabs/pages repeatedly",
            "I take screenshots and compare them in my phone gallery",
            "I share screenshots with friends on WhatsApp/Instagram for advice",
            "I get overwhelmed and abandon buying altogether"
          ],
          required: true
        },
        {
          id: "q6",
          question: "How often do you screenshot apparel items and send them to friends/family for second opinions?",
          type: "multiple_choice",
          options: [
            "Frequently (Almost every major outfit purchase)",
            "Occasionally (Only for party wear, blazers, or expensive items)",
            "Rarely",
            "Never (I decide 100% on my own)"
          ],
          required: true
        }
      ]
    },
    {
      sectionTitle: "Section 3: Ideal Shopping Experience",
      questions: [
        {
          id: "q7",
          question: "How helpful would a side-by-side spec comparison be? (comparing fabric thickness/GSM, verified fit consensus, and unfiltered customer photos on one screen)",
          type: "scale",
          scaleMin: 1,
          scaleMax: 5,
          scaleMinLabel: "Not helpful",
          scaleMaxLabel: "Extremely helpful",
          required: true
        },
        {
          id: "q8",
          question: "How helpful would automated outfit pairing recommendations be? (showing 2-3 complete coordinated looks with matching bottomwear/footwear for a saved piece)",
          type: "scale",
          scaleMin: 1,
          scaleMax: 5,
          scaleMinLabel: "Not helpful",
          scaleMaxLabel: "Extremely helpful",
          required: true
        },
        {
          id: "q9",
          question: "How likely would you be to use a quick 1-tap poll link to let friends vote on Option A vs Option B instead of sending multiple screenshot images?",
          type: "scale",
          scaleMin: 1,
          scaleMax: 5,
          scaleMinLabel: "Unlikely",
          scaleMaxLabel: "Very likely",
          required: true
        },
        {
          id: "q10",
          question: "What is one thing that currently frustrates you most when shopping for clothes online?",
          type: "paragraph",
          required: false
        }
      ]
    },
    {
      sectionTitle: "Section 4: Optional 10-Minute Follow-up Interview",
      questions: [
        {
          id: "q11",
          question: "Would you be open to a quick 10-minute casual chat (Google Meet / Call) to share more about your fashion shopping habits?",
          type: "multiple_choice",
          options: ["Yes, happy to help!", "Maybe later", "No, thanks"],
          required: true
        },
        {
          id: "q12",
          question: "If yes, please share your Name and Phone Number / WhatsApp / Email:",
          type: "paragraph",
          required: false
        }
      ]
    }
  ]
};

export const USER_INTERVIEWS = [
  {
    id: "U1",
    name: "Participant 1 (Gen-Z Cohort)",
    age: 23,
    city: "Bengaluru",
    occupation: "Tech Consultant",
    wishlistSize: 64,
    primaryCategory: "Workwear & Semi-formals",
    verbatimQuote: "I have had a lavender linen blazer in my wishlist for 5 weeks. I love it, but I keep hesitating because I don't know if my beige chinos match it or if I need dark trousers. If the app showed me 2 full outfits with trousers and loafers, I would have checked out in 30 seconds.",
    corePainPoint: "Styling Isolation (Wardrobe Coordination Uncertainty)",
    currentWorkaround: "Saves Instagram reels on blazer styling, creates mental moodboards, eventually postpones purchase.",
    solutionFeedback: "Automated outfit coordination with 1-tap bundle add is an immediate 10/10 need."
  },
  {
    id: "U2",
    name: "Participant 2 (Gen-Z Cohort)",
    age: 21,
    city: "New Delhi",
    occupation: "Final Year B.Com Student",
    wishlistSize: 42,
    primaryCategory: "Streetwear, Cargos & Oversized Tees",
    verbatimQuote: "I have 4 black cargo pants wishlisted. Every Friday I open the app to buy one, but one has 240 GSM cotton, one is relaxed fit, one is parachute. Without seeing them side-by-side with real user fit photos, my brain shuts down and I close the app.",
    corePainPoint: "Comparison Paralysis (Spec & Fabric Ambiguity)",
    currentWorkaround: "Opens 4 tabs on desktop browser or switches between app screens 10 times.",
    solutionFeedback: "Side-by-side spec and real-photo comparison directly removes the mental block."
  },
  {
    id: "U3",
    name: "Participant 3 (Millennial Cohort)",
    age: 27,
    city: "Mumbai",
    occupation: "Brand Marketing Manager",
    wishlistSize: 88,
    primaryCategory: "Festive & Occasion Wear",
    verbatimQuote: "My wishlist has 80+ items dating back months. It's a dumping ground. I can't find the cocktail dress I liked 2 weeks ago among 40 ethnic kurtas. Also, return pickups in Mumbai high-rises are tedious, so if sizing is risky, it stays in the wishlist forever.",
    corePainPoint: "Wishlist Clutter & Sizing Return Anxiety",
    currentWorkaround: "Uses search bar inside wishlist or gives up and buys offline at Zara/FabIndia.",
    solutionFeedback: "Occasion Folders (Party, Work, Everyday) and Verified Fit Consensus score are critical."
  },
  {
    id: "U4",
    name: "Participant 4 (Gen-Z Cohort)",
    age: 25,
    city: "Pune",
    occupation: "UI/UX Designer",
    wishlistSize: 31,
    primaryCategory: "Minimalist Casuals & Sneakers",
    verbatimQuote: "Wishlists are bookmarks where good intentions go to die. Fashion is visual and comparative. When I buy tech gadgets on Amazon, there is a clear spec comparison table. On fashion apps, product cards are identical with studio lighting that hides actual fabric texture.",
    corePainPoint: "Evaluation Friction & Lack of Spec Transparency",
    currentWorkaround: "Searches YouTube for unboxing hauls to check GSM and fabric fall.",
    solutionFeedback: "Loves the GSM fabric indicator and customer photo cycling feature."
  },
  {
    id: "U5",
    name: "Participant 5 (Gen-Z Cohort)",
    age: 22,
    city: "Hyderabad",
    occupation: "Post-Graduate Student",
    wishlistSize: 95,
    primaryCategory: "Trending Gen-Z Fashion",
    verbatimQuote: "I never buy anything above ₹1,200 without sending screenshots to my college WhatsApp group 'The Council'. But taking 4 screenshots, cropping them, and waiting 18 hours for replies makes me lose the shopping impulse. If I had a 1-tap WhatsApp voting card, we'd decide in 5 minutes.",
    corePainPoint: "Social Validation Friction & High Feedback Latency",
    currentWorkaround: "Manual screenshot collages sent to WhatsApp group chats.",
    solutionFeedback: "1-Tap WhatsApp voting card is a viral, zero-friction winner."
  },
  {
    id: "U6",
    name: "Participant 6 (Millennial Cohort)",
    age: 26,
    city: "Gurgaon",
    occupation: "Corporate Lawyer",
    wishlistSize: 53,
    primaryCategory: "Premium Workwear & Handbags",
    verbatimQuote: "I don't need discounts—I have purchasing power. What I need is confidence that the fabric isn't cheap synthetic poly-blend that wrinkles in AC meetings. If the app gives me fabric GSM weights, return risk probabilities, and curated styling, I'll buy 3x more often.",
    corePainPoint: "Fabric Quality Doubts & Margin Willingness",
    currentWorkaround: "Orders 2 sizes and returns 1 (costly for the platform, annoying for user).",
    solutionFeedback: "Confirms that high-intent users do NOT need discounts to convert—they need decision confidence."
  }
];
