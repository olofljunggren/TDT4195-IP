---
# This is a YAML preamble, defining pandoc meta-variables.
# Reference: https://pandoc.org/MANUAL.html#variables
# Change them as you see fit.
title: TDT4195 Assignment 1
author:
- Olof Ljunggren
date: \today # This is a latex command, ignored for HTML output
lang: en-US
papersize: a4
geometry: margin=4cm
toc: false
toc-title: "Table of Contents"
toc-depth: 2
numbersections: true
header-includes:
# The `atkinson` font, requires 'texlive-fontsextra' on arch or the 'atkinson' CTAN package
# Uncomment this line to enable:
#- '`\usepackage[sfdefault]{atkinson}`{=latex}'
colorlinks: true
links-as-notes: true
# The document is following this break is written using "Markdown" syntax
---

<!--
This is a HTML-style comment, not visible in the final PDF.
-->

# TDT4195 Image Processing Assignment 1

# Task 1: Theory, Spatial Filtering [2.4pt]

## Task 1.a 
[0.2pt] Explain in one sentence what sampling is.

- In image processing sampling is the spatial discreteization. Samplerate corresponds to pixelsize.


## Task 1.b
[0.2pt] Explain in one sentence what quantization is.

- Quantization is the discreteization of an image intensity. Corresponds to the specific intensity a pixel gets.

## Task 1.c
[0.4pt] Looking at an image histogram, how can you see that the image has high contrast?

- If there is a large diffrence between high and mid and low intensities. Which for a histogram means there is a lot of high and low intensity pixels and not very many in the grey zone inbetween. Should have a little bit of a u-shape.

## Task 1.d
[0.6pt] Perform histogram equalization by hand on the 3-bit (8 intensity levels) image in Figure 1a
Your report must include all the steps you did to compute the histogram, the transformation, and
the transformed image. Round down any resulting pixel intensities that are not integers (use the
floor operator).

![Histogram.
](assignment1/image_solutions/equalizing.jpg)

## Task 1.e
[0.2pt] What happens to the dynamic range if we apply a log transform to an image with a large variance in pixel intensities?

- The log-transformation compresses the dynamic range. We get more detailed low intensities but less detailed high intensities.

## Task 1.f
[0.8pt] Perform spatial convolution by hand on the image in Figure 1a using the kernel in Figure 1b.
The convolved image should be 3 ×5. You are free to choose how you handle boundary conditions,
and state how you handle them in the report.

![Convolution.
](assignment1/image_solutions/convolution.jpg)

The boundaries was handled by padding with zeros equal to the floor(kernel_size/2). This makes that the image has the same size. Though we might lose some information in the edges.



# Task 2: Programming [1.6pt]

## Task 2.a
[0.3pt] Implement a function that converts an RGB image to grayscale. Use Equation 1. Implement this in the function greyscale.

![Greyscale duck.
](assignment1/image_solutions/gray_duck.jpeg)


## Task 2.b
[0.4pt] Implement a function that takes a grayscale image and applies the following intensity transformation T(p) = 1 − p. Implement this in the function inverse.

![Inverted intensities duck.
](assignment1/image_solutions/inverted_duck.jpeg)



[0.9pt] Implement a function that takes an RGB image and a convolutional kernel as input, and performs 2D spatial convolution. Assume the size of the kernel is odd numbered, e.g. 3 × 3, 5 × 5, or 7 × 7. You must implement the convolution operation yourself from scratch. Implement the function in convolve_im.

![Smoothened duck.
](assignment1/image_solutions/im_smoothed.jpg)


![Sobel kernel duck.
](assignment1/image_solutions/im_sobel.jpg)



# Task 3: Theory, Neural Networks [1.6pt]

## Task 3.a
Try to implement the logic gates AND, OR, NOT, NOR, NAND, or XOR in a single layert neural network. Given that all negative and zero outputs count as 0 and that all positive outputs counts as 1 we can construct every of these except XOR with a single layer network. 

Useful soruce: https://medium.com/@stanleydukor neural-representation-of-and-or-not-xor-and-xnor-logic-gates-perceptron-algorithm-b0275375fea1


## Task 3.b



