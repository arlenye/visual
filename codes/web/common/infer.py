"""
 filename：    infer
 author：      Tim
 date：        2025/8/2 14:24
 description： 推理
"""
import os

import cv2
from matplotlib import pyplot as plt
from ultralytics import YOLO
from common.tool import round_score
from common.tool import get_class_name

# 使用绝对路径读取文件
current_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(current_dir, "..", "model", "best.pt")
model_path = os.path.normpath(model_path)  # 规范化路径

model = YOLO(model = model_path)


def detect(image, conf):
    # 只上传一张图片，这里结果只有一个
    results = model.predict(source = image, conf = conf)

    # 提取检测结果
    result_list = []
    for result in results:
        classes = result.boxes.cls  # 类别索引
        scores = result.boxes.conf  # 置信度分数
        boxes = result.boxes.xyxy  # 边界框坐标

        # 如果有类别名称，可以通过类别索引获取
        class_names = [model.names[int(cls)] for cls in classes]

        # 打印检测结果
        for class_name, score, box in zip(class_names, scores, boxes):
            item = {"class_name": get_class_name(class_name), "score": round_score(score.item()), "box": box}
            result_list.append(item)

    res_plotted = results[0].plot()[:, :, ::-1]  # 带框的图，只有一个，多个检测结果也在一张图上
    return result_list, res_plotted


def display_detected_frames(image, conf):
    # Resize the image to a standard size
    image = cv2.resize(image, (720, int(720 * (9 / 16))))

    # Predict the objects in the image using YOLOv8 model
    res = model.predict(source = image, conf = conf)
    print("video detect", res[0])

    score = res[0].boxes.conf  # 置信度分数
    print(score)

    if score.numel():
        # score_item = score.item()
        # print(score_item)

        # Plot the detected objects on the video frame
        res_plotted = res[0].plot()

        return res_plotted[:, :, ::-1]
        # st_frame.image(res_plotted,
        #                caption = '检测后的视频',
        #                channels = "BGR",
        #                use_column_width = True
        #                )
    else:
        print("detect empty")
        return None


def detect_video(frame, conf, is_save = True):
    res = model.predict(source = frame, conf = conf, save = is_save)

    # Plot the detected objects on the video frame
    res_plotted = res[0].plot()

    return res_plotted


# test
if __name__ == '__main__':
    path = "../testimg/fall_370.jpg"
    res, img = detect(path, 0.25)
    print(type(res))
    print(len(res))
    print(res[0]["class_name"])
    print(res[1]["class_name"])

    print(res[0]["score"])
    print(res[1]["score"])

    # 画出图
    plt.imshow(X = img)
    plt.show()
