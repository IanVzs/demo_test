import os
import uuid
import random
from importlib.machinery import SourceFileLoader


class ModelManager():
    def __init__(self):
        self.models = {}
        
    def load_models(self, list_path: list=[]):
        for i in list_path or self.read_code_file():
            file_path = i
            model_name = f"model_{uuid.uuid4()}"
            model = SourceFileLoader(model_name, file_path).load_module()
            appid = model.get_appid()
            del model
            model_name = f"model_{appid}"
            model = SourceFileLoader(model_name, file_path).load_module()
            self.models[appid] = model
            model.go()
        return None

    def get_models(self, appid):
        # 之后model超多之后使用该方法进行维护, 目前全部存于一个字典之内
        model = self.models.get(appid)
        return model

    def read_code_file(self):
        for _path in os.listdir("./models/"):
            if _path not in ("__pycache__", "__init__.py", "base.py"):
                yield f"./models/{_path}"
    
    def compare_code(self):
        pass

    def rewrite_test(self):
        relines = []
        with open("./models/b.py", 'r') as _f:
            for _l in _f:
                if "False" in _l:
                    _l = _l.replace("False", "True")
                elif "True" in _l:
                    _l = _l.replace("True", "False")
                relines.append(_l)
        with open("./models/b.py", 'w') as _f:
            for _l in relines:
                _f.write(_l)

if "__main__" == __name__:
    mm = ModelManager()
    iis = mm.read_code_file()
    print([i for i in iis])
    mm.load_models()
    print(mm.models)
    mm.models['b'].test_rewrite()
    mm.rewrite_test()
    mm.load_models()
    mm.models['b'].test_rewrite()
