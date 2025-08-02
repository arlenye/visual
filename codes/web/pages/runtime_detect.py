"""
 filename：    runtime_detect
 author：      Tim
 date：        2025/8/2 06:28
 description： 实时分析
"""

import streamlit as st
import tempfile
from common.infer import display_detected_frames
import cv2

st.header("实时分析")

# 设置检测的最小置信度阈值。 将忽略置信度低于此阈值的检测到的对象。 调整此值有助于减少误报。默认0.25
confidence = float(st.slider('阈值设置', 25, 100, 30)) / 100

# 创建一个单行文本输入框
video_path = st.text_input('请输入在线视频地址')


def click_button():
    if video_path:
        st.video(video_path, autoplay = True)

        # TODO 视频展示较慢。循环展示结果？
        try:
            tfile = tempfile.NamedTemporaryFile()
            tfile.write(video_path.read())
            vid_cap = cv2.VideoCapture(tfile.name)
            st_frame = st.empty()

            while (vid_cap.isOpened()):
                success, image = vid_cap.read()
                if success:
                    display_detected_frames(st_frame, image, confidence)
                else:
                    vid_cap.release()
                    break
        except Exception as e:
            st.error(f"Error loading video: {e}")
    else:
        st.error('在线视频地址不能为空')


st.button('检测', on_click = click_button)
