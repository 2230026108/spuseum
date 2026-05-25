import os

output_dir = 'public/images/exhibition'
os.makedirs(output_dir, exist_ok=True)

svgs = {
    'frame1.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600">
  <defs><linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#1a1a2e"/><stop offset="100%" stop-color="#16213e"/></linearGradient></defs>
  <rect width="800" height="600" fill="url(#bg)"/>
  <text x="400" y="80" text-anchor="middle" fill="#c9a84c" font-family="serif" font-size="28">Research Coordinates</text>
  <line x1="200" y1="100" x2="600" y2="100" stroke="#c9a84c" stroke-width="1" opacity="0.5"/>
  <circle cx="250" cy="250" r="100" fill="none" stroke="#c9a84c" stroke-width="2" opacity="0.6"/>
  <circle cx="250" cy="250" r="60" fill="none" stroke="#c9a84c" stroke-width="1" opacity="0.3"/>
  <text x="250" y="255" text-anchor="middle" fill="#c9a84c" font-family="serif" font-size="14">ARCHAEOLOGY</text>
  <circle cx="550" cy="250" r="100" fill="none" stroke="#4a90d9" stroke-width="2" opacity="0.6"/>
  <circle cx="550" cy="250" r="60" fill="none" stroke="#4a90d9" stroke-width="1" opacity="0.3"/>
  <text x="550" y="255" text-anchor="middle" fill="#4a90d9" font-family="serif" font-size="14">TECHNOLOGY</text>
  <line x1="350" y1="250" x2="450" y2="250" stroke="#fff" stroke-width="1" opacity="0.4"/>
  <text x="400" y="420" text-anchor="middle" fill="#fff" font-family="sans-serif" font-size="14" opacity="0.8">Silk Road Era - Contemporary Globalization</text>
  <text x="400" y="450" text-anchor="middle" fill="#c9a84c" font-family="sans-serif" font-size="12" opacity="0.7">Cross-civilizational Exchange | Digital Silk Road | Cultural Heritage</text>
</svg>''',
    'frame2.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600">
  <defs><linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#1a1a2e"/><stop offset="100%" stop-color="#0f3460"/></linearGradient></defs>
  <rect width="800" height="600" fill="url(#bg)"/>
  <text x="400" y="80" text-anchor="middle" fill="#c9a84c" font-family="serif" font-size="28">Why This AI Tool?</text>
  <rect x="150" y="120" width="200" height="150" rx="8" fill="#16213e" stroke="#c9a84c" stroke-width="1" opacity="0.8"/>
  <text x="250" y="200" text-anchor="middle" fill="#c9a84c" font-family="sans-serif" font-size="12">AI Video</text>
  <text x="250" y="220" text-anchor="middle" fill="#c9a84c" font-family="sans-serif" font-size="12">Generation</text>
  <rect x="450" y="120" width="200" height="150" rx="8" fill="#16213e" stroke="#4a90d9" stroke-width="1" opacity="0.8"/>
  <text x="550" y="200" text-anchor="middle" fill="#4a90d9" font-family="sans-serif" font-size="12">Digital</text>
  <text x="550" y="220" text-anchor="middle" fill="#4a90d9" font-family="sans-serif" font-size="12">Reconstruction</text>
  <text x="400" y="420" text-anchor="middle" fill="#fff" font-family="sans-serif" font-size="14" opacity="0.8">JiMeng AI Video Generation</text>
  <text x="400" y="450" text-anchor="middle" fill="#c9a84c" font-family="sans-serif" font-size="12" opacity="0.7">Technology is not only studying history, but reactivating history.</text>
</svg>''',
    'frame3.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600">
  <defs><linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#1a1a2e"/><stop offset="100%" stop-color="#16213e"/></linearGradient></defs>
  <rect width="800" height="600" fill="url(#bg)"/>
  <text x="400" y="80" text-anchor="middle" fill="#c9a84c" font-family="serif" font-size="28">Why These Historical Periods?</text>
  <path d="M100,300 C200,180 300,250 400,200 C500,150 600,220 700,180" fill="none" stroke="#c9a84c" stroke-width="3" opacity="0.6"/>
  <circle cx="100" cy="300" r="15" fill="#c9a84c" opacity="0.3"/>
  <circle cx="400" cy="200" r="15" fill="#c9a84c" opacity="0.5"/>
  <circle cx="700" cy="180" r="15" fill="#c9a84c" opacity="0.7"/>
  <text x="100" y="340" text-anchor="middle" fill="#c9a84c" font-family="serif" font-size="12">Ancient Silk Road</text>
  <text x="700" y="220" text-anchor="middle" fill="#4a90d9" font-family="serif" font-size="12">Digital Silk Road</text>
  <text x="400" y="450" text-anchor="middle" fill="#fff" font-family="sans-serif" font-size="14" opacity="0.8">Connecting Civilizations Across Time</text>
</svg>''',
    'frame4.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600">
  <defs><linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#1a1a2e"/><stop offset="100%" stop-color="#16213e"/></linearGradient></defs>
  <rect width="800" height="600" fill="url(#bg)"/>
  <text x="400" y="80" text-anchor="middle" fill="#c9a84c" font-family="serif" font-size="28">Historical Crossroads</text>
  <rect x="80" y="130" width="180" height="180" rx="8" fill="#16213e" stroke="#c9a84c" stroke-width="1"/>
  <text x="170" y="220" text-anchor="middle" fill="#c9a84c" font-family="serif" font-size="14">Buddhism</text>
  <text x="170" y="250" text-anchor="middle" fill="#fff" font-family="sans-serif" font-size="11" opacity="0.7">India - China</text>
  <rect x="310" y="130" width="180" height="180" rx="8" fill="#16213e" stroke="#c9a84c" stroke-width="1"/>
  <text x="400" y="220" text-anchor="middle" fill="#c9a84c" font-family="serif" font-size="14">Silk Trade</text>
  <text x="400" y="250" text-anchor="middle" fill="#fff" font-family="sans-serif" font-size="11" opacity="0.7">China - West</text>
  <rect x="540" y="130" width="180" height="180" rx="8" fill="#16213e" stroke="#c9a84c" stroke-width="1"/>
  <text x="630" y="220" text-anchor="middle" fill="#c9a84c" font-family="serif" font-size="14">Islamic-Chinese</text>
  <text x="630" y="250" text-anchor="middle" fill="#fff" font-family="sans-serif" font-size="11" opacity="0.7">Cultural Exchange</text>
  <text x="400" y="420" text-anchor="middle" fill="#fff" font-family="sans-serif" font-size="14" opacity="0.8">Civilizations developed through exchange.</text>
</svg>''',
    'frame5.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600">
  <defs><linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#1a1a2e"/><stop offset="100%" stop-color="#0f3460"/></linearGradient></defs>
  <rect width="800" height="600" fill="url(#bg)"/>
  <text x="400" y="80" text-anchor="middle" fill="#c9a84c" font-family="serif" font-size="28">Modern Archaeological Lens</text>
  <rect x="80" y="130" width="180" height="150" rx="8" fill="#16213e" stroke="#4a90d9" stroke-width="1"/>
  <circle cx="170" cy="190" r="30" fill="none" stroke="#4a90d9" stroke-width="2"/>
  <text x="170" y="250" text-anchor="middle" fill="#4a90d9" font-family="sans-serif" font-size="11">3D Scanning</text>
  <rect x="310" y="130" width="180" height="150" rx="8" fill="#16213e" stroke="#4a90d9" stroke-width="1"/>
  <circle cx="400" cy="190" r="25" fill="none" stroke="#4a90d9" stroke-width="1.5"/>
  <text x="400" y="250" text-anchor="middle" fill="#4a90d9" font-family="sans-serif" font-size="11">Drone Mapping</text>
  <rect x="540" y="130" width="180" height="150" rx="8" fill="#16213e" stroke="#4a90d9" stroke-width="1"/>
  <rect x="570" y="160" width="120" height="80" rx="4" fill="none" stroke="#4a90d9" stroke-width="1.5"/>
  <text x="630" y="250" text-anchor="middle" fill="#4a90d9" font-family="sans-serif" font-size="11">Digital Reconstruction</text>
  <text x="400" y="420" text-anchor="middle" fill="#fff" font-family="sans-serif" font-size="14" opacity="0.8">Technology helps civilizations reconnect.</text>
</svg>''',
    'frame6.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600">
  <defs><linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#1a1a2e"/><stop offset="100%" stop-color="#16213e"/></linearGradient></defs>
  <rect width="800" height="600" fill="url(#bg)"/>
  <text x="400" y="80" text-anchor="middle" fill="#c9a84c" font-family="serif" font-size="28">AI and Archaeology</text>
  <circle cx="400" cy="250" r="120" fill="none" stroke="#c9a84c" stroke-width="2" opacity="0.3"/>
  <circle cx="400" cy="250" r="80" fill="none" stroke="#4a90d9" stroke-width="1.5" opacity="0.5"/>
  <circle cx="400" cy="250" r="40" fill="#4a90d9" opacity="0.15"/>
  <text x="400" y="255" text-anchor="middle" fill="#4a90d9" font-family="serif" font-size="18">AI</text>
  <text x="400" y="420" text-anchor="middle" fill="#fff" font-family="sans-serif" font-size="14" opacity="0.8">AI helps discover hidden patterns in archaeological data.</text>
</svg>''',
    'frame7.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600">
  <defs><linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#1a1a2e"/><stop offset="100%" stop-color="#0f3460"/></linearGradient></defs>
  <rect width="800" height="600" fill="url(#bg)"/>
  <text x="400" y="80" text-anchor="middle" fill="#c9a84c" font-family="serif" font-size="28">What Does It Mean Today?</text>
  <rect x="100" y="140" width="180" height="150" rx="8" fill="#16213e" stroke="#4a90d9" stroke-width="1" opacity="0.8"/>
  <text x="190" y="200" text-anchor="middle" fill="#4a90d9" font-family="serif" font-size="14">VR Museum</text>
  <rect x="310" y="140" width="180" height="150" rx="8" fill="#16213e" stroke="#c9a84c" stroke-width="1" opacity="0.8"/>
  <text x="400" y="200" text-anchor="middle" fill="#c9a84c" font-family="serif" font-size="14">Digital Exhibition</text>
  <rect x="520" y="140" width="180" height="150" rx="8" fill="#16213e" stroke="#4a90d9" stroke-width="1" opacity="0.8"/>
  <text x="610" y="200" text-anchor="middle" fill="#4a90d9" font-family="serif" font-size="14">Online Archive</text>
  <text x="400" y="420" text-anchor="middle" fill="#fff" font-family="sans-serif" font-size="14" opacity="0.8">Digital technologies reconnect people with history.</text>
</svg>''',
    'frame8.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600">
  <defs><linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#1a1a2e"/><stop offset="100%" stop-color="#16213e"/></linearGradient>
  <linearGradient id="gold" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="#c9a84c"/><stop offset="100%" stop-color="#4a90d9"/></linearGradient></defs>
  <rect width="800" height="600" fill="url(#bg)"/>
  <text x="400" y="80" text-anchor="middle" fill="#c9a84c" font-family="serif" font-size="28">Conclusion</text>
  <line x1="100" y1="300" x2="700" y2="300" stroke="url(#gold)" stroke-width="3" opacity="0.6"/>
  <circle cx="100" cy="300" r="20" fill="#c9a84c" opacity="0.4"/>
  <text x="100" y="340" text-anchor="middle" fill="#c9a84c" font-family="serif" font-size="14">Ancient Silk Road</text>
  <circle cx="700" cy="300" r="20" fill="#4a90d9" opacity="0.4"/>
  <text x="700" y="340" text-anchor="middle" fill="#4a90d9" font-family="serif" font-size="14">Digital Network</text>
  <text x="400" y="420" text-anchor="middle" fill="#fff" font-family="sans-serif" font-size="14" opacity="0.8">The Silk Road connected civilizations in the past.</text>
  <text x="400" y="450" text-anchor="middle" fill="#c9a84c" font-family="sans-serif" font-size="14" opacity="0.8">Technology connects civilizations today.</text>
</svg>'''
}

for name, content in svgs.items():
    path = os.path.join(output_dir, name)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Created: {name}')
print('Done!')
