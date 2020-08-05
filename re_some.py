"""正则"""
import re

def get_hanji(str_data: str):
    """"""
    pat = re.compile(r'[\u4e00-\u9fa5]+')
    # pat = re.compile(r'[\u4e00-\u9fa5]')
    hanji_list = pat.findall(str_data)
    return hanji_list

def get_letters(str_data):
    pat = re.compile(r'[a-zA-Z]+')
    # pat = re.compile(r'[a-zA-Z]')
    letters_list = pat.findall(str_data)
    return letters_list

def get_letters_num(str_data):
    pat = re.compile(r'[a-zA-Z0-9]+')
    # pat = re.compile(r'[a-zA-Z0-9]')
    letters_list = pat.findall(str_data)
    return letters_list

if __name__ == "__main__":
    func_list = (get_hanji, get_letters, get_letters_num)
    for i in func_list:
        gets = i("你好hi, 世界あ哈sa21哈df3哈哈43434哈")
        print(gets)
