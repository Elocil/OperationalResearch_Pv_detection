# OperationalResearch_Pv_detection
# ☀️ Photovoltaic Panel Detection using YOLOv8

## Overview

This project implements an automatic detection of photovoltaic (PV) panels in aerial or satellite images using a deep learning object detection model based on **YOLOv8**.

The workflow relies on a custom annotated dataset hosted on Roboflow and uses the **Ultralytics YOLOv8** framework for training and inference. The notebook is designed to be simple, reproducible, and suitable for academic use in solar energy, remote sensing, and urban-scale analysis.

---

## Objectives

- Detect photovoltaic panels in aerial or satellite imagery  
- Train a custom YOLOv8 object detection model  
- Perform inference on unseen images  
- Visualize and interpret detection results  

---

## Repository Structure

dataset/
├── train/
│   ├── images/
│   └── labels/
├── valid/
│   ├── images/
│   └── labels/
├── test/
│   ├── images/
│   └── labels/
└── data.yaml

> The `data/` and `runs/` folders are created automatically when running the notebook.

---

## Requirements

### Python
- Python **3.9 or higher** is recommended

### Libraries Used

The following Python libraries are used in the notebook:

- `ultralytics`
- `roboflow`
- `torch`
- `torchvision`
- `matplotlib`
- `Pillow`
- `pathlib`
- `zipfile`
- `os`

### Installation

It is recommended to use a virtual environment.

```bash
pip install ultralytics roboflow matplotlib pillow

