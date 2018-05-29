#誤差修正プログラム
#floatの座標データを取得し、正解のデータとの誤差を修正する

import re
from numpy import *

#座標データを格納する関数
def storeList(dataStr, data):
    for i in range(len(dataStr)):
        for j in range(len(dataStr[i])):
            data.append(float(dataStr[i][j]))
    return data
#座標値の誤差を計算する関数
"""
def calcCordinate(tuple1, tuple2):
    ansx = (tuple1[0] - tuple2[0]) 
    ansy = (cord21 - cord22) 
    ans = (ansx + ansy) / 10
    return ans
"""
#座標値の総和を軸ごとに計算し、タプルに格納
def calcCordinate(cord):
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
    array = zeros((8, 3))
    k = 0
    i = 0
    j = 0
    for i in range(8):
        for j in range(3):
            array[i][j] = data[k]
            k += 1
    #print(array)
    return array

new_data = open(r'teracolo.yml', "r", encoding='UTF-8')
#new_data = open(r'terada_clo.yml', "r", encoding='UTF-8')
#new_data = open(r'inoue_clo.yml', "r", encoding='UTF-8')
master_data = open(r'takecolo.yml', "r", encoding='UTF-8')
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

mas = storeTupleinList(masterData)
new = storeTupleinList(newData)
#print(mas[0])       #printデバッグ用
#print(mas[0][1])    #printデバッグ用

#print(mas2) #printデバッグ用
#print(mas3) #printデバッグ用

#ここから計算パート
"""
grad1 = Gradient(mas2, mas3)
grad2 = Gradient(new2, new3)

print(grad1)        #printデバッグ用
print(grad2)        #printデバッグ用

gradpers = compGradient(grad1, grad2)
gradpers2 = compGradient(grad2, grad1)

print(gradpers)     #printデバッグ用
print(gradpers2)    #printデバッグ用
"""
#masans = calcCordinate(mas)
#newans = calcCordinate(new)
#avex = (masans[0] - newans[0]) / 8
#avey = (masans[1] - newans[1]) / 8
print(new[3][1])
print(new[2][1])

if new[3][1] < new[2][1] and new[4][1] < new[3][1] and new[6][1] < new[5][1] and new[7][1] < new[6][1]:
        print("True")

#print(masans)      #printデバッグ用
#print(newans)      #printデバッグ用
#print(avex)        #printデバッグ用
#print(avey)        #printデバッグ用