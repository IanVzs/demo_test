# import lxml
import json
import requests
from re import L
from datetime import datetime
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
    # import ipdb; ipdb.set_trace()
    base_data = {}
    detail_data = {}
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
            detail_data[list_label[i]] = v
    
    wind_data = {}
    for i in soup.find_all("dd"):
        ii = i.find_all("strong")
        if len(ii) == 3:
            wind_data[ii[0].text] = f"{ii[1].text} {ii[2].text}"
    base_data["当前信息"] = {k:v for k, v in detail_data.items() if k in ("当前天气", "更新时间")}
    base_data["概览信息"] = {k:v for k, v in detail_data.items() if k not in ("当前天气", "更新时间")}
    base_data["风"] = wind_data
    return base_data

def crawl_rich_data(city_code, sport_code):
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
        # ret[v] = f'{sport_data["smallData"][i]["val"]}({sport_data["smallData"][i]["y"]})<br>{sport_data["bigData"][i]["val"]}({sport_data["bigData"][i]["y"]})'
        ret[v] = f'{sport_data["smallData"][i]["val"]}({sport_data["smallData"][i]["y"]})'
    return ret

def get_rich_data():
    
    dict_sport = {
        "跑步": 1,
        "骑自行车": 4,
        "网球": 6,
        "滑板": 7,
        "滑雪": 1,
        "跑步": 15
    }
    dict_health = {
        "关节疼痛": 21,
        "户外烧烤": 24,
        "购物": 39,
        "感冒": 25,
        "修剪草坪": 28
    }
    dict_rest = {
        "观星": 12,
        "省油": 37,
        "航班误点信息": 3,
        "出航": 11
    }
    return {"运动信息": dict_sport, "健康信息": dict_health, "休息信息": dict_rest}

def gen_table(lines, data, title='#'):
    
    for i, v in data.items():
        line = f"{title}# {i}"
        lines.append(line)
        # print(line)
        line = '|'.join([i for i in v.keys()])
        lines.append(line)
        # print(line)
        line = '|'.join([":---:"] * len(v.keys()))
        lines.append(line)
        # print(line)
        line = '|'.join([i for i in v.values()])
        lines.append(line)
        # print(line)

def format_data(base_data={}, rich_data={}):
    lines = []
    line = "# 基本信息"
    # print(line)
    lines.append(line)
    gen_table(lines, base_data)

    line = "# 预报指数"
    # print(line)
    lines.append(line)
    for k, v in rich_data.items():
        line = f"## {k}"
        # print(line)
        lines.append(line)
        gen_table(lines, v, title="##")
    return lines

def write2md(lines) -> bool:
    now = datetime.now()
    now_str = now.strftime("%Y_%m_%d%H%M%S")
    with open(f"./weather_{now_str}_info.md", mode="w", encoding="utf-8") as f:
        for i in lines:
            f.write(i + "\n")
    return True

def main():
    base_data = crawl_base_data(city_code=57520)
    # print(base_data)

    rich_data = {}
    rich_data_index = get_rich_data()
    for title, data in rich_data_index.items():
        dict_detail = {}
        for k, v in data.items():
            detail = crawl_rich_data(city_code=57520, sport_code=v)
            dict_detail[k] = detail
        rich_data[title] = dict_detail
    # print(rich_data)
    lines = format_data(base_data, rich_data)
    write2md(lines)
    print("done")

if __name__ == "__main__":
    main()