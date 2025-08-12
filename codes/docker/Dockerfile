# 使用官方的 Python 3.12 作为基础镜像
FROM python:3.12-slim

# 设置工作目录
WORKDIR /code

# 将代码等相关文件复制到容器中
COPY ./web .

# 升级pip
RUN pip install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple

# 安装依赖项  --no-cache-dir（代表了不适用缓存的依赖，会重新下载依赖，耗时较久，但是镜像体积会较小）
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

# 暴露 8501 端口
EXPOSE 8501

# 设置容器启动命令
ENTRYPOINT ["streamlit", "run", "/code/web/app.py"]