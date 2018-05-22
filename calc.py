#誤差修正プログラム
#floatの座標データを取得し、正解のデータとの誤差を修正する

import re

#座標データを格納する関数
def store(dataStr, data):
    for i in range(len(dataStr)):
        for j in range(len(dataStr[i])):
            data.append(float(dataStr[i][j]))

    return data
#座標値の誤差を計算する関数
def calcXCordinate(x1, x2):
    xans = x1 - x2
    return xans
def calcYCordinate(y1, y2):
    yans = y1 - y2
    return yans
#傾きを計算する関数
#隣接する2つの関節点の傾きを計算する
def calcGradient(x1, y1, x2, y2):
    grad = (y2 - y1) / (x2 - x1)
    return grad
#元データと比較対象データの傾きを比較する関数
def compGradient(oriGrad, newGrad):
    comp = newGrad / oriGrad
    return comp


new_data = open(r'camerat_pose.yml', "r", encoding='UTF-8')
master_data = open(r'master.yml', "r", encoding='UTF-8')
lines = new_data.readlines()
lines2 = master_data.readlines()

i = 0
newDataStr = []
newData = []

masterDataStr = []
masterData = []

data = []
diffX = []
diffY = []

#正規表現のパターンをセット
pattern = r"0\.|[0-9]*\.[0-9]*e[\+-\-][0-9]*"

#配列にデータを追加 1行を読み込んでパターンとマッチしたものを二次元配列に追加
for line in lines:  #新規データ
    newDataStr.append(re.findall(pattern, line))
for line in lines2: #マスターデータ
    masterDataStr.append(re.findall(pattern, line))

#新規データを一次元配列にfloat型で格納しなおす
newData = store(newDataStr, newData)
masterData = store(masterDataStr, masterData)

#print(newData)    #printfデバッグ用
#print(masterData)   #printfデバッグ用

#ここから計算パート
for k in range(0, 17):
    diffX[k] = calcXCordinate(masterData[k], newData[k])
    diffY[k] = calcYCordinate(masterData[k+1], newData[k+1])
    k += 3

print(diffX)
print(diffY)