# Morphological Image Processing

## Overview

This assignment implements four morphological image processing operations using Python and OpenCV.

- **Dilation:** Expands foreground objects.
- **Erosion:** Shrinks foreground objects.
- **Opening:** Erosion followed by dilation. It can remove small foreground noise.
- **Closing:** Dilation followed by erosion. It can fill small background holes and gaps.

## Implementation

The experiment follows these steps:

1. Upload an input image using Google Colab.
2. Convert the image to grayscale.
3. Apply Otsu's thresholding to obtain a binary image.
4. Create four different structuring elements:
   - Vertical (5×1)
   - Horizontal (1×5)
   - Square (5×5)
   - Diamond (5×5)
5. Apply Dilation, Erosion, Opening, and Closing using each structuring element.
6. Visualize and compare the results.

## Source Code and Results

**[morphological_operations.ipynb](morphological_operations.ipynb)**

The notebook contains the complete source code and saved execution results.

The final visualization compares the original binary image and the four morphological operations for each structuring element.

## Experiment Summary

Dilation expands foreground regions, while erosion shrinks them. Opening and closing combine these operations to remove small foreground structures or fill small background gaps.

The results also show that the shape of the structuring element affects the morphological processing results.

## Environment

- Google Colab
- Python
- OpenCV
- NumPy
- Matplotlib

To reproduce the experiment, run the notebook in Google Colab and upload an input image when prompted.
