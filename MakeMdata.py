import re
import numpy as np
import csv
import random
from mFunc import *
from lFunc import *

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
            #else:
             #   k += 1
    # print(array)
    return array

def makeDataforML(src):
    srcArray = src
    print(src)
    for i in range(1, 51):
        for j in range(0, 8):
            randnum = random.uniform(0.8, 1.2)
            print("j = " + str(j))
            srcArray[j] = (src[j] * randnum)
        with open(r'\OpenPose_demo_1.0.1\examples\test_image\pose9-test\model{0}.csv'.format(i), 'w') as f:
            writer = csv.writer(f, lineterminator='\n')
            writer.writerows(srcArray)

    f.close()
    return 0


src = open(r'\OpenPose_demo_1.0.1\examples\masterData\masterPoint9\master9.csv', "r", encoding='UTF-8')

lines1 = src.readlines()

#data string
srcDataStr = []

#data array
srcData = []


#正規表現のパターンをセット
pattern = r"-0\.|-[0-9]*\.[0-9]*|0\.|[0-9]*\.[0-9]*"

#配列にデータを追加 1行を読み込んでパターンとマッチしたものを二次元配列に追加
for line in lines1:
    srcDataStr.append(re.findall(pattern, line))

#新規データを一次元配列にfloat型で格納しなおす
srcData = storeList(srcDataStr, srcData)


srcresult = [[]]


srcresult = reCoord(storeSrcList(srcData))
#print(srcresult)
makeDataforML(srcresult)
