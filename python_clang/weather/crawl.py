# import lxml
import json
import requests
from re import L
from bs4 import BeautifulSoup

def api_get(url):
    resp = requests.get(
        url,
        headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"}
    )
    return resp

def crawl_base_data(city_code):
    resp = api_get(f"http://m.weathercn.com/zh/cn/shunyi-district/{city_code}/current-weather/{city_code}?lang=zh-cn&unit=c&partner=sonymobilecalendar")
    soup = BeautifulSoup(resp.content, 'html.parser', from_encoding='utf-8')
    base_data = {}

    list_label = [
        "当前天气",
        None,
        "更新时间",
        None,
        "今日天气",
        "湿度",
        "紫外线",
        "能见度",

        None,
        None,
        None,
        None,
        None,
        None,
        None,
        "日出日落",

        None,
        None,
        None,
        None,
        None,
        None
    ]
    for i, v in enumerate(soup.find_all('p')):
        # import ipdb; ipdb.set_trace()
        if list_label[i] != None:
            v = v.text.replace("\n", '')
            base_data[list_label[i]] = v
    return base_data

def crawl_sport_data(city_code, sport_code):
    resp = api_get(f"http://m.weathercn.com/indexs-detail.do?day=1&partner=sonymobilecalendar&id={city_code}&p_source=&p_type=&indexId={sport_code}")
    soup = BeautifulSoup(resp.content, 'html.parser', from_encoding='utf-8')
    sport_data = {}
    ret = {}
    for i in soup.find_all("script"):
        if i.contents and "var days =" in i.contents[0] and "var bigData =" in i.contents[0]:
            i = i.contents[0].replace("\t", '').replace("\r", '').replace("\n", '').split("var ")
            for ii in i:
                if "days =" in ii:
                    ii = ii.replace("days =", '').replace(";", '').replace("'", '"')
                    # import ipdb; ipdb.set_trace()
                    ii = json.loads(ii)
                    sport_data["days"] = ii
                elif "bigData =" in ii:
                    ii = ii.replace("bigData =", '').replace(";", '').replace("'", '"').replace('y', '"y"').replace('val', '"val"')
                    ii = json.loads(ii)
                    sport_data["bigData"] = ii
                    # import ipdb; ipdb.set_trace()
                elif "smallData =" in ii:
                    ii = ii.replace("smallData =", '').replace(";", '').replace("'", '"').replace('y', '"y"').replace('val', '"val"')
                    ii = json.loads(ii)
                    sport_data["smallData"] = ii
                    # import ipdb; ipdb.set_trace()
    for i, v in enumerate(sport_data.get("days")):
        ret[v] = f'{sport_data["smallData"][i]["val"]}({sport_data["smallData"][i]["y"]}) - {sport_data["bigData"][i]["val"]}({sport_data["bigData"][i]["y"]})'
    return ret

def main():
    base_data = crawl_base_data(city_code=57520)
    print(base_data)
    sport_data = crawl_sport_data(city_code=57520, sport_code=1)
    print(sport_data)

if __name__ == "__main__":
    main()