#!/usr/bin/env python
import sys
from PIL import Image; Image.MAX_IMAGE_PIXELS=None
import tifffile as t, zarr

if len(sys.argv) < 2:
    sys.exit("Usage: python extract_from_ndpi.py /path/to/slide.ndpi")

p = sys.argv[1]
with t.TiffFile(p, is_ndpi=True) as tf:
    s = tf.series[0]
    lvl0 = getattr(s, "levels", [s])[0]
    z = zarr.open(lvl0.aszarr(), mode="r")
    if not hasattr(z, "shape"):
        z = z[next(iter(z.array_keys()))]

    # 512×512 patch (top-left)
    patch = z[0:512, 0:512]
    Image.fromarray(patch).save("NDPI_patch.tif")

    # thumbnail (~2048 px long side)
    h, w = z.shape[:2]
    step = max(1, max(h, w)//2048)
    thumb = z[0:h:step, 0:w:step]
    Image.fromarray(thumb).save("NDPI_thumb.tif")

print("Wrote NDPI_patch.tif and NDPI_thumb.tif")
