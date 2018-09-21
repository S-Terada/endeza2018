# 誤差修正プログラム
# floatの座標データを取得し、正解のデータとの誤差を修正する

import re
from sys import argv
import sys
import csv
from pFunc import *
from cFunc import *
from mFunc import *
from lFunc import *
import glob
import json
from ReadModel import *
from collections import OrderedDict
import pprint


# 以下p1からp9はpose判定関数
#key1 = int((int(argv[1]) / 100))  # 先頭一桁
#key2 = int(((int(argv[1]) % 100) / 10))  # 二桁目
#key3 = int(((int(argv[1]) % 100) % 10)) # 三桁目
key1 = int(argv[1])
# 実行時のコマンドライン引数としてpose番号を3桁で渡す
# argv[]の第一引数は実行ファイル名，第二引数をkeyとして受け取る
#jsonを取り扱う新版

#imageData = glob.glob(r'\OpenPose_demo_1.0.1\examples\analysisData\*.json')

f1 = open(r'\OpenPose_demo_1.0.1\{0}_keypoints.json'.format(key1), 'r')

json1 = json.load(f1)
#json2 = json.load(f2)
#json3 = json.load(f3)

#print(json1)
#print("this is json mode")
#print(json1["people"][0])
#print(json1["people"][0]["pose_keypoints"][0])

new1 = [[]]
#new2 = [[]]
#new3 = [[]]

new1 = reCoord(storeDoubleList(json1["people"][0]["pose_keypoints"]))
#new2 = reCoord(storeDoubleList(json2["people"][0]["pose_keypoints"]))
#new3 = reCoord(storeDoubleList(json3["people"][0]["pose_keypoints"]))

ave = 0

for i in range(1, 51):
    masterDataStr = []
    masterData = []
    mas = [[]]
    masterDataStr = ReadMaster(key1, i)
    masterData = storeList(masterDataStr, masterData)
    mas = reCoord(storeMasterList(masterData))
    #誤差は絶対値で取り扱う
    cans1 = abs(selectPose(mas, new1, key1))
    ave += cans1
print(mas)
ave = ave/50
#print(cans1)

# ここから計算パート
# keyを辞書に投げて関数を実行し，その結果をcansへ代入する
#cans1 = selectPose(mas1, new1, key1)
#cans2 = selectPose(mas2, new2, key2)
#cans3 = selectPose(mas3, new3, key3)
print("key1 = " + str(key1))
print("cans1 = " + str(cans1))
print("average = " + str(ave))
#print("cans2 = " + str(cans2))
#print("cans3 = " + str(cans3))

#checkAns(cans1, cans2, cans3, key1, key2, key3)