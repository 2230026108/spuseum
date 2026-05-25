"""
svg2png.py — 批量将 37 张 artwork SVG 转为 PNG
试验两种方案: svglib（首选）→ cairosvg（备选）→ 手动CairoSVG
"""
import os, sys, io
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding='utf-8')
except Exception:
    pass

ARTWORK_DIR = Path(r"c:\Users\19741\WorkBuddy\20260523165257\Spuseum-main\public\images\artwork")
PNG_DIR = ARTWORK_DIR / "png512"
PNG_DIR.mkdir(exist_ok=True)

svg_files = sorted(f for f in ARTWORK_DIR.glob("artwork_??_*.svg") if
                   f.stem.split("_")[1].isdigit() and 1 <= int(f.stem.split("_")[1]) <= 37)

print(f"找到 {len(svg_files)} 个 SVG 文件")

# 方案 A: 尝试 cairosvg（最可靠）
try:
    import cairosvg
    USE_CAIRO = True
    print("使用 cairosvg 引擎")
except ImportError:
    USE_CAIRO = False
    print("cairosvg 未安装, 尝试 svglib...")

if not USE_CAIRO:
    try:
        from svglib.svglib import svg2rlg
        from reportlab.graphics import renderPM
        USE_SVGLIB = True
        print("使用 svglib + reportlab 引擎")
    except ImportError:
        import subprocess
        subprocess.check_call([sys.executable, "-m", "pip", "install", "svglib", "reportlab", "pillow", "-q"])
        from svglib.svglib import svg2rlg
        from reportlab.graphics import renderPM
        USE_SVGLIB = True
        print("使用 svglib + reportlab 引擎")

count = 0
for svg_path in svg_files:
    png_path = PNG_DIR / (svg_path.stem + ".png")
    if png_path.exists() and os.path.getsize(png_path) > 1000:
        print(f"  跳过 {svg_path.name} (已存在)")
        count += 1
        continue

    try:
        if USE_CAIRO:
            cairosvg.svg2png(url=str(svg_path), write_to=str(png_path), output_width=512, output_height=512)
        else:
            drawing = svg2rlg(str(svg_path))
            if drawing is None:
                print(f"  !! 失败 {svg_path.name}: svg2rlg 返回 None")
                continue
            pw, ph = 512, 512
            sx = pw / max(drawing.width, 1)
            sy = ph / max(drawing.height, 1)
            s = min(sx, sy, 1.0)
            if s < 1.0:
                drawing.scale(s, s)
            renderPM.drawToFile(drawing, str(png_path), fmt="PNG", dpi=72)

        size_kb = os.path.getsize(png_path) // 1024
        print(f"  OK {svg_path.name} -> {png_path.name} ({size_kb}KB)")
        count += 1
    except Exception as e:
        print(f"  !! 失败 {svg_path.name}: {e}")
        # 如果 png 已生成但是损坏的，删掉
        if png_path.exists():
            png_path.unlink()

print(f"\n完成: {count}/{len(svg_files)} 个")

