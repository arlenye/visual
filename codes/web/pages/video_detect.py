"""
 filename：    video_detect
 author：      Tim
 date：        2025/8/2 06:28
 description： 视频分析
"""
import cv2
import streamlit as st
import tempfile
from common.infer import display_detected_frames

st.header("视频分析")

# 设置检测的最小置信度阈值。 将忽略置信度低于此阈值的检测到的对象。 调整此值有助于减少误报。默认0.25
confidence = float(st.slider('阈值设置', 25, 100, 30)) / 100

# 上传本地视频文件
video_file = st.file_uploader("上传视频文件", type = ["mp4", "mov", "avi"])
if video_file is not None:
    # 播放上传的视频
    st.video(video_file, format = "video/mp4", start_time = 0, autoplay = True)

    # TODO 视频展示较慢。循环展示结果？
    try:
        tfile = tempfile.NamedTemporaryFile()
        tfile.write(video_file.read())
        vid_cap = cv2.VideoCapture(tfile.name)
        st_frame = st.empty()

        while vid_cap.isOpened():
            success, image = vid_cap.read()
            if success:
                display_detected_frames(st_frame, image, confidence)
            else:
                vid_cap.release()
                break
    except Exception as e:
        st.error(f"Error detecting video: {e}")