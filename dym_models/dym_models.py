from importlib.machinery import SourceFileLoader

for i in ({"model_name": 'A', "file_path": "models/a.py"}, {"model_name": "B", "file_path": "models/b.py"}):
    model_name = i["model_name"]
    file_path = i["file_path"]
    model = SourceFileLoader(model_name, file_path).load_module()
    model.go()
