"""Cloudinary 图片缓存版本号递增脚本"""
import re, os

base = os.path.dirname(os.path.abspath(__file__))

pages = [
    "style-cartoon.html", "style-chinese.html", "style-dark-food.html",
    "style-ecommerce.html", "style-japanese.html", "style-minimal.html",
    "style-retro.html", "style-tech.html", "styles.html"
]

# Find current version from first file
sample_path = os.path.join(base, pages[0])
with open(sample_path, 'r', encoding='utf-8') as f:
    sample = f.read()
m = re.search(r'\?v=(\d+)', sample)
current = int(m.group(1)) if m else 0
new_ver = current + 1

print(f"Bumping version: {current} → {new_ver}")

for page in pages:
    path = os.path.join(base, page)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    updated = re.sub(r'\?v=\d+', f'?v={new_ver}', content)
    if updated != content:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(updated)
        print(f"  ✓ {page}")

print(f"\nDone. All pages now use ?v={new_ver}")