import re, xml.etree.ElementTree as ET

FILES = [
    "artwork_23_astronomy",
    "artwork_30_cultural_fusion",
]
BASE = r"c:\Users\19741\WorkBuddy\20260523165257\Spuseum-main\public\images\artwork"

for name in FILES:
    path = f"{BASE}/{name}.svg"
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # 找到重复属性（stroke-width 在标签中出现两次）
    # 策略：用正则去掉第二个重复的 stroke-width="..."
    fixed = re.sub(
        r' stroke-width="[^"]*"(?=.*stroke-width=")',
        "",
        content
    )

    if fixed != content:
        # 二次清理：如果同一个标签里还有重复
        fixed = re.sub(
            r'( stroke-width="[^"]*".*?)( stroke-width="[^"]*")',
            r'\1',
            fixed
        )
        with open(path, "w", encoding="utf-8") as f:
            f.write(fixed)
        print(f"Fixed: {name}.svg")
    else:
        # 用 XML 解析找具体行
        lines = content.split("\n")
        for i, line in enumerate(lines):
            if "stroke-width" in line:
                count = line.count("stroke-width")
                if count > 1:
                    print(f"{name} line {i+1} has {count} stroke-width: {line[:100]}")
