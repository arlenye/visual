from ultralytics import YOLO
import os
import torch
os.environ["KMP_DUPLICATE_LIB"] = "True"

# 检查是否有可用的GPU
def get_available_device():
    if torch.cuda.is_available():
        # 获取GPU数量和名称
        gpu_count = torch.cuda.device_count()
        gpu_name = torch.cuda.get_device_name(0)
        print(f"检测到可用GPU: {gpu_name} (共 {gpu_count} 个)")
        return "0"  # 使用第一个GPU，多GPU可指定为"0,1,2..."
    else:
        print("未检测到可用GPU，将使用CPU进行训练")
        return "cpu"

model = YOLO("yolo11n.yaml")
if __name__ == "__main__" :
    # 获取可用设备
    device = get_available_device()
    results = model.train(data = "smoke_fall.yaml", epochs = 2, imgsz = 640, device=device)