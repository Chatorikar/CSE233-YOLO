# YOLO-Based Hazard Detection and Safe Landing Zone Identification for Drones

**Author**: Prathamesh Chatorikar  
**Institution**: University of California, Santa Cruz  
**Date**: March 2025

## Overview

This repository presents an integrated framework for identifying safe drone landing zones in aerial imagery by combining YOLO-based object detection with Large Language Model (LLM)-driven spatial reasoning. The system prioritizes real-time performance and safety by avoiding hazardous regions such as fire, smoke, debris, and solar panels, while identifying viable zones such as rooftops and ships.

The approach leverages:

- **YOLOv8 Nano** for real-time detection of critical regions,
- **Custom post-processing algorithm (Algorithm 1)** to evaluate rooftop safety,
- **GPT-4 Turbo (via OpenAI API)** to provide fallback reasoning and coordinate generation when object-level metadata is insufficient.


## Model Architecture and Training

- **Base Model**: YOLOv8n (Ultralytics)
- **Trained On**: Merged Roboflow dataset with classes:
  - `rooftop`, `ship` (safe zones)
  - `fire`, `smoke`, `debris`, `solar-panels` (hazards)
- **Labeling and Augmentation**: Manual annotations + geometric augmentations
- **Training Infrastructure**: NVIDIA T4 GPU (Google Colab)
- **Weights**: Best weights saved as `best.pt`, available in this repository

Dataset:
- [Roboflow Link (Dataset-for-YOLO-CSE-233)](https://app.roboflow.com/yolo-rh90o/dataset-for-yolo-cse-233)
