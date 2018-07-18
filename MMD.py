import re
import numpy as np
import csv
import random

#座標データを格納する関数
def storeList(dataStr, data):
    for i in range(len(dataStr)):
        for j in range(len(dataStr[i])):
            data.append(float(dataStr[i][j]))
    return data
#xy座標を二重リストに格納する関数
def storeDoubleList(data):
    array = np.zeros((8, 2))
    k = 0
    i = 0
    j = 0
    for i in range(8):
        for j in range(3):
            if k % 3 != 2 :
                array[i][j] = data[k]
                k += 1
            else:
                k += 1
    #print(array)
    return array
#首基準の相対座標に直す関数
def reCoord(data):
    neckx = data[1][0]
    necky =data[1][1]

    for i in range(0, 8):
        data[i][0] -= neckx
        data[i][1] -= necky
    return data
def makeDataforML(src):
    srcArray = [[]]
    #print(masArray)

    for i in range(1, 50):
        randnum = random.random()
        srcArray = np.array(src * randnum)
        with open('master{0}.csv'.format(i), 'w') as f:
            writer = csv.writer(f, lineterminator='\n')
            writer.writerows(src)

    f.close()

    return 0

src = open(r'master.csv', "r", encoding='UTF-8')

lines1 = src.readlines()

#data string
srcDataStr = []

#data array
srcData = []



#正規表現のパターンをセット
pattern = r"0\.|[0-9]*\.[0-9]*e[\+-\-][0-9]*"

#配列にデータを追加 1行を読み込んでパターンとマッチしたものを二次元配列に追加
for line in lines1:
    srcDataStr.append(re.findall(pattern, line))

#新規データを一次元配列にfloat型で格納しなおす
srcData = storeList(srcDataStr, srcData)


srcresult = [[]]


srcresult = reCoord(storeDoubleList(srcData))

#print(srcresult)
makeDataforML(srcresult)