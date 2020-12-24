import hashlib
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-a", "--aim", type=str, help="will be md str")
args = parser.parse_args()

aim = "123"
if args.aim:
    aim = args.aim
mmm = hashlib.md5(aim.encode()).hexdigest()

print(f"{type(mmm)}: {mmm}")
