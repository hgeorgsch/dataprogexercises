---
jupytext:
  formats: ipynb,md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.18.1
kernelspec:
  name: python3
  display_name: Python 3 (ipykernel)
  language: python
---

+++ {"id": "t6MPjfT5NrKQ"}

<div align="center">
  <a href="https://ultralytics.com/yolo" target="_blank">
    <img width="1024" src="https://raw.githubusercontent.com/ultralytics/assets/main/yolov8/banner-yolov8.png">
  </a>

  [中文](https://docs.ultralytics.com/zh/) | [한국어](https://docs.ultralytics.com/ko/) | [日本語](https://docs.ultralytics.com/ja/) | [Русский](https://docs.ultralytics.com/ru/) | [Deutsch](https://docs.ultralytics.com/de/) | [Français](https://docs.ultralytics.com/fr/) | [Español](https://docs.ultralytics.com/es/) | [Português](https://docs.ultralytics.com/pt/) | [Türkçe](https://docs.ultralytics.com/tr/) | [Tiếng Việt](https://docs.ultralytics.com/vi/) | [العربية](https://docs.ultralytics.com/ar/)

  <a href="https://github.com/ultralytics/ultralytics/actions/workflows/ci.yml"><img src="https://github.com/ultralytics/ultralytics/actions/workflows/ci.yml/badge.svg" alt="Ultralytics CI"></a>
  <a href="https://console.paperspace.com/github/ultralytics/ultralytics"><img src="https://assets.paperspace.io/img/gradient-badge.svg" alt="Run on Gradient"/></a>
  <a href="https://colab.research.google.com/github/ultralytics/ultralytics/blob/main/examples/tutorial.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"></a>
  <a href="https://www.kaggle.com/models/ultralytics/yolo11"><img src="https://kaggle.com/static/images/open-in-kaggle.svg" alt="Open In Kaggle"></a>

  <a href="https://ultralytics.com/discord"><img alt="Discord" src="https://img.shields.io/discord/1089800235347353640?logo=discord&logoColor=white&label=Discord&color=blue"></a>
  <a href="https://community.ultralytics.com"><img alt="Ultralytics Forums" src="https://img.shields.io/discourse/users?server=https%3A%2F%2Fcommunity.ultralytics.com&logo=discourse&label=Forums&color=blue"></a>
  <a href="https://reddit.com/r/ultralytics"><img alt="Ultralytics Reddit" src="https://img.shields.io/reddit/subreddit-subscribers/ultralytics?style=flat&logo=reddit&logoColor=white&label=Reddit&color=blue"></a>
</div>

This **Ultralytics Colab Notebook** is the easiest way to get started with [YOLO models](https://www.ultralytics.com/yolo)—no installation needed. Built by [Ultralytics](https://www.ultralytics.com/), the creators of YOLO, this notebook walks you through running **state-of-the-art** models directly in your browser.

Ultralytics models are constantly updated for performance and flexibility. They're **fast**, **accurate**, and **easy to use**, and they excel at [object detection](https://docs.ultralytics.com/tasks/detect/), [tracking](https://docs.ultralytics.com/modes/track/), [instance segmentation](https://docs.ultralytics.com/tasks/segment/), [image classification](https://docs.ultralytics.com/tasks/classify/), and [pose estimation](https://docs.ultralytics.com/tasks/pose/).

Find detailed documentation in the [Ultralytics Docs](https://docs.ultralytics.com/). Get support via [GitHub Issues](https://github.com/ultralytics/ultralytics/issues/new/choose). Join discussions on [Discord](https://discord.com/invite/ultralytics), [Reddit](https://www.reddit.com/r/ultralytics/), and the [Ultralytics Community Forums](https://community.ultralytics.com/)!

Request an Enterprise License for commercial use at [Ultralytics Licensing](https://www.ultralytics.com/license).

<br>
<div>
  <a href="https://www.youtube.com/watch?v=ZN3nRZT7b24" target="_blank">
    <img src="https://img.youtube.com/vi/ZN3nRZT7b24/maxresdefault.jpg" alt="Ultralytics Video" width="640" style="border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);">
  </a>

  <p style="font-size: 16px; font-family: Arial, sans-serif; color: #555;">
    <strong>Watch: </strong> How to Train
    <a href="https://github.com/ultralytics/ultralytics">Ultralytics</a>
    <a href="https://docs.ultralytics.com/models/yolo11/">YOLO11</a> Model on Custom Dataset using Google Colab Notebook 🚀
  </p>
</div>

+++ {"id": "7mGmQbAO5pQb"}

# Setup

pip install `ultralytics` and [dependencies](https://github.com/ultralytics/ultralytics/blob/main/pyproject.toml) and check software and hardware.

[![PyPI - Version](https://img.shields.io/pypi/v/ultralytics?logo=pypi&logoColor=white)](https://pypi.org/project/ultralytics/) [![Downloads](https://static.pepy.tech/badge/ultralytics)](https://clickpy.clickhouse.com/dashboard/ultralytics) [![PyPI - Python Version](https://img.shields.io/pypi/pyversions/ultralytics?logo=python&logoColor=gold)](https://pypi.org/project/ultralytics/)

```{code-cell} ipython3
---
id: wbvMlHd_QwMG
colab:
  base_uri: https://localhost:8080/
outputId: 4de5a5c9-d3b5-4e4e-a4e5-cd80f159e4ce
---
!pip install ultralytics
import ultralytics
ultralytics.checks()
```

+++ {"id": "4JnkELT0cIJg"}

# 1. Predict

YOLO11 may be used directly in the Command Line Interface (CLI) with a `yolo` command for a variety of tasks and modes and accepts additional arguments, i.e. `imgsz=640`. See a full list of available `yolo` [arguments](https://docs.ultralytics.com/usage/cfg/) and other details in the [YOLO11 Predict Docs](https://docs.ultralytics.com/modes/train/).

```{code-cell} ipython3
---
id: zR9ZbuQCH7FX
colab:
  base_uri: https://localhost:8080/
outputId: 1d438406-032a-4ea9-9ad5-dd17078850d3
---
# Run inference on an image with YOLO11n
!yolo predict model=yolo11n.pt source='https://ultralytics.com/images/zidane.jpg'
```

+++ {"id": "hkAzDWJ7cWTr"}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<img align="left" src="https://user-images.githubusercontent.com/26833433/212889447-69e5bdf1-5800-4e29-835e-2ed2336dede2.jpg" width="600">

+++ {"id": "0eq1SMWl6Sfn"}

# 2. Val
Validate a model's accuracy on the [COCO](https://docs.ultralytics.com/datasets/detect/coco/) dataset's `val` or `test` splits. The latest YOLO11 [models](https://github.com/ultralytics/ultralytics#models) are downloaded automatically the first time they are used. See [YOLO11 Val Docs](https://docs.ultralytics.com/modes/val/) for more information.

```{code-cell} ipython3
:id: WQPtK1QYVaD_

# Download COCO val
from ultralytics.utils.downloads import download

download('https://ultralytics.com/assets/coco2017val.zip', unzip=True, dir='datasets') # download (780MB - 5000 images)
```

```{code-cell} ipython3
---
id: X58w8JLpMnjH
outputId: 27364fde-3aff-47ea-9458-18e4a044e27b
colab:
  base_uri: https://localhost:8080/
---
# Validate YOLO11n on COCO8 val
!yolo val model=yolo11n.pt data=coco8.yaml
```

+++ {"id": "ZY2VXXXu74w5"}

# 3. Train

<p align=""><a href="https://ultralytics.com/hub"><img width="1000" src="https://github.com/ultralytics/assets/raw/main/yolov8/banner-integrations.png"/></a></p>

Train YOLO11 on [Detect](https://docs.ultralytics.com/tasks/detect/), [Segment](https://docs.ultralytics.com/tasks/segment/), [Classify](https://docs.ultralytics.com/tasks/classify/) and [Pose](https://docs.ultralytics.com/tasks/pose/) datasets. See [YOLO11 Train Docs](https://docs.ultralytics.com/modes/train/) for more information.

```{code-cell} ipython3
:id: ktegpM42AooT

#@title Select YOLO11 🚀 logger {run: 'auto'}
logger = 'TensorBoard' #@param ['TensorBoard', 'Weights & Biases']

if logger == 'TensorBoard':
  !yolo settings tensorboard=True
  %load_ext tensorboard
  %tensorboard --logdir .
elif logger == 'Weights & Biases':
  !yolo settings wandb=True
```

```{code-cell} ipython3
---
id: 1NcFxRcFdJ_O
outputId: 849c2875-cd29-4a93-a7c7-e464a9b84dc6
colab:
  base_uri: https://localhost:8080/
---
# Train YOLO11n on COCO8 for 3 epochs
!yolo train model=yolo11n.pt data=coco8.yaml epochs=3 imgsz=640
```

+++ {"id": "nPZZeNrLCQG6"}

# 4. Export

Export a YOLO model to any supported format below with the `format` argument, i.e. `format=onnx`. See [Export Docs](https://docs.ultralytics.com/modes/export/) for more information.

- 💡 ProTip: Export to [ONNX](https://docs.ultralytics.com/integrations/onnx/) or [OpenVINO](https://docs.ultralytics.com/integrations/openvino/) for up to 3x CPU speedup.
- 💡 ProTip: Export to [TensorRT](https://docs.ultralytics.com/integrations/tensorrt/) for up to 5x GPU speedup.

| Format | `format` Argument | Model | Metadata | Arguments |
|--------|-----------------|-------|----------|------------|
| [PyTorch](https://pytorch.org/) | - | `yolo11n.pt` | ✅ | - |
| [TorchScript](https://docs.ultralytics.com/integrations/torchscript) | `torchscript` | `yolo11n.torchscript` | ✅ | `imgsz`, `batch`, `dynamic`, `optimize`, `half`, `nms`, `device` |
| [ONNX](https://docs.ultralytics.com/integrations/onnx) | `onnx` | `yolo11n.onnx` | ✅ | `imgsz`, `batch`, `dynamic`, `half`, `opset`, `simplify`, `nms`, `device` |
| [OpenVINO](https://docs.ultralytics.com/integrations/openvino) | `openvino` | `yolo11n_openvino_model/` | ✅ | `imgsz`, `batch`, `dynamic`, `half`, `int8`, `nms`, `fraction`, `device`, `data` |
| [TensorRT](https://docs.ultralytics.com/integrations/tensorrt) | `engine` | `yolo11n.engine` | ✅ | `imgsz`, `batch`, `dynamic`, `half`, `int8`, `simplify`, `nms`, `fraction`, `device`, `data`, `workspace` |
| [CoreML](https://docs.ultralytics.com/integrations/coreml) | `coreml` | `yolo11n.mlpackage` | ✅ | `imgsz`, `batch`, `half`, `int8`, `nms`, `device` |
| [TF SavedModel](https://docs.ultralytics.com/integrations/tf-savedmodel) | `saved_model` | `yolo11n_saved_model/` | ✅ | `imgsz`, `batch`, `int8`, `keras`, `nms`, `device` |
| [TF GraphDef](https://docs.ultralytics.com/integrations/tf-graphdef) | `pb` | `yolo11n.pb` | ❌ | `imgsz`, `batch`, `device` |
| [TF Lite](https://docs.ultralytics.com/integrations/tflite) | `tflite` | `yolo11n.tflite` | ✅ | `imgsz`, `batch`, `half`, `int8`, `nms`, `fraction`, `device`, `data` |
| [TF Edge TPU](https://docs.ultralytics.com/integrations/edge-tpu) | `edgetpu` | `yolo11n_edgetpu.tflite` | ✅ | `imgsz`, `device` |
| [TF.js](https://docs.ultralytics.com/integrations/tfjs) | `tfjs` | `yolo11n_web_model/` | ✅ | `imgsz`, `batch`, `half`, `int8`, `nms`, `device` |
| [PaddlePaddle](https://docs.ultralytics.com/integrations/paddlepaddle) | `paddle` | `yolo11n_paddle_model/` | ✅ | `imgsz`, `batch`, `device` |
| [MNN](https://docs.ultralytics.com/integrations/mnn) | `mnn` | `yolo11n.mnn` | ✅ | `imgsz`, `batch`, `half`, `int8`, `device` |
| [NCNN](https://docs.ultralytics.com/integrations/ncnn) | `ncnn` | `yolo11n_ncnn_model/` | ✅ | `imgsz`, `batch`, `half`, `device` |
| [IMX500](https://docs.ultralytics.com/integrations/sony-imx500) | `imx` | `yolo11n_imx_model/` | ✅ | `imgsz`, `int8`, `fraction`, `device`, `data` |
| [RKNN](https://docs.ultralytics.com/integrations/rockchip-rknn) | `rknn` | `yolo11n_rknn_model/` | ✅ | `imgsz`, `batch`, `name`, `device` |

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
id: CYIjW4igCjqD
outputId: f06e7d97-01d9-45f4-b24b-e90b08291675
---
!yolo export model=yolo11n.pt format=torchscript
```

+++ {"id": "kUMOQ0OeDBJG"}

# 5. Python Usage

YOLO11 was reimagined using Python-first principles for the most seamless Python YOLO experience yet. YOLO11 models can be loaded from a trained checkpoint or created from scratch. Then methods are used to train, val, predict, and export the model. See detailed Python usage examples in the [YOLO11 Python Docs](https://docs.ultralytics.com/usage/python/).

```{code-cell} ipython3
:id: bpF9-vS_DAaf

from ultralytics import YOLO

# Load a model
model = YOLO('yolo11n.yaml')  # build a new model from scratch
model = YOLO('yolo11n.pt')  # load a pretrained model (recommended for training)

# Use the model
results = model.train(data='coco8.yaml', epochs=3)  # train the model
results = model.val()  # evaluate model performance on the validation set
results = model('https://ultralytics.com/images/bus.jpg')  # predict on an image
results = model.export(format='onnx')  # export the model to ONNX format
```

+++ {"id": "Phm9ccmOKye5"}

# 6. Tasks

YOLO11 can train, val, predict and export models for the most common tasks in vision AI: [Detect](https://docs.ultralytics.com/tasks/detect/), [Segment](https://docs.ultralytics.com/tasks/segment/), [Classify](https://docs.ultralytics.com/tasks/classify/) and [Pose](https://docs.ultralytics.com/tasks/pose/). See [YOLO11 Tasks Docs](https://docs.ultralytics.com/tasks/) for more information.

<br><img width="1024" src="https://raw.githubusercontent.com/ultralytics/assets/main/im/banner-tasks.png">

+++ {"id": "yq26lwpYK1lq"}

## 1. Detection

YOLO11 _detection_ models have no suffix and are the default YOLO11 models, i.e. `yolo11n.pt` and are pretrained on COCO. See [Detection Docs](https://docs.ultralytics.com/tasks/detect/) for full details.

```{code-cell} ipython3
:id: 8Go5qqS9LbC5

# Load YOLO11n, train it on COCO128 for 3 epochs and predict an image with it
from ultralytics import YOLO

model = YOLO('yolo11n.pt')  # load a pretrained YOLO detection model
model.train(data='coco8.yaml', epochs=3)  # train the model
model('https://ultralytics.com/images/bus.jpg')  # predict on an image
```

+++ {"id": "7ZW58jUzK66B"}

## 2. Segmentation

YOLO11 _segmentation_ models use the `-seg` suffix, i.e. `yolo11n-seg.pt` and are pretrained on COCO. See [Segmentation Docs](https://docs.ultralytics.com/tasks/segment/) for full details.

```{code-cell} ipython3
:id: WFPJIQl_L5HT

# Load YOLO11n-seg, train it on COCO128-seg for 3 epochs and predict an image with it
from ultralytics import YOLO

model = YOLO('yolo11n-seg.pt')  # load a pretrained YOLO segmentation model
model.train(data='coco8-seg.yaml', epochs=3)  # train the model
model('https://ultralytics.com/images/bus.jpg')  # predict on an image
```

+++ {"id": "ax3p94VNK9zR"}

## 3. Classification

YOLO11 _classification_ models use the `-cls` suffix, i.e. `yolo11n-cls.pt` and are pretrained on ImageNet. See [Classification Docs](https://docs.ultralytics.com/tasks/classify/) for full details.

```{code-cell} ipython3
:id: 5q9Zu6zlL5rS

# Load YOLO11n-cls, train it on mnist160 for 3 epochs and predict an image with it
from ultralytics import YOLO

model = YOLO('yolo11n-cls.pt')  # load a pretrained YOLO classification model
model.train(data='mnist160', epochs=3)  # train the model
model('https://ultralytics.com/images/bus.jpg')  # predict on an image
```

+++ {"id": "SpIaFLiO11TG"}

## 4. Pose

YOLO11 _pose_ models use the `-pose` suffix, i.e. `yolo11n-pose.pt` and are pretrained on COCO Keypoints. See [Pose Docs](https://docs.ultralytics.com/tasks/pose/) for full details.

```{code-cell} ipython3
:id: si4aKFNg19vX

# Load YOLO11n-pose, train it on COCO8-pose for 3 epochs and predict an image with it
from ultralytics import YOLO

model = YOLO('yolo11n-pose.pt')  # load a pretrained YOLO pose model
model.train(data='coco8-pose.yaml', epochs=3)  # train the model
model('https://ultralytics.com/images/bus.jpg')  # predict on an image
```

+++ {"id": "cf5j_T9-B5F0"}

## 4. Oriented Bounding Boxes (OBB)

YOLO11 _OBB_ models use the `-obb` suffix, i.e. `yolo11n-obb.pt` and are pretrained on the DOTA dataset. See [OBB Docs](https://docs.ultralytics.com/tasks/obb/) for full details.

```{code-cell} ipython3
:id: IJNKClOOB5YS

# Load YOLO11n-obb, train it on DOTA8 for 3 epochs and predict an image with it
from ultralytics import YOLO

model = YOLO('yolo11n-obb.pt')  # load a pretrained YOLO OBB model
model.train(data='dota8.yaml', epochs=3)  # train the model
model('https://ultralytics.com/images/boats.jpg')  # predict on an image
```

+++ {"id": "IEijrePND_2I"}

# Appendix

Additional content below.

```{code-cell} ipython3
:id: pIdE6i8C3LYp

# Pip install from source
!uv pip install git+https://github.com/ultralytics/ultralytics@main
```

```{code-cell} ipython3
:id: uRKlwxSJdhd1

# Git clone and run tests on 'main' branch
!git clone https://github.com/ultralytics/ultralytics -b main
!uv pip install -qe ultralytics
```

```{code-cell} ipython3
:id: GtPlh7mcCGZX

# Run tests (Git clone only)
!pytest ultralytics/tests
```

```{code-cell} ipython3
:id: Wdc6t_bfzDDk

# Validate multiple models
for x in 'nsmlx':
  !yolo val model=yolo11{x}.pt data=coco.yaml
```
