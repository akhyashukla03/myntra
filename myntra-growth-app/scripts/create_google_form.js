function createFashionSurvey() {
  // 1. Create the Form
  var formTitle = "Online Fashion Shopping & Browsing Habits Survey (2026)";
  var form = FormApp.create(formTitle);
  form.setDescription(
    "A quick 3-minute study on how shoppers browse, bookmark, and evaluate apparel online across fashion platforms (Myntra, Ajio, Zara, Nykaa, etc.). Responses are confidential."
  );
  form.setIsQuiz(false);
  form.setAllowResponseEdits(false);
  form.setLimitOneResponsePerUser(false);

  // --- SECTION 1: General Shopping & Bookmarking Habits ---
  var item1 = form.addMultipleChoiceItem();
  item1.setTitle("1. Which fashion apps or websites do you browse or shop on most frequently?")
       .setChoiceValues([
         "Myntra",
         "Ajio / Ajio Luxe",
         "Zara / H&M / Uniqlo",
         "Nykaa Fashion / Tata CliQ",
         "Other fashion apps"
       ])
       .setRequired(true);

  var item2 = form.addMultipleChoiceItem();
  item2.setTitle("2. Roughly how many saved/wishlisted items do you currently have across your favorite fashion apps?")
       .setChoiceValues([
         "Under 15 items (I keep it clean)",
         "15 - 40 items",
         "40 - 100 items",
         "100+ items (A massive bookmark collection)"
       ])
       .setRequired(true);

  var item3 = form.addMultipleChoiceItem();
  item3.setTitle("3. What typically happens to items you save to your wishlist/bookmarks?")
       .setChoiceValues([
         "I buy most of them within a few days",
         "I buy a few, but most stay saved and forgotten for weeks/months",
         "I use it purely as a moodboard / style inspiration gallery",
         "I wait to see if prices drop during sales"
       ])
       .setRequired(true);

  // --- SECTION 2: Decision Making & Purchase Hesitations ---
  form.addPageBreakItem().setTitle("Section 2: Decision Making & Purchase Hesitations");

  var item4 = form.addCheckboxItem();
  item4.setTitle("4. When you really like a piece of clothing/footwear but STOP short of buying it, what are the top reasons? (Select up to 2)")
       .setChoiceValues([
         "Comparison dilemma: I have 2-3 similar options saved and can't figure out which is better",
         "Styling doubt: I love the piece, but I'm not sure how to style it with clothes I already own",
         "Fit & return friction: Unsure about brand sizing and don't want the hassle of returning",
         "Fabric realism: Photos look studio-lit, hard to tell real fabric thickness/texture",
         "Just casual window shopping / waiting for an upcoming occasion"
       ])
       .setRequired(true);

  var item5 = form.addMultipleChoiceItem();
  item5.setTitle("5. When you are stuck choosing between 2 or 3 similar items (e.g., 3 jackets or 2 pairs of sneakers), what is your usual process?")
       .setChoiceValues([
         "I toggle between multiple product tabs/pages repeatedly",
         "I take screenshots and compare them in my phone gallery",
         "I share screenshots with friends on WhatsApp/Instagram for advice",
         "I get overwhelmed and abandon buying altogether"
       ])
       .setRequired(true);

  var item6 = form.addMultipleChoiceItem();
  item6.setTitle("6. How often do you screenshot apparel items and send them to friends/family for second opinions?")
       .setChoiceValues([
         "Frequently (Almost every major outfit purchase)",
         "Occasionally (Only for party wear, blazers, or expensive items)",
         "Rarely",
         "Never (I decide 100% on my own)"
       ])
       .setRequired(true);

  // --- SECTION 3: Ideal Shopping Experience ---
  form.addPageBreakItem().setTitle("Section 3: Ideal Shopping Experience");

  var item7 = form.addScaleItem();
  item7.setTitle("7. How helpful would a side-by-side spec comparison be? (comparing fabric thickness/GSM, verified fit consensus, and unfiltered customer photos on one screen)")
       .setBounds(1, 5)
       .setLabels("Not helpful", "Extremely helpful")
       .setRequired(true);

  var item8 = form.addScaleItem();
  item8.setTitle("8. How helpful would automated outfit pairing recommendations be? (showing 2-3 complete coordinated looks with matching bottomwear/footwear for a saved piece)")
       .setBounds(1, 5)
       .setLabels("Not helpful", "Extremely helpful")
       .setRequired(true);

  var item9 = form.addScaleItem();
  item9.setTitle("9. How likely would you be to use a quick 1-tap poll link to let friends vote on Option A vs Option B instead of sending multiple screenshots?")
       .setBounds(1, 5)
       .setLabels("Unlikely", "Very likely")
       .setRequired(true);

  var item10 = form.addParagraphTextItem();
  item10.setTitle("10. What is one thing that currently frustrates you most when shopping for clothes online?")
        .setRequired(false);

  // --- SECTION 4: Follow-up & Contact Details (Optional) ---
  form.addPageBreakItem().setTitle("Section 4: Optional 10-Minute User Interview");

  var item11 = form.addMultipleChoiceItem();
  item11.setTitle("11. Would you be open to a quick 10-minute casual chat (Google Meet/Call) to share more about your fashion shopping experiences?")
        .setChoiceValues([
          "Yes, happy to help!",
          "Maybe later",
          "No, thanks"
        ])
        .setRequired(true);

  var item12 = form.addTextItem();
  item12.setTitle("12. If yes, please share your Name and Phone Number / WhatsApp / Email:")
        .setRequired(false);

  // 2. Automatically Create and Link a Google Sheet for Live Responses
  var sheet = SpreadsheetApp.create(formTitle + " (Responses)");
  form.setDestination(FormApp.DestinationType.SPREADSHEET, sheet.getId());

  // 3. Print Links to Console
  Logger.log("=================================================");
  Logger.log("🎉 SUCCESS! Your Google Form and Sheet are created:");
  Logger.log("👉 SHAREABLE FORM LINK (Share with cohort): " + form.getPublishedUrl());
  Logger.log("📝 EDIT FORM LINK: " + form.getEditUrl());
  Logger.log("📊 GOOGLE SHEET (Live Responses & Contacts): " + sheet.getUrl());
  Logger.log("=================================================");
}
