# Hamamatsu whole slide imaging to unsupervised tiles pipeline

This repo shows a standard digital pathology pipeline for working with whole-slide images without annotation in ndpi format. The whole slide image I used for this demonstration was taken from openmicroscopy.org, specifically https://downloads.openmicroscopy.org/images/Hamamatsu-NDPI/hamamatsu/DM0014%20-%202020-04-02%2010.25.21.ndpi.

1. Decode Hamamatsu .ndpi
2. Tile to patches
3. Filter low-information tiles
4. Embed with ResNet50, cluster, and UMAP to visualise morphology.

Requirements
macOS, Conda
Scanner formats: NDPI (Hamamatsu); OpenSlide QA also supports SCN/SVS/TIFF.
Conda env (creates dp):

Outputs (local, not committed)
NDPI_patch.tif, NDPI_thumb.tif
tiles_ndpi_l0/, tiles_keep_bw/
unsup_tiles.tsv, umap_tiles.png
tiles_manifest.csv, tiles_with_umap.csv
