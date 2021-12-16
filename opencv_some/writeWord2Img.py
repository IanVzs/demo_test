import cv2
img = cv2.imread("/home/ian/Downloads/20211215_150909.jpeg")
# cv2.putText(img, "hahahah汉字", (123, 123), cv2.FONT_ITALIC, 2, (0, 255, 0), 3)

import numpy as np
from PIL import ImageFont, ImageDraw, Image

def addChinese2ImgCV2(img, text, position, textColor=(0,0,0), textSize=30)-> (np.ndarray, bool):
    if not isinstance(img, np.ndarray):
        return img, False

    font = ImageFont.truetype('./simsun.ttc', textSize)
    img_pil = Image.fromarray(img)
    draw = ImageDraw.Draw(img_pil)
    draw.text(position, text, font = font, fill = textColor)
    img = np.array(img_pil)
    return img, True

# img, ok = addChinese2ImgCV2(img, "jiuyao\n\n就要过年啦～～～～！！！！", (1, 1), (0, 0, 0, 1), textSize=16)

list_axieid = ["1224567862", "1224567862", "1224567862","1224567862","1224567862","1224567862"]
json_our_info = {1: {"血量": 100, "buff": "None, None", "axie_id": "asudgugasdg"}, 2: {"血量": 500, "buff": "None, None"}, 3: {"血量": 450, "buff": "None", "axie_id": "245672563467"}}
json_enemy_info = json_our_info
list_cards = ["sajdhjkasdh","asdhajs asdh asdh",  "kill_name1", "kill_name1", "kill_name1", "kill_name1", "kill_name1", "kill_name1", "kill_name1", "kill_name1", "kill_name1", "kill_name1", "kill_name1","kill_name1"]
model_rst_cards = ["sajdhjkasdh","asdhajs asdh asdh",  "kill_name1", "kill_name1", "kill_name1", "kill_name1", "kill_name1", "kill_name1", "kill_name1", "kill_name1", "kill_name1", "kill_name1", "kill_name1","kill_name1"]

json_text0 = f"出手顺序: {[i for i in list_axieid]}"
json_text1 = """
    our:
"""
import json
json_text1 += json.dumps(json_our_info, indent=4, ensure_ascii=False)
json_text1 = json_text1.replace('"', '').replace("{", '').replace("}", '').replace("\n\n", "\n").replace(" ,\n ", '')

json_text2 = """
    enmey:
"""
json_text2 += json.dumps(json_enemy_info, indent=4, ensure_ascii=False)
json_text2 = json_text2.replace('"', '').replace("{", '').replace("}", '').replace("\n\n", "\n").replace(" ,\n ", '')


json_text3 = """
    剩余能量: 9,                endturn位置: [x, y]
    持有手牌信息: {},
"""
print_cards = []
for i, v in enumerate(list_cards):
    print_cards.append(v)
    if i % 5 ==0 and i != 0:
        print_cards.append("\n\t\t\t")
        
print_rst_cards = []
for i, v in enumerate(model_rst_cards):
    print_rst_cards.append(v)
    if i % 8 ==0 and i != 0:
        print_rst_cards.append("\n\t\t\t\t\t")
json_text3 = json_text3.format(','.join(print_cards))
# json_text = json.dumps(json_text, indent=4, ensure_ascii=False)
# print(json_text)
# img, ok = addChinese2ImgCV2(img, json_text0, (3, 0), (255, 255, 0), textSize=32)
# img, ok = addChinese2ImgCV2(img, json_text1, (3, 50), (255, 255, 0), textSize=32)
# img, ok = addChinese2ImgCV2(img, json_text2, (850, 50), (255, 255, 0), textSize=32)
# img, ok = addChinese2ImgCV2(img, json_text3, (0, 550), (255, 255, 0), textSize=32)
img, ok = addChinese2ImgCV2(img, json_text0, (3, 0), (2, 2, 0), textSize=32)
img, ok = addChinese2ImgCV2(img, json_text1, (3, 50), (5, 5, 0), textSize=32)
img, ok = addChinese2ImgCV2(img, json_text2, (850, 50), (2, 5, 0), textSize=32)
img, ok = addChinese2ImgCV2(img, json_text3, (0, 550), (2, 2, 0), textSize=32)
img, ok = addChinese2ImgCV2(img, '\t\t\t\t模型结果: '+','.join(print_rst_cards), (0, 800), (255, 255, 255), textSize=24)
if ok:
    cv2.imshow("source", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

