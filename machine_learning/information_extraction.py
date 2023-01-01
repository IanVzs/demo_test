# python3.9.2
from paddlenlp import Taskflow

schema = ['时间', '人物', '事件', '地点']
ie = Taskflow('information_extraction', schema=schema)

text = [
    "8月5日——路易·拿破仑·波拿巴在布洛涅发动兵变失败被捕",
    "11月——在美国总统大选当中，威廉·亨利·哈里森击败了马丁·范布伦，成为美国第9任总统。",
    "12月15日——拿破仑一世遗骨运回巴黎。"
]
rst = ie(text)

for i in rst:
    print(f"{schema[0]}: {i[schema[0]][0]['text']}, \
        {schema[1]}: {i[schema[1]][0]['text']}, \
        {schema[2]}: {i[schema[2]][0]['text']}")