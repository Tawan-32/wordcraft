import glob
import os

from fontTools.ttLib import TTFont

lines = []
for p in sorted(glob.glob("craft-fonts/fonts/thai/*.ttf")):
    f = TTFont(p, lazy=True)
    n = f["name"]

    def nm(i):
        r = n.getName(i, 3, 1, 0x409) or n.getName(i, 1, 0, 0)
        return r.toUnicode().strip() if r else ""

    fam, sty = nm(1), nm(2)
    if sty not in ("Regular", "Bold"):
        continue
    rel = os.path.relpath(p, "craft-fonts")
    lines.append(f"{fam} | {sty} | {rel} | Thai")

with open("craft-fonts/fonts/manifest.txt", "a", encoding="utf-8") as m:
    m.write("\n" + "\n".join(lines) + "\n")
print(len(lines), "Thai font lines added")
