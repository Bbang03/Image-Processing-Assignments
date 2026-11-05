# Image Processing Assignments

This repository contains two assignments completed for the Image Processing course.

Each assignment includes Python source code and saved execution results.

## 1. Morphological Image Processing

**[View Notebook](01_Morphological_Operations/morphological_operations.ipynb)**

Implementation of four morphological operations:

- Dilation
- Erosion
- Opening
- Closing

The experiment compares the results using four structuring elements: Vertical, Horizontal, Square, and Diamond.

The notebook includes image preprocessing, morphological operations, and visualization of the results.

## 2. CIFAR-10 KNN Classification

**[View Notebook](02_CIFAR10_KNN/CIFAR10_KNN.ipynb)**

Implementation and evaluation of the K-Nearest Neighbors (KNN) algorithm using the CIFAR-10 dataset.

The experiment includes:

- Different K values: 1, 3, 5, 7, 9
- Manhattan (L1) and Euclidean (L2) distances
- 5-fold Cross-Validation
- Accuracy, Precision, Recall, and F1-score
- Performance comparison and confusion matrix

### Final Test Results

| Metric | Result |
|---|---|
| Best K | 1 |
| Best Distance Metric | L1 (Manhattan) |
| Accuracy | 38.59% |
| Precision (Macro) | 43.33% |
| Recall (Macro) | 38.59% |
| F1-score (Macro) | 38.62% |

The KNN experiment used all 50,000 training images and 10,000 test images from CIFAR-10.

## Execution Environment

Both assignments were implemented using Google Colab.

The morphological processing notebook requires an uploaded input image. The KNN notebook automatically downloads CIFAR-10 to the Colab runtime.

Source code and execution outputs can be viewed directly by opening each notebook on GitHub.
