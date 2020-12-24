import time
from collections import OrderedDict
from concurrent.futures import (
    ThreadPoolExecutor, as_completed
)


def get_thread_time(times):
    time.sleep(times)
    return times


start = time.time()
executor = ThreadPoolExecutor(max_workers=4)
task_list = [executor.submit(get_thread_time, times) for times in [2, 3, 1, 4]]
task_to_time = OrderedDict(zip(["task1", "task2", "task3", "task4"],[2, 3, 1, 4]))
task_map = OrderedDict(zip(task_list, ["task1", "task2", "task3", "task4"]))

for result in as_completed(task_list):
    task_name = task_map.get(result)
    print("{}:{}".format(task_name,task_to_time.get(task_name)))



# url
import requests
def get_requests_resp(tkey_url, tkey):
    print(tkey_url)
    tkey_url_data = requests.get(tkey_url).json()
    print(tkey_url_data)
    tkey_url = tkey_url_data and tkey_url_data["data"]["ok"] and tkey_url_data["data"]["qrcode_url"]
    return (tkey_url, tkey)

tkey_url_list = [
        ("https://wx.zuoshouyisheng.com/wx_api/get_qrcode?app_id=wx7ae5c0d83b1240a8&scene_str=wys_1", 1),
        ("https://wx.zuoshouyisheng.com/wx_api/get_qrcode?app_id=wx7ae5c0d83b1240a8&scene_str=wys_2", 2),
        ]

task_list = []
with ThreadPoolExecutor(max_workers=10) as executor:
    task_list = [executor.submit(get_requests_resp, tkey_url, tkey) for tkey_url, tkey in tkey_url_list]

    qrcode_url_list = {}
    for result in as_completed(task_list):
        result = result.result()
        if result and len(result) == 2:
            qrcode_url_list.update({result[-1]: result[0]})
        else:
            qrcode_url_list.update({'':''})
print(qrcode_url_list)
