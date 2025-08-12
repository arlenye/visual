"""
 filename：    video_detect
 author：      Tim
 date：        2025/8/2 06:28
 description： 视频分析
"""
import os

import cv2
import streamlit as st
import tempfile
from common.infer import detect_video
from common.tool import get_timestamp

st.header("视频分析")

# 设置检测的最小置信度阈值。 将忽略置信度低于此阈值的检测到的对象。 调整此值有助于减少误报。默认0.25
confidence = float(st.slider('阈值设置', 25, 100, 30)) / 100

# 上传本地视频文件
video_file = st.file_uploader("上传视频文件", type = ["mp4", "mov", "avi"])
if video_file is not None:
    # 播放上传的视频
    st.video(video_file, format = "video/mp4", start_time = 0, autoplay = True)

    # 设置进度条的初始文本
    progress_text = "视频解析进行中，请稍候。"
    percent_complete = 0
    # 创建一个进度条对象
    detect_bar = st.progress(percent_complete, text = progress_text)

    # 保存文件
    current_dir = os.path.dirname(os.path.abspath(__file__))
    detected_video_name = str(get_timestamp()) + "_output.mp4"
    detected_video_path = os.path.join(current_dir, "detected_videos", detected_video_name)
    detected_video_path = os.path.normpath(detected_video_path)  # 规范化路径

    # 展示进度条，在解析中，保存视频，最后播放解析后的视频
    try:
        tfile = tempfile.NamedTemporaryFile()
        tfile.write(video_file.read())
        vid_cap = cv2.VideoCapture(tfile.name)

        # 获取视频帧的维度
        frame_width = int(vid_cap.get(3))
        frame_height = int(vid_cap.get(4))

        # 获取视频的总帧数
        total_frames = int(vid_cap.get(cv2.CAP_PROP_FRAME_COUNT))

        # 创建VideoWriter对象
        fourcc = cv2.VideoWriter_fourcc(*'avc1')
        out = cv2.VideoWriter(detected_video_path, fourcc, 20.0, (frame_width, frame_height))  # 保存检测后视频的地址

        read_frames = 0
        while vid_cap.isOpened():
            success, image = vid_cap.read()
            if success:
                res_plotted = detect_video(image, confidence)
                out.write(res_plotted)  # 写入保存
            else:
                break

            read_frames = read_frames + 1

            percent_complete = read_frames / total_frames
            detect_bar.progress(percent_complete, text = progress_text)

        vid_cap.release()
        out.release()

        detect_bar.progress(100, text = "视频解析完成")
        print("视频解析并保存完成，文件路径：" + detected_video_path)

        # 播放解析后的视频
        detected_video_file = open(detected_video_path, 'rb')
        detected_video_file_bytes = detected_video_file.read()
        st.video(detected_video_file_bytes, format = "video/mp4", start_time = 0, autoplay = True)

    except Exception as e:
        st.error(f"Error detecting video: {e}")
