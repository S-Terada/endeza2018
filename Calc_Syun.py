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


# 以下p1からp9はpose判定関数
key1 = int((int(argv[1]) / 100))  # 先頭一桁
key2 = int(((int(argv[1]) % 100) / 10))  # 二桁目
key3 = int(((int(argv[1]) % 100) % 10)) # 三桁目
# 実行時のコマンドライン引数としてpose番号を3桁で渡す
# argv[]の第一引数は実行ファイル名，第二引数をkeyとして受け取る
#print(argv[1])
#print(key1)
#print(key2)
#print(key3)
checkKey(key1, key2, key3)

"""
new1_data = open(r'\OpenPose_demo_1.0.1\examples\analysisData\109_pose.yml', "r", encoding='UTF-8')
new2_data = open(r'\OpenPose_demo_1.0.1\examples\analysisData\209_pose.yml', "r", encoding='UTF-8')
new3_data = open(r'\OpenPose_demo_1.0.1\examples\analysisData\309_pose.yml', "r", encoding='UTF-8')
"""
imageData = glob.glob(r'\OpenPose_demo_1.0.1\examples\analysisData\*.yml')

new1_data = open(imageData[0], "r", encoding='UTF-8')
new2_data = open(imageData[1], "r", encoding='UTF-8')
new3_data = open(imageData[2], "r", encoding='UTF-8')

lines4 = new1_data.readlines()
lines5 = new2_data.readlines()
lines6 = new3_data.readlines()

new1DataStr = []
new2DataStr = []
new3DataStr = []
new1Data = []
new2Data = []
new3Data = []

# 正規表現のパターンをセット
pattern = r"-0\.|-[0-9]*\.[0-9]*|0\.|[0-9]*\.[0-9]*"

# 配列にデータを追加 1行を読み込んでパターンとマッチしたものを二次元配列に追加
for line in lines4:
    new1DataStr.append(re.findall(pattern, line))
for line in lines5:
    new2DataStr.append(re.findall(pattern, line))
for line in lines6:
    new3DataStr.append(re.findall(pattern, line))

# 新規データを一次元配列にfloat型で格納しなおす
new1Data = storeList(new1DataStr, new1Data)
new2Data = storeList(new2DataStr, new2Data)
new3Data = storeList(new3DataStr, new3Data)

master1DataStr = []
master2DataStr = []
master3DataStr = []
master1Data = []
master2Data = []
master3Data = []
mas1 = [[]]
mas2 = [[]]
msa3 = [[]]

master1DataStr = selectMaster(key1)
master2DataStr = selectMaster(key2)
master3DataStr = selectMaster(key3)

master1Data = storeList(master1DataStr, master1Data)
master2Data = storeList(master2DataStr, master2Data)
master3Data = storeList(master3DataStr, master3Data)

mas1 = reCoord(storeMasterList(master1Data))
mas2 = reCoord(storeMasterList(master2Data))
mas3 = reCoord(storeMasterList(master3Data))

new1 = [[]]
new2 = [[]]
new3 = [[]]

new1 = reCoord(storeDoubleList(new1Data))
new2 = reCoord(storeDoubleList(new2Data))
new3 = reCoord(storeDoubleList(new3Data))

# ここから計算パート
# keyを辞書に投げて関数を実行し，その結果をcansへ代入する
cans1 = selectPose(mas1, new1, key1)
cans2 = selectPose(mas2, new2, key2)
cans3 = selectPose(mas3, new3, key3)

checkAns(cans1, cans2, cans3, key1, key2, key3)