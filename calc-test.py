#誤差修正プログラム
#floatの座標データを取得し、正解のデータとの誤差を修正する

import re

#座標データを格納する関数
def storeList(dataStr, data):
    for i in range(len(dataStr)):
        for j in range(len(dataStr[i])):
            data.append(float(dataStr[i][j]))

    return data
#座標値の誤差を計算する関数
def calcCordinate(cord1, cord2):
    ans = cord1 - cord2
    return ans
#傾きを計算する関数
#隣接する2つの関節点の傾きを計算する
def Gradient(x1, y1, x2, y2):
    grad = (y2 - y1) / (x2 - x1)
    return grad
#元データと比較対象データの傾きを比較する関数
def compGradient(oriGrad, newGrad):
    comp = newGrad / oriGrad
    comp *= 100 #パーセンテージに変換
    return comp
#座標データをタプルに格納する関数
def storeTuple(data, parts):
    partsAddr = parts * 3   #部位の先頭アドレス
    tuple = (data[partsAddr], data[partsAddr + 1], data[partsAddr + 2])
    return tuple


new_data = open(r'camerat_pose.yml', "r", encoding='UTF-8')
master_data = open(r'master.yml', "r", encoding='UTF-8')
lines = new_data.readlines()
lines2 = master_data.readlines()
i = 0
newDataStr = []
newData = []

masterDataStr = []
masterData = []

#正規表現のパターンをセット
pattern = r"0\.|[0-9]*\.[0-9]*e[\+-\-][0-9]*"

#配列にデータを追加 1行を読み込んでパターンとマッチしたものを二次元配列に追加
for line in lines:  #新規データ
    newDataStr.append(re.findall(pattern, line))
for line in lines2: #マスターデータ
    masterDataStr.append(re.findall(pattern, line))

#新規データを一次元配列にfloat型で格納しなおす
newData = storeList(newDataStr, newData)
masterData = storeList(masterDataStr, masterData)

#print(newData)    #printfデバッグ用
print(masterData)   #printfデバッグ用

#体の部位ごとの座標をタプルに格納
#スマートじゃないからどうにかしたい
mas0 = storeTuple(masterData, 0)    #Nose
mas1 = storeTuple(masterData, 1)    #Neck
mas2 = storeTuple(masterData, 2)    #Right Sholder
mas3 = storeTuple(masterData, 3)    #Right Elbow
mas4 = storeTuple(masterData, 4)    #Right Wrist
mas5 = storeTuple(masterData, 5)    #Left Sholder
mas6 = storeTuple(masterData, 6)    #Left Elbow
mas7 = storeTuple(masterData, 7)    #Left Wrist
mas8 = storeTuple(masterData, 8)    #Right Hip
mas11 = storeTuple(masterData, 11)  #Left Hip

new0 = storeTuple(newData, 0)    #Nose
new1 = storeTuple(newData, 1)    #Neck
new2 = storeTuple(newData, 2)    #Right Sholder
new3 = storeTuple(newData, 3)    #Right Elbow
new4 = storeTuple(newData, 4)    #Right Wrist
new5 = storeTuple(newData, 5)    #Left Sholder
new6 = storeTuple(newData, 6)    #Left Elbow
new7 = storeTuple(newData, 7)    #Left Wrist
new8 = storeTuple(newData, 8)    #Right Hip
new11 = storeTuple(newData, 11)  #Left Hip

print(mas1)
print(new1)

#ここから計算パート
