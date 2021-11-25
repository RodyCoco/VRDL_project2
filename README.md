# VRDL_project2


## Acknowledge
```
yolov3: https://github.com/ultralytics/yolov3.git
The folder my_yolov3 is rewritten from the above github resources.
```

## Requirements

To install requirements:

```setup
pip install -r requirements.txt

```

## put the weights.pt in my_yolov3/weights and testing images in my_dataset/images/test

## Hardware

NVIDIA GeForce 3090

## Preprocessing for Training


First put all train images provided in homework in my_dataset/images/train
Then run
```
python split_data.py
```
to split train data into train and valid, and it will also create the labels in my_dataset/label/train and in my_dataset/label/valid


## Training
run:

```
python my_yolov3/train.py --data myDataset.yaml --weights yolov3.pt --img 320\
        --cfg yolov3.yaml --epochs 40 --device 0,1,2,3 --batch-size 64
```

## Generating answer.json to reproduce the performance

run:(Needweights in the above instruction)

```
python evaluation.py
```
## Model Weight Link
https://drive.google.com/file/d/1s0iiKQGh-MWlcchAs43w0zwvmGyr6bAw/view?usp=sharing
