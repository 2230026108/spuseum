"""Generate 6 Silk Road themed artwork SVGs for museum walls."""
import math

def svg_header(w, h):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">'

def svg_footer():
    return '</svg>'

# SVG 1: Desert Camel Caravan
art1 = f"""{svg_header(1024, 768)}
  <defs>
    <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#1a0a2e"/>
      <stop offset="40%" stop-color="#d4451a"/>
      <stop offset="70%" stop-color="#f0a040"/>
      <stop offset="100%" stop-color="#f5d060"/>
    </linearGradient>
    <linearGradient id="sand" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#d4a050"/>
      <stop offset="100%" stop-color="#8b5e3c"/>
    </linearGradient>
    <radialGradient id="sun" cx="0.5" cy="0.5" r="0.5">
      <stop offset="0%" stop-color="#fff8e0"/>
      <stop offset="30%" stop-color="#ffe080"/>
      <stop offset="70%" stop-color="#ff88003a"/>
      <stop offset="100%" stop-color="#ff880000"/>
    </radialGradient>
  </defs>
  <rect width="1024" height="768" fill="url(#sky)"/>
  <circle cx="512" cy="380" r="200" fill="url(#sun)" opacity="0.8"/>
  <ellipse cx="512" cy="280" r="80" ry="70" fill="#fff4d0" opacity="0.9"/>
  <path d="M0 500 Q200 460 350 490 Q500 440 650 480 Q800 450 1024 490 L1024 768 L0 768Z" fill="#c89848"/>
  <path d="M0 540 Q180 510 380 535 Q580 490 750 530 Q900 500 1024 520 L1024 768 L0 768Z" fill="url(#sand)"/>
  <path d="M0 600 Q250 570 500 590 Q750 560 1024 580 L1024 768 L0 768Z" fill="#7a4f30"/>
  
  <g transform="translate(180,420)">
    <g id="camel1">
      <ellipse cx="0" cy="0" rx="35" ry="20" fill="#8B6914"/>
      <ellipse cx="-20" cy="-15" rx="10" ry="15" fill="#8B6914"/>
      <ellipse cx="-25" cy="-30" rx="6" ry="10" fill="#8B6914"/>
      <rect x="-4" y="-45" width="3" height="15" fill="#6B4914"/>
      <rect x="-4" y="-45" width="14" height="3" fill="#6B4914"/>
      <ellipse cx="5" cy="-10" rx="5" ry="12" fill="#7a5a10"/>
      <ellipse cx="12" cy="-5" rx="5" ry="12" fill="#7a5a10"/>
      <ellipse cx="19" cy="0" rx="5" ry="12" fill="#7a5a10"/>
      <ellipse cx="26" cy="5" rx="5" ry="12" fill="#7a5a10"/>
      <rect x="-30" y="-20" width="15" height="25" rx="3" fill="#d4a050cc" stroke="#8B6914" stroke-width="1"/>
    </g>
  </g>
  
  <g transform="translate(320,400)">
    <g id="camel2">
      <ellipse cx="0" cy="0" rx="38" ry="22" fill="#9B7924"/>
      <ellipse cx="-22" cy="-18" rx="12" ry="17" fill="#9B7924"/>
      <ellipse cx="-28" cy="-35" rx="7" ry="12" fill="#9B7924"/>
      <rect x="-6" y="-52" width="3" height="17" fill="#5B3904"/>
      <rect x="-6" y="-52" width="16" height="3" fill="#5B3904"/>
      <ellipse cx="6" cy="-12" rx="6" ry="13" fill="#8a6a20"/>
      <ellipse cx="14" cy="-6" rx="6" ry="13" fill="#8a6a20"/>
      <ellipse cx="22" cy="0" rx="6" ry="13" fill="#8a6a20"/>
      <ellipse cx="30" cy="6" rx="6" ry="13" fill="#8a6a20"/>
      <rect x="-32" y="-22" width="16" height="28" rx="3" fill="#e0b060cc" stroke="#9B7924" stroke-width="1"/>
    </g>
  </g>
  
  <g transform="translate(460,430)">
    <g id="camel3" transform="scale(0.85)">
      <ellipse cx="0" cy="0" rx="35" ry="20" fill="#6B5914"/>
      <ellipse cx="-20" cy="-15" rx="10" ry="15" fill="#6B5914"/>
      <ellipse cx="-25" cy="-30" rx="6" ry="10" fill="#6B5914"/>
      <rect x="-4" y="-45" width="3" height="15" fill="#3B2904"/>
      <rect x="-4" y="-45" width="14" height="3" fill="#3B2904"/>
      <ellipse cx="5" cy="-10" rx="5" ry="12" fill="#5a4910"/>
      <ellipse cx="12" cy="-5" rx="5" ry="12" fill="#5a4910"/>
      <ellipse cx="19" cy="0" rx="5" ry="12" fill="#5a4910"/>
      <ellipse cx="26" cy="5" rx="5" ry="12" fill="#5a4910"/>
    </g>
  </g>
  
  <text x="512" y="740" text-anchor="middle" fill="#fff8e0cc" font-family="serif" font-size="28">沙漠驼队 · 黄昏行旅</text>
{svg_footer()}"""

# SVG 2: Ancient Trading Post / Bazaar
art2 = f"""{svg_header(1024, 768)}
  <defs>
    <linearGradient id="sky2" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#87CEEB"/>
      <stop offset="60%" stop-color="#d4e8f0"/>
      <stop offset="100%" stop-color="#f5ecd0"/>
    </linearGradient>
    <linearGradient id="roof" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#8B4513"/>
      <stop offset="100%" stop-color="#5C2D0A"/>
    </linearGradient>
  </defs>
  <rect width="1024" height="768" fill="url(#sky2)"/>
  
  <rect x="0" y="450" width="1024" height="318" fill="#d4b070"/>
  <rect x="0" y="500" width="1024" height="268" fill="#c09860"/>
  
  <rect x="100" y="300" width="200" height="200" fill="#e8d5b0" stroke="#8B6914" stroke-width="2"/>
  <polygon points="80,300 200,220 320,300" fill="url(#roof)" stroke="#4a2500" stroke-width="2"/>
  <rect x="150" y="340" width="100" height="60" fill="#4a2500" opacity="0.7"/>
  <text x="200" y="370" text-anchor="middle" fill="#f5d090" font-size="14">丝绸锦缎</text>
  
  <rect x="400" y="280" width="240" height="220" fill="#eadcc0" stroke="#8B6914" stroke-width="2"/>
  <polygon points="380,280 520,190 660,280" fill="url(#roof)" stroke="#4a2500" stroke-width="2"/>
  <rect x="440" y="330" width="160" height="60" fill="#4a2500" opacity="0.7"/>
  <text x="520" y="365" text-anchor="middle" fill="#f5d090" font-size="14">陶瓷 · 香料 · 珠宝</text>
  
  <rect x="730" y="310" width="180" height="190" fill="#e5d0a0" stroke="#8B6914" stroke-width="2"/>
  <polygon points="710,310 820,240 930,310" fill="url(#roof)" stroke="#4a2500" stroke-width="2"/>
  
  <g transform="translate(120,400)">
    <circle cx="0" cy="0" r="12" fill="#d4a050"/>
    <circle cx="30" cy="-10" r="12" fill="#e0b060"/>
    <circle cx="55" cy="5" r="12" fill="#c89848"/>
    <circle cx="80" cy="-5" r="12" fill="#e8c070"/>
  </g>
  <g transform="translate(500,420)">
    <circle cx="0" cy="0" r="10" fill="#d4a050"/>
    <circle cx="25" cy="5" r="10" fill="#e0b060"/>
    <circle cx="50" cy="-8" r="10" fill="#c89848"/>
  </g>
  <g transform="translate(760,430)">
    <circle cx="0" cy="0" r="10" fill="#e0b060"/>
    <circle cx="28" cy="-5" r="10" fill="#d4a050"/>
  </g>
  
  <text x="512" y="740" text-anchor="middle" fill="#4a2500cc" font-family="serif" font-size="28">丝路集市 · 商贾云集</text>
{svg_footer()}"""

# SVG 3: Dunhuang Cave Paintings Style
art3 = f"""{svg_header(1024, 768)}
  <defs>
    <radialGradient id="glow" cx="0.5" cy="0.4" r="0.6">
      <stop offset="0%" stop-color="#2a1a0a"/>
      <stop offset="100%" stop-color="#0a0a15"/>
    </radialGradient>
    <linearGradient id="aura" x1="0.5" y1="0" x2="0.5" y2="1">
      <stop offset="0%" stop-color="#f5d090" stop-opacity="0.6"/>
      <stop offset="100%" stop-color="#f5d090" stop-opacity="0"/>
    </linearGradient>
  </defs>
  <rect width="1024" height="768" fill="url(#glow)"/>
  
  <ellipse cx="380" cy="350" rx="120" ry="160" fill="url(#aura)"/>
  <ellipse cx="640" cy="350" rx="120" ry="160" fill="url(#aura)"/>
  
  <g transform="translate(380,320)">
    <ellipse cx="0" cy="0" rx="40" ry="50" fill="#d4a05088"/>
    <ellipse cx="0" cy="-15" rx="18" ry="22" fill="#f5e0c0"/>
    <path d="M-30,-5 Q-50,-30 -35,-45" stroke="#f5d09088" stroke-width="2" fill="none"/>
    <path d="M30,-5 Q50,-30 35,-45" stroke="#f5d09088" stroke-width="2" fill="none"/>
    <path d="M-20,20 Q-40,50 -25,65" stroke="#f0c87088" stroke-width="2" fill="none"/>
    <path d="M20,20 Q40,50 25,65" stroke="#f0c87088" stroke-width="2" fill="none"/>
    <ellipse cx="0" cy="0" rx="15" ry="20" fill="#ffe8c0" opacity="0.5"/>
    <ellipse cx="0" cy="-40" rx="8" ry="6" fill="#fff0d0cc"/>
  </g>
  
  <g transform="translate(640,340)">
    <ellipse cx="0" cy="0" rx="38" ry="48" fill="#c8984088"/>
    <ellipse cx="0" cy="-12" rx="16" ry="20" fill="#f0d8b0"/>
    <path d="M-28,-3 Q-45,-28 -32,-40" stroke="#f0c87088" stroke-width="2" fill="none"/>
    <path d="M28,-3 Q45,-28 32,-40" stroke="#f0c87088" stroke-width="2" fill="none"/>
    <ellipse cx="0" cy="0" rx="14" ry="18" fill="#ffe0b0" opacity="0.5"/>
    <ellipse cx="0" cy="-35" rx="7" ry="5" fill="#fff0d0cc"/>
  </g>
  
  <text x="200" y="180" fill="#f5d09088" font-family="serif" font-size="18" transform="rotate(-15,200,180)">༄ 飞天伎乐</text>
  <text x="750" y="200" fill="#f5d09088" font-family="serif" font-size="18" transform="rotate(12,750,200)">梵音缭绕 ༄</text>
  
  <path d="M300,550 Q350,530 400,545 Q450,525 500,540 Q550,520 600,535 Q650,525 700,545" stroke="#d4a05044" stroke-width="1" fill="none"/>
  <path d="M320,570 Q380,555 440,565 Q500,550 560,562 Q620,548 680,560" stroke="#c8984844" stroke-width="1" fill="none"/>
  
  <rect x="250" y="560" width="524" height="40" rx="5" fill="#1a0a0544"/>
  <text x="512" y="588" text-anchor="middle" fill="#f5d090cc" font-family="serif" font-size="24">敦煌莫高 · 丝路佛光</text>
  
  <text x="512" y="740" text-anchor="middle" fill="#d4a050aa" font-family="serif" font-size="22">公元4-14世纪 世界文化遗产</text>
{svg_footer()}"""

# SVG 4: Silk Road Map with Trade Routes
art4 = f"""{svg_header(1024, 768)}
  <defs>
    <linearGradient id="bg4" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#1a1a2e"/>
      <stop offset="100%" stop-color="#16213e"/>
    </linearGradient>
    <filter id="glow4">
      <feGaussianBlur stdDeviation="3" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>
  <rect width="1024" height="768" fill="url(#bg4)"/>
  
  <rect x="40" y="120" width="180" height="30" rx="5" fill="#0a1a2a66" stroke="#f0c87044" stroke-width="1"/>
  <text x="130" y="140" text-anchor="middle" fill="#f0d090" font-size="14" font-family="serif">长安（西安）</text>
  
  <rect x="250" y="250" width="150" height="30" rx="5" fill="#0a1a2a66" stroke="#f0c87044" stroke-width="1"/>
  <text x="325" y="270" text-anchor="middle" fill="#f0d090" font-size="14" font-family="serif">敦煌</text>
  
  <rect x="400" y="180" width="150" height="30" rx="5" fill="#0a1a2a66" stroke="#f0c87044" stroke-width="1"/>
  <text x="475" y="200" text-anchor="middle" fill="#f0d090" font-size="14" font-family="serif">喀什</text>
  
  <rect x="550" y="300" width="140" height="30" rx="5" fill="#0a1a2a66" stroke="#f0c87044" stroke-width="1"/>
  <text x="620" y="320" text-anchor="middle" fill="#f0d090" font-size="14" font-family="serif">撒马尔罕</text>
  
  <rect x="700" y="380" width="140" height="30" rx="5" fill="#0a1a2a66" stroke="#f0c87044" stroke-width="1"/>
  <text x="770" y="400" text-anchor="middle" fill="#f0d090" font-size="14" font-family="serif">巴格达</text>
  
  <rect x="800" y="500" width="140" height="30" rx="5" fill="#0a1a2a66" stroke="#f0c87044" stroke-width="1"/>
  <text x="870" y="520" text-anchor="middle" fill="#f0d090" font-size="14" font-family="serif">君士坦丁堡</text>
  
  <path d="M220,135 Q260,180 300,255" stroke="#f0c87088" stroke-width="3" fill="none" stroke-dasharray="8,5" filter="url(#glow4)"/>
  <path d="M300,265 Q340,230 400,195" stroke="#f0c87088" stroke-width="3" fill="none" stroke-dasharray="8,5" filter="url(#glow4)"/>
  <path d="M475,195 Q510,240 560,295" stroke="#f0c87088" stroke-width="3" fill="none" stroke-dasharray="8,5" filter="url(#glow4)"/>
  <path d="M620,305 Q660,340 710,375" stroke="#f0c87088" stroke-width="3" fill="none" stroke-dasharray="8,5" filter="url(#glow4)"/>
  <path d="M770,390 Q790,430 810,495" stroke="#f0c87088" stroke-width="3" fill="none" stroke-dasharray="8,5" filter="url(#glow4)"/>
  
  <path d="M300,265 Q440,380 560,295" stroke="#f0c87044" stroke-width="2" fill="none" stroke-dasharray="4,8"/>
  <path d="M560,310 Q640,420 710,375" stroke="#f0c87044" stroke-width="2" fill="none" stroke-dasharray="4,8"/>
  
  <text x="512" y="650" text-anchor="middle" fill="#f0d090cc" font-family="serif" font-size="26">丝绸之路 · 陆上贸易路线</text>
  <text x="512" y="690" text-anchor="middle" fill="#f0c87077" font-family="serif" font-size="16">CHINA — CENTRAL ASIA — MIDDLE EAST — EUROPE</text>
  <text x="512" y="740" text-anchor="middle" fill="#c0a060aa" font-family="serif" font-size="20">公元前2世纪 - 公元16世纪</text>
{svg_footer()}"""

# SVG 5: Porcelain & Silk Art
art5 = f"""{svg_header(1024, 768)}
  <defs>
    <linearGradient id="bg5" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#f5efe0"/>
      <stop offset="100%" stop-color="#d4c8b0"/>
    </linearGradient>
    <radialGradient id="porcelain" cx="0.5" cy="0.5" r="0.5">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="70%" stop-color="#e8f0f8"/>
      <stop offset="100%" stop-color="#c0d0e0"/>
    </radialGradient>
    <linearGradient id="silk" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#d4a050"/>
      <stop offset="50%" stop-color="#c89840"/>
      <stop offset="100%" stop-color="#a07030"/>
    </linearGradient>
  </defs>
  <rect width="1024" height="768" fill="url(#bg5)"/>
  
  <ellipse cx="300" cy="350" rx="150" ry="180" fill="url(#porcelain)" stroke="#8090a0" stroke-width="2"/>
  <ellipse cx="300" cy="300" rx="80" ry="50" fill="none" stroke="#4050a0" stroke-width="2" opacity="0.6"/>
  <path d="M240,330 Q260,310 280,330" stroke="#4050a0" stroke-width="1.5" fill="none" opacity="0.5"/>
  <path d="M300,330 Q320,310 340,330" stroke="#4050a0" stroke-width="1.5" fill="none" opacity="0.5"/>
  <circle cx="300" cy="370" r="8" fill="#4050a0" opacity="0.4"/>
  
  <ellipse cx="650" cy="280" rx="140" ry="160" fill="url(#porcelain)" stroke="#8090a0" stroke-width="2"/>
  <path d="M570,240 Q590,220 610,240" stroke="#b03030" stroke-width="2" fill="none" opacity="0.5"/>
  <path d="M650,240 Q670,220 690,240" stroke="#b03030" stroke-width="2" fill="none" opacity="0.5"/>
  <circle cx="600" cy="300" r="6" fill="#b03030" opacity="0.5"/>
  <circle cx="700" cy="300" r="6" fill="#b03030" opacity="0.5"/>
  
  <path d="M450,560 Q500,540 550,560 L570,680 Q520,700 470,680Z" fill="url(#silk)" opacity="0.6"/>
  <path d="M460,570 Q510,550 560,570" stroke="#c89840" stroke-width="3" fill="none"/>
  <path d="M470,590 Q520,570 550,590" stroke="#c89840" stroke-width="3" fill="none"/>
  
  <text x="512" y="500" text-anchor="middle" fill="#4a3a2a" font-family="serif" font-size="22">中国瓷器 · 丝绸之宝</text>
  <text x="512" y="730" text-anchor="middle" fill="#6a5a4a" font-family="serif" font-size="24">陶瓷与丝绸：跨越千年的东方瑰宝</text>
{svg_footer()}"""

# SVG 6: Modern Digital Silk Road
art6 = f"""{svg_header(1024, 768)}
  <defs>
    <linearGradient id="bg6" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#0a0a2e"/>
      <stop offset="50%" stop-color="#1a0a3e"/>
      <stop offset="100%" stop-color="#0a1a2e"/>
    </linearGradient>
    <filter id="glow6">
      <feGaussianBlur stdDeviation="4"/>
      <feMerge><feMergeNode/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <filter id="glowStrong">
      <feGaussianBlur stdDeviation="6"/>
      <feMerge><feMergeNode/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>
  <rect width="1024" height="768" fill="url(#bg6)"/>
  
  <circle cx="512" cy="384" r="200" fill="none" stroke="#2030a044" stroke-width="1"/>
  <circle cx="512" cy="384" r="280" fill="none" stroke="#2030a033" stroke-width="1"/>
  <circle cx="200" cy="250" r="40" fill="#3040c022" stroke="#4060d044" stroke-width="1"/>
  <circle cx="200" cy="250" r="8" fill="#6080ffcc" filter="url(#glowStrong)"/>
  
  <circle cx="750" cy="180" r="40" fill="#3040c022" stroke="#4060d044" stroke-width="1"/>
  <circle cx="750" cy="180" r="8" fill="#6080ffcc" filter="url(#glowStrong)"/>
  
  <circle cx="350" cy="500" r="40" fill="#3040c022" stroke="#4060d044" stroke-width="1"/>
  <circle cx="350" cy="500" r="8" fill="#6080ffcc" filter="url(#glowStrong)"/>
  
  <circle cx="700" cy="550" r="40" fill="#3040c022" stroke="#4060d044" stroke-width="1"/>
  <circle cx="700" cy="550" r="8" fill="#6080ffcc" filter="url(#glowStrong)"/>
  
  <circle cx="500" cy="150" r="40" fill="#3040c022" stroke="#4060d044" stroke-width="1"/>
  <circle cx="500" cy="150" r="8" fill="#6080ffcc" filter="url(#glowStrong)"/>
  
  <circle cx="850" cy="400" r="40" fill="#3040c022" stroke="#4060d044" stroke-width="1"/>
  <circle cx="850" cy="400" r="8" fill="#6080ffcc" filter="url(#glowStrong)"/>
  
  <path d="M200,250 Q350,200 500,150" stroke="#4060d066" stroke-width="2" fill="none" filter="url(#glow6)"/>
  <path d="M500,150 Q620,160 750,180" stroke="#4060d066" stroke-width="2" fill="none" filter="url(#glow6)"/>
  <path d="M350,500 Q400,420 500,150" stroke="#4060d066" stroke-width="2" fill="none" filter="url(#glow6)"/>
  <path d="M200,250 Q270,380 350,500" stroke="#4060d066" stroke-width="2" fill="none" filter="url(#glow6)"/>
  <path d="M700,550 Q780,480 850,400" stroke="#4060d066" stroke-width="2" fill="none" filter="url(#glow6)"/>
  <path d="M750,180 Q800,300 850,400" stroke="#4060d066" stroke-width="2" fill="none" filter="url(#glow6)"/>
  <path d="M350,500 Q520,530 700,550" stroke="#4060d066" stroke-width="2" fill="none" filter="url(#glow6)"/>
  
  <text x="512" y="650" text-anchor="middle" fill="#6080ffcc" font-family="serif" font-size="26">数字丝绸之路</text>
  <text x="512" y="700" text-anchor="middle" fill="#4060d0aa" font-family="serif" font-size="18">AI · 5G · 区块链 · 数字贸易</text>
  
  <rect x="300" y="715" width="424" height="3" rx="1" fill="#4060d044"/>
  <text x="512" y="745" text-anchor="middle" fill="#4060d088" font-family="serif" font-size="16">从驼铃古道到数字网络 · 文明连接从未止步</text>
{svg_footer()}"""

artworks = [
  ("artwork_01_silkroad_caravan.svg", art1, "沙漠驼队"),
  ("artwork_02_trading_post.svg", art2, "丝路集市"),
  ("artwork_03_dunhuang.svg", art3, "敦煌佛光"),
  ("artwork_04_silkroad_map.svg", art4, "丝绸之路地图"),
  ("artwork_05_porcelain_silk.svg", art5, "瓷器丝绸"),
  ("artwork_06_digital_silkroad.svg", art6, "数字丝路"),
]

for filename, content, desc in artworks:
    with open(f"public/images/artwork/{filename}", "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Generated: {filename} ({desc})")

print(f"\nAll 6 artworks generated in public/images/artwork/")
