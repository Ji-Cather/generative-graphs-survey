import re

md_file = 'readme.md'
toc_title = '## Table of Content\n\n'

def slugify(text):
    # 生成锚点格式
    text = text.strip().lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'\s+', '-', text)
    return text

with open(md_file, 'r', encoding='utf-8') as f:
    lines = f.readlines()

toc = []
for line in lines:
    m = re.match(r'^(#{1,6})\s+(.*)', line)
    if m:
        level = len(m.group(1))
        title = m.group(2).strip()
        if title.lower() == 'table of content':
            continue
        anchor = slugify(title)
        indent = '  ' * (level - 1)
        toc.append(f"{indent}- [{title}](#{anchor})\n")

# 查找原有目录并移除
start = 0
for i, line in enumerate(lines):
    if re.match(r'#\s+Table of Content', line):
        start = i + 1
        while start < len(lines) and lines[start].strip():
            start += 1
        break

new_lines = [toc_title] + toc + ['\n'] + lines[start if start else 0:]

with open(md_file, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("目录已自动生成并插入到readme.md顶部。")