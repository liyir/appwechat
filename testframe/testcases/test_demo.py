# 装饰器为什么会存在
import yaml
def test_yaml():
    with open("./tmp.yaml","r",encoding="utf-8") as f:
        data = yaml.load(f)
    print("yaml data :", data)
    data_python =['a','b','c']
    print("python data:",data_python)
