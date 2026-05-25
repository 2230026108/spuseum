"""Generate Silk Road artwork SVGs #01-#20 for museum walls."""
import os
OUTPUT_DIR = "public/images/artwork"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def h(w=1024,h=768): return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">'
def f(): return '</svg>'
def lbl(x,y,t,s="",c="#f0d78c"):
    pw=len(t)*9+20; ph=22 if not s else 42
    r=f'<g transform="translate({x},{y})"><rect x="-{pw//2}" y="-22" width="{pw}" height="{ph}" rx="4" fill="#0a0a1ecc" stroke="{c}55" stroke-width="1"/>'
    r+=f'<text x="0" y="-4" text-anchor="middle" fill="{c}" font-family="serif" font-size="15" font-weight="bold">{t}</text>'
    if s: r+=f'<text x="0" y="16" text-anchor="middle" fill="{c}88" font-family="serif" font-size="11">{s}</text>'
    r+='</g>'; return r
def ttl(t,s="",y=730):
    r=f'<rect x="0" y="{y-28}" width="1024" height="{50 if s else 35}" fill="#0a0a1ecc"/>'
    r+=f'<text x="512" y="{y}" text-anchor="middle" fill="#f0d78c" font-family="serif" font-size="24" font-weight="bold">{t}</text>'
    if s: r+=f'<text x="512" y="{y+20}" text-anchor="middle" fill="#f0d78c99" font-family="serif" font-size="13">{s}</text>'
    return r

def camel(tx,ty,sc=1,flip=False):
    fs=f'scale({sc},{sc})' if not flip else f'scale(-{sc},{sc})'
    return f'''<g transform="translate({tx},{ty})"><g transform="{fs}">
  <ellipse cx="0" cy="0" rx="38" ry="21" fill="#8B6914"/>
  <ellipse cx="-20" cy="-17" rx="11" ry="16" fill="#8B6914"/>
  <ellipse cx="-25" cy="-33" rx="7" ry="11" fill="#8B6914"/>
  <ellipse cx="7" cy="-11" rx="5" ry="12" fill="#7a5a10"/>
  <ellipse cx="17" cy="-6" rx="5" ry="12" fill="#7a5a10"/>
  <ellipse cx="27" cy="-1" rx="5" ry="12" fill="#7a5a10"/>
  <ellipse cx="37" cy="5" rx="5" ry="12" fill="#7a5a10"/>
</g></g>'''

artworks=[]

# ── 01 长安 Chang'an
svg=f'''{h()}
<defs>
  <linearGradient id="g1" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%" stop-color="#1a2a4a"/><stop offset="60%" stop-color="#4a6a9a"/><stop offset="100%" stop-color="#c8a878"/>
  </linearGradient>
</defs>
<rect width="1024" height="768" fill="url(#g1)"/>
<rect x="0" y="580" width="1024" height="188" fill="#8b6a40"/>
<rect x="0" y="548" width="1024" height="35" fill="#b08a50"/>
<rect x="100" y="420" width="824" height="130" fill="#c8a060" stroke="#a08040" stroke-width="3"/>
<rect x="120" y="390" width="40" height="33" fill="#c8a060" stroke="#a08040" stroke-width="2"/>
<rect x="190" y="390" width="40" height="33" fill="#c8a060" stroke="#a08040" stroke-width="2"/>
<rect x="260" y="390" width="40" height="33" fill="#c8a060" stroke="#a08040" stroke-width="2"/>
<rect x="330" y="390" width="40" height="33" fill="#c8a060" stroke="#a08040" stroke-width="2"/>
<rect x="400" y="390" width="40" height="33" fill="#c8a060" stroke="#a08040" stroke-width="2"/>
<rect x="470" y="390" width="40" height="33" fill="#c8a060" stroke="#a08040" stroke-width="2"/>
<rect x="540" y="390" width="40" height="33" fill="#c8a060" stroke="#a08040" stroke-width="2"/>
<rect x="610" y="390" width="40" height="33" fill="#c8a060" stroke="#a08040" stroke-width="2"/>
<rect x="680" y="390" width="40" height="33" fill="#c8a060" stroke="#a08040" stroke-width="2"/>
<rect x="750" y="390" width="40" height="33" fill="#c8a060" stroke="#a08040" stroke-width="2"/>
<rect x="820" y="390" width="40" height="33" fill="#c8a060" stroke="#a08040" stroke-width="2"/>
<rect x="380" y="255" width="264" height="168" fill="#d4b070" stroke="#a08040" stroke-width="2"/>
<polygon points="380,255 512,175 644,255" fill="#8b5a20" stroke="#6a4010" stroke-width="2"/>
<path d="M440,420 Q512,338 584,420" fill="#2a1a0a" stroke="#6a4010" stroke-width="2"/>
<circle cx="450" cy="305" r="11" fill="#ff8020" opacity="0.8"/>
<circle cx="574" cy="305" r="11" fill="#ff8020" opacity="0.8"/>
{camel(690,500,0.7)}
{camel(810,492,0.62)}
{lbl(512,345,"长安 Chang-an","汉武帝派张骞出使西域 起点")}
{ttl("长安 · 丝绸之路的起点","公元前2世纪 · 西汉都城 · 商队西行出发地")}
{f()}'''
artworks.append(("artwork_01_changan.svg",svg))

# ── 02 玉门关 Jade Gate Pass
svg=f'''{h()}
<defs>
  <linearGradient id="g2" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%" stop-color="#0a1a3a"/><stop offset="50%" stop-color="#2a4a7a"/><stop offset="100%" stop-color="#c0a060"/>
  </linearGradient>
</defs>
<rect width="1024" height="768" fill="url(#g2)"/>
<circle cx="200" cy="100" r="2" fill="white" opacity="0.8"/>
<circle cx="400" cy="60" r="2" fill="white" opacity="0.7"/>
<circle cx="700" cy="80" r="2" fill="white" opacity="0.9"/>
<circle cx="900" cy="55" r="1.5" fill="white" opacity="0.6"/>
<path d="M0 510 Q250 475 500 500 Q750 468 1024 488 L1024 768 L0 768Z" fill="#b09050"/>
<path d="M0 570 Q300 538 600 558 Q800 530 1024 548 L1024 768 L0 768Z" fill="#9a7840"/>
<path d="M0 640 Q300 610 600 628 Q800 603 1024 616 L1024 768 L0 768Z" fill="#7a5a28"/>
<rect x="380" y="300" width="264" height="210" fill="#c8a860" stroke="#a08840" stroke-width="3"/>
<rect x="380" y="278" width="264" height="25" fill="#c8a860" stroke="#a08840" stroke-width="2"/>
<rect x="396" y="260" width="36" height="20" fill="#c8a860"/>
<rect x="456" y="260" width="36" height="20" fill="#c8a860"/>
<rect x="516" y="260" width="36" height="20" fill="#c8a860"/>
<rect x="576" y="260" width="36" height="20" fill="#c8a860"/>
<rect x="612" y="260" width="34" height="20" fill="#c8a860"/>
<path d="M450,510 Q512,440 574,510" fill="#1a1008" stroke="#806828" stroke-width="2"/>
<ellipse cx="512" cy="248" rx="24" ry="8" fill="#ff6010" opacity="0.8"/>
<ellipse cx="512" cy="234" rx="14" ry="18" fill="#ff8020" opacity="0.6"/>
<ellipse cx="512" cy="222" rx="8" ry="13" fill="#ffcc40" opacity="0.5"/>
<path d="M644,390 Q800,410 960,400 Q992,398 1024,402" stroke="#c8a860" stroke-width="7" fill="none" opacity="0.6"/>
<path d="M380,390 Q180,420 60,412 Q30,410 0,415" stroke="#c8a860" stroke-width="7" fill="none" opacity="0.6"/>
<rect x="432" y="530" width="160" height="46" rx="5" fill="#d4b870" stroke="#a09040" stroke-width="2"/>
<text x="512" y="551" text-anchor="middle" fill="#4a2800" font-family="serif" font-size="14">玉门关</text>
<text x="512" y="568" text-anchor="middle" fill="#6a4010" font-family="serif" font-size="11">春风不度玉门关</text>
{lbl(512,278,"玉门关 · Jade Gate Pass","汉代西域边关 · 丝路西行门户")}
{ttl("玉门关 · 丝路西行第一关","春风不度玉门关 · 千里戍边烽火台")}
{f()}'''
artworks.append(("artwork_02_yumenguan.svg",svg))

# ── 03 敦煌莫高窟 Dunhuang Mogao
svg=f'''{h()}
<defs>
  <linearGradient id="g3" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%" stop-color="#1a0a2e"/><stop offset="45%" stop-color="#c84010"/><stop offset="72%" stop-color="#f0a030"/><stop offset="100%" stop-color="#f5c860"/>
  </linearGradient>
  <linearGradient id="sg3" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%" stop-color="#d4a040"/><stop offset="100%" stop-color="#8b5e2c"/>
  </linearGradient>
</defs>
<rect width="1024" height="768" fill="url(#g3)"/>
<circle cx="512" cy="340" r="160" fill="#ff9030" opacity="0.3"/>
<ellipse cx="512" cy="250" rx="68" ry="58" fill="#fff4c0" opacity="0.95"/>
<path d="M0 505 Q200 458 380 488 Q540 440 680 478 Q820 445 1024 468 L1024 768 L0 768Z" fill="#c89040"/>
<path d="M0 550 Q220 505 420 535 Q620 488 820 520 Q920 502 1024 512 L1024 768 L0 768Z" fill="url(#sg3)"/>
<path d="M0 615 Q300 578 560 598 Q760 562 1024 578 L1024 768 L0 768Z" fill="#7a4a28"/>
<rect x="55" y="375" width="335" height="162" fill="#c8a050" stroke="#a07830" stroke-width="2"/>
<rect x="70" y="385" width="62" height="82" fill="#2a1a0a"/>
<rect x="152" y="385" width="62" height="82" fill="#2a1a0a"/>
<rect x="234" y="385" width="62" height="82" fill="#2a1a0a"/>
<rect x="316" y="385" width="60" height="82" fill="#2a1a0a"/>
<ellipse cx="101" cy="426" rx="21" ry="26" fill="#f5c060" opacity="0.35"/>
<ellipse cx="183" cy="426" rx="21" ry="26" fill="#f5c060" opacity="0.35"/>
<ellipse cx="265" cy="426" rx="21" ry="26" fill="#f5c060" opacity="0.35"/>
{camel(600,505,0.78)}
{camel(740,497,0.67)}
{camel(870,508,0.58)}
{lbl(220,355,"敦煌 · Dunhuang","丝路要冲 · 莫高窟 735个洞窟")}
{ttl("敦煌莫高窟 · 大漠中的文明绿洲","公元4-14世纪 · 世界文化遗产 · 东西方艺术交汇")}
{f()}'''
artworks.append(("artwork_03_dunhuang.svg",svg))

# ── 04 吐鲁番 Turpan Flaming Mts
svg=f'''{h()}
<defs>
  <linearGradient id="g4" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%" stop-color="#3a1a0a"/><stop offset="40%" stop-color="#c84820"/><stop offset="70%" stop-color="#f07030"/><stop offset="100%" stop-color="#f0b050"/>
  </linearGradient>
  <linearGradient id="mt4" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%" stop-color="#cc4010"/><stop offset="50%" stop-color="#e86030"/><stop offset="100%" stop-color="#c84820"/>
  </linearGradient>
</defs>
<rect width="1024" height="768" fill="url(#g4)"/>
<path d="M0,395 Q80,295 160,358 Q240,248 320,318 Q400,198 480,278 Q560,168 640,248 Q720,178 800,238 Q880,158 960,218 Q1000,198 1024,228 L1024,518 L0,518Z" fill="url(#mt4)"/>
<path d="M0,425 Q100,365 200,398 Q300,348 400,388 Q500,338 600,378 Q700,338 800,368 Q900,328 1024,358 L1024,518 L0,518Z" fill="#d04820" opacity="0.7"/>
<path d="M0 540 Q200 510 400 530 Q600 500 800 520 Q900 505 1024 512 L1024 768 L0 768Z" fill="#8a4010"/>
<rect x="100" y="498" width="350" height="200" fill="#1a3a10" opacity="0.7"/>
<path d="M100,510 L450,510" stroke="#3a5a20" stroke-width="3"/>
<path d="M100,535 L450,535" stroke="#3a5a20" stroke-width="2"/>
<path d="M100,560 L450,560" stroke="#3a5a20" stroke-width="2"/>
<circle cx="150" cy="520" r="5" fill="#6a2080" opacity="0.9"/>
<circle cx="160" cy="514" r="5" fill="#5a1870" opacity="0.9"/>
<circle cx="170" cy="520" r="5" fill="#7a2890" opacity="0.9"/>
<circle cx="250" cy="548" r="5" fill="#6a2080" opacity="0.9"/>
<circle cx="260" cy="542" r="5" fill="#5a1870" opacity="0.9"/>
<circle cx="350" cy="528" r="5" fill="#6a2080" opacity="0.9"/>
<circle cx="360" cy="522" r="5" fill="#7a2890" opacity="0.9"/>
<circle cx="400" cy="558" r="5" fill="#5a1870" opacity="0.9"/>
{lbl(275,465,"吐鲁番 · Turpan","火焰山 · 葡萄谷 · 海拔-154m盆地")}
{ttl("吐鲁番 · 火焰山与葡萄谷","《西游记》火焰山原型 · 绿洲农业文明奇迹")}
{f()}'''
artworks.append(("artwork_04_turpan.svg",svg))

# ── 05 喀什 Kashgar Bazaar
svg=f'''{h()}
<defs>
  <linearGradient id="g5" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%" stop-color="#1a3a5a"/><stop offset="60%" stop-color="#4a8ab0"/><stop offset="100%" stop-color="#d4c090"/>
  </linearGradient>
</defs>
<rect width="1024" height="768" fill="url(#g5)"/>
<rect x="0" y="558" width="1024" height="210" fill="#c4a070"/>
<rect x="0" y="538" width="1024" height="22" fill="#d4b080"/>
<rect x="58" y="348" width="342" height="212" fill="#f0e0b0" stroke="#c8a040" stroke-width="2"/>
<rect x="63" y="248" width="56" height="103" fill="#e8d090"/>
<ellipse cx="91" cy="248" rx="28" ry="36" fill="#d0a040"/>
<rect x="81" y="218" width="20" height="32" fill="#c09030"/>
<circle cx="91" cy="216" r="8" fill="#e8c040"/>
<rect x="342" y="253" width="54" height="98" fill="#e8d090"/>
<ellipse cx="369" cy="253" rx="27" ry="34" fill="#d0a040"/>
<rect x="359" y="222" width="20" height="33" fill="#c09030"/>
<circle cx="369" cy="220" r="8" fill="#e8c040"/>
<path d="M118,348 Q175,298 232,348" fill="#b0d0e0" stroke="#c8a040" stroke-width="1"/>
<path d="M252,348 Q309,298 366,348" fill="#b0d0e0" stroke="#c8a040" stroke-width="1"/>
<ellipse cx="229" cy="348" rx="72" ry="57" fill="#d8b840"/>
<ellipse cx="229" cy="340" rx="52" ry="42" fill="#e8c850"/>
<ellipse cx="229" cy="334" rx="30" ry="26" fill="#f0d040" opacity="0.8"/>
<rect x="518" y="398" width="452" height="168" fill="#f5e8c0" stroke="#c8a040" stroke-width="1"/>
<rect x="533" y="378" width="62" height="30" fill="#e88020"/>
<rect x="613" y="373" width="62" height="35" fill="#c04020"/>
<rect x="693" y="368" width="62" height="40" fill="#208040"/>
<rect x="773" y="376" width="62" height="32" fill="#6020a0"/>
<rect x="853" y="370" width="62" height="38" fill="#204080"/>
<rect x="518" y="408" width="452" height="8" fill="#d04020" opacity="0.6"/>
<rect x="518" y="428" width="452" height="8" fill="#f0a020" opacity="0.6"/>
<rect x="518" y="448" width="452" height="8" fill="#20a040" opacity="0.6"/>
<circle cx="568" cy="520" r="8" fill="#3a2010"/>
<rect x="562" y="528" width="12" height="30" rx="4" fill="#3a2010"/>
<circle cx="648" cy="515" r="8" fill="#2a1a08"/>
<rect x="642" y="523" width="12" height="30" rx="4" fill="#2a1a08"/>
{lbl(378,338,"喀什 · Kashgar","中西亚贸易中心 · 大巴扎")}
{ttl("喀什 · 丝路最大集市","多元文化交汇 · 维吾尔建筑与中亚商贸")}
{f()}'''
artworks.append(("artwork_05_kashgar.svg",svg))

# ── 06 帕米尔高原 Pamir Plateau
svg=f'''{h()}
<defs>
  <linearGradient id="g6" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%" stop-color="#0a1a3a"/><stop offset="40%" stop-color="#1a3a6a"/><stop offset="70%" stop-color="#4a6a9a"/><stop offset="100%" stop-color="#8ab0d0"/>
  </linearGradient>
</defs>
<rect width="1024" height="768" fill="url(#g6)"/>
<path d="M0,340 Q100,195 200,278 Q300,148 400,228 Q500,98 600,198 Q700,128 800,208 Q900,148 1024,218 L1024,768 L0,768Z" fill="#5a7a9a" opacity="0.7"/>
<path d="M150,278 Q200,198 250,278" fill="white" opacity="0.75"/>
<path d="M350,228 Q400,148 450,228" fill="white" opacity="0.75"/>
<path d="M550,198 Q600,98 650,198" fill="white" opacity="0.82"/>
<path d="M750,208 Q800,128 850,208" fill="white" opacity="0.75"/>
<path d="M0,448 Q120,298 250,378 Q380,248 512,338 Q640,218 770,318 Q900,248 1024,328 L1024,768 L0,768Z" fill="#6a8a7a"/>
<path d="M200,378 Q250,298 300,378" fill="white" opacity="0.88"/>
<path d="M462,338 Q512,238 562,338" fill="white" opacity="0.9"/>
<path d="M720,318 Q770,218 820,318" fill="white" opacity="0.88"/>
<path d="M0,578 Q200,548 400,568 Q600,538 800,558 Q900,543 1024,552 L1024 768 L0 768Z" fill="#4a5a4a"/>
<path d="M150,598 Q400,572 650,588 Q800,580 950,586" stroke="#8a7060" stroke-width="3" fill="none" stroke-dasharray="10,5"/>
{camel(300,590,0.52)}
{camel(430,585,0.46)}
{camel(560,592,0.40)}
{lbl(512,448,"帕米尔高原 · Pamir","世界屋脊 · 海拔4000+米")}
{ttl("帕米尔高原 · 世界屋脊商道","驼队翻越雪山天险 连接东西方文明")}
{f()}'''
artworks.append(("artwork_06_pamir.svg",svg))

# ── 07 撒马尔罕 Samarkand Registan
svg=f'''{h()}
<defs>
  <linearGradient id="g7" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%" stop-color="#05050f"/><stop offset="50%" stop-color="#101030"/><stop offset="100%" stop-color="#202050"/>
  </linearGradient>
</defs>
<rect width="1024" height="768" fill="url(#g7)"/>
<circle cx="100" cy="70" r="1.8" fill="white" opacity="0.9"/>
<circle cx="280" cy="45" r="1.5" fill="white" opacity="0.7"/>
<circle cx="500" cy="65" r="2" fill="white" opacity="0.8"/>
<circle cx="700" cy="38" r="1.5" fill="white" opacity="0.6"/>
<circle cx="880" cy="60" r="2" fill="white" opacity="0.9"/>
<circle cx="600" cy="95" r="1.5" fill="white" opacity="0.5"/>
<rect x="0" y="578" width="1024" height="190" fill="#6a5030"/>
<rect x="0" y="556" width="1024" height="25" fill="#7a6040"/>
<rect x="68" y="368" width="230" height="192" fill="#3060a0" stroke="#205080" stroke-width="2"/>
<ellipse cx="183" cy="368" rx="96" ry="88" fill="#4070b0"/>
<ellipse cx="183" cy="362" rx="76" ry="70" fill="#5080c0"/>
<ellipse cx="183" cy="356" rx="46" ry="42" fill="#f0d040" opacity="0.85"/>
<rect x="73" y="198" width="42" height="175" fill="#4070b0"/>
<ellipse cx="94" cy="198" rx="21" ry="32" fill="#3060a0"/>
<circle cx="94" cy="164" r="7" fill="#d8c040"/>
<rect x="254" y="202" width="42" height="170" fill="#4070b0"/>
<ellipse cx="275" cy="202" rx="21" ry="30" fill="#3060a0"/>
<circle cx="275" cy="170" r="7" fill="#d8c040"/>
<rect x="726" y="368" width="230" height="192" fill="#3060a0" stroke="#205080" stroke-width="2"/>
<ellipse cx="841" cy="368" rx="96" ry="88" fill="#4070b0"/>
<ellipse cx="841" cy="362" rx="76" ry="70" fill="#5080c0"/>
<ellipse cx="841" cy="356" rx="46" ry="42" fill="#f0d040" opacity="0.85"/>
<rect x="726" y="200" width="42" height="173" fill="#4070b0"/>
<ellipse cx="747" cy="200" rx="21" ry="32" fill="#3060a0"/>
<circle cx="747" cy="166" r="7" fill="#d8c040"/>
<rect x="910" y="203" width="42" height="170" fill="#4070b0"/>
<ellipse cx="931" cy="203" rx="21" ry="30" fill="#3060a0"/>
<circle cx="931" cy="172" r="7" fill="#d8c040"/>
<rect x="350" y="278" width="324" height="102" fill="#2050a0" stroke="#104080" stroke-width="2"/>
<ellipse cx="512" cy="278" rx="122" ry="102" fill="#3060b0"/>
<ellipse cx="512" cy="270" rx="92" ry="80" fill="#4070c0"/>
<ellipse cx="512" cy="262" rx="57" ry="50" fill="#f0d840" opacity="0.88"/>
{lbl(512,260,"撒马尔罕 · Samarkand","中亚第一重镇 · 帖木儿帝国首都")}
{ttl("撒马尔罕 · 蓝色圆顶之城","雷吉斯坦广场 · 丝路中亚最辉煌都市")}
{f()}'''
artworks.append(("artwork_07_samarkand.svg",svg))

# ── 08 布哈拉 Bukhara
svg=f'''{h()}
<defs>
  <linearGradient id="g8" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%" stop-color="#e8b050"/><stop offset="40%" stop-color="#d4782a"/><stop offset="70%" stop-color="#c04010"/><stop offset="100%" stop-color="#8a2a08"/>
  </linearGradient>
</defs>
<rect width="1024" height="768" fill="url(#g8)"/>
<circle cx="148" cy="198" r="98" fill="#f0c050" opacity="0.38"/>
<ellipse cx="148" cy="118" rx="64" ry="54" fill="#fff0c0" opacity="0.95"/>
<rect x="0" y="568" width="1024" height="200" fill="#b89050"/>
<path d="M0,553 Q300,533 600,548 Q800,528 1024,542 L1024 580 L0 580Z" fill="#c8a060"/>
<rect x="468" y="198" width="88" height="372" fill="#d4a840"/>
<rect x="463" y="218" width="98" height="8" rx="2" fill="#a07830" opacity="0.5"/>
<rect x="460" y="258" width="104" height="8" rx="2" fill="#a07830" opacity="0.5"/>
<rect x="457" y="298" width="110" height="8" rx="2" fill="#a07830" opacity="0.5"/>
<rect x="454" y="338" width="116" height="8" rx="2" fill="#a07830" opacity="0.5"/>
<rect x="451" y="378" width="122" height="8" rx="2" fill="#a07830" opacity="0.5"/>
<rect x="448" y="418" width="128" height="8" rx="2" fill="#a07830" opacity="0.5"/>
<rect x="445" y="458" width="134" height="8" rx="2" fill="#a07830" opacity="0.5"/>
<ellipse cx="512" cy="198" rx="54" ry="26" fill="#b88030"/>
<rect x="499" y="172" width="26" height="30" fill="#c89040"/>
<circle cx="512" cy="170" r="11" fill="#e0a040"/>
<rect x="118" y="388" width="342" height="182" fill="#c8a040" stroke="#a07820" stroke-width="2"/>
<ellipse cx="289" cy="388" rx="92" ry="72" fill="#b08030"/>
<ellipse cx="289" cy="381" rx="70" ry="57" fill="#c09040"/>
<ellipse cx="289" cy="376" rx="42" ry="35" fill="#d8a850" opacity="0.85"/>
<path d="M208,568 Q289,488 370,568" fill="#2a1a08" stroke="#806020" stroke-width="2"/>
{camel(660,555,0.68)}
{camel(800,550,0.58)}
{lbl(512,445,"布哈拉 · Bukhara","中亚古城 · 卡伦宣礼塔")}
{ttl("布哈拉 · 中亚历史名城","世界遗产 · 伊斯兰学术与贸易中心")}
{f()}'''
artworks.append(("artwork_08_bukhara.svg",svg))

# ── 09 波斯集市 Persian Bazaar
svg=f'''{h()}
<defs>
  <linearGradient id="g9" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%" stop-color="#2a1a3a"/><stop offset="40%" stop-color="#5a3a7a"/><stop offset="70%" stop-color="#9a6a9a"/><stop offset="100%" stop-color="#d4a860"/>
  </linearGradient>
</defs>
<rect width="1024" height="768" fill="url(#g9)"/>
<rect x="0" y="558" width="1024" height="210" fill="#b09060"/>
<path d="M0,198 Q256,148 512,178 Q768,148 1024,198 L1024,558 L0,558Z" fill="#3a2a1a" opacity="0.9"/>
<path d="M0,248 Q256,168 512,208 Q768,168 1024,248" stroke="#6a5030" stroke-width="4" fill="none" opacity="0.7"/>
<path d="M0,308 Q256,238 512,268 Q768,238 1024,308" stroke="#6a5030" stroke-width="3" fill="none" opacity="0.6"/>
<path d="M0,378 Q256,318 512,348 Q768,318 1024,378" stroke="#6a5030" stroke-width="3" fill="none" opacity="0.5"/>
<path d="M198,178 L238,558" stroke="#f0d08030" stroke-width="30" fill="none"/>
<path d="M512,168 L512,558" stroke="#f0d08018" stroke-width="40" fill="none"/>
<path d="M798,178 L778,558" stroke="#f0d08030" stroke-width="30" fill="none"/>
<rect x="48" y="378" width="252" height="182" fill="#e8d0a0" stroke="#a08040" stroke-width="1"/>
<rect x="53" y="358" width="242" height="24" fill="#c04020" opacity="0.8"/>
<ellipse cx="98" cy="438" rx="36" ry="12" fill="#c84010"/>
<ellipse cx="158" cy="438" rx="36" ry="12" fill="#f0a030"/>
<ellipse cx="218" cy="438" rx="36" ry="12" fill="#e0c020"/>
<text x="98" y="434" text-anchor="middle" fill="#fff" font-size="10">辣椒</text>
<text x="158" y="434" text-anchor="middle" fill="#fff" font-size="10">肉桂</text>
<text x="218" y="434" text-anchor="middle" fill="#fff" font-size="10">姜黄</text>
<rect x="722" y="378" width="252" height="182" fill="#e0c890" stroke="#a08040" stroke-width="1"/>
<rect x="722" y="358" width="252" height="24" fill="#2060a0" opacity="0.8"/>
<rect x="732" y="383" width="32" height="122" fill="#e83030" opacity="0.7"/>
<rect x="774" y="383" width="32" height="122" fill="#3030e8" opacity="0.7"/>
<rect x="816" y="383" width="32" height="122" fill="#30a030" opacity="0.7"/>
<rect x="858" y="383" width="32" height="122" fill="#c0a020" opacity="0.7"/>
<rect x="900" y="383" width="32" height="122" fill="#a030a0" opacity="0.7"/>
<circle cx="428" cy="498" r="12" fill="#3a2010"/>
<rect x="420" y="510" width="16" height="40" rx="5" fill="#3a2010"/>
<circle cx="578" cy="493" r="12" fill="#2a1808"/>
<rect x="570" y="505" width="16" height="40" rx="5" fill="#2a1808"/>
{lbl(512,438,"波斯集市 · Persian Bazaar","尼沙普尔 · 香料珠宝中转站")}
{ttl("波斯集市 · 香料与珠宝的王国","中东枢纽 · 连接东西方的商贸通道")}
{f()}'''
artworks.append(("artwork_09_persian_bazaar.svg",svg))

# ── 10 巴格达 Baghdad
svg=f'''{h()}
<defs>
  <linearGradient id="g10" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%" stop-color="#0a1a3a"/><stop offset="30%" stop-color="#1a3a6a"/><stop offset="70%" stop-color="#2a5a8a"/><stop offset="100%" stop-color="#6a9ab0"/>
  </linearGradient>
</defs>
<rect width="1024" height="768" fill="url(#g10)"/>
<circle cx="80" cy="58" r="2" fill="white" opacity="0.9"/>
<circle cx="200" cy="88" r="1.5" fill="white" opacity="0.7"/>
<circle cx="380" cy="43" r="2" fill="white" opacity="0.8"/>
<circle cx="600" cy="73" r="1.5" fill="white" opacity="0.6"/>
<circle cx="750" cy="53" r="2" fill="white" opacity="0.9"/>
<circle cx="920" cy="78" r="1.5" fill="white" opacity="0.7"/>
<path d="M0,478 Q200,458 400,473 Q600,448 800,463 Q900,453 1024,458 L1024,528 Q800,518 600,508 Q400,523 200,508 Q100,518 0,513Z" fill="#1a5080" opacity="0.75"/>
<circle cx="512" cy="348" r="202" fill="none" stroke="#d4a840" stroke-width="4"/>
<circle cx="512" cy="348" r="162" fill="none" stroke="#d4a840" stroke-width="2"/>
<circle cx="512" cy="348" r="82" fill="#3a2a10" stroke="#d4a840" stroke-width="3"/>
<rect x="490" y="318" width="44" height="62" fill="#c8a040"/>
<ellipse cx="512" cy="318" rx="22" ry="28" fill="#d8b050"/>
<circle cx="512" cy="314" r="8" fill="#e8c060"/>
<rect x="498" y="145" width="28" height="32" fill="#c8a840"/>
<rect x="498" y="518" width="28" height="32" fill="#c8a840"/>
<rect x="308" y="336" width="32" height="25" fill="#c8a840"/>
<rect x="684" y="336" width="32" height="25" fill="#c8a840"/>
<text x="390" y="498" fill="#6ab0d0" font-family="serif" font-size="18" opacity="0.8">底格里斯河</text>
{lbl(512,228,"巴格达 · Baghdad","阿拔斯王朝 · 圆形城市")}
{ttl("巴格达 · 阿拔斯帝国黄金时代","公元762年建城 · 丝路最繁盛的中东都市")}
{f()}'''
artworks.append(("artwork_10_baghdad.svg",svg))

# ── 11 君士坦丁堡 Constantinople
svg=f'''{h()}
<defs>
  <linearGradient id="g11" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%" stop-color="#c87030"/><stop offset="40%" stop-color="#e09050"/><stop offset="70%" stop-color="#f0c070"/><stop offset="100%" stop-color="#f5e090"/>
  </linearGradient>
</defs>
<rect width="1024" height="768" fill="url(#g11)"/>
<path d="M0,418 Q200,398 400,413 Q600,393 800,408 Q900,398 1024,406 L1024,566 Q800,556 600,563 Q400,553 200,560 Q100,556 0,558Z" fill="#2060a0" opacity="0.82"/>
<path d="M0,278 Q200,238 400,258 Q600,228 800,248 Q900,238 1024,253 L1024,418 L0,418Z" fill="#8a7040"/>
<path d="M0,378 Q150,358 300,368 Q450,353 600,363 Q750,348 900,358 Q970,353 1024,356 L1024,418 L0,418Z" fill="#a08050"/>
<rect x="348" y="268" width="328" height="152" fill="#d4c090" stroke="#b0a070" stroke-width="2"/>
<ellipse cx="512" cy="268" rx="122" ry="97" fill="#e0c890"/>
<ellipse cx="512" cy="260" rx="92" ry="74" fill="#e8d0a0"/>
<ellipse cx="512" cy="253" rx="57" ry="50" fill="#d4b870"/>
<ellipse cx="348" cy="348" rx="72" ry="57" fill="#d8c880" opacity="0.7"/>
<ellipse cx="676" cy="348" rx="72" ry="57" fill="#d8c880" opacity="0.7"/>
<rect x="316" y="238" width="30" height="102" fill="#c8b070"/>
<ellipse cx="331" cy="238" rx="15" ry="22" fill="#b8a060"/>
<circle cx="331" cy="214" r="6" fill="#d8c040"/>
<rect x="678" y="238" width="30" height="102" fill="#c8b070"/>
<ellipse cx="693" cy="238" rx="15" ry="22" fill="#b8a060"/>
<circle cx="693" cy="214" r="6" fill="#d8c040"/>
<rect x="338" y="338" width="26" height="82" fill="#c0a860"/>
<ellipse cx="351" cy="338" rx="13" ry="19" fill="#b09850"/>
<rect x="660" y="338" width="26" height="82" fill="#c0a860"/>
<ellipse cx="673" cy="338" rx="13" ry="19" fill="#b09850"/>
<path d="M198,453 Q240,438 282,448" stroke="#4a3010" stroke-width="5" fill="#6a4820"/>
<rect x="228" y="416" width="3" height="30" fill="#4a3010"/>
<path d="M230,416 L266,428" stroke="#a08050" stroke-width="1"/>
{lbl(512,253,"君士坦丁堡 · Constantinople","拜占庭帝国首都 · 今伊斯坦布尔")}
{ttl("君士坦丁堡 · 东西方帝都","圣索菲亚大教堂 · 欧亚十字路口")}
{f()}'''
artworks.append(("artwork_11_constantinople.svg",svg))

# ── 12 威尼斯 Venice
svg=f'''{h()}
<defs>
  <linearGradient id="g12" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%" stop-color="#1a2a4a"/><stop offset="50%" stop-color="#4a7aaa"/><stop offset="100%" stop-color="#8ab0cc"/>
  </linearGradient>
</defs>
<rect width="1024" height="768" fill="url(#g12)"/>
<path d="M0,438 Q200,418 400,433 Q600,413 800,428 Q900,416 1024,423 L1024,598 Q800,588 600,593 Q400,583 200,590 Q100,586 0,588Z" fill="#1a4a8a" opacity="0.85"/>
<path d="M100,458 Q300,448 500,456" stroke="#4a90d0" stroke-width="1" fill="none" opacity="0.4"/>
<path d="M200,478 Q450,466 700,474" stroke="#4a90d0" stroke-width="1" fill="none" opacity="0.4"/>
<path d="M50,498 Q350,486 650,493 Q850,483 1000,490" stroke="#4a90d0" stroke-width="1" fill="none" opacity="0.3"/>
<rect x="28" y="308" width="182" height="133" fill="#e8d8c0" stroke="#b0a070" stroke-width="2"/>
<rect x="48" y="288" width="142" height="23" fill="#d4c0a0" stroke="#a09060" stroke-width="1"/>
<path d="M68,333 Q90,313 112,333" fill="#a0c0e0"/>
<path d="M132,333 Q154,313 176,333" fill="#a0c0e0"/>
<path d="M68,373 Q90,353 112,373" fill="#a0c0e0"/>
<path d="M132,373 Q154,353 176,373" fill="#a0c0e0"/>
<rect x="248" y="278" width="212" height="165" fill="#f0e0c0" stroke="#c0b080" stroke-width="2"/>
<rect x="263" y="258" width="182" height="23" fill="#e0d0b0"/>
<path d="M283,308 Q309,283 335,308" fill="#b0c8e0"/>
<path d="M355,308 Q381,283 407,308" fill="#b0c8e0"/>
<rect x="488" y="178" width="66" height="267" fill="#e8c870"/>
<rect x="478" y="168" width="86" height="14" fill="#d4b850"/>
<rect x="474" y="155" width="94" height="14" fill="#e0c060"/>
<polygon points="474,155 521,108 568,155" fill="#c8a040"/>
<circle cx="521" cy="103" r="11" fill="#e8c040"/>
<rect x="618" y="338" width="362" height="107" fill="#f8e8d0" stroke="#c0a870" stroke-width="2"/>
<path d="M628,445 Q644,423 660,445" fill="#e0d0b0"/>
<path d="M668,445 Q684,423 700,445" fill="#e0d0b0"/>
<path d="M708,445 Q724,423 740,445" fill="#e0d0b0"/>
<path d="M748,445 Q764,423 780,445" fill="#e0d0b0"/>
<path d="M788,445 Q804,423 820,445" fill="#e0d0b0"/>
<path d="M828,445 Q844,423 860,445" fill="#e0d0b0"/>
<path d="M868,445 Q884,423 900,445" fill="#e0d0b0"/>
<path d="M908,445 Q924,423 940,445" fill="#e0d0b0"/>
<path d="M120,528 Q200,508 280,523 Q260,553 180,550 Q140,548 120,528Z" fill="#1a1010"/>
<rect x="175" y="486" width="4" height="48" fill="#3a2010"/>
<path d="M178,487 Q220,498 178,510" fill="#c0a050" opacity="0.75"/>
{lbl(512,248,"威尼斯 · Venice","马可·波罗故乡 · 丝路西端终点")}
{ttl("威尼斯 · 丝路西端的海洋共和国","马可·波罗从这里出发 开启东西方传奇")}
{f()}'''
artworks.append(("artwork_12_venice.svg",svg))

# ── 13 广州港 Guangzhou Port
svg=f'''{h()}
<defs>
  <linearGradient id="g13" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%" stop-color="#1a3a5a"/><stop offset="50%" stop-color="#3a6a9a"/><stop offset="100%" stop-color="#6a9ab0"/>
  </linearGradient>
  <linearGradient id="sea13" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%" stop-color="#1a5080"/><stop offset="100%" stop-color="#0a2a50"/>
  </linearGradient>
</defs>
<rect width="1024" height="768" fill="url(#g13)"/>
<path d="M0,378 Q200,358 400,373 Q600,353 800,368 Q900,358 1024,363 L1024,768 L0,768Z" fill="url(#sea13)"/>
<path d="M50,398 Q150,386 250,396 Q350,383 450,393" stroke="#5aaad0" stroke-width="1.5" fill="none" opacity="0.6"/>
<path d="M300,418 Q450,406 600,416 Q750,404 900,414" stroke="#5aaad0" stroke-width="1.5" fill="none" opacity="0.5"/>
<path d="M100,443 Q300,431 500,440 Q700,426 950,436" stroke="#5aaad0" stroke-width="1.5" fill="none" opacity="0.4"/>
<rect x="0" y="248" width="352" height="133" fill="#c8a050" stroke="#a07830" stroke-width="2"/>
<rect x="0" y="228" width="352" height="23" fill="#b89040"/>
<rect x="18" y="298" width="52" height="72" rx="3" fill="#d4b060"/>
<rect x="88" y="308" width="52" height="62" rx="3" fill="#c8a050"/>
<rect x="158" y="293" width="52" height="77" rx="3" fill="#d8b060"/>
<rect x="398" y="278" width="82" height="102" fill="#c04010"/>
<rect x="388" y="263" width="102" height="18" fill="#d04818"/>
<rect x="378" y="246" width="122" height="18" fill="#c04010"/>
<rect x="393" y="231" width="92" height="16" fill="#d04818"/>
<rect x="403" y="218" width="72" height="14" fill="#c04010"/>
<rect x="413" y="206" width="52" height="12" fill="#d04818"/>
<rect x="422" y="195" width="34" height="12" fill="#c04010"/>
<rect x="430" y="184" width="18" height="12" fill="#d04818"/>
<path d="M548,388 Q620,368 692,378 Q682,418 612,416 Q568,413 548,388Z" fill="#4a2810"/>
<rect x="608" y="348" width="4" height="47" fill="#2a1808"/>
<path d="M611,349 Q651,360 611,373" fill="#8a6040" opacity="0.85"/>
<path d="M748,373 Q800,360 852,368 Q846,396 796,394 Q762,392 748,373Z" fill="#3a2008" opacity="0.8"/>
<rect x="793" y="343" width="3" height="36" fill="#2a1808" opacity="0.8"/>
<path d="M795,344 Q825,353 795,362" fill="#8a6040" opacity="0.6"/>
<path d="M148,433 Q230,416 312,426 Q300,466 220,463 Q166,460 148,433Z" fill="#3a2010" opacity="0.9"/>
<rect x="220" y="390" width="4" height="48" fill="#2a1808"/>
<path d="M223,391 Q266,403 223,416" fill="#8a6040" opacity="0.8"/>
{lbl(512,288,"广州 · Guangzhou","海上丝绸之路起点 · 唐宋第一港")}
{ttl("广州港 · 海上丝路出发地","大唐番禺 · 东方第一贸易港口")}
{f()}'''
artworks.append(("artwork_13_guangzhou.svg",svg))

# ── 14 郑和宝船 Zheng He
svg=f'''{h()}
<defs>
  <linearGradient id="g14" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%" stop-color="#1a3a5a"/><stop offset="50%" stop-color="#2a5a8a"/><stop offset="100%" stop-color="#4a80a0"/>
  </linearGradient>
  <linearGradient id="sea14" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%" stop-color="#1a5080"/><stop offset="100%" stop-color="#0a2a50"/>
  </linearGradient>
</defs>
<rect width="1024" height="768" fill="url(#g14)"/>
<rect x="0" y="318" width="1024" height="450" fill="url(#sea14)"/>
<path d="M0,338 Q80,323 160,336 Q240,320 320,334 Q400,318 480,332 Q560,316 640,330 Q720,314 800,328 Q880,312 1024,324" stroke="#3a80b0" stroke-width="2" fill="none" opacity="0.7"/>
<path d="M0,378 Q100,360 200,374 Q300,356 400,370 Q500,353 600,367 Q700,350 800,364 Q900,348 1024,360" stroke="#3a80b0" stroke-width="1.5" fill="none" opacity="0.5"/>
<path d="M278,378 Q350,348 512,338 Q674,348 746,378 Q762,428 746,458 Q674,468 512,473 Q350,468 278,458 Q262,428 278,378Z" fill="#3a1808"/>
<rect x="378" y="283" width="268" height="60" fill="#4a2010"/>
<rect x="398" y="263" width="228" height="23" fill="#3a1808"/>
<rect x="503" y="178" width="16" height="173" fill="#2a1008"/>
<path d="M519,180 L742,228 L742,350 L519,350Z" fill="#cc2010" opacity="0.9"/>
<path d="M519,214 L740,248" stroke="#880808" stroke-width="2"/>
<path d="M519,248 L740,280" stroke="#880808" stroke-width="2"/>
<path d="M519,283 L740,310" stroke="#880808" stroke-width="2"/>
<path d="M519,316 L740,336" stroke="#880808" stroke-width="2"/>
<rect x="388" y="198" width="11" height="148" fill="#2a1008"/>
<path d="M399,200 L562,236 L562,342 L399,342Z" fill="#c82008" opacity="0.85"/>
<path d="M399,226 L560,252" stroke="#800808" stroke-width="1.5"/>
<path d="M399,256 L560,276" stroke="#800808" stroke-width="1.5"/>
<path d="M399,286 L560,302" stroke="#800808" stroke-width="1.5"/>
<rect x="633" y="208" width="11" height="138" fill="#2a1008"/>
<path d="M644,210 L782,243 L782,338 L644,338Z" fill="#c01808" opacity="0.8"/>
<path d="M510,178 Q540,168 562,173 Q547,183 532,186 Q537,176 510,178Z" fill="#f0d030"/>
<circle cx="448" cy="293" r="8" fill="#ff6010" opacity="0.8"/>
<circle cx="568" cy="288" r="8" fill="#ff6010" opacity="0.8"/>
<path d="M98,408 Q170,386 242,398 Q232,438 162,436 Q110,433 98,408Z" fill="#2a1008" opacity="0.8"/>
<rect x="158" y="366" width="4" height="48" fill="#1a0808" opacity="0.8"/>
<path d="M161,368 Q222,383 161,398" fill="#c02010" opacity="0.75"/>
<path d="M798,403 Q870,381 942,393 Q932,433 862,431 Q812,428 798,403Z" fill="#2a1008" opacity="0.8"/>
<rect x="858" y="361" width="4" height="48" fill="#1a0808" opacity="0.8"/>
<path d="M861,363 Q922,378 861,393" fill="#c02010" opacity="0.75"/>
<rect x="488" y="168" width="32" height="21" fill="#f0d030" opacity="0.9"/>
<text x="504" y="182" text-anchor="middle" fill="#cc2010" font-size="10">明</text>
{lbl(512,278,"郑和宝船 · Zheng He","1405-1433 · 七次下西洋")}
{ttl("郑和宝船 · 海上丝路的巅峰","永乐年间 七下西洋 最远抵达东非海岸")}
{f()}'''
artworks.append(("artwork_14_zhenghe.svg",svg))

# ── 15 丝绸生产 Silk Production
svg=f'''{h()}
<defs>
  <linearGradient id="g15" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%" stop-color="#f5e8cc"/><stop offset="100%" stop-color="#d4b888"/>
  </linearGradient>
</defs>
<rect width="1024" height="768" fill="url(#g15)"/>
<rect x="78" y="198" width="402" height="352" rx="5" fill="#5a3a10" stroke="#3a2008" stroke-width="3"/>
<rect x="93" y="213" width="372" height="322" rx="3" fill="#2a1808"/>
<g stroke="#f0e8d088" stroke-width="1">
  <line x1="113" y1="213" x2="113" y2="535"/>
  <line x1="128" y1="213" x2="128" y2="535"/>
  <line x1="143" y1="213" x2="143" y2="535"/>
  <line x1="158" y1="213" x2="158" y2="535"/>
  <line x1="173" y1="213" x2="173" y2="535"/>
  <line x1="188" y1="213" x2="188" y2="535"/>
  <line x1="203" y1="213" x2="203" y2="535"/>
  <line x1="218" y1="213" x2="218" y2="535"/>
  <line x1="233" y1="213" x2="233" y2="535"/>
  <line x1="248" y1="213" x2="248" y2="535"/>
  <line x1="263" y1="213" x2="263" y2="535"/>
  <line x1="278" y1="213" x2="278" y2="535"/>
  <line x1="293" y1="213" x2="293" y2="535"/>
  <line x1="308" y1="213" x2="308" y2="535"/>
  <line x1="323" y1="213" x2="323" y2="535"/>
  <line x1="338" y1="213" x2="338" y2="535"/>
  <line x1="353" y1="213" x2="353" y2="535"/>
  <line x1="368" y1="213" x2="368" y2="535"/>
  <line x1="383" y1="213" x2="383" y2="535"/>
  <line x1="398" y1="213" x2="398" y2="535"/>
  <line x1="413" y1="213" x2="413" y2="535"/>
  <line x1="428" y1="213" x2="428" y2="535"/>
  <line x1="443" y1="213" x2="443" y2="535"/>
  <line x1="455" y1="213" x2="455" y2="535"/>
</g>
<rect x="93" y="368" width="372" height="87" fill="#d4305080"/>
<path d="M93,388 L465,388" stroke="#e85070" stroke-width="2"/>
<path d="M93,402 L465,402" stroke="#f06080" stroke-width="2"/>
<path d="M93,416 L465,416" stroke="#d84060" stroke-width="2"/>
<path d="M93,430 L465,430" stroke="#e85070" stroke-width="2"/>
<path d="M93,444 L465,444" stroke="#c83050" stroke-width="2"/>
<ellipse cx="648" cy="398" rx="82" ry="52" fill="#d4a050" stroke="#a07830" stroke-width="2"/>
<rect x="568" y="348" width="162" height="102" fill="#d4a050" stroke="#a07830" stroke-width="2"/>
<ellipse cx="648" cy="348" rx="82" ry="52" fill="#e8b860" stroke="#c09040" stroke-width="2"/>
<path d="M608,358 Q648,333 688,358 Q668,383 648,378 Q628,383 608,358Z" stroke="#c04020" stroke-width="2" fill="none" opacity="0.7"/>
<path d="M648,333 Q658,313 653,293 Q643,308 648,333" stroke="#c04020" stroke-width="2" fill="none" opacity="0.7"/>
<ellipse cx="798" cy="298" rx="19" ry="11" fill="#f0f0e0" stroke="#d0d0c0" stroke-width="1"/>
<ellipse cx="838" cy="283" rx="19" ry="11" fill="#f0f0e0" stroke="#d0d0c0" stroke-width="1"/>
<ellipse cx="878" cy="298" rx="19" ry="11" fill="#f0f0e0" stroke="#d0d0c0" stroke-width="1"/>
<ellipse cx="808" cy="258" rx="23" ry="15" fill="#3a8030" opacity="0.7" transform="rotate(-15,808,258)"/>
<ellipse cx="853" cy="248" rx="23" ry="15" fill="#4a9040" opacity="0.7" transform="rotate(10,853,248)"/>
<ellipse cx="868" cy="268" rx="21" ry="14" fill="#3a8030" opacity="0.7" transform="rotate(-5,868,268)"/>
<rect x="578" y="488" width="362" height="58" rx="5" fill="#8a6030aa"/>
<text x="759" y="518" text-anchor="middle" fill="#f5e0c0" font-family="serif" font-size="16">蚕茧·缫丝·织锦</text>
<text x="759" y="538" text-anchor="middle" fill="#f0d0a0" font-family="serif" font-size="12">中国独有的技术 秘守千年</text>
{lbl(278,173,"中国丝绸生产","养蚕缫丝 · 汉代技术秘密")}
{ttl("养蚕缫丝 · 中国独守千年的秘密","丝绸技术直到唐代才西传")}
{f()}'''
artworks.append(("artwork_15_silk_production.svg",svg))

# ── 16 骆驼商队夜行 Night Caravan
svg=f'''{h()}
<defs>
  <radialGradient id="mn16" cx="0.5" cy="0.5" r="0.5">
    <stop offset="0%" stop-color="#fffae0"/><stop offset="60%" stop-color="#f0e070"/><stop offset="100%" stop-color="#f0e07000"/>
  </radialGradient>
  <linearGradient id="g16" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%" stop-color="#000010"/><stop offset="50%" stop-color="#0a1030"/><stop offset="100%" stop-color="#1a2050"/>
  </linearGradient>
</defs>
<rect width="1024" height="768" fill="url(#g16)"/>
<circle cx="50" cy="40" r="2" fill="white" opacity="0.9"/>
<circle cx="120" cy="78" r="1.5" fill="white" opacity="0.7"/>
<circle cx="200" cy="28" r="2" fill="white" opacity="0.8"/>
<circle cx="320" cy="58" r="1.5" fill="white" opacity="0.6"/>
<circle cx="420" cy="23" r="2" fill="white" opacity="0.9"/>
<circle cx="550" cy="48" r="1.5" fill="white" opacity="0.7"/>
<circle cx="660" cy="33" r="2" fill="white" opacity="0.8"/>
<circle cx="780" cy="53" r="1.5" fill="white" opacity="0.6"/>
<circle cx="880" cy="28" r="2" fill="white" opacity="0.9"/>
<circle cx="960" cy="68" r="1.5" fill="white" opacity="0.7"/>
<circle cx="100" cy="148" r="1.5" fill="white" opacity="0.5"/>
<circle cx="280" cy="128" r="1.5" fill="white" opacity="0.6"/>
<circle cx="480" cy="108" r="1.5" fill="white" opacity="0.5"/>
<circle cx="720" cy="118" r="1.5" fill="white" opacity="0.6"/>
<circle cx="920" cy="138" r="1.5" fill="white" opacity="0.5"/>
<path d="M0,198 Q200,148 400,178 Q600,138 800,158 Q900,143 1024,168" stroke="white" stroke-width="28" fill="none" opacity="0.04"/>
<circle cx="850" cy="128" r="68" fill="url(#mn16)"/>
<circle cx="855" cy="122" r="53" fill="#fffae0" opacity="0.95"/>
<path d="M0,478 Q150,418 300,458 Q450,398 600,448 Q750,398 900,438 Q970,418 1024,433 L1024 768 L0 768Z" fill="#1a1208"/>
<path d="M0,518 Q200,478 400,508 Q600,468 800,498 Q900,478 1024,488 L1024 768 L0 768Z" fill="#2a1e10"/>
<path d="M0,568 Q250,538 500,558 Q750,533 1024,550 L1024 768 L0 768Z" fill="#3a2a18"/>
<g transform="translate(100,490) scale(0.9)"><ellipse cx="0" cy="0" rx="36" ry="20" fill="#1a1208"/><ellipse cx="-20" cy="-17" rx="10" ry="15" fill="#1a1208"/><ellipse cx="-24" cy="-33" rx="7" ry="10" fill="#1a1208"/><ellipse cx="6" cy="-10" rx="5" ry="11" fill="#1a1208"/><ellipse cx="15" cy="-5" rx="5" ry="11" fill="#1a1208"/><ellipse cx="24" cy="0" rx="5" ry="11" fill="#1a1208"/><ellipse cx="33" cy="5" rx="5" ry="11" fill="#1a1208"/></g>
<g transform="translate(280,478) scale(0.83)"><ellipse cx="0" cy="0" rx="36" ry="20" fill="#150e06"/><ellipse cx="-20" cy="-17" rx="10" ry="15" fill="#150e06"/><ellipse cx="-24" cy="-33" rx="7" ry="10" fill="#150e06"/><ellipse cx="6" cy="-10" rx="5" ry="11" fill="#150e06"/><ellipse cx="15" cy="-5" rx="5" ry="11" fill="#150e06"/><ellipse cx="24" cy="0" rx="5" ry="11" fill="#150e06"/></g>
<g transform="translate(460,488) scale(0.77)"><ellipse cx="0" cy="0" rx="34" ry="19" fill="#1a1208"/><ellipse cx="-19" cy="-15" rx="9" ry="14" fill="#1a1208"/><ellipse cx="-23" cy="-30" rx="6" ry="9" fill="#1a1208"/><ellipse cx="5" cy="-9" rx="5" ry="11" fill="#1a1208"/><ellipse cx="14" cy="-4" rx="5" ry="11" fill="#1a1208"/><ellipse cx="23" cy="0" rx="5" ry="11" fill="#1a1208"/></g>
<g transform="translate(640,482) scale(0.72)"><ellipse cx="0" cy="0" rx="34" ry="19" fill="#150e06"/><ellipse cx="-19" cy="-15" rx="9" ry="14" fill="#150e06"/><ellipse cx="-23" cy="-30" rx="6" ry="9" fill="#150e06"/><ellipse cx="5" cy="-9" rx="5" ry="11" fill="#150e06"/><ellipse cx="14" cy="-4" rx="5" ry="11" fill="#150e06"/></g>
<g transform="translate(810,476) scale(0.67)"><ellipse cx="0" cy="0" rx="33" ry="18" fill="#1a1208"/><ellipse cx="-18" cy="-14" rx="9" ry="13" fill="#1a1208"/><ellipse cx="-22" cy="-28" rx="6" ry="9" fill="#1a1208"/><ellipse cx="5" cy="-9" rx="5" ry="10" fill="#1a1208"/><ellipse cx="14" cy="-4" rx="5" ry="10" fill="#1a1208"/></g>
<text x="300" y="463" fill="#f0e09066" font-family="serif" font-size="20">♪ 驼铃声声</text>
{lbl(512,428,"大漠星空","商队夜行 · 以星辰导航")}
{ttl("大漠星空 · 驼铃声声夜行路","商队在星光下穿越塔克拉玛干大沙漠")}
{f()}'''
artworks.append(("artwork_16_night_caravan.svg",svg))

# ── 17 佛法东传 Buddhism Spread
svg=f'''{h()}
<defs>
  <radialGradient id="dv17" cx="0.5" cy="0.3" r="0.7">
    <stop offset="0%" stop-color="#f5d06044"/><stop offset="100%" stop-color="#0a0a1500"/>
  </radialGradient>
  <linearGradient id="g17" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%" stop-color="#0a0a20"/><stop offset="100%" stop-color="#2a1a0a"/>
  </linearGradient>
</defs>
<rect width="1024" height="768" fill="url(#g17)"/>
<ellipse cx="512" cy="298" rx="302" ry="252" fill="url(#dv17)"/>
<ellipse cx="512" cy="278" rx="62" ry="77" fill="#f0d08044"/>
<circle cx="512" cy="218" r="36" fill="#f0d0a0"/>
<circle cx="512" cy="196" r="16" fill="#d4b870"/>
<circle cx="512" cy="186" r="9" fill="#c8a860"/>
<circle cx="512" cy="218" r="62" fill="none" stroke="#f0d06066" stroke-width="3"/>
<circle cx="512" cy="218" r="57" fill="none" stroke="#f0d06033" stroke-width="8"/>
<ellipse cx="512" cy="378" rx="122" ry="31" fill="#d4a05044"/>
<path d="M390,378 Q420,358 452,373 Q482,353 512,366 Q542,353 572,373 Q604,358 634,378" stroke="#d4a050" stroke-width="2" fill="none" opacity="0.6"/>
<path d="M463,263 Q438,318 443,378 Q478,398 512,393 Q546,398 581,378 Q586,318 561,263" fill="#ff8020" opacity="0.4"/>
<path d="M148,548 Q350,498 512,478 Q682,458 902,508" stroke="#f0d06066" stroke-width="3" fill="none" stroke-dasharray="10,8"/>
<circle cx="148" cy="548" r="13" fill="#f0a030" opacity="0.8"/>
<text x="148" y="578" text-anchor="middle" fill="#f0d08088" font-family="serif" font-size="14">印度</text>
<circle cx="512" cy="478" r="13" fill="#f0a030" opacity="0.8"/>
<text x="512" y="508" text-anchor="middle" fill="#f0d08088" font-family="serif" font-size="14">敦煌</text>
<circle cx="902" cy="508" r="13" fill="#f0a030" opacity="0.8"/>
<text x="902" y="538" text-anchor="middle" fill="#f0d08088" font-family="serif" font-size="14">长安</text>
<text x="198" y="278" fill="#f0d07044" font-size="24" transform="rotate(-15,198,278)">ॐ</text>
<text x="798" y="298" fill="#f0d07044" font-size="24" transform="rotate(10,798,298)">卍</text>
<text x="298" y="398" fill="#f0d07033" font-family="serif" font-size="18">南无阿弥陀佛</text>
{lbl(512,163,"佛法东传","公元1世纪 · 丝路精神文明")}
{ttl("佛法东传 · 精神文明的丝绸之路","佛教经丝路传入中国 深刻改变中华文明")}
{f()}'''
artworks.append(("artwork_17_buddhism.svg",svg))

# ── 18 贸易商品 Trade Goods
svg=f'''{h()}
<defs>
  <linearGradient id="g18" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%" stop-color="#f0e8d8"/><stop offset="100%" stop-color="#c8b898"/>
  </linearGradient>
  <radialGradient id="gl1" cx="0.4" cy="0.3" r="0.7">
    <stop offset="0%" stop-color="#e0f8f8"/><stop offset="40%" stop-color="#80d0d8"/><stop offset="100%" stop-color="#2080a0"/>
  </radialGradient>
  <radialGradient id="gl2" cx="0.35" cy="0.25" r="0.7">
    <stop offset="0%" stop-color="#f8f0e8"/><stop offset="40%" stop-color="#e8c080"/><stop offset="100%" stop-color="#c07820"/>
  </radialGradient>
</defs>
<rect width="1024" height="768" fill="url(#g18)"/>
<rect x="0" y="498" width="1024" height="270" fill="#8a6a40"/>
<rect x="0" y="478" width="1024" height="23" fill="#a07850"/>
<ellipse cx="198" cy="488" rx="57" ry="16" fill="#2080a088"/>
<path d="M141,488 Q136,396 157,357 Q173,327 198,317 Q223,327 240,357 Q260,396 255,488Z" fill="url(#gl1)" opacity="0.87"/>
<ellipse cx="198" cy="317" rx="31" ry="11" fill="#3a90b0" opacity="0.7"/>
<rect x="186" y="287" width="25" height="33" rx="10" fill="#5aa0c0" opacity="0.7"/>
<ellipse cx="198" cy="287" rx="15" ry="9" fill="#4a90b0" opacity="0.7"/>
<path d="M158,378 Q163,358 168,378" stroke="#f0f8ff" stroke-width="3" fill="none" opacity="0.6"/>
<ellipse cx="378" cy="478" rx="67" ry="19" fill="#c89040aa"/>
<path d="M311,478 Q304,357 337,307 Q357,272 378,262 Q399,272 419,307 Q452,357 445,478Z" fill="url(#gl2)" opacity="0.9"/>
<ellipse cx="378" cy="262" rx="33" ry="11" fill="#c89040" opacity="0.8"/>
<rect x="364" y="228" width="29" height="38" rx="12" fill="#d4a050" opacity="0.8"/>
<ellipse cx="378" cy="228" rx="17" ry="10" fill="#c89040" opacity="0.8"/>
<path d="M311,368 Q286,348 311,318" stroke="#c89040" stroke-width="9" fill="none" opacity="0.7"/>
<path d="M445,368 Q470,348 445,318" stroke="#c89040" stroke-width="9" fill="none" opacity="0.7"/>
<ellipse cx="578" cy="488" rx="62" ry="17" fill="#e8f0f888"/>
<path d="M516,488 Q511,376 536,331 Q556,291 578,281 Q600,291 620,331 Q645,376 640,488Z" fill="#f0f4f8" opacity="0.95"/>
<ellipse cx="578" cy="281" rx="36" ry="12" fill="#e8f0f8" opacity="0.9"/>
<path d="M536,398 Q558,383 578,398 Q598,383 620,398" stroke="#1848a0" stroke-width="2" fill="none" opacity="0.7"/>
<path d="M530,428 Q553,413 578,428 Q603,413 626,428" stroke="#1848a0" stroke-width="2" fill="none" opacity="0.7"/>
<circle cx="563" cy="358" r="9" fill="none" stroke="#1848a0" stroke-width="2" opacity="0.6"/>
<circle cx="593" cy="358" r="9" fill="none" stroke="#1848a0" stroke-width="2" opacity="0.6"/>
<ellipse cx="778" cy="428" rx="82" ry="23" fill="#d04050aa"/>
<rect x="698" y="318" width="162" height="112" fill="#d04050" opacity="0.85"/>
<ellipse cx="778" cy="318" rx="82" ry="23" fill="#e05060"/>
<path d="M728,358 Q758,338 788,358 Q758,378 728,358Z" stroke="#f0d080" stroke-width="1.5" fill="none" opacity="0.7"/>
<ellipse cx="918" cy="488" rx="52" ry="16" fill="#c84010aa"/>
<path d="M866,488 Q866,437 918,422 Q970,437 970,488Z" fill="#d04820" opacity="0.9"/>
<ellipse cx="918" cy="422" rx="32" ry="11" fill="#c84010"/>
<text x="918" y="419" text-anchor="middle" fill="#fff8e0" font-size="11">香料</text>
<text x="198" y="548" text-anchor="middle" fill="#e8d8c0" font-family="serif" font-size="13">罗马玻璃</text>
<text x="378" y="548" text-anchor="middle" fill="#e8d8c0" font-family="serif" font-size="13">双耳瓶</text>
<text x="578" y="548" text-anchor="middle" fill="#e8d8c0" font-family="serif" font-size="13">青花瓷</text>
<text x="778" y="548" text-anchor="middle" fill="#e8d8c0" font-family="serif" font-size="13">丝绸</text>
<text x="918" y="548" text-anchor="middle" fill="#e8d8c0" font-family="serif" font-size="13">东方香料</text>
{lbl(512,178,"丝路贸易商品","玻璃·瓷器·丝绸·香料")}
{ttl("丝路珍品 · 东西方价值交换","丝绸换玻璃 瓷器换香料 跨越万里")}
{f()}'''
artworks.append(("artwork_18_trade_goods.svg",svg))

# ── 19 印度洋航线 Indian Ocean
svg=f'''{h()}
<defs>
  <linearGradient id="g19" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%" stop-color="#0a1a3a"/><stop offset="60%" stop-color="#1a4a7a"/><stop offset="100%" stop-color="#2a6a9a"/>
  </linearGradient>
  <linearGradient id="sea19" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%" stop-color="#1a5080"/><stop offset="100%" stop-color="#0a2a50"/>
  </linearGradient>
</defs>
<rect width="1024" height="768" fill="url(#g19)"/>
<circle cx="100" cy="78" r="2" fill="white" opacity="0.9"/>
<circle cx="250" cy="48" r="1.5" fill="white" opacity="0.7"/>
<circle cx="450" cy="73" r="2" fill="white" opacity="0.8"/>
<circle cx="650" cy="43" r="1.5" fill="white" opacity="0.6"/>
<circle cx="850" cy="63" r="2" fill="white" opacity="0.9"/>
<ellipse cx="778" cy="98" rx="42" ry="40" fill="none" stroke="#f0e090" stroke-width="2"/>
<circle cx="793" cy="90" r="33" fill="#0a1a3a"/>
<rect x="0" y="278" width="1024" height="490" fill="url(#sea19)"/>
<path d="M0,318 Q80,298 160,313 Q240,296 320,310 Q400,293 480,308 Q560,291 640,306 Q720,289 800,304 Q880,287 1024,300" stroke="#3a80b0" stroke-width="2" fill="none" opacity="0.7"/>
<path d="M0,358 Q100,340 200,354 Q300,336 400,350 Q500,333 600,347 Q700,330 800,344 Q900,328 1024,340" stroke="#3a80b0" stroke-width="1.5" fill="none" opacity="0.5"/>
<path d="M0,398 Q120,380 240,394 Q360,376 480,390 Q600,372 720,386 Q840,368 1024,380" stroke="#3a80b0" stroke-width="1.5" fill="none" opacity="0.4"/>
<path d="M348,318 Q450,293 552,308 Q530,358 428,356 Q368,353 348,318Z" fill="#3a2010"/>
<rect x="436" y="248" width="6" height="77" fill="#3a2010"/>
<path d="M441,250 Q532,283 441,318" fill="#d4b060" opacity="0.9"/>
<path d="M678,338 Q752,320 823,331 Q811,366 740,364 Q690,361 678,338Z" fill="#2a1808" opacity="0.8"/>
<rect x="737" y="293" width="4" height="53" fill="#2a1808" opacity="0.8"/>
<path d="M740,295 L803,316 L740,334" fill="#c0a050" opacity="0.7"/>
<circle cx="178" cy="498" r="62" fill="none" stroke="#f0d06044" stroke-width="1"/>
<path d="M178,443 L178,553" stroke="#f0d060" stroke-width="2" opacity="0.6"/>
<path d="M123,498 L233,498" stroke="#f0d060" stroke-width="2" opacity="0.6"/>
<path d="M138,458 L218,538" stroke="#f0d060" stroke-width="1" opacity="0.4"/>
<path d="M218,458 L138,538" stroke="#f0d060" stroke-width="1" opacity="0.4"/>
<text x="178" y="436" text-anchor="middle" fill="#f0d060" font-size="13" opacity="0.7">N</text>
<path d="M598,178 Q680,198 762,183 Q832,193 903,178" stroke="#f0d06066" stroke-width="2" fill="none" stroke-dasharray="5,5"/>
<text x="752" y="168" fill="#f0d060" font-family="serif" font-size="14" opacity="0.7">季风航线</text>
{lbl(512,293,"印度洋 · Indian Ocean","海上丝路 · 季风贸易路线")}
{ttl("印度洋 · 季风海上丝绸之路","阿拉伯商人与中国船队往来的贸易大洋")}
{f()}'''
artworks.append(("artwork_19_indian_ocean.svg",svg))

# ── 20 茶马古道 Tea Horse Road
svg=f'''{h()}
<defs>
  <linearGradient id="g20" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%" stop-color="#1a3a2a"/><stop offset="40%" stop-color="#2a5a4a"/><stop offset="70%" stop-color="#4a8a6a"/><stop offset="100%" stop-color="#8ab0a0"/>
  </linearGradient>
</defs>
<rect width="1024" height="768" fill="url(#g20)"/>
<path d="M0,298 Q150,198 300,258 Q450,158 600,238 Q750,158 900,218 Q960,193 1024,213 L1024,498 L0,498Z" fill="#3a5a3a" opacity="0.7"/>
<path d="M150,258 Q200,196 250,258" fill="white" opacity="0.7"/>
<path d="M550,238 Q600,158 650,238" fill="white" opacity="0.78"/>
<path d="M850,218 Q900,158 950,218" fill="white" opacity="0.7"/>
<path d="M0,348 Q200,268 400,318 Q600,248 800,298 Q900,268 1024,283 L1024,498 L0,498Z" fill="#4a6a4a" opacity="0.6"/>
<rect x="0" y="308" width="1024" height="18" fill="#a0c8b8" opacity="0.22"/>
<rect x="0" y="358" width="1024" height="14" fill="#a0c8b8" opacity="0.18"/>
<path d="M0,548 Q150,518 300,538 Q450,508 550,528 Q650,503 800,518 Q900,506 1024,513" stroke="#6a5030" stroke-width="8" fill="none"/>
<path d="M0,548 Q150,518 300,538 Q450,508 550,528 Q650,503 800,518 Q900,506 1024,513" stroke="#8a7050" stroke-width="4" fill="none" stroke-dasharray="15,8"/>
<g transform="translate(278,506)"><circle cx="0" cy="-55" r="13" fill="#3a2010"/><rect x="-7" y="-42" width="15" height="38" rx="4" fill="#4a2a10"/><rect x="-5" y="-4" width="11" height="28" rx="3" fill="#3a2010"/><rect x="-21" y="-55" width="19" height="52" rx="4" fill="#6a4820" stroke="#4a3010" stroke-width="1"/><path d="M-21,-55 L-8,-65 L3,-55" stroke="#4a3010" stroke-width="2" fill="#7a5830"/></g>
<g transform="translate(448,513)"><circle cx="0" cy="-51" r="11" fill="#2a1808"/><rect x="-6" y="-40" width="13" height="36" rx="4" fill="#3a2010"/><rect x="-5" y="-4" width="10" height="26" rx="3" fill="#2a1808"/><rect x="-19" y="-51" width="18" height="47" rx="4" fill="#6a4820" stroke="#4a3010" stroke-width="1"/><path d="M-19,-51 L-7,-61 L2,-51" stroke="#4a3010" stroke-width="2" fill="#7a5830"/></g>
<g transform="translate(648,508) scale(0.78)"><ellipse cx="0" cy="0" rx="38" ry="19" fill="#4a3010"/><ellipse cx="-20" cy="-16" rx="10" ry="15" fill="#4a3010"/><ellipse cx="-24" cy="-30" rx="6" ry="9" fill="#4a3010"/><ellipse cx="6" cy="-10" rx="5" ry="11" fill="#3a2808"/><ellipse cx="16" cy="-5" rx="5" ry="11" fill="#3a2808"/><ellipse cx="26" cy="0" rx="5" ry="11" fill="#3a2808"/><ellipse cx="36" cy="5" rx="5" ry="11" fill="#3a2808"/><rect x="-12" y="-35" width="28" height="22" rx="3" fill="#8a6030"/></g>
<circle cx="148" cy="488" r="31" fill="#2a5a20" opacity="0.8"/>
<circle cx="128" cy="503" r="23" fill="#3a6a28" opacity="0.8"/>
<circle cx="168" cy="498" r="26" fill="#2a5a20" opacity="0.8"/>
<rect x="143" y="508" width="11" height="31" fill="#3a2010"/>
<path d="M848,428 Q858,408 868,428 Q878,408 888,428 Q898,408 908,428 Q918,408 928,428 Q938,408 948,428" stroke="#8a6020" stroke-width="2" fill="none"/>
<rect x="849" y="408" width="19" height="19" fill="#c02020" opacity="0.7"/>
<rect x="869" y="408" width="19" height="19" fill="#f0c020" opacity="0.7"/>
<rect x="889" y="408" width="19" height="19" fill="#f0f0f0" opacity="0.7"/>
<rect x="909" y="408" width="19" height="19" fill="#2060c0" opacity="0.7"/>
<rect x="929" y="408" width="19" height="19" fill="#20a020" opacity="0.7"/>
{lbl(512,348,"茶马古道 · Tea Horse Road","云南普洱茶 → 西藏")}
{ttl("茶马古道 · 另一条丝绸之路","普洱茶与战马的千年贸易 穿越横断山脉")}
{f()}'''
artworks.append(("artwork_20_tea_horse_road.svg",svg))

# Write all
for name, content in artworks:
    path = os.path.join(OUTPUT_DIR, name)
    with open(path, "w", encoding="utf-8") as fp:
        fp.write(content)
    size = os.path.getsize(path)
    print("OK " + name + "  " + str(size//1024) + "KB")

print("Part 1 done: " + str(len(artworks)) + " artworks")
