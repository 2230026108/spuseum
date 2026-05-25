"""Fix duplicate opacity attributes in 2 SVG files"""
import re

FILES = ["artwork_23_astronomy", "artwork_30_cultural_fusion"]
BASE = r"c:\Users\19741\WorkBuddy\20260523165257\Spuseum-main\public\images\artwork"

for name in FILES:
    path = f"{BASE}/{name}.svg"
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Remove duplicate opacity within same tag: keep first, drop second
    # Pattern: opacity="X" ... opacity="Y" (within same tag, i.e. no > between them)
    fixed = re.sub(
        r'(opacity="[^"]*")([^>]*?)( opacity="[^"]*")',
        r'\1\2',
        content
    )

    if fixed != content:
        with open(path, "w", encoding="utf-8") as f:
            f.write(fixed)
        print(f"Fixed: {name}.svg")
    else:
        print(f"No change: {name}.svg")
