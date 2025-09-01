#!/usr/bin/env python
import sys, os
from PIL import Image; Image.MAX_IMAGE_PIXELS=None
import openslide as osl

if len(sys.argv) < 2:
    sys.exit("Usage: python check_wsi.py /path/to/slide.(scn|svs|tiff)")

p = os.path.abspath(sys.argv[1])
assert os.path.exists(p), f"Missing: {p}"

s = osl.OpenSlide(p)
print("dims:", s.dimensions, "levels:", s.level_count, "downs:", s.level_downsamples)

base = os.path.splitext(os.path.basename(p))[0]
outdir = os.path.expanduser("~/dp_work/out"); os.makedirs(outdir, exist_ok=True)
s.get_thumbnail((2048,2048)).save(os.path.join(outdir, f"{base}_thumb.jpg"), quality=90)
s.read_region((0,0), 0, (512,512)).convert("RGB").save(os.path.join(outdir, f"{base}_patch_0_0.jpg"), quality=95)
s.close()
print("wrote:", outdir)
