# -*- coding: utf-8 -*-
from google.colab import files
import cv2
import numpy as np
import matplotlib.pyplot as plt

uploaded = files.upload()
filename = next(iter(uploaded))

# 이미지 읽기
img = cv2.imread(filename)

# Grayscale 변환
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

plt.figure(figsize=(8, 6))
plt.imshow(gray, cmap="gray")
plt.title("Grayscale Image")
plt.axis("off")
plt.show()

print("Image shape:", gray.shape)

# Otsu Thresholding
threshold, binary = cv2.threshold(
    gray,
    0,
    255,
    cv2.THRESH_BINARY + cv2.THRESH_OTSU
)

print("Otsu Threshold:", threshold)

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.imshow(gray, cmap="gray")
plt.title("Grayscale")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(binary, cmap="gray")
plt.title("Binary Image")
plt.axis("off")

plt.show()

# 5x5 Square Structuring Element
SE = np.ones((5, 5), dtype=np.uint8)

print("Structuring Element")
print(SE)

# ============================================================
# Dilation
# foreground(white region)를 확장
# ============================================================

dilation = cv2.dilate(
    binary,
    SE,
    iterations=1
)

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.imshow(binary, cmap="gray")
plt.title("Original Binary Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(dilation, cmap="gray")
plt.title("Dilation")
plt.axis("off")

plt.tight_layout()
plt.show()

# ============================================================
# Erosion
# foreground(white region)를 축소
# ============================================================

erosion = cv2.erode(
    binary,
    SE,
    iterations=1
)

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.imshow(binary, cmap="gray")
plt.title("Original Binary Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(erosion, cmap="gray")
plt.title("Erosion")
plt.axis("off")

plt.tight_layout()
plt.show()

# Opening Step 1: Erosion

opened_erosion = cv2.erode(
    binary,
    SE,
    iterations=1
)

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.imshow(binary, cmap="gray")
plt.title("Original Binary")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(opened_erosion, cmap="gray")
plt.title("Step 1: Erosion")
plt.axis("off")

plt.show()

# Opening Step 2: Dilation

opening = cv2.dilate(
    opened_erosion,
    SE,
    iterations=1
)

plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.imshow(binary, cmap="gray")
plt.title("Original")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(opened_erosion, cmap="gray")
plt.title("Erosion")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(opening, cmap="gray")
plt.title("Opening Result")
plt.axis("off")

plt.show()

# Closing Step 1: Dilation

closed_dilation = cv2.dilate(
    binary,
    SE,
    iterations=1
)

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.imshow(binary, cmap="gray")
plt.title("Original Binary")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(closed_dilation, cmap="gray")
plt.title("Step 1: Dilation")
plt.axis("off")

plt.show()

# Closing Step 2: Erosion

closing = cv2.erode(
    closed_dilation,
    SE,
    iterations=1
)

plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.imshow(binary, cmap="gray")
plt.title("Original")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(closed_dilation, cmap="gray")
plt.title("Dilation")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(closing, cmap="gray")
plt.title("Closing Result")
plt.axis("off")

plt.show()

# ============================================================
# Final Comparison
# ============================================================

plt.figure(figsize=(18, 10))

plt.subplot(2, 3, 1)
plt.imshow(binary, cmap="gray")
plt.title("Original")
plt.axis("off")

plt.subplot(2, 3, 2)
plt.imshow(dilation, cmap="gray")
plt.title("Dilation")
plt.axis("off")

plt.subplot(2, 3, 3)
plt.imshow(erosion, cmap="gray")
plt.title("Erosion")
plt.axis("off")

plt.subplot(2, 3, 4)
plt.imshow(opening, cmap="gray")
plt.title("Opening")
plt.axis("off")

plt.subplot(2, 3, 5)
plt.imshow(closing, cmap="gray")
plt.title("Closing")
plt.axis("off")

plt.tight_layout()
plt.show()

