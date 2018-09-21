import re
import numpy as np
import csv
import random
from mFunc import *
from lFunc import *
import matplotlib.pyplot as plt


def storeSrcList(data):
    array = np.zeros((8, 2))
    k = 0
    i = 0
    j = 0
    for i in range(8):
        for j in range(2):
            #if k % 3 != 2:
                array[i][j] = data[k]
                k += 1
    # print(array)
    return array


for i in range(1, 51):
    with open(r'\OpenPose_demo_1.0.1\examples\test_image\pose9-test\model{0}.csv'.format(i), 'r') as f:
        lines1 = f.readlines()

        # data string
        srcDataStr = []

        # data array
        srcData = []

        # 正規表現のパターンをセット
        pattern = r"-0\.|-[0-9]*\.[0-9]*|0\.|[0-9]*\.[0-9]*"

        # 配列にデータを追加 1行を読み込んでパターンとマッチしたものを二次元配列に追加
        for line in lines1:
            srcDataStr.append(re.findall(pattern, line))

        # 新規データを一次元配列にfloat型で格納しなおす
        srcData = storeList(srcDataStr, srcData)
        point = [[]]
        point = (reCoord(storeSrcList(srcData)))
        plt.plot([point[2][0], point[3][0]], [point[2][1], point[3][1]], 'g')
        plt.plot([point[3][0], point[4][0]], [point[3][1], point[4][1]], 'b')
        plt.plot([point[2][0], point[5][0]], [point[2][1], point[5][1]], 'y')

    f.close()


# 描画実行
plt.show()
