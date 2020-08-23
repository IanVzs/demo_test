import os
import uuid
import random
from unittest.mock import patch
from importlib.machinery import SourceFileLoader

def safe_operation(func):
    """安全运行"""
    def wrapper(self, *args, **kwargs):
        rlt = func(self, *args, **kwargs)
        return rlt

        # time_now = datetime.datetime.now()
        # if time_now < self.access_token_expired_time:
        #     return func(self, *args, **kwargs)
        # else:
        #     return func(self, *args, **kwargs)

    return wrapper

class ModelManager():
    def __init__(self):
        self.sign_need_reload = True
        self.models = {}

    @safe_operation
    def load_models(self, list_path: list=[]):
        """加载model(如果代码更新后, 调用会刷新)"""
        for i in list_path or self.read_code_file():
            file_path = i
            model_name = f"model_{uuid.uuid4()}"
            model = SourceFileLoader(model_name, file_path).load_module()
            appid = model.get_appid()
            del model
            model_name = f"model_{appid}"
            model = SourceFileLoader(model_name, file_path).load_module()
            if appid not in self.models:
                self.models[appid] = {}
            self.models[appid]["model"] = model
            self.models[appid]["path"] = file_path
            model.go()
        return None

    def reload_models(self):
        self.sign_need_reload = False
        # 从数据库中读取
        # 从文件中读取
        # 对比合并(优先原则: 数据库优先, 文件优先, 时间优先 |
        #       选用原则: 必须测试通过, 文件当天修改可忽略测试, 数据库当天修改可忽略测试)

    def get_models(self, appid):
        # 之后model超多之后使用该方法进行维护, 目前全部存于一个字典之内
        model_dict = self.models.get(appid)
        model = model_dict and model_dict["model"]
        return model

    def read_code_file(self):
        for _path in os.listdir("./models/"):
            if _path not in ("__pycache__", "__init__.py", "base.py"):
                yield f"./models/{_path}"
    
    def read_code_db(self):
        for _path in os.listdir("./str_models/"):
            if _path not in ("__pycache__", "__init__.py", "base.py"):
                model_code = SourceFileLoader("C", f"./str_models/{_path}").load_module()
                _file_name = f"model_{model_code.appid}.py"
                _code_list = model_code.code.split("\n")
                self.write_code(_file_name, [model_code.code])

    def compare_code(self):
        pass

    def write_code(self, file_name, code_list):
        with open(f"./models/{file_name}", 'w') as _f:
            for _l in code_list:
                _f.write(_l)

    def rewrite_test(self):
        relines = []
        with open("./models/b.py", 'r') as _f:
            for _l in _f:
                if "False" in _l:
                    _l = _l.replace("False", "True")
                elif "True" in _l:
                    _l = _l.replace("True", "False")
                relines.append(_l)
        self.write_code("b.py", relines)
        #with open("./models/b.py", 'w') as _f:
        #    for _l in relines:
        #        _f.write(_l)

if "__main__" == __name__:
    mm = ModelManager()
    iis = mm.read_code_file()
    print([i for i in iis])
    mm.load_models()
    print(mm.models)
    model = mm.get_models("b")
    model.test_rewrite()
    mm.rewrite_test()
    mm.load_models()
    model = mm.get_models("b")
    model.test_rewrite()

    mm.read_code_db()