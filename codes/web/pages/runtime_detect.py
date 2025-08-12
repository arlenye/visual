"""
 filename：    runtime_detect
 author：      Tim
 date：        2025/8/2 06:28
 description： 实时分析
"""

import streamlit as st
from common.infer import display_detected_frames
import cv2

st.header("实时分析")

# 设置检测的最小置信度阈值。 将忽略置信度低于此阈值的检测到的对象。 调整此值有助于减少误报。默认0.25
confidence = float(st.slider('阈值设置', 25, 100, 60)) / 100

# 创建一个单行文本输入框
video_path = st.text_input('请输入在线视频地址')


def start_detect():
    if video_path:
        st.video(video_path, autoplay = True)

        # 初始化session state
        if 'frame_index' not in st.session_state:
            st.session_state.frame_index = 0
        if 'frames' not in st.session_state:
            st.session_state.frames = [None, None, None]

        # 创建三个图像占位符
        st.subheader("检测报警")
        cols = st.columns(3)
        placeholders = [cols[0].empty(), cols[1].empty(), cols[2].empty()]

        try:
            vid_cap = cv2.VideoCapture(video_path)
            while vid_cap.isOpened():
                # 跳过指定帧数
                for _ in range(20):
                    vid_cap.grab()  # 跳过帧但不解码

                success, image = vid_cap.read()
                if success:
                    # st_frame = st.empty()
                    res_plotted = display_detected_frames(image, confidence)

                    if res_plotted is not None:
                        # 更新当前帧索引
                        current_index = st.session_state.frame_index % 3
                        st.session_state.frames[current_index] = res_plotted
                        st.session_state.frame_index += 1

                        # 更新所有三个位置的图像
                        for i in range(3):
                            idx = (current_index - i) % 3
                            if st.session_state.frames[idx] is not None:
                                placeholders[i].image(
                                    st.session_state.frames[idx],
                                    caption = f"报警 {i + 1}",
                                    use_column_width = True
                                )
                else:
                    vid_cap.release()
                    break
        except Exception as e:
            raise e
            # st.error(f"Error detecting video: {e}")
    else:
        st.error('在线视频地址不能为空！')


st.button('检测', on_click = start_detect)
