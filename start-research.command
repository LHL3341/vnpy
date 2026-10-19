#!/bin/zsh
cd "$(dirname "$0")"
export OMP_NUM_THREADS=2
export OPENBLAS_NUM_THREADS=2
exec .venv/bin/python local_setup/run.py
