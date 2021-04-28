# float 仅作为示例,实际并不能使用此类型

class Order:
    def __init__(self, coupons: list):
        self.list_item = []
        self.sum_gross = 0
        self.list_coupons = coupons
        self.use_coupons = []

    def add(self, item: dict):
        self.sum_gross += item["p"] * item["num"]
        self.optimal()
        self.list_item.append(item)

    def optimal(self):
        # TODO
        if self.list_coupons:
            for i in range(len(self.list_coupons)):
                c = self.list_coupons.pop()
                if c.check(self):
                    self.use_coupons.append(c)
                else:
                    self.list_coupons.append(c)

    def sum(self):
        sum_reduce = 0
        for i in self.list_item:
            sum_reduce += i["p"] * i["num"]
        for ii in self.use_coupons:
            sum_reduce = ii.sum(self, sum_reduce)
        return sum_reduce

def fmt_coupons(txt: str):
    date = deal = otype = _min = p = None
    list_data = [i.replace(' ', '') for i in txt.split("|")]
    if len(list_data) == 3:
        date, deal, otype = list_data
    elif len(list_data) == 5:
        date, deal, otype, _min, p = list_data
    deal = float(deal or 0)
    return {"date": date, "deal": deal, "type": otype, "min": float(_min or 0), "p": float(p or 0)}

def fmt_item(txt: str):
    num = txt.split("*")[0].replace(' ', '')
    num = int(num)

    p = txt.split(":")[-1].replace(' ', '')
    p = float(p)
    
    name = txt.split("*")[-1].replace(' ', '').split(":")[0].replace(' ', '')
    otype = (name in "ipad，iphone，显示器，笔记本电脑，键盘") and 1 or 0

    return {"type": otype, "p": p, "num": num}
    

class C:
    def __init__(self, otype, data):
        self.otype = otype
        self.data = data

    def check(self, order) -> bool:
        return True

    def sum(self, order, rst):
        if self.otype > 0:
            rst = rst - self.data["p"]
        else:
            rst = rst - (sum([i["p"] for i in order.list_item if i["type"] > 0]) * (1-self.data["deal"]))
        return rst



if __name__ == "__main__":
    txt = "2013.11.11 | 0.7 | 电⼦"
    txt2 = "2014.3.2 | | | 1000 | 200"
    c = fmt_coupons(txt)
    c = C(0, c)
    c2 = fmt_coupons(txt2)
    c2 = C(1, c2)
    order = Order([c, c2])
    for i in ["1 * ipad : 2399.00 ", "1 * 显示器 : 1799.00", "12 * 啤酒 : 25.00", "5 * ⾯包 : 9.00"]:
        ii = fmt_item(i)
        order.add(ii)
    print(order.sum())
