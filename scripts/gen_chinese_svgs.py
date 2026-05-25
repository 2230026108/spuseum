import os

output_dir = 'c:/Users/19741/WorkBuddy/20260523165257/Spuseum-main/public/images/exhibition'
os.makedirs(output_dir, exist_ok=True)

# Color palette - brighter for readability on dark bg
GOLD = "#f0d78c"       # warm gold, much brighter than #c9a84c
GOLD_DIM = "#d4a853"   # slightly dimmer gold for secondary
BLUE = "#8ec8f2"        # brighter blue than #4a90d9
WHITE = "#ffffff"
WHITE_DIM = "rgba(255,255,255,0.85)"
BODY_TEXT = "rgba(255,255,255,0.9)"
BG1 = "#0d1117"
BG2 = "#161b22"
BG3 = "#1a1a2e"
BG4 = "#16213e"
BG5 = "#0f3460"
CARD_BG = "#16213e"

svgs = {}

# ============ Frame 1: Research Coordinates ============
svgs['frame1.svg'] = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600">
  <defs><linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="{BG3}"/><stop offset="100%" stop-color="{BG4}"/></linearGradient></defs>
  <rect width="800" height="600" fill="url(#bg)"/>
  <text x="400" y="80" text-anchor="middle" fill="{GOLD}" font-family="sans-serif" font-size="28" font-weight="bold">研究方向</text>
  <line x1="200" y1="100" x2="600" y2="100" stroke="{GOLD}" stroke-width="1" opacity="0.5"/>
  <circle cx="250" cy="250" r="110" fill="none" stroke="{GOLD}" stroke-width="2.5" opacity="0.7"/>
  <circle cx="250" cy="250" r="65" fill="none" stroke="{GOLD}" stroke-width="1" opacity="0.35"/>
  <text x="250" y="258" text-anchor="middle" fill="{GOLD}" font-family="sans-serif" font-size="16" font-weight="bold">考古学</text>
  <circle cx="550" cy="250" r="110" fill="none" stroke="{BLUE}" stroke-width="2.5" opacity="0.7"/>
  <circle cx="550" cy="250" r="65" fill="none" stroke="{BLUE}" stroke-width="1" opacity="0.35"/>
  <text x="550" y="258" text-anchor="middle" fill="{BLUE}" font-family="sans-serif" font-size="16" font-weight="bold">技术文明</text>
  <line x1="360" y1="250" x2="440" y2="250" stroke="{WHITE}" stroke-width="1.5" opacity="0.5"/>
  <text x="400" y="420" text-anchor="middle" fill="{BODY_TEXT}" font-family="sans-serif" font-size="15">丝绸之路时代 — 当代全球化</text>
  <text x="400" y="455" text-anchor="middle" fill="{GOLD}" font-family="sans-serif" font-size="13">跨文明交流 | 数字丝绸之路 | 文化遗产</text>
</svg>'''

# ============ Frame 2: Why This AI Tool ============
svgs['frame2.svg'] = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600">
  <defs><linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="{BG3}"/><stop offset="100%" stop-color="{BG5}"/></linearGradient></defs>
  <rect width="800" height="600" fill="url(#bg)"/>
  <text x="400" y="80" text-anchor="middle" fill="{GOLD}" font-family="sans-serif" font-size="28" font-weight="bold">为什么选择这个AI工具？</text>
  <rect x="120" y="120" width="220" height="160" rx="8" fill="{CARD_BG}" stroke="{GOLD}" stroke-width="1.5" opacity="0.9"/>
  <text x="230" y="200" text-anchor="middle" fill="{GOLD}" font-family="sans-serif" font-size="13" font-weight="bold">AI视频</text>
  <text x="230" y="225" text-anchor="middle" fill="{GOLD}" font-family="sans-serif" font-size="13">生成</text>
  <rect x="460" y="120" width="220" height="160" rx="8" fill="{CARD_BG}" stroke="{BLUE}" stroke-width="1.5" opacity="0.9"/>
  <text x="570" y="200" text-anchor="middle" fill="{BLUE}" font-family="sans-serif" font-size="13" font-weight="bold">数字</text>
  <text x="570" y="225" text-anchor="middle" fill="{BLUE}" font-family="sans-serif" font-size="13">重建</text>
  <polygon points="380,200 400,230 420,200" fill="{GOLD}" opacity="0.4"/>
  <polygon points="400,200 420,230 440,200" fill="{GOLD}" opacity="0.4"/>
  <text x="400" y="420" text-anchor="middle" fill="{BODY_TEXT}" font-family="sans-serif" font-size="15">即梦AI视频生成 | 电影级叙事</text>
  <text x="400" y="455" text-anchor="middle" fill="{GOLD}" font-family="sans-serif" font-size="13">技术不仅在研究历史，更在激活历史</text>
</svg>'''

# ============ Frame 3: Why These Periods (TIMELINE) ============
svgs['frame3.svg'] = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600">
  <defs><linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="{BG3}"/><stop offset="100%" stop-color="{BG4}"/></linearGradient></defs>
  <rect width="800" height="600" fill="url(#bg)"/>
  <text x="400" y="80" text-anchor="middle" fill="{GOLD}" font-family="sans-serif" font-size="28" font-weight="bold">为什么选择这些历史时期？</text>
  <path d="M80,280 C180,180 280,260 400,220 C520,180 620,240 720,200" fill="none" stroke="{GOLD}" stroke-width="4" opacity="0.7"/>
  <circle cx="80" cy="280" r="18" fill="{GOLD}" opacity="0.5"/>
  <circle cx="400" cy="220" r="18" fill="{GOLD}" opacity="0.7"/>
  <circle cx="720" cy="200" r="18" fill="{GOLD}" opacity="0.85"/>
  <text x="80" y="325" text-anchor="middle" fill="{WHITE}" font-family="sans-serif" font-size="14" font-weight="bold">古丝绸之路</text>
  <text x="80" y="345" text-anchor="middle" fill="{GOLD}" font-family="sans-serif" font-size="11">驼队·商旅·文化</text>
  <text x="400" y="245" text-anchor="middle" fill="{WHITE}" font-family="sans-serif" font-size="26" font-weight="bold">→</text>
  <text x="720" y="240" text-anchor="middle" fill="{WHITE}" font-family="sans-serif" font-size="14" font-weight="bold">数字丝绸之路</text>
  <text x="720" y="260" text-anchor="middle" fill="{BLUE}" font-family="sans-serif" font-size="11">AI·互联网·全球化</text>
  <text x="400" y="455" text-anchor="middle" fill="{BODY_TEXT}" font-family="sans-serif" font-size="15">跨越时空连接文明</text>
</svg>'''

# ============ Frame 4: Historical Crossroads ============
svgs['frame4.svg'] = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600">
  <defs><linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="{BG3}"/><stop offset="100%" stop-color="{BG4}"/></linearGradient></defs>
  <rect width="800" height="600" fill="url(#bg)"/>
  <text x="400" y="80" text-anchor="middle" fill="{GOLD}" font-family="sans-serif" font-size="28" font-weight="bold">历史的十字路口</text>
  <rect x="70" y="130" width="200" height="200" rx="10" fill="{CARD_BG}" stroke="{GOLD}" stroke-width="1.5"/>
  <text x="170" y="230" text-anchor="middle" fill="{GOLD}" font-family="sans-serif" font-size="15" font-weight="bold">佛教传播</text>
  <text x="170" y="260" text-anchor="middle" fill="{BODY_TEXT}" font-family="sans-serif" font-size="12">印度 → 中国</text>
  <rect x="300" y="130" width="200" height="200" rx="10" fill="{CARD_BG}" stroke="{GOLD}" stroke-width="1.5"/>
  <text x="400" y="230" text-anchor="middle" fill="{GOLD}" font-family="sans-serif" font-size="15" font-weight="bold">丝绸贸易</text>
  <text x="400" y="260" text-anchor="middle" fill="{BODY_TEXT}" font-family="sans-serif" font-size="12">中国 → 西方</text>
  <rect x="530" y="130" width="200" height="200" rx="10" fill="{CARD_BG}" stroke="{GOLD}" stroke-width="1.5"/>
  <text x="630" y="230" text-anchor="middle" fill="{GOLD}" font-family="sans-serif" font-size="15" font-weight="bold">伊斯兰-中华</text>
  <text x="630" y="260" text-anchor="middle" fill="{BODY_TEXT}" font-family="sans-serif" font-size="12">文化交流</text>
  <text x="400" y="430" text-anchor="middle" fill="{BODY_TEXT}" font-family="sans-serif" font-size="15">文明在交流中发展</text>
</svg>'''

# ============ Frame 5: Modern Archaeological Lens ============
svgs['frame5.svg'] = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600">
  <defs><linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="{BG3}"/><stop offset="100%" stop-color="{BG5}"/></linearGradient></defs>
  <rect width="800" height="600" fill="url(#bg)"/>
  <text x="400" y="80" text-anchor="middle" fill="{GOLD}" font-family="sans-serif" font-size="28" font-weight="bold">现代考古视角</text>
  <rect x="70" y="130" width="200" height="160" rx="10" fill="{CARD_BG}" stroke="{BLUE}" stroke-width="1.5"/>
  <circle cx="170" cy="195" r="35" fill="none" stroke="{BLUE}" stroke-width="2.5"/>
  <circle cx="170" cy="195" r="10" fill="{BLUE}" opacity="0.3"/>
  <text x="170" y="265" text-anchor="middle" fill="{BLUE}" font-family="sans-serif" font-size="13" font-weight="bold">3D扫描</text>
  <rect x="300" y="130" width="200" height="160" rx="10" fill="{CARD_BG}" stroke="{BLUE}" stroke-width="1.5"/>
  <circle cx="400" cy="195" r="30" fill="none" stroke="{BLUE}" stroke-width="2"/>
  <path d="M380,175 L400,155 L420,175" fill="none" stroke="{BLUE}" stroke-width="1.5"/>
  <line x1="400" y1="175" x2="400" y2="220" stroke="{BLUE}" stroke-width="1"/>
  <text x="400" y="265" text-anchor="middle" fill="{BLUE}" font-family="sans-serif" font-size="13" font-weight="bold">无人机测绘</text>
  <rect x="530" y="130" width="200" height="160" rx="10" fill="{CARD_BG}" stroke="{BLUE}" stroke-width="1.5"/>
  <rect x="560" y="160" width="140" height="90" rx="6" fill="none" stroke="{BLUE}" stroke-width="2"/>
  <rect x="570" y="170" width="50" height="35" rx="3" fill="{BLUE}" opacity="0.25"/>
  <rect x="630" y="170" width="50" height="35" rx="3" fill="{BLUE}" opacity="0.15"/>
  <text x="630" y="265" text-anchor="middle" fill="{BLUE}" font-family="sans-serif" font-size="13" font-weight="bold">数字重建</text>
  <text x="400" y="430" text-anchor="middle" fill="{BODY_TEXT}" font-family="sans-serif" font-size="15">技术帮助文明重新连接</text>
</svg>'''

# ============ Frame 6: AI and Archaeology ============
svgs['frame6.svg'] = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600">
  <defs><linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="{BG3}"/><stop offset="100%" stop-color="{BG4}"/></linearGradient></defs>
  <rect width="800" height="600" fill="url(#bg)"/>
  <text x="400" y="80" text-anchor="middle" fill="{GOLD}" font-family="sans-serif" font-size="28" font-weight="bold">AI与考古学</text>
  <circle cx="400" cy="260" r="140" fill="none" stroke="{GOLD}" stroke-width="2.5" opacity="0.35"/>
  <circle cx="400" cy="260" r="95" fill="none" stroke="{BLUE}" stroke-width="2" opacity="0.55"/>
  <circle cx="400" cy="260" r="50" fill="{BLUE}" opacity="0.18"/>
  <text x="400" y="270" text-anchor="middle" fill="{BLUE}" font-family="sans-serif" font-size="22" font-weight="bold">AI</text>
  <line x1="260" y1="260" x2="285" y2="260" stroke="{GOLD}" stroke-width="1.5" opacity="0.5"/>
  <line x1="515" y1="260" x2="540" y2="260" stroke="{GOLD}" stroke-width="1.5" opacity="0.5"/>
  <text x="400" y="430" text-anchor="middle" fill="{BODY_TEXT}" font-family="sans-serif" font-size="15">AI帮助考古学家发现隐藏的模式</text>
</svg>'''

# ============ Frame 7: What Does It Mean Today ============
svgs['frame7.svg'] = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600">
  <defs><linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="{BG3}"/><stop offset="100%" stop-color="{BG5}"/></linearGradient></defs>
  <rect width="800" height="600" fill="url(#bg)"/>
  <text x="400" y="80" text-anchor="middle" fill="{GOLD}" font-family="sans-serif" font-size="28" font-weight="bold">今天这意味着什么？</text>
  <rect x="70" y="140" width="200" height="160" rx="10" fill="{CARD_BG}" stroke="{BLUE}" stroke-width="1.5" opacity="0.9"/>
  <text x="170" y="230" text-anchor="middle" fill="{BLUE}" font-family="sans-serif" font-size="15" font-weight="bold">VR博物馆</text>
  <rect x="300" y="140" width="200" height="160" rx="10" fill="{CARD_BG}" stroke="{GOLD}" stroke-width="1.5" opacity="0.9"/>
  <text x="400" y="225" text-anchor="middle" fill="{GOLD}" font-family="sans-serif" font-size="15" font-weight="bold">数字展览</text>
  <rect x="530" y="140" width="200" height="160" rx="10" fill="{CARD_BG}" stroke="{BLUE}" stroke-width="1.5" opacity="0.9"/>
  <text x="630" y="230" text-anchor="middle" fill="{BLUE}" font-family="sans-serif" font-size="15" font-weight="bold">在线档案</text>
  <text x="400" y="430" text-anchor="middle" fill="{BODY_TEXT}" font-family="sans-serif" font-size="15">数字技术让人们重新与历史建立联系</text>
</svg>'''

# ============ Frame 8: Conclusion ============
svgs['frame8.svg'] = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600">
  <defs><linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="{BG3}"/><stop offset="100%" stop-color="{BG4}"/></linearGradient>
  <linearGradient id="bridge" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="{GOLD}"/><stop offset="100%" stop-color="{BLUE}"/></linearGradient></defs>
  <rect width="800" height="600" fill="url(#bg)"/>
  <text x="400" y="80" text-anchor="middle" fill="{GOLD}" font-family="sans-serif" font-size="28" font-weight="bold">结论</text>
  <line x1="80" y1="300" x2="720" y2="300" stroke="url(#bridge)" stroke-width="4" opacity="0.65"/>
  <circle cx="80" cy="300" r="22" fill="{GOLD}" opacity="0.55"/>
  <text x="80" y="350" text-anchor="middle" fill="{WHITE}" font-family="sans-serif" font-size="15" font-weight="bold">古丝绸之路</text>
  <text x="80" y="370" text-anchor="middle" fill="{GOLD}" font-family="sans-serif" font-size="11">过去的连接</text>
  <circle cx="720" cy="300" r="22" fill="{BLUE}" opacity="0.55"/>
  <text x="720" y="350" text-anchor="middle" fill="{WHITE}" font-family="sans-serif" font-size="15" font-weight="bold">数字网络</text>
  <text x="720" y="370" text-anchor="middle" fill="{BLUE}" font-family="sans-serif" font-size="11">今天的连接</text>
  <text x="400" y="265" text-anchor="middle" fill="{WHITE}" font-family="sans-serif" font-size="28" font-weight="bold">→</text>
  <text x="400" y="440" text-anchor="middle" fill="{BODY_TEXT}" font-family="sans-serif" font-size="15">丝绸之路在过去连接了文明</text>
  <text x="400" y="475" text-anchor="middle" fill="{GOLD}" font-family="sans-serif" font-size="15" font-weight="bold">技术在今天连接着文明</text>
</svg>'''

# ============ Silk Road Map ============
svgs['silkroad.svg'] = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 520">
  <defs>
    <linearGradient id="bgGrad" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="{BG1}"/>
      <stop offset="100%" stop-color="{BG2}"/>
    </linearGradient>
    <linearGradient id="routeGrad" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="{GOLD}"/>
      <stop offset="50%" stop-color="#f5da81"/>
      <stop offset="100%" stop-color="{GOLD}"/>
    </linearGradient>
    <filter id="glow">
      <feGaussianBlur stdDeviation="3.5" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>
  <rect width="1000" height="520" fill="url(#bgGrad)"/>

  <!-- Grid lines -->
  <g opacity="0.04" stroke="#fff" stroke-width="0.5">
    <line x1="0" y1="104" x2="1000" y2="104"/><line x1="0" y1="208" x2="1000" y2="208"/>
    <line x1="0" y1="312" x2="1000" y2="312"/><line x1="0" y1="416" x2="1000" y2="416"/>
    <line x1="200" y1="0" x2="200" y2="520"/><line x1="400" y1="0" x2="400" y2="520"/>
    <line x1="600" y1="0" x2="600" y2="520"/><line x1="800" y1="0" x2="800" y2="520"/>
  </g>

  <!-- Silk Road Main Route -->
  <path d="M120,190 C200,170 250,150 320,180 C400,220 420,240 480,200 C540,160 600,190 680,170 C730,160 780,180 850,200"
    fill="none" stroke="url(#routeGrad)" stroke-width="5" opacity="0.85" filter="url(#glow)"/>

  <!-- Northern Route -->
  <path d="M120,190 C180,130 250,110 320,140 C380,165 440,190 480,200"
    fill="none" stroke="{GOLD}" stroke-width="2.5" stroke-dasharray="10,5" opacity="0.45"/>

  <!-- Southern Route -->
  <path d="M320,180 C400,230 440,260 500,250 C560,240 620,220 680,230 C720,240 770,220 850,200"
    fill="none" stroke="{GOLD}" stroke-width="2.5" stroke-dasharray="10,5" opacity="0.45"/>

  <!-- Maritime Route -->
  <path d="M680,170 C700,210 720,290 680,310 C640,330 600,310 580,290 C560,270 570,240 550,220"
    fill="none" stroke="{BLUE}" stroke-width="2.5" stroke-dasharray="7,7" opacity="0.55"/>

  <!-- City Markers - China / Chang'an -->
  <circle cx="120" cy="190" r="13" fill="{GOLD}" opacity="0.9"/>
  <circle cx="120" cy="190" r="20" fill="{GOLD}" opacity="0.25"/>
  <text x="120" y="215" text-anchor="middle" fill="{WHITE}" font-family="sans-serif" font-size="14" font-weight="bold">中国</text>
  <text x="120" y="235" text-anchor="middle" fill="{GOLD}" font-family="sans-serif" font-size="11">长安</text>

  <!-- Dunhuang -->
  <circle cx="205" cy="163" r="8" fill="{GOLD}" opacity="0.8"/>
  <text x="205" y="185" text-anchor="middle" fill="{WHITE}" font-family="sans-serif" font-size="10">敦煌</text>

  <!-- Central Asia / Samarkand -->
  <circle cx="320" cy="180" r="11" fill="{GOLD}" opacity="0.9"/>
  <circle cx="320" cy="180" r="17" fill="{GOLD}" opacity="0.2"/>
  <text x="320" y="200" text-anchor="middle" fill="{WHITE}" font-family="sans-serif" font-size="14" font-weight="bold">中亚</text>
  <text x="320" y="220" text-anchor="middle" fill="{GOLD}" font-family="sans-serif" font-size="11">撒马尔罕</text>

  <!-- Persia -->
  <circle cx="480" cy="200" r="11" fill="{GOLD}" opacity="0.9"/>
  <circle cx="480" cy="200" r="17" fill="{GOLD}" opacity="0.2"/>
  <text x="480" y="222" text-anchor="middle" fill="{WHITE}" font-family="sans-serif" font-size="14" font-weight="bold">波斯</text>

  <!-- Baghdad -->
  <circle cx="590" cy="195" r="8" fill="{GOLD}" opacity="0.8"/>
  <text x="590" y="215" text-anchor="middle" fill="{WHITE}" font-family="sans-serif" font-size="10">巴格达</text>

  <!-- Constantinople -->
  <circle cx="730" cy="175" r="9" fill="{GOLD}" opacity="0.8"/>
  <text x="730" y="198" text-anchor="middle" fill="{WHITE}" font-family="sans-serif" font-size="10">君士坦丁堡</text>

  <!-- Europe / Rome -->
  <circle cx="850" cy="200" r="13" fill="{GOLD}" opacity="0.9"/>
  <circle cx="850" cy="200" r="20" fill="{GOLD}" opacity="0.25"/>
  <text x="850" y="222" text-anchor="middle" fill="{WHITE}" font-family="sans-serif" font-size="14" font-weight="bold">欧洲</text>
  <text x="850" y="242" text-anchor="middle" fill="{GOLD}" font-family="sans-serif" font-size="11">罗马</text>

  <!-- India -->
  <circle cx="550" cy="280" r="10" fill="{BLUE}" opacity="0.8"/>
  <text x="560" y="300" text-anchor="middle" fill="{WHITE}" font-family="sans-serif" font-size="13" font-weight="bold">印度</text>
  <line x1="500" y1="210" x2="550" y2="275" stroke="{BLUE}" stroke-width="1.5" stroke-dasharray="5,5" opacity="0.35"/>

  <!-- Trade Goods -->
  <text x="240" y="310" fill="{GOLD}" font-family="sans-serif" font-size="10" opacity="0.7">丝绸 · 香料 · 瓷器 · 典籍</text>
  <text x="560" y="325" fill="{BLUE}" font-family="sans-serif" font-size="10" opacity="0.7">宝石 · 象牙 · 纺织品</text>

  <!-- Legend -->
  <g transform="translate(15, 455)">
    <rect x="0" y="0" width="200" height="50" rx="5" fill="{BG1}" stroke="{GOLD}" stroke-width="1" opacity="0.6"/>
    <text x="10" y="14" fill="{GOLD}" font-family="sans-serif" font-size="12" font-weight="bold">丝绸之路</text>
    <line x1="10" y1="26" x2="45" y2="26" stroke="{GOLD}" stroke-width="2.5"/>
    <text x="52" y="28" fill="{WHITE}" font-family="sans-serif" font-size="9">陆上路线</text>
    <line x1="10" y1="36" x2="45" y2="36" stroke="{BLUE}" stroke-width="2.5" stroke-dasharray="6,6"/>
    <text x="52" y="38" fill="{WHITE}" font-family="sans-serif" font-size="9">海上路线</text>
  </g>

  <!-- Title -->
  <text x="500" y="45" text-anchor="middle" fill="{GOLD}" font-family="sans-serif" font-size="28" font-weight="bold">丝绸之路</text>
  <text x="500" y="72" text-anchor="middle" fill="{BODY_TEXT}" font-family="sans-serif" font-size="12">连接文明的古代贸易路线</text>
</svg>'''


# Write all SVGs
for name, content in svgs.items():
    path = os.path.join(output_dir, name)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content.strip() + '\n')
    print(f'Written: {name}')

print('\nAll 9 SVGs regenerated successfully!')
