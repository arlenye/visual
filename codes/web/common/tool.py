"""
 filename：    common
 author：      Tim
 date：        2025/8/2 06:26
 description： 公共函数
"""
import time


# 对分数进行转换
def round_score(score):
    rounded = round(score, 2) * 100
    return f"{rounded:g}%"  # :g会自动去掉无意义的小数部分


# 获取分类
def get_class_name(str_key):
    class_dict = {
        "fall": "跌倒",
        "smoke": "吸烟"
    }

    return class_dict[str_key]


def get_timestamp():
    timestamp = int(time.time())

    return timestamp


# main
if __name__ == '__main__':
    print(round_score(0.84))
    print(get_class_name("fall"))
    print(get_class_name("smoke"))
    print(get_timestamp())
