from ultralytics import YOLO
import os
os.environ["KMP_DUPLICATE_LIB"] = "True"
model = YOLO("yolo11n.yaml")
if __name__ == "__main__" :
    results = model.train(data = "smoke_fall.yaml", device = 0, epochs = 100, imgsz = 640)