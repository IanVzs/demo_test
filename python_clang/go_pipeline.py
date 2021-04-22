"""
无缝链接`bash`
通过重定向/管道/文件接受输入
echo "hinihaohi" | python3 go_pipeline.py | grep "ao"
"""
import fileinput

with fileinput.input() as f_input:
    for line in f_input:
        print(line, end='')

