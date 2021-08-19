# -*- coding: utf-8 -*-
# @Time : 2020/7/9 3:39 下午
# @Author : Zhangfusheng
# @File : calculate_time.py
import numpy as np
import pandas as pd


def calculate_time():
    """根据填好的数据，计算耗时"""
    df = pd.read_csv("./data/label.csv")
    duration_frame = df["end_frame"] - df["start_frame"]
    duration_time = round(duration_frame * 1000 / 30, 4).values
    run(duration_time)
    df["time"] = duration_time
    df.to_csv("./data/label.csv", index=False, sep=",")


def data_process(data=[]):
    if len(data) == 0:
        raise Exception("data's lenth is 0")
    # 求均值 求方差，求标准差，最大，min
    result = {"max": np.max(data), "min": np.min(data), "avg": np.mean(data), "variance": np.var(data),
              "standard_deviation": np.std(data, ddof=0)}
    return result


# 在均方差在平均值20%以内, 所有数据在平均值-+均方差之内
def run(data):
    print("总数据量{0}".format(len(data)))
    del_data = []
    while True:
        result = data_process(data)
        if 0.2 * result["avg"] >= result["standard_deviation"] and result["min"] >= result["avg"] - 2 * result[
            "standard_deviation"] and result["max"] <= result["avg"] + 2 * result["standard_deviation"]:
            print(result)
            break

        if result["max"] - result["avg"] > result["avg"] - result["min"]:
            del_data.append(result["max"])
            data = np.delete(data, data.argmax())
        else:
            del_data.append(result["min"])
            data = np.delete(data, data.argmin())
    print("请删除数据{0}".format(del_data))
    print("可用数据{0}".format(data))
    print("可用数据数量{0}".format(len(data)))
    if len(data) < 15:
        print("请补充{0}条数据，至少保证15条可用数据".format(15 - len(data)))

    return del_data, data


# if __name__ == '__main__':
#     a = [799.92,
#          666.6,
#          633.27,
#          666.6,
#          833.25,
#          966.57,
#          633.27,
#          533.28,
#          499.95,
#          466.62,
#          733.26,
#          466.62,
#          533.28,
#          566.61,
#          733.26]
#     run(a)

if __name__ == '__main__':
    calculate_time()
