import cv2
import numpy as np

from typing import List
from pydantic import BaseModel

class RangeInfo(BaseModel):
    lable: str
    x_min: int = 0
    x_max: int = 0
    y_min: int = 0
    y_max: int = 0
    img: np.ndarray = None
    
    class Config:
        arbitrary_types_allowed = True
    

def get_shape(list_info: List[RangeInfo]):
    """
    将X拼起来，获取Y的最大值
    list_info:
        List(RangeInfo)

    return:
        x_sum, y_max
    """
    x_sum = 0
    y_max = 0
    for i in list_info:
        _y, _x, _ = i.img.shape
        x_sum += _x
        if _y > y_max:
            y_max = _y
    return x_sum, y_max

def merge(list_img_info: List[RangeInfo]) -> np.ndarray:
    x, y = get_shape(list_img_info)
    img = np.zeros((y, x, 3), np.uint8)

    cursor = 0
    for n, i in enumerate(list_img_info):
        _y, _x, _ = i.img.shape
        i.y_min = y-_y
        i.y_max = y
        i.x_min = cursor
        i.x_max = _x+cursor
        img[ i.y_min: i.y_max, i.x_min: i.x_max] = i.img
        list_img_info[n] = i
        cursor += _x
    #     cv2.imshow("merge_result", img)
    #     cv2.waitKey()
    # cv2.destroyAllWindows()
    return img

if __name__ == "__main__":
    import os
    list_img_info = []
    for i in os.listdir("img_number"):
        _path = os.path.join("img_number", i)
        lable = i.split('.')[0]
        _img = cv2.imread(_path)
        if _img is None:
            print(f"fuck: {i}")
            continue
        _range_info = RangeInfo(lable=lable, img=_img)
        list_img_info.append(_range_info)

    img = merge(list_img_info)

    res = [
        {"lable": "290", "x": 30},
        {"lable": "272", "x": 90},
        {"lable": "320", "x": 150},
        {"lable": "188", "x": 210},
        {"lable": "4", "x": 265},
        {"lable": "11", "x": 295},
        {"lable": "2", "x": 330},
        {"lable": "2", "x": 365},
    ]
    _x_dict = {}
    for i in res:
        _x_dict[i['x']] = i["lable"]
    
    for x, v in _x_dict.items():
        for i in list_img_info:
            if x > i.x_min and x < i.x_max:
                print(f"{i.lable} -> {v}")
                continue
    cv2.imshow("merge_result", img)
    cv2.waitKey()
    cv2.destroyAllWindows()
