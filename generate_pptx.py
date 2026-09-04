import sys
import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

# Initialize Presentation with 16:9 Widescreen dimensions
prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)

blank_slide_layout = prs.slide_layouts[6]

# Authentic Myntra Corporate Brand Palette Definitions
COLOR_WHITE = RGBColor(255, 255, 255)
COLOR_OFFWHITE = RGBColor(245, 245, 246)          # Official Myntra App Background #F5F5F6
COLOR_BG_CARD = RGBColor(255, 255, 255)           # Pure White Card #FFFFFF
COLOR_BORDER = RGBColor(234, 234, 236)            # Official Myntra Card Border #EAEAEC
COLOR_TEXT_PRIMARY = RGBColor(40, 44, 63)         # Official Myntra Deep Charcoal #282C3F
COLOR_TEXT_MUTED = RGBColor(83, 87, 102)          # Official Myntra Subtext Slate #535766
COLOR_MYNTRA_PINK = RGBColor(255, 63, 108)        # Signature Myntra Pink #FF3F6C
COLOR_PURPLE_PILL = RGBColor(255, 63, 108)        # Myntra Pink Primary Header Pill
COLOR_SUBTITLE = RGBColor(255, 63, 108)           # Myntra Pink Subtitle Accent
COLOR_SYNTHESIS_BG = RGBColor(255, 240, 244)      # Myntra Soft Pink Glow #FFF0F4
COLOR_SYNTHESIS_BORDER = RGBColor(255, 194, 209)  # Myntra Soft Pink Border #FFC2D1
COLOR_SYNTHESIS_TEXT = RGBColor(40, 44, 63)       # Myntra Deep Charcoal #282C3F
COLOR_PHONE_BG = RGBColor(40, 44, 63)             # Myntra Deep Charcoal #282C3F
COLOR_MYNTRA_GREEN = RGBColor(3, 166, 133)        # Myntra Verified Trust Green #03A685

SLIDE_TRACKS = [
    "Context", "Market", "Research", "Insights", "Canvas", 
    "Ideation", "MVP", "Architecture", "Metrics", "GTM"
]

def add_card_shape(slide, left, top, width, height, bg_rgb, border_rgb=None):
    shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    shape.fill.solid()
    shape.fill.fore_color.rgb = bg_rgb
    if border_rgb:
        shape.line.color.rgb = border_rgb
        shape.line.width = Pt(1)
    else:
        shape.line.fill.background()
    return shape

# Import slide data from python logic
from data_pptx import SLIDES_DATA

for data in SLIDES_DATA:
    slide = prs.slides.add_slide(blank_slide_layout)
    
    # 1. Top Category Pill Banner
    banner_width = Inches(6.5)
    banner_height = Inches(0.4)
    banner_left = Inches((13.333 - 6.5) / 2)
    banner_top = Inches(0.25)
    
    pill_shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, banner_left, banner_top, banner_width, banner_height)
    pill_shape.fill.solid()
    pill_shape.fill.fore_color.rgb = COLOR_PURPLE_PILL
    pill_shape.line.fill.background()
    
    tf = pill_shape.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = data["topBanner"]
    p.alignment = PP_ALIGN.CENTER
    p.font.size = Pt(10)
    p.font.bold = True
    p.font.color.rgb = COLOR_WHITE

    # 2. Main Header & Brand Title
    title_box = slide.shapes.add_textbox(Inches(0.7), Inches(0.75), Inches(10.5), Inches(0.85))
    tf = title_box.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = data["title"]
    p.font.size = Pt(14.5)
    p.font.bold = True
    p.font.color.rgb = COLOR_TEXT_PRIMARY
    
    p2 = tf.add_paragraph()
    p2.text = data["subtitle"]
    p2.font.size = Pt(11.5)
    p2.font.bold = True
    p2.font.color.rgb = COLOR_SUBTITLE
    
    brand_box = slide.shapes.add_textbox(Inches(11.4), Inches(0.75), Inches(1.3), Inches(0.5))
    tf = brand_box.text_frame
    p = tf.paragraphs[0]
    p.text = "myntra"
    p.font.size = Pt(22)
    p.font.bold = True
    p.font.color.rgb = COLOR_MYNTRA_PINK
    p.alignment = PP_ALIGN.RIGHT

    # 3. Slide Content Area (Varying Layouts)
    card_top = Inches(1.8)
    card_height = Inches(4.15)
    
    # SPECIAL LAYOUT: SLIDE 3 (Research Thinking Evolution & Discovery Workflow)
    if data["slideNumber"] == 3:
        # Left Box: Thinking Evolution Timeline
        add_card_shape(slide, Inches(0.7), card_top, Inches(5.8), card_height, COLOR_BG_CARD, COLOR_BORDER)
        box = slide.shapes.add_textbox(Inches(0.85), card_top + Inches(0.15), Inches(5.5), card_height - Inches(0.3))
        tf = box.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = "🧠 STRATEGIC THINKING EVOLUTION NARRATIVE"
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = COLOR_PURPLE_PILL
        
        for item in data["thinkingEvolution"]:
            p = tf.add_paragraph()
            p.font.size = Pt(10)
            r1 = p.add_run()
            r1.text = "► " + item["stage"] + "\n"
            r1.font.bold = True
            r1.font.color.rgb = COLOR_MYNTRA_PINK
            
            r2 = p.add_run()
            r2.text = item["desc"]
            r2.font.color.rgb = COLOR_TEXT_PRIMARY

        # Right Box: AI Discovery Pipeline
        add_card_shape(slide, Inches(6.8), card_top, Inches(5.8), card_height, COLOR_SYNTHESIS_BG, COLOR_SYNTHESIS_BORDER)
        box = slide.shapes.add_textbox(Inches(6.95), card_top + Inches(0.15), Inches(5.5), card_height - Inches(0.3))
        tf = box.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = "🔬 AI DISCOVERY PIPELINE WORKFLOW"
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = COLOR_SUBTITLE
        
        for wf in data["discoveryWorkflow"]:
            p = tf.add_paragraph()
            p.font.size = Pt(10)
            r1 = p.add_run()
            r1.text = "• " + wf["step"] + ": "
            r1.font.bold = True
            r1.font.color.rgb = COLOR_TEXT_PRIMARY
            
            r2 = p.add_run()
            r2.text = wf["detail"]
            r2.font.color.rgb = COLOR_TEXT_PRIMARY

    # SPECIAL LAYOUT: SLIDE 5 (Financial Waterfall & Sensitivity Table)
    elif data["slideNumber"] == 5:
        # Left Box: Financial Waterfall
        add_card_shape(slide, Inches(0.7), card_top, Inches(5.8), card_height, COLOR_BG_CARD, COLOR_BORDER)
        box = slide.shapes.add_textbox(Inches(0.85), card_top + Inches(0.15), Inches(5.5), card_height - Inches(0.3))
        tf = box.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = "📊 BOTTOM-UP FINANCIAL WATERFALL"
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = COLOR_PURPLE_PILL
        
        for item in data["financialWaterfall"]:
            p = tf.add_paragraph()
            p.font.size = Pt(9.5)
            r1 = p.add_run()
            r1.text = "• " + item["metric"] + ": "
            r1.font.bold = True
            r1.font.color.rgb = COLOR_TEXT_PRIMARY
            
            r2 = p.add_run()
            r2.text = item["val"] + " (" + item["detail"] + ")"
            r2.font.color.rgb = COLOR_MYNTRA_PINK
            r2.font.bold = True

        # Right Box: Sensitivity Stress Test
        add_card_shape(slide, Inches(6.8), card_top, Inches(5.8), card_height, COLOR_BG_CARD, COLOR_BORDER)
        box = slide.shapes.add_textbox(Inches(6.95), card_top + Inches(0.15), Inches(5.5), card_height - Inches(0.3))
        tf = box.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = "🛡️ SENSITIVITY STRESS-TESTING SCENARIOS"
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = COLOR_PURPLE_PILL
        
        for sens in data["sensitivityTable"]:
            p = tf.add_paragraph()
            p.font.size = Pt(10)
            r1 = p.add_run()
            r1.text = "► " + sens["scenario"] + "\n"
            r1.font.bold = True
            r1.font.color.rgb = COLOR_SUBTITLE
            
            r2 = p.add_run()
            r2.text = f"Lift: {sens['convLift']} | Profit: {sens['monthlyProfit']}/mo | ROI: {sens['featureRoi']} | Payback: {sens['payback']}"
            r2.font.color.rgb = COLOR_TEXT_PRIMARY

    # SPECIAL LAYOUT: SLIDE 7 (MVP Wireframe Cards Showcase with Figma Assets)
    elif data["slideNumber"] == 7:
        card_w = Inches(3.8)
        gap_w = Inches(0.26)
        for mIdx, wf in enumerate(data["mvpWireframes"]):
            cleft = Inches(0.7) + mIdx * (card_w + gap_w)
            add_card_shape(slide, cleft, card_top, card_w, card_height, COLOR_BG_CARD, COLOR_BORDER)
            
            box = slide.shapes.add_textbox(cleft + Inches(0.1), card_top + Inches(0.05), card_w - Inches(0.2), Inches(0.45))
            tf = box.text_frame
            tf.word_wrap = True
            
            p = tf.paragraphs[0]
            p.text = wf["feature"]
            p.font.size = Pt(9.5)
            p.font.bold = True
            p.font.color.rgb = COLOR_PURPLE_PILL
            
            # Embed Figma Design PNG if present
            img_path = wf.get("figmaImage")
            if img_path and os.path.exists(img_path):
                slide.shapes.add_picture(img_path, cleft + Inches(0.15), card_top + Inches(0.45), card_w - Inches(0.3), Inches(3.2))
            else:
                p_hdr = tf.add_paragraph()
                p_hdr.text = wf["uiBox"]["header"]
                p_hdr.font.size = Pt(9)
                p_hdr.font.bold = True
                p_hdr.font.color.rgb = COLOR_TEXT_PRIMARY

            p_val_box = slide.shapes.add_textbox(cleft + Inches(0.1), card_top + Inches(3.7), card_w - Inches(0.2), Inches(0.4))
            tf_v = p_val_box.text_frame
            tf_v.word_wrap = True
            p_v = tf_v.paragraphs[0]
            p_v.text = "⚡ " + wf["value"]
            p_v.font.size = Pt(8.5)
            p_v.font.bold = True
            p_v.font.color.rgb = COLOR_MYNTRA_PINK

    # STANDARD 3-COLUMN LAYOUT (SLIDES 1, 2, 4, 6, 8, 9, 10)
    else:
        # Left Card
        add_card_shape(slide, Inches(0.7), card_top, Inches(4.5), card_height, COLOR_BG_CARD, COLOR_BORDER)
        lcard_box = slide.shapes.add_textbox(Inches(0.85), card_top + Inches(0.15), Inches(4.2), card_height - Inches(0.3))
        tf = lcard_box.text_frame
        tf.word_wrap = True
        
        p = tf.paragraphs[0]
        p.text = data["leftCard"]["title"]
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = COLOR_PURPLE_PILL
        
        for bold_text, reg_text in data["leftCard"]["bullets"]:
            p = tf.add_paragraph()
            p.font.size = Pt(10)
            run_bullet = p.add_run()
            run_bullet.text = "• "
            run_bullet.font.color.rgb = COLOR_MYNTRA_PINK
            run_bullet.font.bold = True
            
            run_bold = p.add_run()
            run_bold.text = bold_text + " "
            run_bold.font.bold = True
            run_bold.font.color.rgb = COLOR_TEXT_PRIMARY
            
            run_reg = p.add_run()
            run_reg.text = reg_text
            run_reg.font.color.rgb = COLOR_TEXT_PRIMARY

        # Mid Card
        add_card_shape(slide, Inches(5.35), card_top, Inches(4.5), card_height, COLOR_BG_CARD, COLOR_BORDER)
        mcard_box = slide.shapes.add_textbox(Inches(5.5), card_top + Inches(0.15), Inches(4.2), card_height - Inches(0.3))
        tf = mcard_box.text_frame
        tf.word_wrap = True
        
        p = tf.paragraphs[0]
        p.text = data["midCard"]["title"]
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = COLOR_PURPLE_PILL
        
        for bold_text, reg_text in data["midCard"]["bullets"]:
            p = tf.add_paragraph()
            p.font.size = Pt(10)
            run_bullet = p.add_run()
            run_bullet.text = "• "
            run_bullet.font.color.rgb = COLOR_MYNTRA_PINK
            run_bullet.font.bold = True
            
            run_bold = p.add_run()
            run_bold.text = bold_text + " "
            run_bold.font.bold = True
            run_bold.font.color.rgb = COLOR_TEXT_PRIMARY
            
            run_reg = p.add_run()
            run_reg.text = reg_text
            run_reg.font.color.rgb = COLOR_TEXT_PRIMARY

        # Phone Mockup (Right Column) with Real Figma Screen Embed
        phone_left = Inches(10.0)
        phone_width = Inches(2.63)
        add_card_shape(slide, phone_left, card_top, phone_width, card_height, COLOR_PHONE_BG, RGBColor(15, 23, 42))
        
        # Embedded Figma Image if available
        figma_img = data.get("figmaImage")
        if figma_img and os.path.exists(figma_img):
            slide.shapes.add_picture(figma_img, phone_left + Inches(0.08), card_top + Inches(0.08), phone_width - Inches(0.16), card_height - Inches(0.16))
        else:
            phone_box = slide.shapes.add_textbox(phone_left + Inches(0.15), card_top + Inches(0.2), phone_width - Inches(0.3), card_height - Inches(0.4))
            tf = phone_box.text_frame
            tf.word_wrap = True
            
            p = tf.paragraphs[0]
            p.text = data["phoneMockup"]["screenName"]
            p.font.size = Pt(10.5)
            p.font.bold = True
            p.font.color.rgb = COLOR_WHITE
            
            p_badge = tf.add_paragraph()
            p_badge.text = "[" + data["phoneMockup"]["badge"] + "]"
            p_badge.font.size = Pt(9)
            p_badge.font.bold = True
            p_badge.font.color.rgb = COLOR_MYNTRA_PINK
            
            for label, val in data["phoneMockup"]["items"]:
                p_item = tf.add_paragraph()
                p_item.font.size = Pt(9)
                
                r_lbl = p_item.add_run()
                r_lbl.text = label + "\n"
                r_lbl.font.color.rgb = COLOR_TEXT_MUTED
                
                r_val = p_item.add_run()
                r_val.text = val
                r_val.font.bold = True
                r_val.font.color.rgb = COLOR_WHITE

            p_cta = tf.add_paragraph()
            p_cta.alignment = PP_ALIGN.CENTER
            r_cta = p_cta.add_run()
            r_cta.text = "▶ " + data["phoneMockup"]["ctaText"]
            r_cta.font.size = Pt(9.5)
            r_cta.font.bold = True
            r_cta.font.color.rgb = COLOR_MYNTRA_PINK

    # 4. Bottom Synthesis Banner
    synth_top = Inches(6.05)
    synth_height = Inches(0.7)
    add_card_shape(slide, Inches(0.7), synth_top, Inches(11.933), synth_height, COLOR_SYNTHESIS_BG, COLOR_SYNTHESIS_BORDER)
    
    synth_box = slide.shapes.add_textbox(Inches(0.85), synth_top + Inches(0.08), Inches(11.633), synth_height - Inches(0.16))
    tf = synth_box.text_frame
    tf.word_wrap = True
    
    p = tf.paragraphs[0]
    p.text = "★ " + data["bottomBanner"]["title"]
    p.font.size = Pt(10)
    p.font.bold = True
    p.font.color.rgb = RGBColor(67, 56, 202)
    
    p2 = tf.add_paragraph()
    p2.text = data["bottomBanner"]["text"]
    p2.font.size = Pt(10)
    p2.font.bold = True
    p2.font.color.rgb = COLOR_SYNTHESIS_TEXT

    # 5. Bottom 10-Stage Breadcrumb Ribbon Tracker
    ribbon_top = Inches(6.85)
    ribbon_height = Inches(0.35)
    pill_width = Inches(1.15)
    pill_gap = Inches(0.04)
    
    start_left = Inches(0.7)
    for idx, track_name in enumerate(SLIDE_TRACKS):
        pleft = start_left + idx * (pill_width + pill_gap)
        is_active = (track_name.lower() == data["track"].lower())
        
        bg_col = COLOR_PURPLE_PILL if is_active else RGBColor(241, 245, 249)
        border_col = COLOR_PURPLE_PILL if is_active else RGBColor(203, 213, 225)
        text_col = COLOR_WHITE if is_active else COLOR_TEXT_MUTED
        
        rb_shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, pleft, ribbon_top, pill_width, ribbon_height)
        rb_shape.fill.solid()
        rb_shape.fill.fore_color.rgb = bg_col
        rb_shape.line.color.rgb = border_col
        rb_shape.line.width = Pt(1)
        
        tf = rb_shape.text_frame
        p = tf.paragraphs[0]
        p.text = track_name
        p.alignment = PP_ALIGN.CENTER
        p.font.size = Pt(9)
        p.font.bold = True
        p.font.color.rgb = text_col

# Save Presentation
output_path = "Myntra_Wishlist_Studio_10_Slide_Deck.pptx"
try:
    prs.save(output_path)
    print(f"SUCCESS: Generated 16:9 Executive PowerPoint Presentation at {output_path}")
except PermissionError:
    output_path = "Myntra_Wishlist_Studio_10_Slide_Deck_Updated.pptx"
    prs.save(output_path)
    print(f"SUCCESS: Primary PPTX locked. Saved updated presentation at {output_path}")
