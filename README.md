# VRDL_project2

## Requirements

To install requirements:

```setup
pip install -r requirements.txt

```

# replace your picture in below instruction

```
my_dataset
├── images
│   ├── test  replace your testing picture here
│   ├── train replace your training picture here
│   ├── valid replace your validation picture here
├── labels
│   ├── train replace your training labels here
│   ├── valid replace your validation labels here
```

## Hardware

NVIDIA GeForce 3090

## Training

To train the model, run this command:

```train
python my_yolov3/train.py --data myDataset.yaml --weights yolov3.pt --img 320\
        --cfg yolov3.yaml --epochs 40 --device 0,1,2,3 --batch-size 64
```

## Generating answer.json

put the weights.pt in my_yolov3/weights and run:

```
python evaluation.py
```
## Model Weight Link
https://drive.google.com/file/d/1s0iiKQGh-MWlcchAs43w0zwvmGyr6bAw/view?usp=sharing
