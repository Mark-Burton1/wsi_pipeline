#!/usr/bin/env python
import sys, pandas as pd, matplotlib.pyplot as plt

if len(sys.argv) < 3:
    sys.exit("Usage: python plot_umap.py input.tsv output.png")

tsv, out = sys.argv[1], sys.argv[2]
df = pd.read_csv(tsv, sep="\t")
plt.figure(figsize=(6,5))
for c,g in df.groupby("cluster"):
    plt.scatter(g.umap1, g.umap2, s=5, label=f"c{c}", alpha=0.6)
plt.legend(markerscale=4, fontsize=8, frameon=False)
plt.title("UMAP of WSI tiles (unsupervised)")
plt.tight_layout()
plt.savefig(out, dpi=180)
print("wrote:", out)
