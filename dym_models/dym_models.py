import os
import uuid
import random
from unittest import mock
from importlib.machinery import SourceFileLoader

import config

def safe_operation(func):
    """
    安全运行
    有此装饰器的函数中不能进行此函数中被mock过的方法, 不然只能拿到mock值
    """
    
    @mock.patch("os.rmdir")
    @mock.patch("os.remove")
    @mock.patch("os.unlink")
    @mock.patch("os.listdir")
    @mock.patch("os.removedirs")
    def wrapper(self, *args, **kwargs):
        real_args = []
        for i in args:
            if isinstance(i, mock.MagicMock):
                i.return_value = None
            else:
                real_args.append(i)
        rlt = func(self, *real_args, **kwargs)
        return rlt

        # time_now = datetime.datetime.now()
        # if time_now < self.access_token_expired_time:
        #     return func(self, *args, **kwargs)
        # else:
        #     return func(self, *args, **kwargs)
    return wrapper

def write_code(file_name, code_list: list, file_path: str=''):
    file_path = file_path or f"./models/{file_name}"
    with open(file_path, 'w') as _f:
        for _l in code_list:
            _f.write(_l)

def check_code(code: str) -> bool:
    # TODO 风险关键字检测
    sign = True
    return sign

def test(file_path) -> int:
    """
    引入错误: 0
    测试错误: -1
    测试通过: 1

    理论上, 如果返回值为0 绝不允许使用该方法.
    """
    model = None
    model_name = f"model_{uuid.uuid4()}"
    try:
        model = SourceFileLoader(model_name, file_path).load_module()
    except:
        return 0
    if model and "test" in model.__dir__():
        sign_test = model and model.test()
    else:
        sign_test = False
    os.remove(file_path)
    return int(bool(sign_test)) or -1

def compare_code(file_name, _code_str,_code_datetime:str) -> bool:
    """
    file_name: 全路径
    _code_datetime: %Y-%m-%d %H:%M:%S

    对比需要重写, 返回1,
    无需重写, 返回0
    """
    sign = 1
    file_path = f"./models/{file_name}"
    cache_model_path = f"./cache_models/{file_name}"
    if config.TIME_PRIORITY and os.path.exists(file_path):
        file_datetime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.path.getmtime(_file_name)))
        if file_datetime > _code_datetime:
            sign = 0
    if sign:
        write_code(file_name, [_code_str], cache_model_path)
        sign_test = test(file_path)
        if sign_test:
            if config.CLIENT_NEED_TEST and sign_test < 0:
                sign = 0
        else:
            sign = 0
    return sign

class ModelManager():
    def __init__(self):
        self.sign_need_reload = True
        self.models = {}

    def load_models(self, list_path: list=[]):
        """加载model(如果代码更新后, 调用会刷新)"""
        for i in list_path or self.read_code_file():
            file_path = i
            model_name = f"model_{uuid.uuid4()}"
            model = SourceFileLoader(model_name, file_path).load_module()
            appid = model.get_appid()
            # import ipdb; ipdb.set_trace()
            sign_test = False
            if "test" in model.__dir__():
                # 自测函数
                sign_test = model.test()
            del model
            if config.CLIENT_NEED_TEST and not sign_test:
                continue
            model_name = f"model_{appid}"
            model = SourceFileLoader(model_name, file_path).load_module()
            if appid not in self.models:
                self.models[appid] = {}
            self.models[appid]["model"] = model
            self.models[appid]["path"] = file_path
        self.sign_need_reload = False

    def reload_models(self):
        self.sign_need_reload = False
        # 从数据库中读取
        # 从文件中读取
        # 对比合并(优先原则: 数据库优先, 文件优先, 时间优先 |
        #       选用原则: 必须测试通过, 文件当天修改可忽略测试, 数据库当天修改可忽略测试)

    @safe_operation
    def get_model(self, appid):
        # 之后model超多之后使用该方法进行维护, 目前全部存于一个字典之内
        model_dict = self.models.get(appid)
        model = model_dict and model_dict["model"]
        return model

    def read_code_file(self):
        for _path in os.listdir("./models/"):
            if _path not in ("__pycache__", "__init__.py", "base.py"):
                yield f"./models/{_path}"
    
    def read_code_db(self):
        """从数据库中获取代码, 并写入文件中"""
        # TODO
        for _path in os.listdir("./str_models/"):
            if _path not in ("__pycache__", "__init__.py", "base.py"):
                model_code = SourceFileLoader("C", f"./str_models/{_path}").load_module()
                _file_name = f"model_{model_code.appid}.py"
                if check_code(model_code.code) and compare_code(_file_name, model_code.code, _code_date_datetime):
                    write_code(_file_name, [model_code.code])

    def test_rewrite(self):
        relines = []
        self.get_model("b").test_rewrite()
        with open("./models/b.py", 'r') as _f:
            for _l in _f:
                if "False" in _l:
                    _l = _l.replace("False", "True")
                elif "True" in _l:
                    _l = _l.replace("True", "False")
                relines.append(_l)
        write_code("b.py", relines)
        self.load_models(["./models/b.py"])
        self.get_model("b").test_rewrite()
        #with open("./models/b.py", 'w') as _f:
        #    for _l in relines:
        #        _f.write(_l)

    @safe_operation
    def run(self, appid):
        model = self.get_model(appid)
        if model:
            model.go()


if "__main__" == __name__:
    mm = ModelManager()
    iis = mm.read_code_file()
    print([i for i in iis])
    mm.load_models()
    print(mm.models)
    mm.test_rewrite()
    #mm.read_code_db()
    mm.run("c")
