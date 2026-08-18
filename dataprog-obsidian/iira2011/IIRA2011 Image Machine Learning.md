
# IIRA2011 Image Machine Learning

+ Annotation
+ COCO/YOLO Conversion
+ Training and testing in torch
+ Predefined models
+ Training in Yolo

## Components of a Machine Learining Model

1. Problem templates
	1. Regression
	2. Classification
	3. Detection 
	4. Segmentation
2. Model architecture
	1. Neural network
	2. Optimised
	3. Loss function
	4. Pre-trained models
3. Dataset
	1. images 
	2. annotations
		1. YOLO
		2. COCO
	3. loader
		1. custom loader in torch 
		2. config file for Yolo
4. Preprocessing
	1. Object type
	2. Image size
	3. Data type (float)
	4. Scaling
5. Training and testing
6. Evaluation
	1. heuristics
	2. plots
	3. difficult cases


## torch normalise

```
from torchvision.transforms import v2
transforms = v2.Compose([
    v2.ToImage(),  # Convert to tensor, only needed if you had a PIL image
    v2.ToDtype(torch.uint8, scale=True),  # optional, most input are already uint8 at this point
    # ...
    v2.RandomResizedCrop(size=(224, 224), antialias=True),  # Or Resize(antialias=True)
    # ...
    v2.ToDtype(torch.float32, scale=True),  # Normalize expects float input
    v2.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])
```