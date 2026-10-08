"""Build a single-file preview of the landing page for publishing as a Claude Artifact.

Usage: python3 tools/build-preview.py <output.html>

Inlines style.css and main.js into one HTML body fragment (the Artifact host adds
<html>/<head>/<body>), drops <meta> and the Pretendard stylesheet (blocked by the
Artifact CSP), and forces .reveal elements visible. Images stay as relative
paths under assets/img/, so publish them alongside via the Artifact `files` map.
"""
import pathlib
import re
import sys

root = pathlib.Path(__file__).resolve().parent.parent
out = pathlib.Path(sys.argv[1])

html = (root / "index.html").read_text()
css = (root / "assets/css/style.css").read_text()
js = (root / "assets/js/main.js").read_text()

head = re.search(r"<head>(.*?)</head>", html, re.S).group(1)
body = re.search(r"<body>(.*?)</body>", html, re.S).group(1)
head = re.sub(r"\s*<meta[^>]*>", "", head)
head = re.sub(r"\s*<link[^>]*(jsdelivr|style\.css)[^>]*>", "", head)
head = re.sub(r"<title>.*?</title>", "<title>e.je PMU</title>", head)
body = body.replace('<script src="assets/js/main.js"></script>', "<script>\n" + js + "\n</script>")

out.write_text(
    head.strip()
    + "\n<style>\n" + css
    + "\n/* preview: content visible at rest */\n.reveal{opacity:1;transform:none}\n</style>\n"
    + body.strip() + "\n"
)
print(f"wrote {out} ({out.stat().st_size} bytes)")
