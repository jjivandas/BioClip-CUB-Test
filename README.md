# BioCLIP Evaluation on CUB-200-2011

## Overview

This repository contains an evaluation of the [BioCLIP](https://imageomics.github.io/pybioclip/) model on the [CUB-200-2011](https://www.vision.caltech.edu/datasets/cub_200_2011/) dataset.

We tested the model using the official test split and computed overall and per-class accuracy.

## Contents

* `test_data.json`: Preprocessed test set with image paths and class labels
* `bioclip_eval.ipynb`: Jupyter notebook that runs predictions and computes metrics
* `per_class_accuracy.csv`: Accuracy breakdown by class

## Setup

1. Clone the repo
2. Install `pybioclip` and other dependencies
3. Place the `CUB_200_2011` folder in the root directory

## Steps

* Parsed metadata files and built `test_data.json`
* Removed numeric prefixes from class names (e.g., `001.Black_footed_Albatross` → `Black_footed_Albatross`)
* Ran predictions using BioCLIP’s `CustomLabelsClassifier`
* Compared predictions to ground truth labels
* Computed overall and per-class accuracy

## Results

* **Overall Accuracy:** 69.3%
* Per-class accuracy saved in `per_class_accuracy.csv`

## Notes

* Initial evaluation used numeric class names, which led to mismatches
* Stripped numeric prefixes from both predictions and labels to ensure accurate comparison

---

Scripts and evaluation results included in this repo. Run the notebook to replicate the evaluation.
