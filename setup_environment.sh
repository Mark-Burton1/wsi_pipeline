#!/usr/bin/env bash
set -euo pipefail
# create env + core deps
conda install -n base -y conda-libmamba-solver || true
conda config --set solver libmamba || true
conda env update -n dp -f environment.yml || conda env create -f environment.yml
conda activate dp
python -m pip install --upgrade pip
python -m pip install openslide-python openslide-bin
echo "env ready: conda activate dp"
