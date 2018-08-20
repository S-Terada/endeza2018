#誤差修正プログラム
#floatの座標データを取得し、正解のデータとの誤差を修正する

import re
from sys import argv
import sys
import numpy as np
import csv

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
            if k % 3 != 2:
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
def makeMaster(mas1, mas2, mas3, mas4, mas5):
    masArray = [[]]
    masArray = np.array((mas1 + mas2 + mas3 + mas4 + mas5) / 5)
    print(masArray)
    with open('\OpenPose_demo_1.0.1\examples\masterData\masterPoint9\master9.csv', 'w') as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerows(masArray)

    f.close()

    return 0


master1_proto = open(r'\OpenPose_demo_1.0.1\examples\masterData\masterPoint9\proto1_pose.yml', "r", encoding='UTF-8')
master2_proto = open(r'\OpenPose_demo_1.0.1\examples\masterData\masterPoint9\proto2_pose.yml', "r", encoding='UTF-8')
master3_proto = open(r'\OpenPose_demo_1.0.1\examples\masterData\masterPoint9\proto3_pose.yml', "r", encoding='UTF-8')
master4_proto = open(r'\OpenPose_demo_1.0.1\examples\masterData\masterPoint9\proto4_pose.yml', "r", encoding='UTF-8')
master5_proto = open(r'\OpenPose_demo_1.0.1\examples\masterData\masterPoint9\proto5_pose.yml', "r", encoding='UTF-8')

lines1 = master1_proto.readlines()
lines2 = master2_proto.readlines()
lines3 = master3_proto.readlines()
lines4 = master4_proto.readlines()
lines5 = master5_proto.readlines()

#data string
mas1DataStr = []
mas2DataStr = []
mas3DataStr = []
mas4DataStr = []
mas5DataStr = []

#data array
mas1Data = []
mas2Data = []
mas3Data = []
mas4Data = []
mas5Data = []

#正規表現のパターンをセット
pattern = r"-0\.|-[0-9]*\.[0-9]*|0\.|[0-9]*\.[0-9]*"

#配列にデータを追加 1行を読み込んでパターンとマッチしたものを二次元配列に追加
for line in lines1:
    mas1DataStr.append(re.findall(pattern, line))
for line in lines2:
    mas2DataStr.append(re.findall(pattern, line))
for line in lines3:
    mas3DataStr.append(re.findall(pattern, line))
for line in lines4:
    mas4DataStr.append(re.findall(pattern, line))
for line in lines5:
    mas5DataStr.append(re.findall(pattern, line))

#新規データを一次元配列にfloat型で格納しなおす
mas1Data = storeList(mas1DataStr, mas1Data)
mas2Data = storeList(mas2DataStr, mas2Data)
mas3Data = storeList(mas3DataStr, mas3Data)
mas4Data = storeList(mas4DataStr, mas4Data)
mas5Data = storeList(mas5DataStr, mas5Data)


mas1 = [[]]
mas2 = [[]]
mas3 = [[]]
mas4 = [[]]
mas5 = [[]]

mas1 = reCoord(storeDoubleList(mas1Data))
mas2 = reCoord(storeDoubleList(mas2Data))
mas3 = reCoord(storeDoubleList(mas3Data))
mas4 = reCoord(storeDoubleList(mas4Data))
mas5 = reCoord(storeDoubleList(mas5Data))



#print(mas1)
makeMaster(mas1, mas2, mas3, mas4, mas5)
