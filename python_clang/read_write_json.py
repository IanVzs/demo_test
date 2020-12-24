# -*-coding: utf-8-*-
"""写入、读取JSON文件"""

import os
import json


def read_json(path):
    """读取JOSN文件"""
    with open(path, 'r') as file_data:
        try:
            data_json = json.loads(file_data.read())
        except json.decoder.JSONDecodeError:
            data_json = {}
    return data_json


def write_json(path, data, para='a'):
    """写入JSON文件，默认添加的方式"""
    with open(path, para) as file_data:
        file_data.write(json.dumps(data, ensure_ascii=False))
    return 1

if __name__ == "__main__":
    TEST_PATH = "hello.json"
    write_json(TEST_PATH, {"a": 123})
    print(read_json(TEST_PATH))
    # 显示
    write_json(TEST_PATH, {"a": 123})
    print(read_json(TEST_PATH))
    # 因为'a'添加模式 文件变为非JSON格式，loads出错
    write_json(TEST_PATH, {"a": 123, "kanji": "漢字"}, 'w')
    print(read_json(TEST_PATH))
    # 覆盖式写入，显示
    os.remove(TEST_PATH)
