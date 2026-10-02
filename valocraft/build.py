#!/usr/bin/env python3
"""Embeds every pages/<lang>/<slug>.md into index.html so the site also works offline (file://).
Run `python3 build.py` after editing any .md file, then commit index.html."""
import json,glob,os,re
pages={f"{l}/{os.path.basename(p)[:-3]}":open(p,encoding='utf-8').read() for l in('en','fr') for p in glob.glob(f'pages/{l}/*.md')}
data=json.dumps(pages,ensure_ascii=False).replace('</','<\\/')
h=open('index.html',encoding='utf-8').read()
h=re.sub(r'<script id="pages-data">.*?</script>',lambda m:f'<script id="pages-data">window.PAGES={data}</script>',h,count=1,flags=re.S)
open('index.html','w',encoding='utf-8').write(h)
print(f'{len(pages)} pages embedded')
