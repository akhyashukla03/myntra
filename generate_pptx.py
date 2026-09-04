import sys
import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
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
COLOR_LIGHT_GRAY = RGBColor(248, 249, 250)

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

def set_bullet_indent(p, left_margin_pt=18, hanging_indent_pt=14):
    """
    Sets true OpenXML paragraph left margin (marL) and negative first-line indent (indent)
    so that multi-line wrapped bullet text aligns cleanly under the text block.
    """
    pPr = p._p.get_or_add_pPr()
    pPr.set('marL', str(int(Pt(left_margin_pt))))
    pPr.set('indent', str(int(-Pt(hanging_indent_pt))))

# Import slide data from python logic
from data_pptx import SLIDES_DATA

for data in SLIDES_DATA:
    slide = prs.slides.add_slide(blank_slide_layout)
    s_num = data["slideNumber"]
    
    # 1. Top Category Pill Banner
    banner_width = Inches(6.5)
    banner_height = Inches(0.38)
    banner_left = Inches((13.333 - 6.5) / 2)
    banner_top = Inches(0.22)
    
    pill_shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, banner_left, banner_top, banner_width, banner_height)
    pill_shape.fill.solid()
    pill_shape.fill.fore_color.rgb = COLOR_PURPLE_PILL
    pill_shape.line.fill.background()
    
    tf = pill_shape.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    tf.margin_left = Inches(0.1)
    tf.margin_right = Inches(0.1)
    tf.margin_top = Inches(0.02)
    tf.margin_bottom = Inches(0.02)
    
    p = tf.paragraphs[0]
    p.text = data["topBanner"]
    p.alignment = PP_ALIGN.CENTER
    p.font.size = Pt(9.5)
    p.font.bold = True
    p.font.color.rgb = COLOR_WHITE
    p.space_before = Pt(0)
    p.space_after = Pt(0)

    # 2. Main Header & Brand Title Block
    title_box = slide.shapes.add_textbox(Inches(0.7), Inches(0.68), Inches(10.5), Inches(0.85))
    tf = title_box.text_frame
    tf.word_wrap = True
    tf.margin_left = Inches(0)
    tf.margin_right = Inches(0)
    tf.margin_top = Inches(0)
    tf.margin_bottom = Inches(0)
    
    p = tf.paragraphs[0]
    p.text = data["title"]
    p.font.size = Pt(13.5)
    p.font.bold = True
    p.font.color.rgb = COLOR_TEXT_PRIMARY
    p.space_after = Pt(2)
    
    p2 = tf.add_paragraph()
    p2.text = data["subtitle"]
    p2.font.size = Pt(10)
    p2.font.bold = True
    p2.font.color.rgb = COLOR_SUBTITLE
    p2.space_before = Pt(2)
    p2.space_after = Pt(4)
    
    brand_box = slide.shapes.add_textbox(Inches(11.4), Inches(0.68), Inches(1.3), Inches(0.5))
    tf_b = brand_box.text_frame
    tf_b.margin_left = Inches(0)
    tf_b.margin_right = Inches(0)
    tf_b.margin_top = Inches(0)
    tf_b.margin_bottom = Inches(0)
    p_b = tf_b.paragraphs[0]
    p_b.text = "myntra"
    p_b.font.size = Pt(22)
    p_b.font.bold = True
    p_b.font.color.rgb = COLOR_MYNTRA_PINK
    p_b.alignment = PP_ALIGN.RIGHT

    # 3. Slide Content Area Layouts
    card_top = Inches(1.68)
    card_height = Inches(4.28)
    
    # ==========================================
    # SLIDE 1: STRATEGIC GOAL, HYPOTHESIS & MACRO METRICS
    # ==========================================
    if s_num == 1:
        # Left Card: Strategic Goal
        add_card_shape(slide, Inches(0.7), card_top, Inches(4.5), card_height - Inches(0.9), COLOR_BG_CARD, COLOR_BORDER)
        box = slide.shapes.add_textbox(Inches(0.82), card_top + Inches(0.1), Inches(4.26), card_height - Inches(1.1))
        tf = box.text_frame
        tf.word_wrap = True
        tf.margin_left = Inches(0.08); tf.margin_right = Inches(0.08)
        tf.margin_top = Inches(0.06); tf.margin_bottom = Inches(0.06)
        
        p = tf.paragraphs[0]
        p.text = data["leftCard"]["title"]
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = COLOR_PURPLE_PILL
        p.space_after = Pt(6)
        for bold_text, reg_text in data["leftCard"]["bullets"]:
            p = tf.add_paragraph()
            p.font.size = Pt(9.5)
            p.line_spacing = 1.15
            p.space_before = Pt(2)
            p.space_after = Pt(4)
            set_bullet_indent(p, left_margin_pt=16, hanging_indent_pt=12)
            r0 = p.add_run(); r0.text = "• "; r0.font.color.rgb = COLOR_MYNTRA_PINK; r0.font.bold = True
            r1 = p.add_run(); r1.text = bold_text + " "; r1.font.bold = True; r1.font.color.rgb = COLOR_TEXT_PRIMARY
            r2 = p.add_run(); r2.text = reg_text; r2.font.color.rgb = COLOR_TEXT_PRIMARY

        # Mid Card: Why it Matters
        add_card_shape(slide, Inches(5.35), card_top, Inches(4.5), card_height - Inches(0.9), COLOR_BG_CARD, COLOR_BORDER)
        box = slide.shapes.add_textbox(Inches(5.47), card_top + Inches(0.1), Inches(4.26), card_height - Inches(1.1))
        tf = box.text_frame
        tf.word_wrap = True
        tf.margin_left = Inches(0.08); tf.margin_right = Inches(0.08)
        tf.margin_top = Inches(0.06); tf.margin_bottom = Inches(0.06)
        
        p = tf.paragraphs[0]
        p.text = data["midCard"]["title"]
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = COLOR_PURPLE_PILL
        p.space_after = Pt(6)
        for bold_text, reg_text in data["midCard"]["bullets"]:
            p = tf.add_paragraph()
            p.font.size = Pt(9.5)
            p.line_spacing = 1.15
            p.space_before = Pt(2)
            p.space_after = Pt(4)
            set_bullet_indent(p, left_margin_pt=16, hanging_indent_pt=12)
            r0 = p.add_run(); r0.text = "• "; r0.font.color.rgb = COLOR_MYNTRA_PINK; r0.font.bold = True
            r1 = p.add_run(); r1.text = bold_text + " "; r1.font.bold = True; r1.font.color.rgb = COLOR_TEXT_PRIMARY
            r2 = p.add_run(); r2.text = reg_text; r2.font.color.rgb = COLOR_TEXT_PRIMARY

        # Right Phone Screen
        phone_left = Inches(10.0)
        phone_width = Inches(2.63)
        add_card_shape(slide, phone_left, card_top, phone_width, card_height - Inches(0.9), COLOR_PHONE_BG, RGBColor(15, 23, 42))
        figma_img = data.get("figmaImage")
        if figma_img and os.path.exists(figma_img):
            slide.shapes.add_picture(figma_img, phone_left + Inches(0.06), card_top + Inches(0.06), phone_width - Inches(0.12), card_height - Inches(1.02))

        # 4 Macro Metrics Boxes along the bottom
        macro_top = card_top + card_height - Inches(0.8)
        macro_w = Inches(2.86)
        macro_gap = Inches(0.16)
        for m_idx, (m_val, m_lbl) in enumerate(data["macroMetrics"]):
            m_left = Inches(0.7) + m_idx * (macro_w + macro_gap)
            add_card_shape(slide, m_left, macro_top, macro_w, Inches(0.72), COLOR_WHITE, COLOR_BORDER)
            m_box = slide.shapes.add_textbox(m_left, macro_top + Inches(0.05), macro_w, Inches(0.62))
            tf_m = m_box.text_frame
            tf_m.word_wrap = True
            p_val = tf_m.paragraphs[0]
            p_val.text = m_val
            p_val.alignment = PP_ALIGN.CENTER
            p_val.font.size = Pt(14)
            p_val.font.bold = True
            p_val.font.color.rgb = COLOR_MYNTRA_PINK
            p_lbl = tf_m.add_paragraph()
            p_lbl.text = m_lbl
            p_lbl.alignment = PP_ALIGN.CENTER
            p_lbl.font.size = Pt(8.5)
            p_lbl.font.bold = True
            p_lbl.font.color.rgb = COLOR_TEXT_MUTED

    # ==========================================
    # SLIDE 2: CORE HYPOTHESIS & VISUAL DISCOVERY FLOW
    # ==========================================
    elif s_num == 2:
        # Top Hypothesis Card
        add_card_shape(slide, Inches(0.7), card_top, Inches(6.5), Inches(1.3), COLOR_WHITE, COLOR_BORDER)
        box = slide.shapes.add_textbox(Inches(0.82), card_top + Inches(0.08), Inches(6.26), Inches(1.14))
        tf = box.text_frame
        tf.word_wrap = True
        tf.margin_left = Inches(0.08); tf.margin_right = Inches(0.08)
        p = tf.paragraphs[0]
        p.text = "💡 THE CORE HYPOTHESIS"
        p.font.size = Pt(10.5)
        p.font.bold = True
        p.font.color.rgb = COLOR_PURPLE_PILL
        p.space_after = Pt(3)
        p_body = tf.add_paragraph()
        p_body.text = data["hypothesisBox"]
        p_body.font.size = Pt(9.5)
        p_body.line_spacing = 1.15
        p_body.font.color.rgb = COLOR_TEXT_PRIMARY

        # Bottom Left: Current Discovery Flow (4 Visual Step Process Flowchart)
        flow_top = card_top + Inches(1.42)
        add_card_shape(slide, Inches(0.7), flow_top, Inches(6.5), card_height - Inches(1.42), COLOR_WHITE, COLOR_BORDER)
        box_hdr = slide.shapes.add_textbox(Inches(0.82), flow_top + Inches(0.06), Inches(6.26), Inches(0.35))
        tf_h = box_hdr.text_frame; tf_h.word_wrap = True
        p_h = tf_h.paragraphs[0]
        p_h.text = "🔄 CURRENT DISCOVERY FLOW (THE GRAVEYARD LOOP)"
        p_h.font.size = Pt(10.5); p_h.font.bold = True; p_h.font.color.rgb = COLOR_PURPLE_PILL

        step_w = Inches(1.48)
        step_gap = Inches(0.12)
        for s_idx, (step_title, step_desc) in enumerate(data["discoveryFunnel"]):
            s_left = Inches(0.82) + s_idx * (step_w + step_gap)
            add_card_shape(slide, s_left, flow_top + Inches(0.42), step_w, card_height - Inches(1.95), COLOR_SYNTHESIS_BG, COLOR_SYNTHESIS_BORDER)
            s_box = slide.shapes.add_textbox(s_left + Inches(0.04), flow_top + Inches(0.46), step_w - Inches(0.08), card_height - Inches(2.05))
            tf_s = s_box.text_frame; tf_s.word_wrap = True
            tf_s.margin_left = Inches(0.02); tf_s.margin_right = Inches(0.02)
            p_st = tf_s.paragraphs[0]
            p_st.text = step_title
            p_st.font.size = Pt(8.5); p_st.font.bold = True; p_st.font.color.rgb = COLOR_MYNTRA_PINK; p_st.space_after = Pt(2)
            p_sd = tf_s.add_paragraph()
            p_sd.text = step_desc
            p_sd.font.size = Pt(7.5); p_sd.line_spacing = 1.1; p_sd.font.color.rgb = COLOR_TEXT_PRIMARY

        # Right: 3 Friction Cards
        f_card_w = Inches(5.2)
        f_card_h = Inches(1.34)
        for f_idx, (f_title, f_desc) in enumerate(data["frictionCards"]):
            f_top = card_top + f_idx * (f_card_h + Inches(0.13))
            add_card_shape(slide, Inches(7.433), f_top, f_card_w, f_card_h, COLOR_SYNTHESIS_BG, COLOR_SYNTHESIS_BORDER)
            f_box = slide.shapes.add_textbox(Inches(7.55), f_top + Inches(0.08), f_card_w - Inches(0.24), f_card_h - Inches(0.16))
            tf_f = f_box.text_frame
            tf_f.word_wrap = True
            tf_f.margin_left = Inches(0.08); tf_f.margin_right = Inches(0.08)
            p_ft = tf_f.paragraphs[0]
            p_ft.text = "⚠️ " + f_title
            p_ft.font.size = Pt(10.5)
            p_ft.font.bold = True
            p_ft.font.color.rgb = COLOR_MYNTRA_PINK
            p_ft.space_after = Pt(3)
            p_fb = tf_f.add_paragraph()
            p_fb.text = f_desc
            p_fb.font.size = Pt(9.5)
            p_fb.line_spacing = 1.15
            p_fb.font.color.rgb = COLOR_TEXT_PRIMARY

    # ==========================================
    # SLIDE 3: AI DISCOVERY ENGINE & NLP WORKFLOW
    # ==========================================
    elif s_num == 3:
        # Left Card: Natural Language Querying Prompts
        add_card_shape(slide, Inches(0.7), card_top, Inches(6.8), card_height, COLOR_BG_CARD, COLOR_BORDER)
        box = slide.shapes.add_textbox(Inches(0.82), card_top + Inches(0.1), Inches(6.56), card_height - Inches(0.2))
        tf = box.text_frame
        tf.word_wrap = True
        tf.margin_left = Inches(0.08); tf.margin_right = Inches(0.08)
        p = tf.paragraphs[0]
        p.text = "💬 AI INSIGHTS VIA NATURAL LANGUAGE QUERYING"
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = COLOR_PURPLE_PILL
        p.space_after = Pt(6)
        for q_txt, ans_txt in data["nlpPrompts"]:
            p1 = tf.add_paragraph()
            p1.font.size = Pt(9.5)
            p1.space_before = Pt(4)
            p1.space_after = Pt(1)
            r1 = p1.add_run(); r1.text = q_txt; r1.font.bold = True; r1.font.color.rgb = COLOR_MYNTRA_PINK
            p2 = tf.add_paragraph()
            p2.font.size = Pt(9)
            p2.line_spacing = 1.15
            p2.space_before = Pt(0)
            p2.space_after = Pt(5)
            set_bullet_indent(p2, left_margin_pt=14, hanging_indent_pt=0)
            r2 = p2.add_run(); r2.text = ans_txt; r2.font.color.rgb = COLOR_TEXT_PRIMARY

        # Right Top Card: Corpus Funnel & 3 Flowchart Process Boxes
        add_card_shape(slide, Inches(7.7), card_top, Inches(4.933), Inches(2.0), COLOR_SYNTHESIS_BG, COLOR_SYNTHESIS_BORDER)
        box_hdr = slide.shapes.add_textbox(Inches(7.82), card_top + Inches(0.06), Inches(4.69), Inches(0.35))
        tf_ch = box_hdr.text_frame; tf_ch.word_wrap = True
        p_ch = tf_ch.paragraphs[0]
        p_ch.text = "🔬 CORPUS FUNNEL & NLP PIPELINE"
        p_ch.font.size = Pt(10.5); p_ch.font.bold = True; p_ch.font.color.rgb = COLOR_SUBTITLE

        c_w = Inches(1.46)
        c_gap = Inches(0.12)
        for c_idx, (c_step, c_detail) in enumerate(data["corpusFunnel"]):
            c_left = Inches(7.82) + c_idx * (c_w + c_gap)
            add_card_shape(slide, c_left, card_top + Inches(0.42), c_w, Inches(1.45), COLOR_WHITE, COLOR_BORDER)
            c_box = slide.shapes.add_textbox(c_left + Inches(0.04), card_top + Inches(0.46), c_w - Inches(0.08), Inches(1.35))
            tf_c = c_box.text_frame; tf_c.word_wrap = True
            tf_c.margin_left = Inches(0.02); tf_c.margin_right = Inches(0.02)
            p_ct = tf_c.paragraphs[0]
            p_ct.text = c_step
            p_ct.font.size = Pt(8.5); p_ct.font.bold = True; p_ct.font.color.rgb = COLOR_MYNTRA_PINK; p_ct.space_after = Pt(2)
            p_cd = tf_c.add_paragraph()
            p_cd.text = c_detail
            p_cd.font.size = Pt(7.5); p_cd.line_spacing = 1.1; p_cd.font.color.rgb = COLOR_TEXT_PRIMARY

        # Right Bottom Card: Final Key Takeaways
        t_top = card_top + Inches(2.15)
        add_card_shape(slide, Inches(7.7), t_top, Inches(4.933), card_height - Inches(2.15), COLOR_BG_CARD, COLOR_BORDER)
        box = slide.shapes.add_textbox(Inches(7.82), t_top + Inches(0.08), Inches(4.69), card_height - Inches(2.31))
        tf = box.text_frame
        tf.word_wrap = True
        tf.margin_left = Inches(0.08); tf.margin_right = Inches(0.08)
        p = tf.paragraphs[0]
        p.text = "✅ FINAL RESEARCH TAKEAWAYS"
        p.font.size = Pt(10.5)
        p.font.bold = True
        p.font.color.rgb = COLOR_MYNTRA_GREEN
        p.space_after = Pt(4)
        for t_item in data["finalTakeaways"]:
            p = tf.add_paragraph()
            p.font.size = Pt(9.5)
            p.line_spacing = 1.15
            p.space_before = Pt(3)
            p.space_after = Pt(4)
            set_bullet_indent(p, left_margin_pt=16, hanging_indent_pt=12)
            r0 = p.add_run(); r0.text = "✓ "; r0.font.color.rgb = COLOR_MYNTRA_GREEN; r0.font.bold = True
            r1 = p.add_run(); r1.text = t_item; r1.font.color.rgb = COLOR_TEXT_PRIMARY

    # ==========================================
    # SLIDE 4: 4-QUADRANT TARGET SEGMENT CANVAS
    # ==========================================
    elif s_num == 4:
        quad_w = Inches(5.8)
        quad_h = Inches(2.05)
        positions = [
            (Inches(0.7), card_top),
            (Inches(6.8), card_top),
            (Inches(0.7), card_top + Inches(2.18)),
            (Inches(6.8), card_top + Inches(2.18))
        ]
        for q_idx, q_data in enumerate(data["quadrants"]):
            q_left, q_top = positions[q_idx]
            add_card_shape(slide, q_left, q_top, quad_w, quad_h, COLOR_BG_CARD, COLOR_BORDER)
            box = slide.shapes.add_textbox(q_left + Inches(0.12), q_top + Inches(0.08), quad_w - Inches(0.24), quad_h - Inches(0.16))
            tf = box.text_frame
            tf.word_wrap = True
            tf.margin_left = Inches(0.08); tf.margin_right = Inches(0.08)
            p = tf.paragraphs[0]
            p.text = f"{q_data['icon']} {q_data['title']}"
            p.font.size = Pt(10.5)
            p.font.bold = True
            p.font.color.rgb = COLOR_PURPLE_PILL
            p.space_after = Pt(4)
            for b_lbl, b_txt in q_data["bullets"]:
                p = tf.add_paragraph()
                p.font.size = Pt(9)
                p.line_spacing = 1.15
                p.space_before = Pt(1)
                p.space_after = Pt(3)
                set_bullet_indent(p, left_margin_pt=14, hanging_indent_pt=10)
                r1 = p.add_run(); r1.text = "• " + b_lbl + " "; r1.font.bold = True; r1.font.color.rgb = COLOR_TEXT_PRIMARY
                r2 = p.add_run(); r2.text = b_txt; r2.font.color.rgb = COLOR_TEXT_PRIMARY

    # ==========================================
    # SLIDE 5: USER RESEARCH INTERVIEW INSIGHTS TABLE
    # ==========================================
    elif s_num == 5:
        # Top 3 Synthesis Cards
        syn_w = Inches(3.86)
        syn_gap = Inches(0.17)
        for s_idx, (s_title, s_desc) in enumerate(data["topSynthesis"]):
            s_left = Inches(0.7) + s_idx * (syn_w + syn_gap)
            add_card_shape(slide, s_left, card_top, syn_w, Inches(1.1), COLOR_SYNTHESIS_BG, COLOR_SYNTHESIS_BORDER)
            box = slide.shapes.add_textbox(s_left + Inches(0.08), card_top + Inches(0.06), syn_w - Inches(0.16), Inches(0.98))
            tf = box.text_frame
            tf.word_wrap = True
            tf.margin_left = Inches(0.06); tf.margin_right = Inches(0.06)
            p = tf.paragraphs[0]
            p.text = "📌 " + s_title
            p.font.size = Pt(10)
            p.font.bold = True
            p.font.color.rgb = COLOR_MYNTRA_PINK
            p.space_after = Pt(2)
            p2 = tf.add_paragraph()
            p2.text = s_desc
            p2.font.size = Pt(8.5)
            p2.line_spacing = 1.12
            p2.font.color.rgb = COLOR_TEXT_PRIMARY

        # Bottom User Interview Table
        table_top = card_top + Inches(1.22)
        add_card_shape(slide, Inches(0.7), table_top, Inches(11.933), card_height - Inches(1.22), COLOR_BG_CARD, COLOR_BORDER)
        box = slide.shapes.add_textbox(Inches(0.82), table_top + Inches(0.06), Inches(11.69), card_height - Inches(1.34))
        tf = box.text_frame
        tf.word_wrap = True
        tf.margin_left = Inches(0.08); tf.margin_right = Inches(0.08)
        p = tf.paragraphs[0]
        p.text = "📋 QUALITATIVE USER INTERVIEWS (N=6 ANONYMOUS PARTICIPANTS)"
        p.font.size = Pt(10)
        p.font.bold = True
        p.font.color.rgb = COLOR_PURPLE_PILL
        p.space_after = Pt(4)
        for u_name, u_demo, u_habit, u_barrier, u_trigger in data["userTable"]:
            p = tf.add_paragraph()
            p.font.size = Pt(8.5)
            p.line_spacing = 1.15
            p.space_before = Pt(1)
            p.space_after = Pt(3)
            set_bullet_indent(p, left_margin_pt=14, hanging_indent_pt=10)
            r0 = p.add_run(); r0.text = "• "; r0.font.bold = True; r0.font.color.rgb = COLOR_MYNTRA_PINK
            r1 = p.add_run(); r1.text = u_name + " (" + u_demo + "): "; r1.font.bold = True; r1.font.color.rgb = COLOR_TEXT_PRIMARY
            r2 = p.add_run(); r2.text = "Habit: " + u_habit + " | Barrier: " + u_barrier + " | Trigger: " + u_trigger; r2.font.color.rgb = COLOR_TEXT_PRIMARY

    # ==========================================
    # SLIDE 6: PROBLEM FRAMING (5 GOLD-STANDARD PM QUESTIONS)
    # ==========================================
    elif s_num == 6:
        # Top Row: 3 Cards (Q1, Q2, Q3)
        row1_w = Inches(3.86)
        row1_gap = Inches(0.17)
        row1_h = Inches(1.85)
        for q_idx in range(3):
            q_data = data["pmQuestions"][q_idx]
            q_left = Inches(0.7) + q_idx * (row1_w + row1_gap)
            add_card_shape(slide, q_left, card_top, row1_w, row1_h, COLOR_BG_CARD, COLOR_BORDER)
            box = slide.shapes.add_textbox(q_left + Inches(0.08), card_top + Inches(0.06), row1_w - Inches(0.16), row1_h - Inches(0.12))
            tf = box.text_frame
            tf.word_wrap = True
            tf.margin_left = Inches(0.06); tf.margin_right = Inches(0.06)
            p = tf.paragraphs[0]
            p.text = f"❓ {q_data['q']}"
            p.font.size = Pt(10)
            p.font.bold = True
            p.font.color.rgb = COLOR_PURPLE_PILL
            p.space_after = Pt(3)
            p2 = tf.add_paragraph()
            p2.text = q_data['ans']
            p2.font.size = Pt(8.5)
            p2.line_spacing = 1.15
            p2.font.color.rgb = COLOR_TEXT_PRIMARY

        # Bottom Row: 2 Cards (Q4 - Value, Q5 - Why Now)
        row2_top = card_top + Inches(1.98)
        row2_w = Inches(5.88)
        row2_gap = Inches(0.17)
        row2_h = card_height - Inches(1.98)

        # Q4 Card
        q4_data = data["pmQuestions"][3]
        add_card_shape(slide, Inches(0.7), row2_top, row2_w, row2_h, COLOR_BG_CARD, COLOR_BORDER)
        box = slide.shapes.add_textbox(Inches(0.78), row2_top + Inches(0.06), row2_w - Inches(0.16), row2_h - Inches(0.12))
        tf = box.text_frame
        tf.word_wrap = True
        tf.margin_left = Inches(0.06); tf.margin_right = Inches(0.06)
        p = tf.paragraphs[0]
        p.text = f"💰 {q4_data['q']}"
        p.font.size = Pt(10)
        p.font.bold = True
        p.font.color.rgb = COLOR_PURPLE_PILL
        p.space_after = Pt(2)
        p_c = tf.add_paragraph()
        p_c.text = "• " + q4_data["customerValue"]
        p_c.font.size = Pt(8.5)
        p_c.line_spacing = 1.12
        p_c.font.color.rgb = COLOR_TEXT_PRIMARY
        set_bullet_indent(p_c, left_margin_pt=12, hanging_indent_pt=8)
        p_b = tf.add_paragraph()
        p_b.text = "• " + q4_data["businessValue"]
        p_b.font.size = Pt(8.5)
        p_b.line_spacing = 1.12
        p_b.font.color.rgb = COLOR_TEXT_PRIMARY
        set_bullet_indent(p_b, left_margin_pt=12, hanging_indent_pt=8)

        # Q5 Card
        q5_data = data["pmQuestions"][4]
        add_card_shape(slide, Inches(6.75), row2_top, row2_w, row2_h, COLOR_BG_CARD, COLOR_BORDER)
        box = slide.shapes.add_textbox(Inches(6.83), row2_top + Inches(0.06), row2_w - Inches(0.16), row2_h - Inches(0.12))
        tf = box.text_frame
        tf.word_wrap = True
        tf.margin_left = Inches(0.06); tf.margin_right = Inches(0.06)
        p = tf.paragraphs[0]
        p.text = f"⏰ {q5_data['q']}"
        p.font.size = Pt(10)
        p.font.bold = True
        p.font.color.rgb = COLOR_PURPLE_PILL
        p.space_after = Pt(2)
        p_ans = tf.add_paragraph()
        p_ans.text = q5_data['ans']
        p_ans.font.size = Pt(8.5)
        p_ans.line_spacing = 1.15
        p_ans.font.color.rgb = COLOR_TEXT_PRIMARY

    # ==========================================
    # SLIDE 7: IDEATION, PRINCIPLES & RICE PRIORITIZATION
    # ==========================================
    elif s_num == 7:
        # Top Principles Card
        add_card_shape(slide, Inches(0.7), card_top, Inches(11.933), Inches(1.35), COLOR_SYNTHESIS_BG, COLOR_SYNTHESIS_BORDER)
        box = slide.shapes.add_textbox(Inches(0.82), card_top + Inches(0.06), Inches(11.69), Inches(1.23))
        tf = box.text_frame
        tf.word_wrap = True
        tf.margin_left = Inches(0.08); tf.margin_right = Inches(0.08)
        p = tf.paragraphs[0]
        p.text = "⭐ CORE PRINCIPLES OF THE FRAMEWORK"
        p.font.size = Pt(10.5)
        p.font.bold = True
        p.font.color.rgb = COLOR_MYNTRA_PINK
        p.space_after = Pt(3)
        for pr_title, pr_desc in data["principles"]:
            p = tf.add_paragraph()
            p.font.size = Pt(9)
            p.line_spacing = 1.15
            p.space_before = Pt(1)
            p.space_after = Pt(2)
            set_bullet_indent(p, left_margin_pt=14, hanging_indent_pt=10)
            r1 = p.add_run(); r1.text = "• " + pr_title + ": "; r1.font.bold = True; r1.font.color.rgb = COLOR_TEXT_PRIMARY
            r2 = p.add_run(); r2.text = pr_desc; r2.font.color.rgb = COLOR_TEXT_PRIMARY

        # Bottom RICE Prioritization Table
        r_top = card_top + Inches(1.48)
        add_card_shape(slide, Inches(0.7), r_top, Inches(11.933), card_height - Inches(1.48), COLOR_BG_CARD, COLOR_BORDER)
        box = slide.shapes.add_textbox(Inches(0.82), r_top + Inches(0.08), Inches(11.69), card_height - Inches(1.64))
        tf = box.text_frame
        tf.word_wrap = True
        tf.margin_left = Inches(0.08); tf.margin_right = Inches(0.08)
        p = tf.paragraphs[0]
        p.text = "📊 SOLUTION PRIORITIZATION (RICE FRAMEWORK MATRIX)"
        p.font.size = Pt(10.5)
        p.font.bold = True
        p.font.color.rgb = COLOR_PURPLE_PILL
        p.space_after = Pt(4)
        for sol_name, sol_desc, r_val, i_val, c_val, e_val, score_val, verdict_txt in data["riceTable"]:
            p = tf.add_paragraph()
            p.font.size = Pt(9)
            p.line_spacing = 1.15
            p.space_before = Pt(2)
            p.space_after = Pt(4)
            set_bullet_indent(p, left_margin_pt=14, hanging_indent_pt=10)
            r0 = p.add_run(); r0.text = "► "; r0.font.bold = True; r0.font.color.rgb = COLOR_MYNTRA_PINK
            r1 = p.add_run(); r1.text = sol_name + " — "; r1.font.bold = True; r1.font.color.rgb = COLOR_TEXT_PRIMARY
            r2 = p.add_run(); r2.text = f"R: {r_val}/10 | I: {i_val}/5 | C: {c_val} | E: {e_val}/5 | Score: {score_val} | Verdict: "; r2.font.color.rgb = COLOR_TEXT_MUTED
            r3 = p.add_run(); r3.text = verdict_txt; r3.font.bold = True; r3.font.color.rgb = COLOR_MYNTRA_GREEN if "Winner" in verdict_txt else COLOR_MYNTRA_PINK

    # ==========================================
    # SLIDE 8: MVP ARCHITECTURE & FEATURE SHOWCASE (VISUAL FLOWCHART)
    # ==========================================
    elif s_num == 8:
        # Top Architecture Pipeline: 4 Visual Flowchart Process Boxes
        box_hdr = slide.shapes.add_textbox(Inches(0.7), card_top - Inches(0.04), Inches(11.933), Inches(0.32))
        tf_h = box_hdr.text_frame; tf_h.word_wrap = True
        p_h = tf_h.paragraphs[0]
        p_h.text = "⚙️ DECISION STUDIO ARCHITECTURE PIPELINE (4-STEP ML FLOW)"
        p_h.font.size = Pt(10.5); p_h.font.bold = True; p_h.font.color.rgb = COLOR_PURPLE_PILL

        pipe_w = Inches(2.82)
        pipe_gap = Inches(0.21)
        pipe_h = Inches(1.18)
        for p_idx, (p_step, p_desc) in enumerate(data["pipeline"]):
            p_left = Inches(0.7) + p_idx * (pipe_w + pipe_gap)
            add_card_shape(slide, p_left, card_top + Inches(0.32), pipe_w, pipe_h, COLOR_WHITE, COLOR_BORDER)
            p_box = slide.shapes.add_textbox(p_left + Inches(0.06), card_top + Inches(0.36), pipe_w - Inches(0.12), pipe_h - Inches(0.08))
            tf_p = p_box.text_frame; tf_p.word_wrap = True
            tf_p.margin_left = Inches(0.02); tf_p.margin_right = Inches(0.02)
            p_pt = tf_p.paragraphs[0]
            p_pt.text = p_step
            p_pt.font.size = Pt(9); p_pt.font.bold = True; p_pt.font.color.rgb = COLOR_MYNTRA_PINK; p_pt.space_after = Pt(2)
            p_pd = tf_p.add_paragraph()
            p_pd.text = p_desc
            p_pd.font.size = Pt(7.5); p_pd.line_spacing = 1.1; p_pd.font.color.rgb = COLOR_TEXT_PRIMARY

        # Bottom: 3 MVP Feature Wireframe Cards with Figma Embeds
        w_top = card_top + Inches(1.6)
        w_card_w = Inches(3.8)
        w_card_gap = Inches(0.26)
        for m_idx, feat in enumerate(data["mvpFeatures"]):
            c_left = Inches(0.7) + m_idx * (w_card_w + w_card_gap)
            add_card_shape(slide, c_left, w_top, w_card_w, card_height - Inches(1.6), COLOR_BG_CARD, COLOR_BORDER)
            box = slide.shapes.add_textbox(c_left + Inches(0.08), w_top + Inches(0.04), w_card_w - Inches(0.16), Inches(0.38))
            tf = box.text_frame
            tf.word_wrap = True
            p = tf.paragraphs[0]
            p.text = feat["title"]
            p.font.size = Pt(9.5)
            p.font.bold = True
            p.font.color.rgb = COLOR_PURPLE_PILL
            img_path = feat.get("figmaImage")
            if img_path and os.path.exists(img_path):
                slide.shapes.add_picture(img_path, c_left + Inches(0.12), w_top + Inches(0.4), w_card_w - Inches(0.24), Inches(2.2))

    # ==========================================
    # SLIDE 9: SUCCESS METRICS & EXPERIMENTATION HIERARCHY
    # ==========================================
    elif s_num == 9:
        # Top Metrics Hierarchy Table
        add_card_shape(slide, Inches(0.7), card_top, Inches(11.933), Inches(2.2), COLOR_BG_CARD, COLOR_BORDER)
        box = slide.shapes.add_textbox(Inches(0.82), card_top + Inches(0.08), Inches(11.69), Inches(2.04))
        tf = box.text_frame
        tf.word_wrap = True
        tf.margin_left = Inches(0.08); tf.margin_right = Inches(0.08)
        p = tf.paragraphs[0]
        p.text = "⭐ SUCCESS METRICS HIERARCHY & OPERATIONAL GUARDRAILS"
        p.font.size = Pt(10.5)
        p.font.bold = True
        p.font.color.rgb = COLOR_PURPLE_PILL
        p.space_after = Pt(4)
        for m_type, m_kpi, m_target, m_goal in data["metricsTable"]:
            p = tf.add_paragraph()
            p.font.size = Pt(9)
            p.line_spacing = 1.15
            p.space_before = Pt(2)
            p.space_after = Pt(3)
            set_bullet_indent(p, left_margin_pt=14, hanging_indent_pt=10)
            r0 = p.add_run(); r0.text = "► "; r0.font.bold = True; r0.font.color.rgb = COLOR_MYNTRA_PINK
            r1 = p.add_run(); r1.text = m_type + ": "; r1.font.bold = True; r1.font.color.rgb = COLOR_TEXT_PRIMARY
            r2 = p.add_run(); r2.text = m_kpi + " [" + m_target + "] — " + m_goal; r2.font.color.rgb = COLOR_TEXT_PRIMARY

        # Bottom Experimentation Design Card
        exp_top = card_top + Inches(2.32)
        add_card_shape(slide, Inches(0.7), exp_top, Inches(11.933), card_height - Inches(2.32), COLOR_SYNTHESIS_BG, COLOR_SYNTHESIS_BORDER)
        box = slide.shapes.add_textbox(Inches(0.82), exp_top + Inches(0.08), Inches(11.69), card_height - Inches(2.48))
        tf = box.text_frame
        tf.word_wrap = True
        tf.margin_left = Inches(0.08); tf.margin_right = Inches(0.08)
        p = tf.paragraphs[0]
        p.text = "🔬 200,000-USER RANDOMIZED CONTROLLED TRIAL (RCT) & SAFEGUARDS"
        p.font.size = Pt(10)
        p.font.bold = True
        p.font.color.rgb = COLOR_SUBTITLE
        p.space_after = Pt(3)
        for exp_lbl, exp_txt in data["experimentDesign"]:
            p = tf.add_paragraph()
            p.font.size = Pt(8.5)
            p.line_spacing = 1.15
            p.space_before = Pt(1)
            p.space_after = Pt(2)
            set_bullet_indent(p, left_margin_pt=14, hanging_indent_pt=10)
            r1 = p.add_run(); r1.text = "• " + exp_lbl + " "; r1.font.bold = True; r1.font.color.rgb = COLOR_TEXT_PRIMARY
            r2 = p.add_run(); r2.text = exp_txt; r2.font.color.rgb = COLOR_TEXT_PRIMARY

    # ==========================================
    # SLIDE 10: PITFALLS, MITIGATIONS & PHASED ROLLOUT
    # ==========================================
    elif s_num == 10:
        # Top 3 Pitfall Cards
        pit_w = Inches(3.86)
        pit_gap = Inches(0.17)
        for p_idx, pit in enumerate(data["pitfalls"]):
            p_left = Inches(0.7) + p_idx * (pit_w + pit_gap)
            add_card_shape(slide, p_left, card_top, pit_w, Inches(1.6), COLOR_BG_CARD, COLOR_BORDER)
            box = slide.shapes.add_textbox(p_left + Inches(0.08), card_top + Inches(0.06), pit_w - Inches(0.16), Inches(1.48))
            tf = box.text_frame
            tf.word_wrap = True
            tf.margin_left = Inches(0.06); tf.margin_right = Inches(0.06)
            p = tf.paragraphs[0]
            p.text = "⚠️ " + pit["title"]
            p.font.size = Pt(10)
            p.font.bold = True
            p.font.color.rgb = COLOR_MYNTRA_PINK
            p.space_after = Pt(2)
            p_pit = tf.add_paragraph()
            p_pit.font.size = Pt(8.5); p_pit.line_spacing = 1.12; p_pit.space_after = Pt(2)
            set_bullet_indent(p_pit, left_margin_pt=10, hanging_indent_pt=0)
            r1 = p_pit.add_run(); r1.text = "Pitfall: "; r1.font.bold = True; r1.font.color.rgb = COLOR_TEXT_PRIMARY
            r2 = p_pit.add_run(); r2.text = pit["pitfall"]; r2.font.color.rgb = COLOR_TEXT_PRIMARY
            p_mit = tf.add_paragraph()
            p_mit.font.size = Pt(8.5); p_mit.line_spacing = 1.12; p_mit.space_after = Pt(0)
            set_bullet_indent(p_mit, left_margin_pt=10, hanging_indent_pt=0)
            r3 = p_mit.add_run(); r3.text = "Mitigation: "; r3.font.bold = True; r3.font.color.rgb = COLOR_MYNTRA_GREEN
            r4 = p_mit.add_run(); r4.text = pit["mitigation"]; r4.font.color.rgb = COLOR_TEXT_PRIMARY

        # Bottom: 3-Phase Rollout Roadmap
        r_top = card_top + Inches(1.72)
        r_card_w = Inches(3.86)
        r_card_gap = Inches(0.17)
        r_card_h = card_height - Inches(1.72)
        for r_idx, phase in enumerate(data["rolloutPhases"]):
            r_left = Inches(0.7) + r_idx * (r_card_w + r_card_gap)
            add_card_shape(slide, r_left, r_top, r_card_w, r_card_h, COLOR_SYNTHESIS_BG, COLOR_SYNTHESIS_BORDER)
            box = slide.shapes.add_textbox(r_left + Inches(0.08), r_top + Inches(0.06), r_card_w - Inches(0.16), r_card_h - Inches(0.12))
            tf = box.text_frame
            tf.word_wrap = True
            tf.margin_left = Inches(0.06); tf.margin_right = Inches(0.06)
            p = tf.paragraphs[0]
            p.text = "🚀 " + phase["phase"]
            p.font.size = Pt(10)
            p.font.bold = True
            p.font.color.rgb = COLOR_PURPLE_PILL
            p.space_after = Pt(2)
            
            p_tgt = tf.add_paragraph()
            p_tgt.font.size = Pt(8.5); p_tgt.line_spacing = 1.12; p_tgt.space_after = Pt(2)
            set_bullet_indent(p_tgt, left_margin_pt=10, hanging_indent_pt=0)
            r1 = p_tgt.add_run(); r1.text = "Target: "; r1.font.bold = True; r1.font.color.rgb = COLOR_TEXT_PRIMARY
            r2 = p_tgt.add_run(); r2.text = phase["target"]; r2.font.color.rgb = COLOR_TEXT_PRIMARY
            
            p_scp = tf.add_paragraph()
            p_scp.font.size = Pt(8.5); p_scp.line_spacing = 1.12; p_scp.space_after = Pt(2)
            set_bullet_indent(p_scp, left_margin_pt=10, hanging_indent_pt=0)
            r3 = p_scp.add_run(); r3.text = "Scope: "; r3.font.bold = True; r3.font.color.rgb = COLOR_TEXT_PRIMARY
            r4 = p_scp.add_run(); r4.text = phase["scope"]; r4.font.color.rgb = COLOR_TEXT_PRIMARY
            
            p_gate = tf.add_paragraph()
            p_gate.font.size = Pt(8.5); p_gate.line_spacing = 1.12; p_gate.space_after = Pt(0)
            set_bullet_indent(p_gate, left_margin_pt=10, hanging_indent_pt=0)
            r5 = p_gate.add_run(); r5.text = "Gate: "; r5.font.bold = True; r5.font.color.rgb = COLOR_MYNTRA_GREEN
            r6 = p_gate.add_run(); r6.text = phase["gate"]; r6.font.color.rgb = COLOR_TEXT_PRIMARY

    # 4. Bottom Synthesis Banner
    synth_top = Inches(6.05)
    synth_height = Inches(0.68)
    add_card_shape(slide, Inches(0.7), synth_top, Inches(11.933), synth_height, COLOR_SYNTHESIS_BG, COLOR_SYNTHESIS_BORDER)
    
    synth_box = slide.shapes.add_textbox(Inches(0.85), synth_top + Inches(0.05), Inches(11.633), synth_height - Inches(0.1))
    tf = synth_box.text_frame
    tf.word_wrap = True
    tf.margin_left = Inches(0.1)
    tf.margin_right = Inches(0.1)
    tf.margin_top = Inches(0.04)
    tf.margin_bottom = Inches(0.04)
    
    p = tf.paragraphs[0]
    p.text = "★ " + data["bottomBanner"]["title"]
    p.font.size = Pt(9.5)
    p.font.bold = True
    p.font.color.rgb = RGBColor(67, 56, 202)
    p.space_after = Pt(2)
    
    p2 = tf.add_paragraph()
    p2.text = data["bottomBanner"]["text"]
    p2.font.size = Pt(9)
    p2.font.bold = True
    p2.font.color.rgb = COLOR_SYNTHESIS_TEXT
    p2.line_spacing = 1.15
    p2.space_before = Pt(0)

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
        tf.vertical_anchor = MSO_ANCHOR.MIDDLE
        tf.margin_left = Inches(0.02)
        tf.margin_right = Inches(0.02)
        tf.margin_top = Inches(0.02)
        tf.margin_bottom = Inches(0.02)
        
        p = tf.paragraphs[0]
        p.text = track_name
        p.alignment = PP_ALIGN.CENTER
        p.font.size = Pt(9)
        p.font.bold = True
        p.font.color.rgb = text_col
        p.space_before = Pt(0)
        p.space_after = Pt(0)

# Save Presentation
output_path_primary = "Myntra_Wishlist_Studio_10_Slide_Deck.pptx"
output_path_updated = "Myntra_Wishlist_Studio_10_Slide_Deck_Updated.pptx"

try:
    prs.save(output_path_primary)
    print(f"SUCCESS: Generated 16:9 Executive PowerPoint Presentation at {output_path_primary}")
except PermissionError:
    print(f"NOTICE: {output_path_primary} is locked. Saved updated presentation at {output_path_updated}")

try:
    prs.save(output_path_updated)
    print(f"SUCCESS: Saved updated presentation at {output_path_updated}")
except PermissionError:
    print(f"NOTICE: {output_path_updated} is locked.")
