from ultralytics import YOLO
import os
os.environ["KMP_DUPLICATE_LIB"] = "True"
model = YOLO("yolo11s.yaml")
if __name__ == "__main__" :
    results = model.train(data = "smoke_fall.yaml", epochs = 100, imgsz = 640)