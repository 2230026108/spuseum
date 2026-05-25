"""Generate Silk Road artwork SVGs #21-#37 for museum walls.
#21-#30: More physical Silk Road scenes
#31-#37: Digital Silk Road & modern tech
"""
import os
OUTPUT_DIR = "public/images/artwork"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def h(w=1024,hh=768): return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {hh}" width="{w}" height="{hh}">'
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

artworks=[]

# ── 21 蒙古草原 Mongol Steppe - Pax Mongolica
svg=f'''{h()}
<defs>
  <linearGradient id="g21" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%" stop-color="#1a2a10"/><stop offset="50%" stop-color="#3a5a20"/><stop offset="100%" stop-color="#6a8a50"/>
  </linearGradient>
</defs>
<rect width="1024" height="768" fill="url(#g21)"/>
<path d="M0,428 Q200,398 400,418 Q600,393 800,413 Q900,398 1024,408 L1024,768 L0,768Z" fill="#4a6a30"/>
<path d="M0,498 Q300,466 600,483 Q800,460 1024,473 L1024,768 L0,768Z" fill="#3a5a28"/>
<path d="M0,568 Q250,540 500,556 Q750,530 1024,546 L1024,768 L0,768Z" fill="#2a4a20"/>
<path d="M100,426 Q105,413 110,423" stroke="#5a8030" stroke-width="2" fill="none"/>
<path d="M280,418 Q285,405 290,415" stroke="#5a8030" stroke-width="2" fill="none"/>
<path d="M550,410 Q555,397 560,407" stroke="#5a8030" stroke-width="2" fill="none"/>
<path d="M750,416 Q755,403 760,413" stroke="#5a8030" stroke-width="2" fill="none"/>
<path d="M900,408 Q905,395 910,405" stroke="#5a8030" stroke-width="2" fill="none"/>
<ellipse cx="512" cy="388" rx="122" ry="41" fill="#d4c090"/>
<path d="M390,388 Q430,313 512,303 Q594,313 634,388Z" fill="#e8d0a0"/>
<rect x="462" y="355" width="52" height="35" fill="#2a1a08"/>
<circle cx="512" cy="328" r="9" fill="#c84020"/>
<path d="M418,373 Q466,358 512,368 Q558,358 606,373" stroke="#c84020" stroke-width="2" fill="none" opacity="0.6"/>
<ellipse cx="278" cy="413" rx="72" ry="26" fill="#c8b880"/>
<path d="M206,413 Q240,361 278,352 Q316,361 350,413Z" fill="#d4c490"/>
<ellipse cx="742" cy="408" rx="72" ry="26" fill="#c8b880"/>
<path d="M670,408 Q704,356 742,347 Q780,356 814,408Z" fill="#d4c490"/>
<g transform="translate(148,488) scale(0.68)"><ellipse cx="0" cy="0" rx="38" ry="20" fill="#3a2a10"/><ellipse cx="-18" cy="-16" rx="10" ry="15" fill="#3a2a10"/><ellipse cx="-22" cy="-31" rx="6" ry="10" fill="#3a2a10"/><ellipse cx="6" cy="-10" rx="5" ry="11" fill="#2a1a08"/><ellipse cx="15" cy="-5" rx="5" ry="11" fill="#2a1a08"/><ellipse cx="24" cy="0" rx="5" ry="11" fill="#2a1a08"/><ellipse cx="33" cy="5" rx="5" ry="11" fill="#2a1a08"/></g>
<g transform="translate(258,478) scale(0.62)"><ellipse cx="0" cy="0" rx="36" ry="19" fill="#4a3a18"/><ellipse cx="-17" cy="-15" rx="9" ry="14" fill="#4a3a18"/><ellipse cx="-21" cy="-29" rx="6" ry="9" fill="#4a3a18"/><ellipse cx="5" cy="-9" rx="5" ry="11" fill="#3a2a10"/><ellipse cx="14" cy="-4" rx="5" ry="11" fill="#3a2a10"/><ellipse cx="23" cy="1" rx="5" ry="11" fill="#3a2a10"/></g>
<g transform="translate(820,483) scale(0.65)"><ellipse cx="0" cy="0" rx="37" ry="19" fill="#3a2a10"/><ellipse cx="-17" cy="-15" rx="9" ry="14" fill="#3a2a10"/><ellipse cx="-21" cy="-29" rx="6" ry="9" fill="#3a2a10"/><ellipse cx="5" cy="-9" rx="5" ry="11" fill="#2a1a08"/><ellipse cx="14" cy="-4" rx="5" ry="11" fill="#2a1a08"/><ellipse cx="23" cy="1" rx="5" ry="11" fill="#2a1a08"/></g>
{lbl(512,368,"蒙古草原 · Mongol Steppe","蒙古帝国 · 最后的丝路繁荣时代")}
{ttl("蒙古草原 · 帕克斯蒙古利亚","蒙古帝国保障了丝路的最后一次大繁荣")}
{f()}'''
artworks.append(("artwork_21_mongol_steppe.svg",svg))

# ── 22 敦煌壁画 Dunhuang Murals
svg=f'''{h()}
<defs>
  <radialGradient id="g22" cx="0.5" cy="0.5" r="0.7">
    <stop offset="0%" stop-color="#2a1a0a"/><stop offset="100%" stop-color="#0a0a18"/>
  </radialGradient>
  <linearGradient id="ag22" x1="0.5" y1="0" x2="0.5" y2="1">
    <stop offset="0%" stop-color="#f5d090" stop-opacity="0.6"/><stop offset="100%" stop-color="#f5d090" stop-opacity="0"/>
  </linearGradient>
</defs>
<rect width="1024" height="768" fill="url(#g22)"/>
<rect x="0" y="0" width="1024" height="768" fill="#1a0e05" opacity="0.7"/>
<ellipse cx="380" cy="348" rx="123" ry="163" fill="url(#ag22)"/>
<ellipse cx="640" cy="348" rx="123" ry="163" fill="url(#ag22)"/>
<g transform="translate(380,318)">
  <ellipse cx="0" cy="0" rx="42" ry="52" fill="#d4a05088"/>
  <ellipse cx="0" cy="-16" rx="19" ry="23" fill="#f5e0c0"/>
  <path d="M-32,-6 Q-52,-32 -37,-47" stroke="#f5d09088" stroke-width="2" fill="none"/>
  <path d="M32,-6 Q52,-32 37,-47" stroke="#f5d09088" stroke-width="2" fill="none"/>
  <path d="M-22,22 Q-42,52 -27,67" stroke="#f0c87088" stroke-width="2" fill="none"/>
  <path d="M22,22 Q42,52 27,67" stroke="#f0c87088" stroke-width="2" fill="none"/>
  <ellipse cx="0" cy="0" rx="16" ry="21" fill="#ffe8c0" opacity="0.5"/>
  <ellipse cx="0" cy="-42" rx="9" ry="7" fill="#fff0d0cc"/>
</g>
<g transform="translate(640,338)">
  <ellipse cx="0" cy="0" rx="40" ry="50" fill="#c8984088"/>
  <ellipse cx="0" cy="-13" rx="17" ry="21" fill="#f0d8b0"/>
  <path d="M-30,-4 Q-47,-30 -34,-42" stroke="#f0c87088" stroke-width="2" fill="none"/>
  <path d="M30,-4 Q47,-30 34,-42" stroke="#f0c87088" stroke-width="2" fill="none"/>
  <ellipse cx="0" cy="0" rx="15" ry="19" fill="#ffe0b0" opacity="0.5"/>
  <ellipse cx="0" cy="-37" rx="8" ry="6" fill="#fff0d0cc"/>
</g>
<text x="198" y="178" fill="#f5d09088" font-family="serif" font-size="19" transform="rotate(-15,198,178)">飞天伎乐</text>
<text x="748" y="198" fill="#f5d09088" font-family="serif" font-size="19" transform="rotate(12,748,198)">梵音缭绕</text>
<path d="M298,548 Q350,528 402,543 Q452,523 502,538 Q552,518 602,533 Q652,523 702,543" stroke="#d4a05044" stroke-width="1" fill="none"/>
<path d="M318,568 Q380,553 440,563 Q500,548 560,560 Q620,546 680,558" stroke="#c8984844" stroke-width="1" fill="none"/>
<rect x="248" y="558" width="528" height="42" rx="5" fill="#1a0a0544"/>
<text x="512" y="586" text-anchor="middle" fill="#f5d090cc" font-family="serif" font-size="23">敦煌壁画 · 飞天菩萨</text>
{lbl(512,198,"敦煌壁画艺术","公元4-14世纪 · 佛教艺术瑰宝")}
{ttl("敦煌莫高窟 · 飞天壁画","东西方文化与宗教融合的艺术巅峰")}
{f()}'''
artworks.append(("artwork_22_dunhuang_murals.svg",svg))

# ── 23 古代天文 / 星象导航 Ancient Astronomy
svg=f'''{h()}
<defs>
  <radialGradient id="g23" cx="0.5" cy="0.4" r="0.8">
    <stop offset="0%" stop-color="#0a1030"/><stop offset="100%" stop-color="#000008"/>
  </radialGradient>
</defs>
<rect width="1024" height="768" fill="url(#g23)"/>
<circle cx="80" cy="55" r="1.8" fill="white" opacity="0.9"/>
<circle cx="150" cy="85" r="1.5" fill="white" opacity="0.7"/>
<circle cx="220" cy="40" r="2" fill="white" opacity="0.8"/>
<circle cx="310" cy="75" r="1.5" fill="white" opacity="0.6"/>
<circle cx="390" cy="28" r="2.5" fill="white" opacity="0.95"/>
<circle cx="450" cy="62" r="1.5" fill="white" opacity="0.7"/>
<circle cx="510" cy="18" r="2" fill="white" opacity="0.8"/>
<circle cx="570" cy="50" r="1.5" fill="white" opacity="0.6"/>
<circle cx="640" cy="35" r="2" fill="white" opacity="0.9"/>
<circle cx="710" cy="70" r="1.5" fill="white" opacity="0.7"/>
<circle cx="790" cy="45" r="2.5" fill="white" opacity="0.95"/>
<circle cx="860" cy="80" r="1.5" fill="white" opacity="0.7"/>
<circle cx="930" cy="30" r="2" fill="white" opacity="0.8"/>
<circle cx="985" cy="60" r="1.5" fill="white" opacity="0.6"/>
<circle cx="120" cy="140" r="1.5" fill="white" opacity="0.5"/>
<circle cx="280" cy="160" r="1.5" fill="white" opacity="0.6"/>
<circle cx="480" cy="120" r="1.5" fill="white" opacity="0.5"/>
<circle cx="680" cy="150" r="1.5" fill="white" opacity="0.6"/>
<circle cx="880" cy="130" r="1.5" fill="white" opacity="0.5"/>
<path d="M0,198 Q200,148 400,178 Q600,138 800,158 Q900,143 1024,168" stroke="white" stroke-width="22" fill="none" opacity="0.05"/>
<circle cx="512" cy="280" r="180" fill="none" stroke="#d4a04033" stroke-width="1"/>
<circle cx="512" cy="280" r="140" fill="none" stroke="#d4a04022" stroke-width="1"/>
<circle cx="512" cy="280" r="100" fill="none" stroke="#d4a04022" stroke-width="1"/>
<path d="M512,100 L512,460" stroke="#d4a04033" stroke-width="1"/>
<path d="M332,280 L692,280" stroke="#d4a04033" stroke-width="1"/>
<path d="M385,153 L639,407" stroke="#d4a04022" stroke-width="1"/>
<path d="M639,153 L385,407" stroke="#d4a04022" stroke-width="1"/>
<circle cx="512" cy="280" r="8" fill="#f0d060" opacity="0.9"/>
<circle cx="200" cy="95" r="5" fill="#f0d060" opacity="0.8"/>
<circle cx="300" cy="155" r="4" fill="#d0c060" opacity="0.8"/>
<circle cx="390" cy="200" r="4" fill="#d0c060" opacity="0.8"/>
<circle cx="720" cy="82" r="5" fill="#f0d060" opacity="0.8"/>
<circle cx="620" cy="155" r="4" fill="#d0c060" opacity="0.8"/>
<path d="M200,95 L300,155 L390,200 L512,280" stroke="#f0d06088" stroke-width="1.5" fill="none" stroke-dasharray="5,4"/>
<path d="M720,82 L620,155 L512,280" stroke="#f0d06088" stroke-width="1.5" fill="none" stroke-dasharray="5,4"/>
<text x="185" y="75" fill="#f0d060" font-family="serif" font-size="12" opacity="0.7">北极星</text>
<text x="712" y="63" fill="#f0d060" font-family="serif" font-size="12" opacity="0.7">北斗七星</text>
<circle cx="512" cy="590" r="90" fill="#c89030" opacity="0.15" stroke="#c89030" stroke-width="2" opacity="0.4"/>
<rect x="478" y="555" width="68" height="80" rx="5" fill="#d4a030" opacity="0.2" stroke="#d4a030" stroke-width="1"/>
<circle cx="512" cy="565" r="18" fill="none" stroke="#d4a030" stroke-width="1.5" opacity="0.6"/>
<path d="M494,572 L530,572" stroke="#d4a030" stroke-width="1.5" opacity="0.6"/>
<path d="M512,555 L512,590" stroke="#d4a030" stroke-width="1.5" opacity="0.6"/>
<text x="512" y="648" text-anchor="middle" fill="#d4a030" font-family="serif" font-size="12" opacity="0.6">星盘导航</text>
<text x="512" y="445" text-anchor="middle" fill="#f0d06099" font-family="serif" font-size="16">以星辰指引方向</text>
{lbl(512,190,"古代星象导航","中国·阿拉伯·希腊天文学")}
{ttl("古代天文 · 星辰指引商路","中国与阿拉伯天文学共同支撑丝路导航")}
{f()}'''
artworks.append(("artwork_23_astronomy.svg",svg))

# ── 24 唐代长安国际都市 Tang Cosmopolitan City
svg=f'''{h()}
<defs>
  <linearGradient id="g24" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%" stop-color="#2a1a4a"/><stop offset="50%" stop-color="#5a3a8a"/><stop offset="100%" stop-color="#9a7ac0"/>
  </linearGradient>
</defs>
<rect width="1024" height="768" fill="url(#g24)"/>
<rect x="0" y="558" width="1024" height="210" fill="#5a4020"/>
<rect x="0" y="538" width="1024" height="23" fill="#6a5030"/>
<rect x="48" y="298" width="160" height="260" fill="#d4a040" stroke="#a07820" stroke-width="2"/>
<polygon points="48,298 128,218 208,298" fill="#8b3a10" stroke="#5a2a08" stroke-width="2"/>
<polygon points="68,298 128,232 188,298" fill="#a84a18"/>
<rect x="88" y="368" width="80" height="70" fill="#2a1a08" opacity="0.8"/>
<rect x="48" y="298" width="160" height="12" fill="#c89030" opacity="0.7"/>
<rect x="48" y="370" width="160" height="10" fill="#c89030" opacity="0.7"/>
<rect x="48" y="430" width="160" height="10" fill="#c89030" opacity="0.7"/>
<rect x="348" y="228" width="328" height="328" fill="#e0c080" stroke="#c0a040" stroke-width="3"/>
<polygon points="330,228 512,128 694,228" fill="#9a4010" stroke="#6a2a08" stroke-width="2"/>
<polygon points="360,228 512,148 664,228" fill="#b85018"/>
<rect x="456" y="388" width="112" height="100" fill="#2a1808" opacity="0.8"/>
<rect x="348" y="238" width="328" height="14" fill="#d4a030" opacity="0.7"/>
<rect x="348" y="328" width="328" height="12" fill="#d4a030" opacity="0.7"/>
<rect x="348" y="428" width="328" height="12" fill="#d4a030" opacity="0.7"/>
<circle cx="508" cy="185" r="10" fill="#f0d060"/>
<circle cx="516" cy="185" r="10" fill="#f0d060"/>
<rect x="814" y="318" width="162" height="242" fill="#c8a050" stroke="#a07830" stroke-width="2"/>
<polygon points="814,318 895,248 976,318" fill="#8b3a10" stroke="#5a2a08" stroke-width="2"/>
<rect x="834" y="378" width="122" height="70" fill="#2a1808" opacity="0.8"/>
<rect x="814" y="328" width="162" height="10" fill="#c89030" opacity="0.6"/>
<g transform="translate(148,548) scale(0.72)"><circle cx="0" cy="-52" r="11" fill="#2a1a08"/><rect x="-6" y="-41" width="13" height="36" rx="4" fill="#3a2010"/><rect x="-5" y="-5" width="10" height="26" rx="3" fill="#2a1a08"/></g>
<g transform="translate(500,552) scale(0.72)"><circle cx="0" cy="-52" r="11" fill="#6a4020"/><rect x="-6" y="-41" width="13" height="36" rx="4" fill="#7a5030"/></g>
<g transform="translate(700,545) scale(0.72)"><circle cx="0" cy="-52" r="11" fill="#3a2810"/><rect x="-6" y="-41" width="13" height="36" rx="4" fill="#4a3020"/></g>
<text x="280" y="528" fill="#f0d08066" font-family="serif" font-size="13">东市 · 西市</text>
<text x="620" y="520" fill="#f0d08066" font-family="serif" font-size="13">万国来朝</text>
{lbl(512,228,"唐代长安 · Tang Chang-an","世界最繁华城市 百万人口")}
{ttl("唐代长安 · 盛唐万国来朝","来自72个国家的商人·使节聚集于此")}
{f()}'''
artworks.append(("artwork_24_tang_capital.svg",svg))

# ── 25 亚历山大港 Alexandria
svg=f'''{h()}
<defs>
  <linearGradient id="g25" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%" stop-color="#1a3a6a"/><stop offset="60%" stop-color="#4a7ab0"/><stop offset="100%" stop-color="#8ab8d0"/>
  </linearGradient>
  <linearGradient id="sea25" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%" stop-color="#1a5090"/><stop offset="100%" stop-color="#0a2a60"/>
  </linearGradient>
</defs>
<rect width="1024" height="768" fill="url(#g25)"/>
<rect x="0" y="368" width="1024" height="400" fill="url(#sea25)"/>
<path d="M0,388 Q100,368 200,382 Q300,362 400,376 Q500,356 600,370 Q700,352 800,366 Q900,348 1024,360" stroke="#4a90d0" stroke-width="2" fill="none" opacity="0.6"/>
<path d="M0,418 Q150,398 300,412 Q450,392 600,406 Q750,388 900,402 Q970,392 1024,396" stroke="#4a90d0" stroke-width="1.5" fill="none" opacity="0.5"/>
<path d="M0,288 Q200,248 400,268 Q600,238 800,258 Q900,248 1024,258 L1024,368 L0,368Z" fill="#8a7040"/>
<path d="M0,348 Q200,328 400,338 Q600,318 800,328 Q900,318 1024,322 L1024,368 L0,368Z" fill="#a08050"/>
<rect x="468" y="78" width="88" height="292" fill="#d4c070" stroke="#b0a040" stroke-width="3"/>
<rect x="458" y="60" width="108" height="22" fill="#c8b060"/>
<rect x="448" y="42" width="128" height="22" fill="#d4c070"/>
<rect x="438" y="24" width="148" height="22" fill="#c8b060"/>
<rect x="442" y="0" width="140" height="28" fill="#d4c070"/>
<ellipse cx="512" cy="0" rx="70" ry="14" fill="#c8b060" opacity="0.7"/>
<path d="M480,0 Q512,-15 544,0" fill="none" stroke="#f0d060" stroke-width="2" opacity="0.6"/>
<circle cx="512" cy="-8" r="12" fill="#f0d060" opacity="0.9"/>
<circle cx="512" cy="-8" r="38" fill="none" stroke="#f0d06044" stroke-width="8"/>
<path d="M468,368 Q300,388 200,378 Q100,368 50,372" stroke="#c8b060" stroke-width="6" fill="none" opacity="0.6"/>
<path d="M556,368 Q700,388 820,378 Q920,368 970,372" stroke="#c8b060" stroke-width="6" fill="none" opacity="0.6"/>
<path d="M148,408 Q220,386 292,398 Q282,438 210,435 Q158,432 148,408Z" fill="#3a2010"/>
<rect x="208" y="366" width="4" height="48" fill="#2a1808"/>
<path d="M211,368 Q253,380 211,394" fill="#c8a040" opacity="0.8"/>
<path d="M668,402 Q740,380 812,392 Q802,432 730,429 Q678,426 668,402Z" fill="#3a2010"/>
<rect x="728" y="360" width="4" height="48" fill="#2a1808"/>
<path d="M731,362 Q773,374 731,388" fill="#c8a040" opacity="0.8"/>
{lbl(512,170,"亚历山大港 · Alexandria","古代世界第一灯塔 · 希腊化文明")}
{ttl("亚历山大港 · 古代世界的知识中心","法罗斯灯塔 · 大图书馆 · 东西方文明汇聚")}
{f()}'''
artworks.append(("artwork_25_alexandria.svg",svg))

# ── 26 古罗马市场 Roman Forum
svg=f'''{h()}
<defs>
  <linearGradient id="g26" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%" stop-color="#b8d0e8"/><stop offset="60%" stop-color="#e8dcc8"/><stop offset="100%" stop-color="#d4c8a8"/>
  </linearGradient>
</defs>
<rect width="1024" height="768" fill="url(#g26)"/>
<rect x="0" y="548" width="1024" height="220" fill="#c4b090"/>
<rect x="0" y="528" width="1024" height="22" fill="#d4c0a0"/>
<rect x="68" y="298" width="180" height="258" fill="#e8d8b0" stroke="#b8a870" stroke-width="2"/>
<g fill="#e8d8b0" stroke="#a09060" stroke-width="1">
  <rect x="68" y="268" width="16" height="32"/>
  <rect x="100" y="268" width="16" height="32"/>
  <rect x="132" y="268" width="16" height="32"/>
  <rect x="164" y="268" width="16" height="32"/>
  <rect x="196" y="268" width="16" height="32"/>
  <rect x="228" y="268" width="16" height="32"/>
</g>
<rect x="60" y="258" width="196" height="12" fill="#d4c490" stroke="#a09060" stroke-width="1"/>
<rect x="56" y="246" width="204" height="14" fill="#c8b880" stroke="#a09060" stroke-width="1"/>
<polygon points="56,246 158,188 260,246" fill="#c0a840" stroke="#908030" stroke-width="2"/>
<rect x="338" y="238" width="348" height="318" fill="#f0e0c0" stroke="#c0b080" stroke-width="2"/>
<g fill="#f0e0c0" stroke="#b0a070" stroke-width="1">
  <rect x="338" y="200" width="20" height="40"/>
  <rect x="380" y="200" width="20" height="40"/>
  <rect x="422" y="200" width="20" height="40"/>
  <rect x="464" y="200" width="20" height="40"/>
  <rect x="506" y="200" width="20" height="40"/>
  <rect x="548" y="200" width="20" height="40"/>
  <rect x="590" y="200" width="20" height="40"/>
  <rect x="632" y="200" width="20" height="40"/>
  <rect x="666" y="200" width="20" height="40"/>
</g>
<rect x="328" y="190" width="368" height="14" fill="#e0d0a0" stroke="#b0a070" stroke-width="1"/>
<rect x="320" y="176" width="384" height="16" fill="#d0c090" stroke="#a09060" stroke-width="1"/>
<polygon points="320,176 512,98 704,176" fill="#c8b840" stroke="#988020" stroke-width="2"/>
<rect x="446" y="318" width="132" height="82" fill="#2a1808" opacity="0.7"/>
<rect x="778" y="318" width="178" height="238" fill="#e8d8b0" stroke="#b8a870" stroke-width="2"/>
<g fill="#e8d8b0" stroke="#a09060" stroke-width="1">
  <rect x="778" y="288" width="16" height="32"/>
  <rect x="810" y="288" width="16" height="32"/>
  <rect x="842" y="288" width="16" height="32"/>
  <rect x="874" y="288" width="16" height="32"/>
  <rect x="906" y="288" width="16" height="32"/>
  <rect x="938" y="288" width="16" height="32"/>
</g>
<rect x="770" y="278" width="194" height="12" fill="#d4c490"/>
<polygon points="770,278 865,218 960,278" fill="#c0a840" stroke="#908030" stroke-width="2"/>
<circle cx="178" cy="528" r="12" fill="#2a1808"/>
<rect x="170" y="540" width="16" height="38" rx="5" fill="#2a1808"/>
<circle cx="498" cy="528" r="12" fill="#3a2a18"/>
<rect x="490" y="540" width="16" height="38" rx="5" fill="#3a2a18"/>
<circle cx="718" cy="525" r="12" fill="#2a1808"/>
<rect x="710" y="537" width="16" height="38" rx="5" fill="#2a1808"/>
{lbl(512,218,"古罗马 · Ancient Rome","丝路终点 · 大理石之城")}
{ttl("古罗马 · 丝路西端终点","皇帝奥古斯都禁止进口丝绸 因为太贵了")}
{f()}'''
artworks.append(("artwork_26_ancient_rome.svg",svg))

# ── 27 张骞出使 Zhang Qian's Mission
svg=f'''{h()}
<defs>
  <linearGradient id="g27" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%" stop-color="#1a2a4a"/><stop offset="50%" stop-color="#3a5a8a"/><stop offset="100%" stop-color="#6a8ab0"/>
  </linearGradient>
</defs>
<rect width="1024" height="768" fill="url(#g27)"/>
<path d="M0,498 Q200,468 400,488 Q600,458 800,478 Q900,465 1024,472 L1024,768 L0,768Z" fill="#8a7040"/>
<path d="M0,558 Q300,528 600,548 Q800,520 1024,538 L1024,768 L0,768Z" fill="#7a6030"/>
<path d="M0,628 Q300,598 600,618 Q800,590 1024,608 L1024,768 L0,768Z" fill="#6a5020"/>
<path d="M100,498 Q300,450 512,468 Q700,448 900,460" stroke="#a0904077" stroke-width="4" fill="none"/>
<text x="512" y="455" text-anchor="middle" fill="#f0d08066" font-family="serif" font-size="14">向西行进的路途</text>
<circle cx="145" cy="498" r="12" fill="#d4a050" opacity="0.8"/>
<text x="145" y="530" text-anchor="middle" fill="#f0d08088" font-family="serif" font-size="12">长安</text>
<circle cx="390" cy="478" r="10" fill="#d4a050" opacity="0.7"/>
<text x="390" y="510" text-anchor="middle" fill="#f0d08077" font-family="serif" font-size="11">河西走廊</text>
<circle cx="588" cy="468" r="10" fill="#d4a050" opacity="0.7"/>
<text x="588" y="500" text-anchor="middle" fill="#f0d08077" font-family="serif" font-size="11">大宛</text>
<circle cx="808" cy="460" r="10" fill="#d4a050" opacity="0.7"/>
<text x="808" y="492" text-anchor="middle" fill="#f0d08077" font-family="serif" font-size="11">大月氏</text>
<g transform="translate(512,418)">
  <circle cx="0" cy="-70" r="18" fill="#d4a080"/>
  <rect x="-10" y="-52" width="20" height="48" rx="5" fill="#d44020"/>
  <rect x="-8" y="0" width="16" height="38" rx="4" fill="#a03010"/>
  <rect x="-50" y="-35" width="48" height="8" rx="3" fill="#6a4820"/>
  <circle cx="-50" cy="-31" r="5" fill="#c8a030"/>
</g>
<g transform="translate(412,428)">
  <circle cx="0" cy="-60" r="15" fill="#c8906a"/>
  <rect x="-8" y="-45" width="18" height="42" rx="4" fill="#8a3010"/>
  <rect x="-7" y="-3" width="14" height="32" rx="3" fill="#6a2808"/>
</g>
<g transform="translate(612,422)">
  <circle cx="0" cy="-62" r="15" fill="#d4a080"/>
  <rect x="-8" y="-47" width="18" height="44" rx="4" fill="#d03020"/>
  <rect x="-7" y="-3" width="14" height="34" rx="3" fill="#a02010"/>
</g>
<rect x="300" y="250" width="424" height="158" rx="8" fill="#1a1a2ecc" stroke="#f0d06055" stroke-width="2"/>
<text x="512" y="290" text-anchor="middle" fill="#f0d78c" font-family="serif" font-size="20" font-weight="bold">张骞出使西域</text>
<text x="512" y="318" text-anchor="middle" fill="#f0d08099" font-family="serif" font-size="14">公元前138年 汉武帝派遣张骞</text>
<text x="512" y="340" text-anchor="middle" fill="#f0d08099" font-family="serif" font-size="14">出使大月氏 寻求军事同盟</text>
<text x="512" y="368" text-anchor="middle" fill="#f0d080bb" font-family="serif" font-size="14">历时十三年 带回西域信息</text>
<text x="512" y="392" text-anchor="middle" fill="#d4a06099" font-family="serif" font-size="13">正式开辟了丝绸之路</text>
{lbl(512,248,"张骞出使 · Zhang Qian","公元前138年 · 丝路奠基之旅")}
{ttl("张骞出使西域 · 丝路开辟","凿空西域 开启了中西方文明交流的大门")}
{f()}'''
artworks.append(("artwork_27_zhang_qian.svg",svg))

# ── 28 丝路全程地图 Full Silk Road Map
svg=f'''{h()}
<defs>
  <linearGradient id="g28" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%" stop-color="#0a1a3a"/><stop offset="100%" stop-color="#1a3060"/>
  </linearGradient>
  <filter id="gf28">
    <feGaussianBlur stdDeviation="3" result="blur"/>
    <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
  </filter>
</defs>
<rect width="1024" height="768" fill="url(#g28)"/>
<rect x="38" y="118" width="948" height="555" rx="5" fill="#0d1a2a" stroke="#f0c87033" stroke-width="1"/>
<text x="512" y="108" text-anchor="middle" fill="#f0d78c" font-family="serif" font-size="18" opacity="0.6">SILK ROAD · 丝绸之路 · 全程路线图</text>
<path d="M95,305 Q190,290 285,295 Q380,282 470,288 Q565,278 635,295 Q705,285 775,302 Q845,298 915,308" stroke="#f0c870bb" stroke-width="3" fill="none" stroke-dasharray="8,4" filter="url(#gf28)"/>
<path d="M285,295 Q310,320 330,338 Q355,358 390,368 Q430,375 470,368 Q510,362 545,368 Q575,375 610,368 Q650,358 685,368 Q725,378 775,368 Q820,358 860,368 Q900,378 940,368" stroke="#f0c87077" stroke-width="2" fill="none" stroke-dasharray="5,6"/>
<circle cx="95" cy="305" r="7" fill="#f0d060" filter="url(#gf28)"/>
<text x="95" y="293" text-anchor="middle" fill="#f0d060" font-family="serif" font-size="12">长安</text>
<circle cx="285" cy="295" r="6" fill="#e0c050"/>
<text x="285" y="283" text-anchor="middle" fill="#e0c050" font-family="serif" font-size="11">敦煌</text>
<circle cx="380" cy="282" r="5" fill="#d0b040"/>
<text x="380" y="270" text-anchor="middle" fill="#d0b040" font-family="serif" font-size="11">喀什</text>
<circle cx="470" cy="288" r="5" fill="#d0b040"/>
<text x="470" y="276" text-anchor="middle" fill="#d0b040" font-family="serif" font-size="11">撒马尔罕</text>
<circle cx="635" cy="295" r="5" fill="#d0b040"/>
<text x="635" y="283" text-anchor="middle" fill="#d0b040" font-family="serif" font-size="11">波斯</text>
<circle cx="775" cy="302" r="6" fill="#e0c050"/>
<text x="775" y="290" text-anchor="middle" fill="#e0c050" font-family="serif" font-size="11">巴格达</text>
<circle cx="915" cy="308" r="7" fill="#f0d060" filter="url(#gf28)"/>
<text x="915" y="296" text-anchor="middle" fill="#f0d060" font-family="serif" font-size="12">罗马</text>
<path d="M95,305 Q150,350 200,368 Q250,388 310,418 Q370,448 420,468 Q470,488 540,508 Q600,525 660,518 Q720,508 770,518 Q820,528 870,538 Q910,545 940,548" stroke="#80c8f0aa" stroke-width="2.5" fill="none" stroke-dasharray="6,5"/>
<circle cx="150" cy="430" r="4" fill="#80c8f0"/>
<text x="150" y="448" text-anchor="middle" fill="#80c8f0" font-family="serif" font-size="10">广州</text>
<circle cx="310" cy="450" r="4" fill="#80c8f0"/>
<text x="310" y="465" text-anchor="middle" fill="#80c8f0" font-family="serif" font-size="10">马六甲</text>
<circle cx="520" cy="505" r="4" fill="#80c8f0"/>
<text x="520" y="520" text-anchor="middle" fill="#80c8f0" font-family="serif" font-size="10">印度洋</text>
<circle cx="800" cy="520" r="4" fill="#80c8f0"/>
<text x="800" y="535" text-anchor="middle" fill="#80c8f0" font-family="serif" font-size="10">波斯湾</text>
<rect x="68" y="618" width="200" height="38" rx="4" fill="#0a1a2a88" stroke="#f0c87055" stroke-width="1"/>
<line x1="78" y1="632" x2="118" y2="632" stroke="#f0c870" stroke-width="2" stroke-dasharray="5,3"/>
<text x="128" y="636" fill="#f0d080" font-family="serif" font-size="12">陆上丝绸之路</text>
<rect x="68" y="660" width="200" height="38" rx="4" fill="#0a1a2a88" stroke="#80c8f055" stroke-width="1"/>
<line x1="78" y1="674" x2="118" y2="674" stroke="#80c8f0" stroke-width="2" stroke-dasharray="5,3"/>
<text x="128" y="678" fill="#80c8f0" font-family="serif" font-size="12">海上丝绸之路</text>
{lbl(512,145,"丝绸之路 · 全程路线图","")}
{ttl("丝绸之路全图 · 陆路与海路","横贯亚欧大陆 连接东西方文明的贸易走廊")}
{f()}'''
artworks.append(("artwork_28_full_map.svg",svg))

# ── 29 马可波罗 Marco Polo
svg=f'''{h()}
<defs>
  <linearGradient id="g29" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%" stop-color="#1a1a3a"/><stop offset="50%" stop-color="#2a3a6a"/><stop offset="100%" stop-color="#5a5a9a"/>
  </linearGradient>
</defs>
<rect width="1024" height="768" fill="url(#g29)"/>
<circle cx="88" cy="68" r="2" fill="white" opacity="0.8"/>
<circle cx="200" cy="48" r="1.5" fill="white" opacity="0.6"/>
<circle cx="400" cy="75" r="2" fill="white" opacity="0.9"/>
<circle cx="600" cy="42" r="1.5" fill="white" opacity="0.7"/>
<circle cx="780" cy="60" r="2" fill="white" opacity="0.8"/>
<circle cx="920" cy="85" r="1.5" fill="white" opacity="0.6"/>
<rect x="0" y="498" width="1024" height="270" fill="#4a3a28"/>
<rect x="0" y="478" width="1024" height="22" fill="#5a4a38"/>
<rect x="108" y="228" width="808" height="268" rx="6" fill="#1a1820cc" stroke="#d4a04066" stroke-width="1"/>
<circle cx="512" cy="498" r="140" fill="#1a3050aa"/>
<path d="M100,498 Q250,455 512,478 Q750,455 924,498" stroke="#f0d06099" stroke-width="2.5" fill="none" stroke-dasharray="8,5"/>
<circle cx="100" cy="498" r="10" fill="#d4a050" opacity="0.8"/>
<text x="100" y="528" text-anchor="middle" fill="#f0d08088" font-family="serif" font-size="13">威尼斯</text>
<circle cx="320" cy="470" r="8" fill="#c8a040" opacity="0.7"/>
<text x="320" y="492" text-anchor="middle" fill="#f0d08066" font-family="serif" font-size="11">君士坦丁堡</text>
<circle cx="512" cy="465" r="8" fill="#c8a040" opacity="0.7"/>
<text x="512" y="487" text-anchor="middle" fill="#f0d08066" font-family="serif" font-size="11">波斯</text>
<circle cx="720" cy="472" r="8" fill="#c8a040" opacity="0.7"/>
<text x="720" y="494" text-anchor="middle" fill="#f0d08066" font-family="serif" font-size="11">忽必烈大汗</text>
<circle cx="924" cy="498" r="10" fill="#d4a050" opacity="0.8"/>
<text x="924" y="528" text-anchor="middle" fill="#f0d08088" font-family="serif" font-size="13">元大都</text>
<text x="512" y="270" text-anchor="middle" fill="#f0d78c" font-family="serif" font-size="28" font-weight="bold">马可·波罗游记</text>
<text x="512" y="305" text-anchor="middle" fill="#f0d08099" font-family="serif" font-size="15">MILIONE · IL DIVISAMENT DOU MONDE</text>
<rect x="248" y="325" width="528" height="130" rx="5" fill="#0a0a1a88" stroke="#d4a04044" stroke-width="1"/>
<text x="512" y="355" text-anchor="middle" fill="#f0d08099" font-family="serif" font-size="14">1271年 17岁的马可·波罗随父出发</text>
<text x="512" y="378" text-anchor="middle" fill="#f0d08099" font-family="serif" font-size="14">历经3年半 抵达元大都</text>
<text x="512" y="401" text-anchor="middle" fill="#f0d08099" font-family="serif" font-size="14">服务忽必烈大汗17年</text>
<text x="512" y="424" text-anchor="middle" fill="#d4a060bb" font-family="serif" font-size="13">其游记让欧洲人第一次真正认识中国</text>
{lbl(512,255,"马可·波罗 · Marco Polo","1271-1295 · 威尼斯旅行家")}
{ttl("马可·波罗 · 打开东西方之窗","其游记激发了欧洲探索东方的热情")}
{f()}'''
artworks.append(("artwork_29_marco_polo.svg",svg))

# ── 30 丝路文化融合 Cultural Fusion
svg=f'''{h()}
<defs>
  <radialGradient id="g30" cx="0.5" cy="0.5" r="0.7">
    <stop offset="0%" stop-color="#1a1838"/><stop offset="100%" stop-color="#080810"/>
  </radialGradient>
</defs>
<rect width="1024" height="768" fill="url(#g30)"/>
<circle cx="512" cy="338" r="198" fill="none" stroke="#f0d06033" stroke-width="2"/>
<circle cx="512" cy="338" r="148" fill="none" stroke="#f0d06022" stroke-width="1"/>
<circle cx="318" cy="338" r="148" fill="#c04020" opacity="0.12" stroke="#c04020" stroke-width="1.5" opacity="0.4"/>
<circle cx="706" cy="338" r="148" fill="#2060a0" opacity="0.12" stroke="#2060a0" stroke-width="1.5" opacity="0.4"/>
<circle cx="512" cy="168" r="148" fill="#20a040" opacity="0.12" stroke="#20a040" stroke-width="1.5" opacity="0.4"/>
<text x="248" y="328" text-anchor="middle" fill="#c04020" font-family="serif" font-size="16" opacity="0.8">中华文明</text>
<text x="248" y="348" text-anchor="middle" fill="#c04020" font-family="serif" font-size="13" opacity="0.7">汉字·丝绸·茶·瓷器</text>
<text x="768" y="328" text-anchor="middle" fill="#2060a0" font-family="serif" font-size="16" opacity="0.8">欧洲文明</text>
<text x="768" y="348" text-anchor="middle" fill="#2060a0" font-family="serif" font-size="13" opacity="0.7">玻璃·黄金·法律</text>
<text x="512" y="128" text-anchor="middle" fill="#20a040" font-family="serif" font-size="16" opacity="0.8">伊斯兰文明</text>
<text x="512" y="148" text-anchor="middle" fill="#20a040" font-family="serif" font-size="13" opacity="0.7">数学·天文·医学</text>
<circle cx="512" cy="338" r="58" fill="#f0d060" opacity="0.15" stroke="#f0d060" stroke-width="2"/>
<text x="512" y="333" text-anchor="middle" fill="#f0d060" font-family="serif" font-size="15" font-weight="bold">丝绸之路</text>
<text x="512" y="353" text-anchor="middle" fill="#f0d060" font-family="serif" font-size="11">文明交汇点</text>
<path d="M364,338 Q388,328 430,338" stroke="#f0d060" stroke-width="2" fill="none" opacity="0.5"/>
<path d="M594,338 Q636,328 660,338" stroke="#f0d060" stroke-width="2" fill="none" opacity="0.5"/>
<path d="M512,280 Q522,258 512,240" stroke="#f0d060" stroke-width="2" fill="none" opacity="0.5"/>
<rect x="168" y="548" width="688" height="125" rx="6" fill="#0a0a1ecc" stroke="#f0d06044" stroke-width="1"/>
<text x="512" y="582" text-anchor="middle" fill="#f0d78c" font-family="serif" font-size="17" font-weight="bold">丝绸之路上的文明交流</text>
<text x="512" y="608" text-anchor="middle" fill="#f0d08099" font-family="serif" font-size="13">佛教 · 基督教 · 伊斯兰教 沿路传播</text>
<text x="512" y="628" text-anchor="middle" fill="#f0d08099" font-family="serif" font-size="13">造纸术 · 印刷术 · 火药 · 指南针 向西传递</text>
<text x="512" y="648" text-anchor="middle" fill="#f0d08099" font-family="serif" font-size="13">玻璃制造 · 织毯技艺 · 葡萄酿酒 向东传递</text>
{lbl(512,278,"文明大融合","三大文明圈的碰撞与交流")}
{ttl("丝路文明交融 · 人类共同遗产","没有任何一条道路比丝绸之路改变了更多文明")}
{f()}'''
artworks.append(("artwork_30_cultural_fusion.svg",svg))

# ════════════════════════════════════════════
# #31-#37 数字丝绸之路 Digital Silk Road
# ════════════════════════════════════════════

# ── 31 一带一路倡议 Belt and Road Initiative
svg=f'''{h()}
<defs>
  <linearGradient id="g31" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%" stop-color="#040410"/><stop offset="100%" stop-color="#080820"/>
  </linearGradient>
  <filter id="glow31">
    <feGaussianBlur stdDeviation="4" result="blur"/>
    <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
  </filter>
</defs>
<rect width="1024" height="768" fill="url(#g31)"/>
<rect x="38" y="78" width="948" height="545" rx="4" fill="#060818" stroke="#f0c87022" stroke-width="1"/>
<circle cx="120" cy="305" r="7" fill="#e8c040" filter="url(#glow31)"/>
<circle cx="310" cy="278" r="6" fill="#e0b830"/>
<circle cx="455" cy="268" r="6" fill="#e0b830"/>
<circle cx="565" cy="278" r="6" fill="#e0b830"/>
<circle cx="688" cy="268" r="6" fill="#e0b830"/>
<circle cx="818" cy="278" r="7" fill="#e8c040" filter="url(#glow31)"/>
<circle cx="938" cy="295" r="7" fill="#e8c040" filter="url(#glow31)"/>
<path d="M120,305 Q200,285 310,278 Q380,272 455,268 Q510,264 565,278 Q625,285 688,268 Q750,255 818,278 Q875,290 938,295" stroke="#f0c870cc" stroke-width="3" fill="none" stroke-dasharray="0" filter="url(#glow31)"/>
<text x="120" y="323" text-anchor="middle" fill="#e8c040" font-family="serif" font-size="11">北京</text>
<text x="310" y="296" text-anchor="middle" fill="#d0a830" font-family="serif" font-size="11">中亚</text>
<text x="455" y="286" text-anchor="middle" fill="#d0a830" font-family="serif" font-size="11">伊朗</text>
<text x="688" y="286" text-anchor="middle" fill="#d0a830" font-family="serif" font-size="11">土耳其</text>
<text x="818" y="296" text-anchor="middle" fill="#d0a830" font-family="serif" font-size="11">欧洲</text>
<path d="M120,305 Q200,370 280,420 Q350,465 420,488 Q500,508 580,518 Q660,525 740,518 Q820,508 900,498" stroke="#4090d0cc" stroke-width="2.5" fill="none" stroke-dasharray="0" filter="url(#glow31)"/>
<circle cx="280" cy="420" r="5" fill="#4090d0"/>
<text x="280" y="440" text-anchor="middle" fill="#4090d0" font-family="serif" font-size="11">东南亚</text>
<circle cx="500" cy="510" r="5" fill="#4090d0"/>
<text x="500" y="528" text-anchor="middle" fill="#4090d0" font-family="serif" font-size="11">印度洋</text>
<circle cx="730" cy="518" r="5" fill="#4090d0"/>
<text x="730" y="536" text-anchor="middle" fill="#4090d0" font-family="serif" font-size="11">非洲</text>
<rect x="178" y="600" width="668" height="88" rx="5" fill="#080818cc" stroke="#f0c87055" stroke-width="1"/>
<text x="512" y="632" text-anchor="middle" fill="#f0d78c" font-family="serif" font-size="18" font-weight="bold">一带一路倡议</text>
<text x="512" y="656" text-anchor="middle" fill="#d0a83099" font-family="serif" font-size="13">Belt and Road Initiative · 2013</text>
<text x="512" y="676" text-anchor="middle" fill="#c8a02088" font-family="serif" font-size="12">连接140+国家 · 古丝路的现代延伸</text>
{lbl(512,148,"一带一路 · BRI","2013 · 习近平提出 · 140+国家")}
{ttl("一带一路 · 21世纪丝绸之路","古代商路的现代复兴 连接亚欧非大陆")}
{f()}'''
artworks.append(("artwork_31_belt_road.svg",svg))

# ── 32 海底光缆 Undersea Internet Cables
svg=f'''{h()}
<defs>
  <linearGradient id="g32" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%" stop-color="#020212"/><stop offset="100%" stop-color="#040820"/>
  </linearGradient>
  <filter id="glow32"><feGaussianBlur stdDeviation="5" result="blur"/><feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
</defs>
<rect width="1024" height="768" fill="url(#g32)"/>
<rect x="0" y="280" width="1024" height="488" fill="#0a1a30" opacity="0.85"/>
<path d="M0,320 Q200,308 400,318 Q600,305 800,315 Q900,308 1024,312" stroke="#2a5080" stroke-width="2" fill="none" opacity="0.5"/>
<path d="M0,380 Q250,368 500,378 Q750,365 1024,372" stroke="#2a5080" stroke-width="1.5" fill="none" opacity="0.4"/>
<path d="M0,450 Q300,438 600,448 Q800,435 1024,442" stroke="#2a5080" stroke-width="1.5" fill="none" opacity="0.35"/>
<path d="M120,280 Q200,380 260,450 Q320,520 350,580 Q380,638 400,700" stroke="#20d080" stroke-width="2.5" fill="none" filter="url(#glow32)" opacity="0.8"/>
<path d="M120,280 Q250,310 400,320 Q550,330 680,338 Q800,348 920,338" stroke="#20d080" stroke-width="2.5" fill="none" filter="url(#glow32)" opacity="0.8"/>
<path d="M400,320 Q420,380 430,440 Q440,500 450,560" stroke="#20d080" stroke-width="2" fill="none" filter="url(#glow32)" opacity="0.6"/>
<path d="M680,338 Q700,390 710,448 Q720,508 730,558" stroke="#20d080" stroke-width="2" fill="none" filter="url(#glow32)" opacity="0.6"/>
<path d="M900,260 Q860,310 840,380 Q820,450 800,520" stroke="#20a0e0" stroke-width="2" fill="none" filter="url(#glow32)" opacity="0.7"/>
<path d="M900,260 Q940,310 960,380 Q980,450 990,520" stroke="#20a0e0" stroke-width="2" fill="none" filter="url(#glow32)" opacity="0.7"/>
<circle cx="120" cy="280" r="12" fill="#20d080" filter="url(#glow32)" opacity="0.9"/>
<circle cx="900" cy="260" r="12" fill="#20a0e0" filter="url(#glow32)" opacity="0.9"/>
<circle cx="400" cy="320" r="8" fill="#20d080" opacity="0.7"/>
<circle cx="680" cy="338" r="8" fill="#20d080" opacity="0.7"/>
<text x="120" y="263" text-anchor="middle" fill="#20d080" font-family="serif" font-size="13">上海</text>
<text x="900" y="243" text-anchor="middle" fill="#20a0e0" font-family="serif" font-size="13">伦敦</text>
<text x="400" y="305" text-anchor="middle" fill="#20d080" font-family="serif" font-size="11">新加坡</text>
<text x="680" y="323" text-anchor="middle" fill="#20d080" font-family="serif" font-size="11">迪拜</text>
<rect x="248" y="135" width="528" height="110" rx="6" fill="#040820cc" stroke="#20d08055" stroke-width="1"/>
<text x="512" y="170" text-anchor="middle" fill="#20d080" font-family="serif" font-size="18" font-weight="bold">海底光缆网络</text>
<text x="512" y="196" text-anchor="middle" fill="#20d08099" font-family="serif" font-size="13">全球430+条海底光缆</text>
<text x="512" y="218" text-anchor="middle" fill="#20d08099" font-family="serif" font-size="13">承载99%的国际互联网流量</text>
<text x="512" y="238" text-anchor="middle" fill="#1890c888" font-family="serif" font-size="12">现代海上丝绸之路的数字版本</text>
{lbl(512,148,"海底光缆 · Undersea Cables","数字信息的现代海上丝路")}
{ttl("海底光缆 · 数字信息的丝绸之路","承载全球互联网流量的海底神经网络")}
{f()}'''
artworks.append(("artwork_32_undersea_cables.svg",svg))

# ── 33 全球电商 Global E-Commerce
svg=f'''{h()}
<defs>
  <linearGradient id="g33" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0%" stop-color="#060818"/><stop offset="100%" stop-color="#0a1028"/>
  </linearGradient>
  <filter id="glow33"><feGaussianBlur stdDeviation="5" result="blur"/><feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
</defs>
<rect width="1024" height="768" fill="url(#g33)"/>
<circle cx="512" cy="338" r="198" fill="none" stroke="#2040a022" stroke-width="1"/>
<circle cx="512" cy="338" r="258" fill="none" stroke="#2040a015" stroke-width="1"/>
<circle cx="512" cy="338" r="288" fill="none" stroke="#2040a010" stroke-width="1"/>
<circle cx="200" cy="248" r="38" fill="#203060" opacity="0.6" stroke="#3060a0" stroke-width="1.5"/>
<text x="200" y="244" text-anchor="middle" fill="#6090d0" font-size="20">🛒</text>
<text x="200" y="262" text-anchor="middle" fill="#6090d0" font-family="serif" font-size="11">阿里巴巴</text>
<circle cx="780" cy="218" r="38" fill="#203060" opacity="0.6" stroke="#3060a0" stroke-width="1.5"/>
<text x="780" y="214" text-anchor="middle" fill="#6090d0" font-size="20">📦</text>
<text x="780" y="232" text-anchor="middle" fill="#6090d0" font-family="serif" font-size="11">Amazon</text>
<circle cx="148" cy="488" r="33" fill="#203060" opacity="0.6" stroke="#3060a0" stroke-width="1.5"/>
<text x="148" y="484" text-anchor="middle" fill="#6090d0" font-size="18">📱</text>
<text x="148" y="500" text-anchor="middle" fill="#6090d0" font-family="serif" font-size="10">移动支付</text>
<circle cx="868" cy="458" r="33" fill="#203060" opacity="0.6" stroke="#3060a0" stroke-width="1.5"/>
<text x="868" y="454" text-anchor="middle" fill="#6090d0" font-size="18">🚀</text>
<text x="868" y="470" text-anchor="middle" fill="#6090d0" font-family="serif" font-size="10">跨境物流</text>
<circle cx="388" cy="558" r="33" fill="#203060" opacity="0.6" stroke="#3060a0" stroke-width="1.5"/>
<text x="388" y="554" text-anchor="middle" fill="#6090d0" font-size="18">🌐</text>
<text x="388" y="570" text-anchor="middle" fill="#6090d0" font-family="serif" font-size="10">数字货币</text>
<circle cx="688" cy="548" r="33" fill="#203060" opacity="0.6" stroke="#3060a0" stroke-width="1.5"/>
<text x="688" y="544" text-anchor="middle" fill="#6090d0" font-size="18">📊</text>
<text x="688" y="560" text-anchor="middle" fill="#6090d0" font-family="serif" font-size="10">大数据贸易</text>
<path d="M238,248 Q350,285 480,338" stroke="#3060a066" stroke-width="2" fill="none" filter="url(#glow33)"/>
<path d="M742,218 Q640,278 548,338" stroke="#3060a066" stroke-width="2" fill="none" filter="url(#glow33)"/>
<path d="M178,488 Q310,428 476,338" stroke="#3060a066" stroke-width="2" fill="none" filter="url(#glow33)"/>
<path d="M835,458 Q710,408 548,338" stroke="#3060a066" stroke-width="2" fill="none" filter="url(#glow33)"/>
<path d="M420,555 Q464,448 512,338" stroke="#3060a066" stroke-width="2" fill="none" filter="url(#glow33)"/>
<path d="M655,548 Q588,448 512,338" stroke="#3060a066" stroke-width="2" fill="none" filter="url(#glow33)"/>
<circle cx="512" cy="338" r="48" fill="#1a2850" stroke="#4070c0" stroke-width="2"/>
<text x="512" y="333" text-anchor="middle" fill="#6090d0" font-size="26">🛍️</text>
<text x="512" y="355" text-anchor="middle" fill="#6090d0" font-family="serif" font-size="11">全球电商</text>
{lbl(512,148,"全球电商 · Global E-Commerce","数字丝绸之路 · 年交易额8万亿美元")}
{ttl("全球电商 · 数字化贸易革命","商队变成物流无人机 集市变成直播间")}
{f()}'''
artworks.append(("artwork_33_ecommerce.svg",svg))

# ── 34 5G与AI 5G and AI
svg=f'''{h()}
<defs>
  <radialGradient id="g34" cx="0.5" cy="0.5" r="0.8">
    <stop offset="0%" stop-color="#0a0a25"/><stop offset="100%" stop-color="#020210"/>
  </radialGradient>
  <filter id="glow34"><feGaussianBlur stdDeviation="6" result="blur"/><feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
</defs>
<rect width="1024" height="768" fill="url(#g34)"/>
<circle cx="512" cy="338" r="188" fill="none" stroke="#6020e044" stroke-width="2" filter="url(#glow34)"/>
<circle cx="512" cy="338" r="148" fill="none" stroke="#6020e033" stroke-width="1.5"/>
<circle cx="512" cy="338" r="108" fill="none" stroke="#6020e022" stroke-width="1"/>
<circle cx="512" cy="338" r="68" fill="none" stroke="#6020e022" stroke-width="1"/>
<circle cx="512" cy="338" r="28" fill="#4010c0" opacity="0.6" filter="url(#glow34)"/>
<text x="512" y="344" text-anchor="middle" fill="#c0a0f0" font-family="serif" font-size="13" font-weight="bold">AI</text>
<circle cx="512" cy="148" r="20" fill="#8030d0" opacity="0.8" filter="url(#glow34)"/>
<text x="512" y="154" text-anchor="middle" fill="#c0a0f0" font-size="11">大模型</text>
<circle cx="690" cy="218" r="20" fill="#8030d0" opacity="0.8" filter="url(#glow34)"/>
<text x="690" y="224" text-anchor="middle" fill="#c0a0f0" font-size="11">5G</text>
<circle cx="700" cy="448" r="20" fill="#8030d0" opacity="0.8" filter="url(#glow34)"/>
<text x="700" y="454" text-anchor="middle" fill="#c0a0f0" font-size="11">算力</text>
<circle cx="512" cy="518" r="20" fill="#8030d0" opacity="0.8" filter="url(#glow34)"/>
<text x="512" y="524" text-anchor="middle" fill="#c0a0f0" font-size="11">区块链</text>
<circle cx="322" cy="448" r="20" fill="#8030d0" opacity="0.8" filter="url(#glow34)"/>
<text x="322" y="454" text-anchor="middle" fill="#c0a0f0" font-size="11">云计算</text>
<circle cx="332" cy="218" r="20" fill="#8030d0" opacity="0.8" filter="url(#glow34)"/>
<text x="332" y="224" text-anchor="middle" fill="#c0a0f0" font-size="11">IoT</text>
<path d="M512,162 L512,310" stroke="#8030d066" stroke-width="2" fill="none" filter="url(#glow34)"/>
<path d="M676,230 L548,310" stroke="#8030d066" stroke-width="2" fill="none" filter="url(#glow34)"/>
<path d="M684,440 L548,366" stroke="#8030d066" stroke-width="2" fill="none" filter="url(#glow34)"/>
<path d="M512,504 L512,366" stroke="#8030d066" stroke-width="2" fill="none" filter="url(#glow34)"/>
<path d="M334,440 L476,366" stroke="#8030d066" stroke-width="2" fill="none" filter="url(#glow34)"/>
<path d="M346,230 L476,310" stroke="#8030d066" stroke-width="2" fill="none" filter="url(#glow34)"/>
<rect x="168" y="608" width="688" height="95" rx="6" fill="#06060ecc" stroke="#8030d055" stroke-width="1"/>
<text x="512" y="640" text-anchor="middle" fill="#c0a0f0" font-family="serif" font-size="18" font-weight="bold">5G · AI · 数字文明基础设施</text>
<text x="512" y="665" text-anchor="middle" fill="#a080d099" font-family="serif" font-size="13">如同汉代修建的驿站与烽火台</text>
<text x="512" y="688" text-anchor="middle" fill="#a080d099" font-family="serif" font-size="13">支撑着新时代的文明连接</text>
{lbl(512,155,"5G · AI · 数字文明","现代丝路的信息基础设施")}
{ttl("5G与人工智能 · 数字文明的基石","技术连接代替驼队 算法代替地图导航")}
{f()}'''
artworks.append(("artwork_34_5g_ai.svg",svg))

# ── 35 数字文化遗产 Digital Cultural Heritage
svg=f'''{h()}
<defs>
  <radialGradient id="g35" cx="0.5" cy="0.4" r="0.8">
    <stop offset="0%" stop-color="#0a1520"/><stop offset="100%" stop-color="#040810"/>
  </radialGradient>
  <filter id="glow35"><feGaussianBlur stdDeviation="5" result="blur"/><feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
</defs>
<rect width="1024" height="768" fill="url(#g35)"/>
<rect x="58" y="168" width="908" height="508" rx="8" fill="#080e18" stroke="#2a5080" stroke-width="1"/>
<rect x="78" y="188" width="428" height="468" rx="5" fill="#0a1520"/>
<rect x="78" y="188" width="428" height="468" rx="5" fill="none" stroke="#2a4060" stroke-width="1"/>
<ellipse cx="292" cy="328" rx="148" ry="198" fill="#c89040" opacity="0.08"/>
<g transform="translate(292,298)">
  <ellipse cx="0" cy="0" rx="58" ry="72" fill="#d4a05022"/>
  <circle cx="0" cy="-20" r="32" fill="#f0d0a0" opacity="0.7"/>
  <circle cx="0" cy="-20" r="62" fill="none" stroke="#f0d06055" stroke-width="2"/>
  <path d="M-48,-8 Q-68,-35 -55,-52" stroke="#f5d09055" stroke-width="2" fill="none"/>
  <path d="M48,-8 Q68,-35 55,-52" stroke="#f5d09055" stroke-width="2" fill="none"/>
</g>
<rect x="248" y="448" width="88" height="38" rx="3" fill="#0a1a2a" stroke="#2a50803" stroke-width="1"/>
<path d="M248,448 Q292,438 336,448" stroke="#4080c0" stroke-width="1" fill="none" opacity="0.5"/>
<path d="M248,456 Q292,446 336,456" stroke="#4080c0" stroke-width="1" fill="none" opacity="0.4"/>
<path d="M248,464 Q292,454 336,464" stroke="#4080c0" stroke-width="1" fill="none" opacity="0.3"/>
<path d="M248,472 Q292,462 336,472" stroke="#4080c0" stroke-width="1" fill="none" opacity="0.2"/>
<text x="292" y="520" text-anchor="middle" fill="#4080c0" font-family="serif" font-size="12">3D扫描重建</text>
<text x="78" y="682" text-anchor="middle" fill="#4080c099" font-family="serif" font-size="11">VR 沉浸体验</text>
<text x="428" y="682" text-anchor="middle" fill="#4080c099" font-family="serif" font-size="11">AI 色彩修复</text>
<rect x="526" y="188" width="418" height="215" rx="4" fill="#060e18"/>
<rect x="536" y="198" width="398" height="195" rx="3" fill="#080808"/>
<text x="735" y="275" text-anchor="middle" fill="#20c080" font-family="serif" font-size="14" opacity="0.7">数字敦煌项目</text>
<text x="735" y="298" text-anchor="middle" fill="#20c08099" font-family="serif" font-size="12">全球用户在线游览</text>
<rect x="546" y="218" width="55" height="35" rx="2" fill="#2a4a2a" stroke="#20c080" stroke-width="1"/>
<rect x="611" y="218" width="55" height="35" rx="2" fill="#2a4a2a" stroke="#20c080" stroke-width="1"/>
<rect x="676" y="218" width="55" height="35" rx="2" fill="#2a4a2a" stroke="#20c080" stroke-width="1"/>
<rect x="741" y="218" width="55" height="35" rx="2" fill="#2a4a2a" stroke="#20c080" stroke-width="1"/>
<rect x="806" y="218" width="55" height="35" rx="2" fill="#2a4a2a" stroke="#20c080" stroke-width="1"/>
<rect x="871" y="218" width="55" height="35" rx="2" fill="#2a4a2a" stroke="#20c080" stroke-width="1"/>
<rect x="526" y="418" width="418" height="235" rx="4" fill="#060e18"/>
<text x="735" y="455" text-anchor="middle" fill="#20a0d0" font-family="serif" font-size="14" opacity="0.7">数字文物数据库</text>
<text x="735" y="478" text-anchor="middle" fill="#20a0d099" font-family="serif" font-size="12">AI识别·分类·跨库比对</text>
<rect x="545" y="498" width="378" height="35" rx="3" fill="#0a1a2a"/>
<rect x="545" y="498" width="248" height="35" rx="3" fill="#1a4a6a" opacity="0.7"/>
<text x="735" y="520" text-anchor="middle" fill="#20a0d0" font-family="serif" font-size="11">已数字化: 65%</text>
<rect x="545" y="545" width="378" height="30" rx="3" fill="#0a1a2a"/>
<rect x="545" y="545" width="148" height="30" rx="3" fill="#1a4a6a" opacity="0.7"/>
<text x="735" y="564" text-anchor="middle" fill="#20a0d0" font-family="serif" font-size="11">全球可访问: 38%</text>
{lbl(512,155,"数字文化遗产 · Digital Heritage","VR·3D扫描·AI修复")}
{ttl("数字文化遗产 · 让历史永远可见","VR游览莫高窟 · AI修复壁画 · 3D打印文物")}
{f()}'''
artworks.append(("artwork_35_digital_heritage.svg",svg))

# ── 36 数字丝绸之路连接 Digital Connections
svg=f'''{h()}
<defs>
  <linearGradient id="g36" x1="0" y1="1" x2="1" y2="0">
    <stop offset="0%" stop-color="#020208"/><stop offset="100%" stop-color="#080820"/>
  </linearGradient>
  <filter id="glow36"><feGaussianBlur stdDeviation="5" result="blur"/><feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
</defs>
<rect width="1024" height="768" fill="url(#g36)"/>
<path d="M0,108 Q200,58 400,88 Q600,48 800,68 Q900,52 1024,62" stroke="white" stroke-width="18" fill="none" opacity="0.035"/>
<circle cx="120" cy="298" r="48" fill="#0a1830" stroke="#4080c0" stroke-width="1.5" opacity="0.8"/>
<text x="120" y="293" text-anchor="middle" fill="#6090d0" font-size="24">🏛️</text>
<text x="120" y="315" text-anchor="middle" fill="#6090d0" font-family="serif" font-size="11">传统博物馆</text>
<circle cx="120" cy="518" r="48" fill="#0a1830" stroke="#4080c0" stroke-width="1.5" opacity="0.8"/>
<text x="120" y="513" text-anchor="middle" fill="#6090d0" font-size="24">🏺</text>
<text x="120" y="535" text-anchor="middle" fill="#6090d0" font-family="serif" font-size="11">实体文物</text>
<circle cx="512" cy="198" r="52" fill="#0a1030" stroke="#8040e0" stroke-width="2" filter="url(#glow36)"/>
<text x="512" y="190" text-anchor="middle" fill="#a060e0" font-size="28">🌐</text>
<text x="512" y="218" text-anchor="middle" fill="#a060e0" font-family="serif" font-size="12" font-weight="bold">数字平台</text>
<circle cx="512" cy="468" r="52" fill="#0a1030" stroke="#8040e0" stroke-width="2" filter="url(#glow36)"/>
<text x="512" y="460" text-anchor="middle" fill="#a060e0" font-size="28">🤖</text>
<text x="512" y="488" text-anchor="middle" fill="#a060e0" font-family="serif" font-size="12" font-weight="bold">AI助手</text>
<circle cx="904" cy="298" r="48" fill="#0a1830" stroke="#40c080" stroke-width="1.5" opacity="0.8"/>
<text x="904" y="293" text-anchor="middle" fill="#40c080" font-size="24">👨‍💻</text>
<text x="904" y="315" text-anchor="middle" fill="#40c080" font-family="serif" font-size="11">全球学者</text>
<circle cx="904" cy="518" r="48" fill="#0a1830" stroke="#40c080" stroke-width="1.5" opacity="0.8"/>
<text x="904" y="513" text-anchor="middle" fill="#40c080" font-size="24">🎓</text>
<text x="904" y="535" text-anchor="middle" fill="#40c080" font-family="serif" font-size="11">公众访问</text>
<path d="M168,298 Q320,248 460,198" stroke="#6080c0" stroke-width="2" fill="none" filter="url(#glow36)" opacity="0.7"/>
<path d="M168,518 Q320,498 460,468" stroke="#6080c0" stroke-width="2" fill="none" filter="url(#glow36)" opacity="0.7"/>
<path d="M564,198 Q740,248 856,298" stroke="#6080c0" stroke-width="2" fill="none" filter="url(#glow36)" opacity="0.7"/>
<path d="M564,468 Q740,498 856,518" stroke="#6080c0" stroke-width="2" fill="none" filter="url(#glow36)" opacity="0.7"/>
<path d="M512,250 L512,416" stroke="#8040e0" stroke-width="2" fill="none" filter="url(#glow36)" opacity="0.8" stroke-dasharray="8,4"/>
<circle cx="512" cy="338" r="22" fill="#1a0840" stroke="#8040e0" stroke-width="1.5" filter="url(#glow36)"/>
<text x="512" y="344" text-anchor="middle" fill="#c0a0f0" font-family="serif" font-size="11">连接</text>
{lbl(512,155,"数字连接 · Digital Bridge","让历史跨越时空触达每个人")}
{ttl("数字平台 · 跨越时空的文明桥梁","打破地域界限 任何人都能访问人类共同遗产")}
{f()}'''
artworks.append(("artwork_36_digital_connection.svg",svg))

# ── 37 古代与数字丝路 Then & Now
svg=f'''{h()}
<defs>
  <linearGradient id="left37" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0%" stop-color="#2a1508"/><stop offset="100%" stop-color="#1a0a04"/>
  </linearGradient>
  <linearGradient id="right37" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0%" stop-color="#080818"/><stop offset="100%" stop-color="#040812"/>
  </linearGradient>
  <filter id="glow37"><feGaussianBlur stdDeviation="5" result="blur"/><feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
</defs>
<rect x="0" y="0" width="512" height="768" fill="url(#left37)"/>
<rect x="512" y="0" width="512" height="768" fill="url(#right37)"/>
<line x1="512" y1="0" x2="512" y2="768" stroke="#f0d060" stroke-width="2" opacity="0.3"/>
<text x="256" y="88" text-anchor="middle" fill="#c89040" font-family="serif" font-size="18" opacity="0.7">古代丝绸之路</text>
<text x="768" y="88" text-anchor="middle" fill="#4080c0" font-family="serif" font-size="18" opacity="0.7">数字丝绸之路</text>
<path d="M0,478 Q100,438 200,458 Q300,428 380,448 Q430,438 512,443" stroke="#c89040" stroke-width="2.5" fill="none" opacity="0.6" stroke-dasharray="8,5"/>
<circle cx="80" cy="458" r="5" fill="#c89040" opacity="0.7"/>
<circle cx="200" cy="448" r="5" fill="#c89040" opacity="0.7"/>
<circle cx="320" cy="438" r="5" fill="#c89040" opacity="0.7"/>
<g transform="translate(80,458) scale(0.55)"><ellipse cx="0" cy="0" rx="36" ry="19" fill="#8B6914" opacity="0.8"/><ellipse cx="-19" cy="-15" rx="10" ry="14" fill="#8B6914" opacity="0.8"/><ellipse cx="-23" cy="-29" rx="6" ry="9" fill="#8B6914" opacity="0.8"/><ellipse cx="5" cy="-9" rx="5" ry="10" fill="#7a5a10" opacity="0.8"/><ellipse cx="14" cy="-4" rx="5" ry="10" fill="#7a5a10" opacity="0.8"/><ellipse cx="23" cy="1" rx="5" ry="10" fill="#7a5a10" opacity="0.8"/></g>
<g transform="translate(200,448) scale(0.48)"><ellipse cx="0" cy="0" rx="34" ry="18" fill="#9B7924" opacity="0.8"/><ellipse cx="-18" cy="-14" rx="9" ry="13" fill="#9B7924" opacity="0.8"/><ellipse cx="-22" cy="-27" rx="6" ry="8" fill="#9B7924" opacity="0.8"/><ellipse cx="5" cy="-8" rx="5" ry="10" fill="#8a6820" opacity="0.8"/><ellipse cx="14" cy="-3" rx="5" ry="10" fill="#8a6820" opacity="0.8"/></g>
<path d="M512,443 Q600,428 680,438 Q760,425 840,432 Q900,428 970,435" stroke="#4080c0" stroke-width="2.5" fill="none" opacity="0.7" filter="url(#glow37)"/>
<circle cx="600" cy="435" r="5" fill="#4080c0" opacity="0.8"/>
<circle cx="720" cy="430" r="5" fill="#4080c0" opacity="0.8"/>
<circle cx="840" cy="432" r="5" fill="#4080c0" opacity="0.8"/>
<text x="600" y="418" text-anchor="middle" fill="#4080c0" font-family="serif" font-size="10">数据节点</text>
<text x="720" y="413" text-anchor="middle" fill="#4080c0" font-family="serif" font-size="10">云服务器</text>
<text x="840" y="415" text-anchor="middle" fill="#4080c0" font-family="serif" font-size="10">终端用户</text>
<rect x="38" y="168" width="440" height="245" rx="5" fill="#1a0a0488" stroke="#c8904044" stroke-width="1"/>
<text x="258" y="202" text-anchor="middle" fill="#c89040" font-family="serif" font-size="14">骆驼载货量: 200公斤</text>
<text x="258" y="228" text-anchor="middle" fill="#c89040" font-family="serif" font-size="14">长安→罗马: 约1-2年</text>
<text x="258" y="254" text-anchor="middle" fill="#c89040" font-family="serif" font-size="14">商队人数: 数百人</text>
<text x="258" y="280" text-anchor="middle" fill="#c89040" font-family="serif" font-size="14">危险: 强盗、沙漠、疾病</text>
<text x="258" y="306" text-anchor="middle" fill="#c89040" font-family="serif" font-size="14">货物: 丝绸、瓷器、香料</text>
<text x="258" y="332" text-anchor="middle" fill="#c89040" font-family="serif" font-size="14">利润率: 50倍以上</text>
<text x="258" y="390" text-anchor="middle" fill="#c89040aa" font-family="serif" font-size="17" font-weight="bold">古代</text>
<rect x="546" y="168" width="440" height="245" rx="5" fill="#04081888" stroke="#4080c044" stroke-width="1"/>
<text x="766" y="202" text-anchor="middle" fill="#4080c0" font-family="serif" font-size="14">数据传输: 太比特/秒</text>
<text x="766" y="228" text-anchor="middle" fill="#4080c0" font-family="serif" font-size="14">上海→伦敦: 0.2秒</text>
<text x="766" y="254" text-anchor="middle" fill="#4080c0" font-family="serif" font-size="14">用户数量: 50亿+人</text>
<text x="766" y="280" text-anchor="middle" fill="#4080c0" font-family="serif" font-size="14">风险: 网络攻击、数据安全</text>
<text x="766" y="306" text-anchor="middle" fill="#4080c0" font-family="serif" font-size="14">货物: 信息、文化、服务</text>
<text x="766" y="332" text-anchor="middle" fill="#4080c0" font-family="serif" font-size="14">全球贸易额: 28万亿美元</text>
<text x="766" y="390" text-anchor="middle" fill="#4080c0aa" font-family="serif" font-size="17" font-weight="bold">今天</text>
<rect x="168" y="568" width="688" height="65" rx="5" fill="#08081888" stroke="#f0d06033" stroke-width="1"/>
<text x="512" y="600" text-anchor="middle" fill="#f0d78c" font-family="serif" font-size="18" font-weight="bold">文明连接 · 从未停止</text>
<text x="512" y="622" text-anchor="middle" fill="#f0d08099" font-family="serif" font-size="13">技术在变 · 人类渴望连接的心 · 从未改变</text>
{lbl(512,148,"古代丝路 VS 数字丝路","两千年的连接进化史")}
{ttl("古代 VS 数字 · 文明连接的进化","从驼铃到光纤 连接的本质始终是人与人")}
{f()}'''
artworks.append(("artwork_37_then_and_now.svg",svg))

# Write all
for name, content in artworks:
    path = os.path.join(OUTPUT_DIR, name)
    with open(path, "w", encoding="utf-8") as fp:
        fp.write(content)
    size = os.path.getsize(path)
    print("OK " + name + "  " + str(size//1024) + "KB")

print("Part 2 done: " + str(len(artworks)) + " artworks (#21-#37)")
