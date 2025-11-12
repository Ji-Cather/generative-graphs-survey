import csv
from collections import defaultdict

# 定义类别顺序
category_order = [
    "statistical-based simulation",
    "AR",
    "VAE",
    "GAN",
    "diffusion",
    "flow",
    "llm-based simulation"
]

# 读取CSV
with open('model_tree.csv', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    models = [row for row in reader]

# 分类
categories = defaultdict(list)
for m in models:
    cat = m['generative modeling'].strip()
    if cat:
        categories[cat].append(m)

# 按时间排序
for cat in categories:
    categories[cat].sort(key=lambda x: int(x['year']) if x['year'].isdigit() else 0)

# 生成Markdown
md = []
for cat in category_order:
    if cat in categories:
        md.append(f"## {cat}\n")
        for m in categories[cat]:
            year = m['year']
            journal = m['journal']
            title = m['title']
            url = m['url']
            cite = m['cite_name']
            md.append(f"- **({journal} {year}) {title} [{cite}]({url})**\n")
        md.append('\n')

# 写入Markdown到文件
with open('readme.md', 'w', encoding='utf-8') as fout:
    fout.write(''.join(md))