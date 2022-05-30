"""
命令行OpenCV App
"""
import os
import cv2
from loguru import logger
import argparse
import numpy as np

parser = argparse.ArgumentParser()
commands_help = """
resize: 转换图片到指定分辨率\n\t- para: 720,1080,4k\n

"""
parser.add_argument("command", type=str, help=commands_help)
parser.add_argument("-para", "--parameter", type=str, help="")
parser.add_argument("img_path", type=str, help="图片地址")

ARGS = parser.parse_args()

command = ARGS.command

def resize(img):
    list_path = list(os.path.split(ARGS.img_path))
    file_name = list_path[-1]
    suffix = ''
    if '.' in file_name:
        file_name = file_name.split(".")
        suffix = file_name[-1]
        file_name = '.'.join(file_name[:-1])
        
    list_new_path = list_path[:-1]
    list_new_path.append(file_name + f"-{ARGS.parameter}." + suffix)
    if len(list_new_path) != 2:
        logger.warning(f"resize path error: {list_new_path}")
        return
    new_path = os.path.join(list_new_path[0], list_new_path[-1])

    resize_data = {
        "720": (1280, 720),
        "1080": (1920, 1080),
        "4k": (3840, 2160),
        }.get(ARGS.parameter)
    if resize_data:
        img = cv2.resize(img, resize_data)
        cv2.imwrite(new_path, img)

    logger.info(f"resize done -> {new_path}")

IMG = None
func = locals().get(command)

if not func:
    logger.error(f"没有找到该方法: {command}\n\n方法库中有: {[i for i in locals().keys() if isinstance(eval(i), type(resize))]}")

if func and not os.path.isfile(ARGS.img_path):
    logger.error(f"找不到该图片 {ARGS.img_path}")

IMG = cv2.imread(ARGS.img_path)

if __name__ == "__main__" and func and isinstance(IMG, np.ndarray):
    func(IMG)
