# 异常行为检测-Web端

## 功能简介
实现异常行为的检测，支持图片、离线视频、实时视频的检测

## 本地运行
```第一次运行前安装依赖
pip install -r requirements.txt
```

```commandline
cd codes/web
streamlit run app.py
```

## 部署方式
### 直接部署
* 1.安装conda
```commandline
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh
```

* 2.安装依赖
```commandline
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

* 3.将web文件夹打包，放到服务器上
* 4.进入web文件夹
```commandline
streamlit run app.py
```

### docker部署
* 1.生成镜像
```commandline
cd docker
./docker_build.sh
```

* 2.部署
```commandline
docker load -i <镜像>
docker run -p 8501:8501 streamlit
```