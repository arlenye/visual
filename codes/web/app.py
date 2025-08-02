"""
 filename：    app
 author：      Tim
 date：        2025/8/2 06:26
 description： 主应用，负责启动应用和配置
"""

import streamlit as st


def main():
    img_detect_page = st.Page("pages/img_detect.py", title = "图片分析", default = True)
    video_detect_page = st.Page("pages/video_detect.py", title = "视频分析")
    runtime_detect_page = st.Page("pages/runtime_detect.py", title = "实时分析")
    about_page = st.Page("pages/about.py", title = "关于")

    pg = st.navigation(pages = [img_detect_page, video_detect_page, runtime_detect_page, about_page])
    pg.run()


# main
if __name__ == '__main__':
    main()
