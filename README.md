# Hamamatsu whole slide imaging to unsupervised tiles pipeline

This project builds an end-to-end pipeline for processing Hamamatsu NDPI whole slide images. It tiles slides, filters irrelevant patches, embeds each tile with a ResNet50 model, and clusters them using KMeans + UMAP. The result is an unsupervised map of morphological variability, allowing exploratory analysis of pathology slides even when no labels are available. 

The whole slide image I used for this demonstration was taken from openmicroscopy.org, specifically https://downloads.openmicroscopy.org/images/Hamamatsu-NDPI/hamamatsu/DM0014%20-%202020-04-02%2010.25.21.ndpi.

Main steps:

1. Decode Hamamatsu .ndpi
2. Tile to patches
3. Filter low-information tiles
4. Embed with ResNet50, cluster, and UMAP to visualise cell morphology.

Requirements
macOS, Conda
Scanner formats: NDPI (Hamamatsu); OpenSlide QA also supports SCN/SVS/TIFF.
Conda env (creates dp):

Outputs (local, not committed)
NDPI_patch.tif, NDPI_thumb.tif
tiles_ndpi_l0/, tiles_keep_bw/
unsup_tiles.tsv, umap_tiles.png
tiles_manifest.csv, tiles_with_umap.csv
