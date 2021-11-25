# VRDL_project1

## Requirements

To install requirements:

```setup
pip install -r requirements.txt
pip install -r my_yolov3/requirements.txt

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
https://drive.google.com/drive/folders/1qMi1xaPWkpJr7vNadyh4fJ_niqN22O92?usp=sharing
