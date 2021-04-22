import argparse
parser = argparse.ArgumentParser()
parser.add_argument("data_dir", type=str, help="训练数据地址")
parser.add_argument("output_dir", type=str, help="模型输出保存路径/训练日志输出路径")

args = parser.parse_args()
data_dir = args.data_dir
output_dir = args.output_dir
