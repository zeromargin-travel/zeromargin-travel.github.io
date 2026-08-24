import json
import os

def generate_paris_lp():
    os.makedirs('destinations', exist_ok=True)
    
    # Load Paris Data
    with open('data/cities/paris.json', 'r', encoding='utf-8') as f:
        spots = json.load(f)
        
    top_spots = [s for s in spots if s.get('top7')]
    if not top_spots:
        top_spots = spots[:7]
        
    spots_html = ""
    for idx, s in enumerate(top_spots[:5]):
        spots_html += f"""
        <div style="display:flex; gap:1rem; margin-bottom:1.5rem; background:#FFF; border-radius:12px; padding:1rem; box-shadow:0 4px 6px rgba(0,0,0,0.05);">
            <img src="../{s.get('image')}" alt="{s.get('name')}" style="width:100px; height:100px; object-fit:cover; border-radius:8px;">
            <div>
                <h3 style="margin:0 0 0.5rem 0; font-size:1.2rem; color:#0F172A;">{idx+1}. {s.get('name')}</h3>
                <p style="margin:0; font-size:0.9rem; color:#475569;">{s.get('description', '')[:120]}...</p>
                <div style="margin-top:0.5rem; font-size:0.8rem; color:#047857; font-weight:bold;">★ {s.get('rating')}</div>
            </div>
        </div>
        """

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>1-Day Paris Walking Tour & Itinerary | Free AI Google Maps Route</title>
    <meta name="description" content="Explore Paris smarter. Generate a 1-day walking tour with handpicked ★4.5+ spots and instant Google Maps multi-stop navigation. 100% Free.">
    <style>
        body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; line-height: 1.6; color: #333; margin: 0; background: #F8FAFC; }}
        .header {{ background: #0F172A; color: white; padding: 3rem 1rem; text-align: center; }}
        .container {{ max-width: 800px; margin: 0 auto; padding: 2rem 1rem; }}
        .cta-btn {{ display: block; width: 100%; max-width: 400px; margin: 2rem auto; text-align: center; background: #F59E0B; color: white; padding: 1rem; border-radius: 50px; text-decoration: none; font-weight: bold; font-size: 1.1rem; box-shadow: 0 4px 15px rgba(245, 158, 11, 0.4); transition: transform 0.2s; }}
        .cta-btn:hover {{ transform: translateY(-2px); }}
        .footer {{ text-align: center; padding: 2rem; color: #64748B; font-size: 0.85rem; }}
    </style>
</head>
<body>
    <div class="header">
        <h1 style="margin-bottom:0.5rem;">The Ultimate 1-Day Paris Walking Tour</h1>
        <p style="font-size:1.2rem; color:#CBD5E1;">Instantly send this route to your Google Maps. 100% Free.</p>
    </div>
    
    <div class="container">
        <h2>Experience the Magic of Paris</h2>
        <p>Planning a trip to Paris can be overwhelming. That's why we've curated the perfect 1-day walking tour featuring only the highest-rated (★4.5+) spots. From the iconic Eiffel Tower to the historic Louvre Museum, experience the best of the French capital without the planning fatigue.</p>
        
        <a href="../index.html?country=France&city=Paris%2C%20France" class="cta-btn">🚀 Customize this Paris Route in 1 Click</a>
        
        <h2 style="margin-top:3rem;">Top Highlights in This Route</h2>
        {spots_html}
        
        <a href="../index.html?country=France&city=Paris%2C%20France" class="cta-btn" style="background:#047857; box-shadow: 0 4px 15px rgba(4, 120, 87, 0.4);">📍 Load Full Route in 0 Margin Travel</a>
    </div>
    
    <div class="footer">
        &copy; 2026 0 Margin Travel. All rights reserved.
    </div>
</body>
</html>"""

    with open('destinations/paris.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Generated destinations/paris.html")

if __name__ == "__main__":
    generate_paris_lp()
