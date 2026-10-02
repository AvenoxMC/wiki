#!/usr/bin/env python3
"""Embed pages/<lang>/<slug>.md in index.html for offline use."""
import glob
import json
import os
import re

pages = {
    f"{lang}/{os.path.basename(path)[:-3]}": open(path, encoding="utf-8").read()
    for lang in ("en", "fr")
    for path in glob.glob(f"pages/{lang}/*.md")
}
data = json.dumps(pages, ensure_ascii=False).replace("</", "<\\/")
with open("index.html", encoding="utf-8") as file:
    html = file.read()
html = re.sub(
    r'<script id="pages-data">.*?</script>',
    lambda _: f'<script id="pages-data">window.PAGES={data}</script>',
    html,
    count=1,
    flags=re.S,
)
with open("index.html", "w", encoding="utf-8") as file:
    file.write(html)
print(f"{len(pages)} pages embedded")
