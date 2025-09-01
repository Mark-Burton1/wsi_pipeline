#!/usr/bin/env python
import sys, os, csv
if len(sys.argv) < 3:
    sys.exit("Usage: python manifest.py tiles_dir out.csv")
root, out = sys.argv[1], sys.argv[2]
rows=[["path"]]
for f in sorted(os.listdir(root)):
    if f.lower().endswith((".tif",".tiff",".jpg",".jpeg",".png")):
        rows.append([os.path.join(root,f)])
with open(out,"w",newline="") as fh:
    csv.writer(fh).writerows(rows)
print("wrote:", out, f"({len(rows)-1} tiles)")
