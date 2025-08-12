#!/bin/bash

# 产品版本
product_version="v1.0"

function build_image()
{
    work_path=$(pwd)
    echo "当前目录："$work_path

    # 清理当前代码目录
    echo "清理web"
    cd web
    rm -rf *

    cd ../../
    project_path=$(pwd)
    echo "当前项目路径："$project_path

    # 获取当前分支名称
    branch=$(git symbolic-ref --short -q HEAD)
    echo "当前分支名称："$branch

    # 获取当前分支最后commitId
    latest_commit_id=$(git rev-parse --short HEAD)
    echo "当前分支最后commitId："$latest_commit_id

    # 将代码拷贝到docker目录中
    cp -r $project_path"/web/" $project_path"/docker/web"
    cd $project_path"/docker"
    ls

    # 构建镜像名称 工程名称:版本号_分支名称_日期_时间_commitid
    time=$(date "+%Y%m%d_%H%M%S")
    tag=$product_version"_"$branch"_"$time"_"$latest_commit_id
    docker_name=$1":"$tag

    # 执行Dockerfile生成镜像
    sudo docker build -t $docker_name .
    echo "镜像生成完成！"
}

project_name="visual-anomaly-detection"
build_image $project_name