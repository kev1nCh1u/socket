#!/bin/zsh
# Program:
#       This program start motion_capture
# History:
# 2021/10/23	kevin	First release

pathVar=$(pwd)
# echo "\nNow path:"
# echo $pathVar

# startPath="${pathVar}/src/kevin_start/src"
startPath="/home/kevin/src/socket/kevin_start"
# echo "\nStart path:"
# echo $startPath

PATH=$PATH:$startPath
# echo "\nNew system path:"
# echo $PATH