#!/bin/bash
# Program:
#       This program start socket
# History:
# 2022/6/10	kevin	First release

echo -e "\033[32m
##############################
# socket
# by Kevin Chiu 2022
##############################
\033[0m"
ws_path="/home/kevin/src/socket/" # 路徑
# ws_path=$(pwd) # 自動路徑
echo -e "ws_path:" $ws_path "\n" # 列印路徑
cd $ws_path
# source devel/setup.bash

python3.8 src/robot_udp_send.py