# import lxml
from re import L
import requests
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
    
    for i in soup.find_all("script"):
        
        print(i.contents)
        import ipdb; ipdb.set_trace()
        if i.contents and "var days =" in i.contents:
            i = i.contents[0].replace("\t", '').replace("\r", '').replace("\n", '').split("var ")
            

    sport_data = {}


def main():
    # base_data = crawl_base_data(city_code=57520)
    # print(base_data)
    crawl_sport_data(city_code=57520, sport_code=1)


if __name__ == "__main__":
    main()