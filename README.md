# Hamamatsu whole slide imaging to unsupervised tiles pipeline with openslide

This project builds an end-to-end pipeline for processing Hamamatsu NDPI whole slide images. It tiles slides, filters irrelevant patches, embeds each tile with a ResNet50 model, and clusters them using KMeans + UMAP. The result is an unsupervised map of morphological variability, allowing exploratory analysis of pathology slides even when no labels are available. 

The whole slide image I used for this demonstration was taken from openmicroscopy.org, specifically https://downloads.openmicroscopy.org/images/Hamamatsu-NDPI/hamamatsu/DM0014%20-%202020-04-02%2010.25.21.ndpi.

Order of execution is as follows:

1. setup_env.sh
2. check_wsi.py
3. extract_from_ndpi.py
4. tile_ndpi.py
5. filter_tiles_bw.py
6. embed_cluster_umap.py
7. plot_umap.py
8. manifest.py

Requirements
macOS, Conda,
Scanner formats: NDPI (Hamamatsu)

Outputs (local, not committed)
NDPI_patch.tif, NDPI_thumb.tif
tiles_ndpi_l0/, tiles_keep_bw/
unsup_tiles.tsv, umap_tiles.png
tiles_manifest.csv, tiles_with_umap.csv
