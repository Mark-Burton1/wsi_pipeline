#!/usr/bin/env python
import sys, os, numpy as np, torch
from PIL import Image
from torchvision import models, transforms
from sklearn.cluster import KMeans
import umap

if len(sys.argv) < 3:
    sys.exit("Usage: python embed_cluster_umap.py tiles_dir out.tsv")

tiles_dir, out_tsv = sys.argv[1], sys.argv[2]
MAX_TILES = 3000
N_CLUSTERS = 6

paths = [os.path.join(tiles_dir,f) for f in os.listdir(tiles_dir)
         if f.lower().endswith((".tif",".tiff",".jpg",".jpeg",".png"))]
paths.sort()
if MAX_TILES: paths = paths[:MAX_TILES]

device = "cuda" if torch.cuda.is_available() else "cpu"
model = models.resnet50(weights=models.ResNet50_Weights.IMAGENET1K_V2).to(device).eval()
feat = torch.nn.Sequential(*(list(model.children())[:-1]))
pre = transforms.Compose([
    transforms.Resize(256), transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=(0.485,0.456,0.406), std=(0.229,0.224,0.225)),
])

def load_rgb(p):
    im = Image.open(p)
    if im.mode != "RGB": im = im.convert("RGB")
    return pre(im)

X=[]
with torch.no_grad():
    for p in paths:
        try:
            v = feat(load_rgb(p).unsqueeze(0).to(device)).squeeze().cpu().numpy()
            X.append(v)
        except Exception as e:
            print("[skip]", os.path.basename(p), e)

X = np.stack(X)
labels = KMeans(n_clusters=N_CLUSTERS, n_init=10, random_state=0).fit_predict(X)
emb = umap.UMAP(n_components=2, random_state=0).fit_transform(X)

with open(out_tsv,"w") as f:
    f.write("path\tumap1\tumap2\tcluster\n")
    for p,(u1,u2),c in zip(paths,emb,labels):
        f.write(f"{os.path.basename(p)}\t{u1:.4f}\t{u2:.4f}\t{c}\n")
print("wrote:", out_tsv)
