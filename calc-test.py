#誤差修正プログラム
#floatの座標データを取得し、正解のデータとの誤差を修正する

import re
import numpy as np

#座標データを格納する関数
def storeList(dataStr, data):
    for i in range(len(dataStr)):
        for j in range(len(dataStr[i])):
            data.append(float(dataStr[i][j]))
    return data
#座標値の誤差を計算する関数

#座標値の総和を軸ごとに計算し、タプルに格納
def calcCoordinate(cord):
    uprx = (cord[0][0] + cord[1][0] + cord[2][0] + cord[3][0])
    lowx = (cord[4][0] + cord[5][0] + cord[6][0] + cord[7][0])

    upry = (cord[0][1] + cord[1][1] + cord[2][1] + cord[3][1])
    lowy = (cord[4][1] + cord[5][1] + cord[6][1] + cord[7][1])

    x = uprx + lowx
    y = upry + lowy
    ans = (x, y)
    return ans
#傾きを計算する関数
#隣接する2つの関節点の傾きを計算する
def Gradient(parts1, parts2):
    grad = (parts1[1] - parts2[1]) / (parts1[0] - parts2[0])
    return grad
#元データと比較対象データの傾きを比較する関数
def compGradient(masGrad, newGrad):
    comp = (newGrad - masGrad) / masGrad
    comp *= 100 #パーセンテージに変換
    return comp
#xy座標を二重リストに格納する関数
def storeTupleinList(data):
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
#コロンビアチェック
def checkColombia(mas, new):
    mas1x = mas[7][0] - mas[4][0]
    mas1y = mas[7][1] - mas[4][1]
    mas2x = mas[6][0] - mas[3][0]
    mas2y = mas[6][1] - mas[3][1]
    new1x = new[7][0] - new[4][0]
    new1y = new[7][1] - new[4][1]
    new2x = new[6][0] - new[3][0]
    new2y = new[6][1] - new[3][1]

    preans1 = (mas1x * new1y) - (mas1y * new1x)
    preans2 = (mas2x * new2y) - (mas2y * new2x)

    ans = (preans1 + preans2) / 2

    return ans

new_data = open(r'sawaclo.yml', "r", encoding='UTF-8')
master_data = open(r'daclo.yml', "r", encoding='UTF-8')
#new_data = open(r'inoclo.yml', "r", encoding='UTF-8')
#master_data = open(r'takeclo.yml', "r", encoding='UTF-8')
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

#print(newDataStr)

#新規データを一次元配列にfloat型で格納しなおす
newData = storeList(newDataStr, newData)
masterData = storeList(masterDataStr, masterData)

#print(newData)    #printデバッグ用
#print(masterData)   #printデバッグ用

#体の部位ごとの座標をタプルに格納
#スマートじゃないからどうにかしたい
#スマートになった
mas = [[]]
new = [[]]


mas = reCoord(storeTupleinList(masterData))
new = reCoord(storeTupleinList(newData))
#print(mas[2])       #printデバッグ用
#print(mas[5])    #printデバッグ用


#ここから計算パート


cans = checkColombia(mas, new)


if abs(cans) < 3000 :
    print("Pose Correct")
    print("The door will unlock")
else:
    print("Pose Incorrect")
    print("Go Back to your Home")
