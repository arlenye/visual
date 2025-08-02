"""
 filename：    img_detect
 author：      Tim
 date：        2025/8/2 06:27
 description： 图片分析
"""
import cv2
import numpy as np
import streamlit as st
from PIL import Image
from common.infer import detect

st.header("图片分析")

# 设置检测的最小置信度阈值。 将忽略置信度低于此阈值的检测到的对象。 调整此值有助于减少误报。默认0.25
confidence = float(st.slider('阈值设置', 25, 100, 30)) / 100

img_file = st.file_uploader("选择一张图片", type = ["jpg", "jpeg", "png"])

if img_file is not None:
    # 使用PIL打开图片
    image = Image.open(img_file)

    # 使用两列展示数据
    col1, col2 = st.columns(2)

    with col1:
        # 展示图片
        st.image(image, caption = "上传的图片", use_column_width = True)

    # 转换为OpenCV格式 (YOLO需要)
    opencv_image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

    # 显示检测到的对象
    result_list, res_plotted = detect(opencv_image, confidence)

    with col2:
        st.image(res_plotted,
                 caption = "检测结果",
                 use_column_width = True)

    st.write("检测结果详细:")
    for result in result_list:
        st.write("异常行为：" + result["class_name"], "可信度：" + result["score"])
