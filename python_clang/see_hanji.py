"""
将文件中编码有问题的汉字换成我能看得懂的
"""
def format_word(file_path, aim_path):
    """
    执行para_data后， 将print写入文件，但Linux >> 写入有编码问题， 需要在手动重新编码

    不如直接把print换为 写文件，然而懒
    """
    import csv
    with open(aim_path,'w',newline='',encoding='utf-8-sig') as f:
        with open(file_path, 'r') as r:
            for i in r:
                print(i)
                f.write(str(i))

if "__main__" == __name__:
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=str, help="文件路径")
    parser.add_argument("-to", "--to_path", type=str, help="保存文件路径")
    args = parser.parse_args()

    file_path = args.path
    aim_path = ''
    if not args.to_path:
        t = file_path.split(".")[-1]
        h = ''.join(file_path.split(".")[:-1])
        aim_path = f"{h}_aim.{t}"
    else:
        aim_path = args.to_path
    format_word(file_path, aim_path)
