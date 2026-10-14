import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract script IDs
js_content = re.search(r'<script>(.*?)</script>', content, re.DOTALL)
if js_content:
    js_text = js_content.group(1)
    element_ids = set(re.findall(r"document\.getElementById\(['\"]([^'\"]+)['\"]", js_text))
    print(f"Found {len(element_ids)} IDs referenced in JS:")
    missing = []
    for eid in sorted(element_ids):
        pattern = rf'id=[\'"]{eid}[\'"]'
        if not re.search(pattern, content):
            missing.append(eid)
    if missing:
        print("MISSING IDS:", missing)
    else:
        print("SUCCESS: All JS IDs are PRESENT in HTML!")

# Check basic tags
for tag in ['html', 'head', 'body', 'main', 'footer']:
    opens = len(re.findall(r'<' + tag + r'[\s>]', content))
    closes = len(re.findall(r'</' + tag + r'>', content))
    print(f"Tag <{tag}>: {opens} opens, {closes} closes")

sections = re.findall(r'<section\s+id=[\'"]([^\'"]+)[\'"]\s+class=[\'"]([^\'"]+)[\'"]', content)
print(f"\nFound {len(sections)} sections:")
for sid, sclass in sections:
    bg = [c for c in sclass.split() if c.startswith('bg-')]
    print(f"  #{sid}: {' '.join(bg)}")
