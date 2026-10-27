"""Prépare le document RTN SSA pour la consultation dans le site.

Usage : python3 outils/pages_rtn.py chemin/vers/references_techniques_nationales_ssa.pdf

Copie le PDF dans rtn/, convertit chaque page en image WebP (rtn/pages/pNN.webp)
et affiche la table « fiche -> [première page, dernière page] » à recopier dans
index.html (constante PAGES). Nécessite pdftoppm et pdftotext (poppler-utils) et Pillow.
"""
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

from PIL import Image

DPI = 150
QUALITY = 80
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "rtn")
CODE = re.compile(r"\[(0\d(?:AC|PR|FT)\d\d) / ")


def page_text(pdf, n):
    return subprocess.run(["pdftotext", "-f", str(n), "-l", str(n), pdf, "-"],
                          capture_output=True, text=True, check=True).stdout


def main(pdf):
    info = subprocess.run(["pdfinfo", pdf], capture_output=True, text=True, check=True).stdout
    count = int(re.search(r"^Pages:\s+(\d+)", info, re.M).group(1))

    # Une fiche commence à la page qui porte son en-tête « [01AC02 / 09-2026] » (pas le sommaire,
    # qui en liste plusieurs) et s'arrête avant la fiche suivante ou une page de séparation de chapitre.
    pages, current = {}, None
    for n in range(1, count + 1):
        text = page_text(pdf, n)
        codes = set(CODE.findall(text))
        if len(codes) == 1:
            current = codes.pop()
            pages[current] = [n, n]
        elif len(text.split()) < 20 or len(codes) > 1:
            current = None
        elif current:
            pages[current][1] = n

    os.makedirs(os.path.join(OUT, "pages"), exist_ok=True)
    shutil.copyfile(pdf, os.path.join(OUT, "references-techniques-nationales-ssa.pdf"))
    with tempfile.TemporaryDirectory() as tmp:
        subprocess.run(["pdftoppm", "-r", str(DPI), "-png", pdf, os.path.join(tmp, "p")], check=True)
        for name in sorted(os.listdir(tmp)):
            n = int(re.search(r"(\d+)\.png$", name).group(1))
            Image.open(os.path.join(tmp, name)).convert("RGB").save(
                os.path.join(OUT, "pages", "p%02d.webp" % n), "WEBP", quality=QUALITY, method=6)

    print("var PDF_PAGES = %d;" % count)
    print("var PAGES = " + json.dumps(pages, separators=(",", ":")) + ";")


if __name__ == "__main__":
    main(sys.argv[1])
