import os
import subprocess
import time

edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
if not os.path.exists(edge_path):
    edge_path = r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"

target_dir = os.path.join(os.getcwd(), 'figma_design_assets')

assets = [
    ("01_Figma_Mobile_Spec_Comparison_Matrix.svg", "01_Figma_Mobile_Spec_Comparison_Matrix.png", 375, 812),
    ("02_Figma_Mobile_AI_Outfit_Coordinator.svg", "02_Figma_Mobile_AI_Outfit_Coordinator.png", 375, 812),
    ("03_Figma_Mobile_WhatsApp_Voting_Card.svg", "03_Figma_Mobile_WhatsApp_Voting_Card.png", 375, 812),
    ("04_Figma_Mobile_Wishlist_Studio_Home.svg", "04_Figma_Mobile_Wishlist_Studio_Home.png", 375, 812),
    ("05_Figma_Desktop_Web_Wishlist_Studio.svg", "05_Figma_Desktop_Web_Wishlist_Studio.png", 1440, 900)
]

for svg_name, png_name, w, h in assets:
    svg_file = os.path.join(target_dir, svg_name)
    png_file = os.path.join(target_dir, png_name)
    html_wrapper = os.path.join(target_dir, f"temp_{svg_name}.html")
    
    with open(html_wrapper, 'w', encoding='utf-8') as f:
        f.write(f'''<!DOCTYPE html>
<html>
<head>
<style>
  body {{ margin: 0; padding: 0; background: transparent; overflow: hidden; }}
  svg {{ width: {w}px; height: {h}px; display: block; }}
</style>
</head>
<body>
{open(svg_file, 'r', encoding='utf-8').read()}
</body>
</html>''')
    
    file_url = "file:///" + html_wrapper.replace("\\", "/")
    cmd = [
        edge_path,
        "--headless=new",
        "--disable-gpu",
        "--hide-scrollbars",
        f"--window-size={w},{h}",
        f"--screenshot={png_file}",
        file_url
    ]
    
    print(f"Rendering {svg_name} -> {png_name} ({w}x{h})...")
    subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    if os.path.exists(png_file):
        print(f"SUCCESS: {png_name} created ({os.path.getsize(png_file)} bytes)")
    else:
        print(f"FAILED to create {png_name}")
        
    if os.path.exists(html_wrapper):
        os.remove(html_wrapper)
