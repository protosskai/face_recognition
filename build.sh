#!/bin/bash

# 配置anaconda的路径
CONDA_PATH=~/software/anaconda3
# 配置所使用的conda的环境
CONDA_ENV="face"
# 找到conda环境中的Python解释器
PYTHON=$CONDA_PATH/envs/$CONDA_ENV/bin/python

build(){
  # 将所有的ui文件编译成py文件
  UI_PATH="./ui"
  UI_FILES=$(ls $UI_PATH | grep ui)
  for filename in $UI_FILES
  do
    # 文件名去掉ui后缀,并且增加base前缀和.py后缀
    filename_new=base${filename%%.ui}.py
    # 生成py文件
    pyuic5 -o ./base/$filename_new $UI_PATH/$filename
  done

}


# 程序的入口
if [ $# -lt 1 ]; then
  # 打印提示信息
  echo -e "Usage:  $0 build  构建项目\n\t./build.sh run    运行项目"
  exit 1
fi

if [ $1 = "build" ];
then
  # 构建项目，把所有ui文件转为py文件
  build
elif [ $1 = "run" ];
then
  # 运行项目
  $PYTHON EntryWindow.py
fi

