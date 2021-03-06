from my_yolov3.detect import run
import shutil
import os
from PIL import Image
import os
import json

weights = 'my_yolov3/weights/weights.pt'
source = "my_dataset/images/test/"
imgsz = [320, 320]
conf_thres = 0.05
iou_thres = 0.8
max_det = 4
device = ""
view_img = False
save_txt = True
save_conf = True
save_crop = False
nosave = False
classes = None
agnostic_nms = False
augment = False
visualize = False
update = False
project = "runs/detect"
name = "test"
exist_ok = False
line_thickness = 3
hide_labels = False
hide_conf = False
half = False
dnn = False


def model(source=source, weights=weights):
    if os.path.exists("runs"):
        shutil.rmtree("runs")

    pred = run(
        weights=weights,
        source=source,
        imgsz=imgsz,
        conf_thres=conf_thres,
        iou_thres=iou_thres,
        max_det=max_det,
        device=device,
        view_img=view_img,
        save_txt=save_txt,
        save_conf=save_conf,
        save_crop=save_crop,
        nosave=nosave,
        classes=classes,
        agnostic_nms=agnostic_nms,
        augment=augment,
        visualize=visualize,
        update=update,
        project=project,
        name=name,
        exist_ok=exist_ok,
        line_thickness=line_thickness,
        hide_labels=hide_labels,
        hide_conf=hide_conf,
        half=half,
        dnn=dnn,
        )

    return pred

if __name__ == "__main__":
    model_detection_output = model()
    data_listdir = os.listdir("my_dataset/images/test/")
    data_listdir.sort(key=lambda x: int(x[:-4]))
    TEST_IMAGE_NUMBER = 13068
    result_to_json = []

    num = 0
    # for each test image
    for img_name in data_listdir:
        num += 1
        print("json:", num)
        # the image_name is as same as the image_id
        image_id = int(img_name[:-4])

        # add each detection box infomation into list
        if model_detection_output[img_name] == []:
            continue

        for det_box in model_detection_output[img_name]:
            det_box_info = det_box

            # An integer to identify the image
            image_id = det_box_info["image_id"]

            # A list ( [left_x, top_y, width, height] )
            det_box["bbox"] = det_box_info["bbox"]

            # A float number between 0~1 which means the confidence of the bbox
            det_box["score"] = det_box_info["score"]

            # An integer which means the label class
            det_box["category_id"] = det_box_info["category_id"]

            result_to_json.append(det_box_info)

        # Write the list to answer.json
        json_object = json.dumps(result_to_json, indent=4)

        with open("answer.json", "w") as outfile:
            outfile.write(json_object)

    if os.path.exists("runs"):
        shutil.rmtree("runs")
