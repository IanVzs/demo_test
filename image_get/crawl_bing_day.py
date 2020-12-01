"""
抓取bing搜索每日图片

来源为一个第三方整理网站(套娃抓取)
"""
import requests
from bs4 import BeautifulSoup

def save_one_page(num_page: int) -> int:
    """
    rsp: 
    页面打开失败: 0
    图片保存失败: -n (失败多少个则为负数多少)
    图片保存成功: n (成多少个则为正数多少
    """
    url = f"http://tupian.sioe.cn/b/bing-home-image/?p={num_page}"
    aaa = requests.get(url, verify=False).content.decode()
    soup = BeautifulSoup(aaa, 'lxml')
    list_simg = soup.find_all("img")

    for dd in list_simg:
        """
        {'src': 'pic/small/20201013.jpg', 'alt': '赤狐，荷兰 (© Wim Weenink/Minden Pictures)'}
        """
        src = dd.attrs.get("src")
        alt = dd.attrs.get("alt")
        """
        完整图片链接示例: https://tupian.sioe.cn/b/bing-home-image/pic/20201101.jpg
        """
        bsrc = src.replace("small/", '')
        url_bimg = f"https://tupian.sioe.cn/b/bing-home-image/{bsrc}"
        img_content = requests.get(url_bimg, verify=False).content
        with open(bsrc, "wb") as f:
            f.write(img_content)
        size = int(len(img_content)/1024)
        print(f"{bsrc} saved: {size}Kb")

def save_all():
    is_page_exits = True
    num_page = 1
    list_page_err = 0
    while is_page_exits:
        sts = save_one_page(num_page)
        if sts == 0:
            list_page_err += 1
            if list_page_err > 3:
                is_page_exits = False
        elif sts > 0:
            list_page_err = 0
            print(f"----------------page: {num_page} sucess {sts}.---------------")
        elif sts < 0:
            list_page_err = 0
            print(f"----------------page: {num_page} failed {sts}.---------------")
        num_page += 1
            
if "__main__" == __name__:
    pass