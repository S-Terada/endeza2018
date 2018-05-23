#誤差修正プログラム
#floatの座標データを取得し、正解のデータとの誤差を修正する

import re
import matplotlib.pyplot as plt

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
def compGradient(oriGrad, terasawaGrad):
    comp = terasawaGrad / oriGrad
    comp *= 100 #パーセンテージに変換
    return comp
#座標データをタプルに格納する関数
def storeTuple(data, parts):
    partsAddr = parts * 3   #部位の先頭アドレス
    tuple = (data[partsAddr], data[partsAddr + 1], data[partsAddr + 2])
    return tuple


taketi_data = open(r'\OpenPose_demo_1.0.1\examples\test_image\PointData\taketi_clombia_pose.yml', "r", encoding='UTF-8')
terasawa_data = open(r'\OpenPose_demo_1.0.1\examples\test_image\PointData\terasawa_clombia_pose.yml', "r", encoding='UTF-8')
terada_data = open(r'\OpenPose_demo_1.0.1\examples\test_image\PointData\terada_clo.yml', "r", encoding='UTF-8')
inoue_data = open(r'\OpenPose_demo_1.0.1\examples\test_image\PointData\inoue_clo.yml', "r", encoding='UTF-8')
lines = taketi_data.readlines()
lines2 = terasawa_data.readlines()
lines3 = terada_data.readlines()
lines4 = inoue_data.readlines()
i = 0
taketiDataStr = []
taketiData = []

terasawaDataStr = []
terasawaData = []

teradaDataStr = []
teradaData = []

inoueDataStr = []
inoueData = []

#正規表現のパターンをセット
pattern = r"0\.|[0-9]*\.[0-9]*e[\+-\-][0-9]*"

#配列にデータを追加 1行を読み込んでパターンとマッチしたものを二次元配列に追加
for line in lines:  #竹地データ
    taketiDataStr.append(re.findall(pattern, line))
for line in lines2: #寺沢データ
    terasawaDataStr.append(re.findall(pattern, line))
for line in lines3: #寺田データ
    teradaDataStr.append(re.findall(pattern, line))
for line in lines4: #井上データ
    inoueDataStr.append(re.findall(pattern, line))

#print(terasawaDataStr)

#新規データを一次元配列にfloat型で格納しなおす
taketiData = storeList(taketiDataStr, taketiData)
terasawaData = storeList(terasawaDataStr, terasawaData)
teradaData = storeList(teradaDataStr, teradaData)
inoueData = storeList(inoueDataStr, inoueData)


#print(terasawaData)    #printfデバッグ用
print(taketiData)   #printfデバッグ用

#体の部位ごとの座標をタプルに格納
#スマートじゃないからどうにかしたい
#竹地データセット
taketi0 = storeTuple(taketiData, 0)    #Nose
taketi1 = storeTuple(taketiData, 1)    #Neck
taketi2 = storeTuple(taketiData, 2)    #Right Sholder
taketi3 = storeTuple(taketiData, 3)    #Right Elbow
taketi4 = storeTuple(taketiData, 4)    #Right Wrist
taketi5 = storeTuple(taketiData, 5)    #Left Sholder
taketi6 = storeTuple(taketiData, 6)    #Left Elbow
taketi7 = storeTuple(taketiData, 7)    #Left Wrist
taketi8 = storeTuple(taketiData, 8)    #Right Hip
taketi11 = storeTuple(taketiData, 11)  #Left Hip

#寺沢データセット
terasawa0 = storeTuple(terasawaData, 0)    #Nose
terasawa1 = storeTuple(terasawaData, 1)    #Neck
terasawa2 = storeTuple(terasawaData, 2)    #Right Sholder
terasawa3 = storeTuple(terasawaData, 3)    #Right Elbow
terasawa4 = storeTuple(terasawaData, 4)    #Right Wrist
terasawa5 = storeTuple(terasawaData, 5)    #Left Sholder
terasawa6 = storeTuple(terasawaData, 6)    #Left Elbow
terasawa7 = storeTuple(terasawaData, 7)    #Left Wrist
terasawa8 = storeTuple(terasawaData, 8)    #Right Hip
terasawa11 = storeTuple(terasawaData, 11)  #Left Hip

#寺田データセット
terada0 = storeTuple(teradaData, 0)    #Nose
terada1 = storeTuple(teradaData, 1)    #Neck
terada2 = storeTuple(teradaData, 2)    #Right Sholder
terada3 = storeTuple(teradaData, 3)    #Right Elbow
terada4 = storeTuple(teradaData, 4)    #Right Wrist
terada5 = storeTuple(teradaData, 5)    #Left Sholder
terada6 = storeTuple(teradaData, 6)    #Left Elbow
terada7 = storeTuple(teradaData, 7)    #Left Wrist
terada8 = storeTuple(teradaData, 8)    #Right Hip
terada11 = storeTuple(teradaData, 11)  #Left Hip

#井上データセット
inoue0 = storeTuple(inoueData, 0)    #Nose
inoue1 = storeTuple(inoueData, 1)    #Neck
inoue2 = storeTuple(inoueData, 2)    #Right Sholder
inoue3 = storeTuple(inoueData, 3)    #Right Elbow
inoue4 = storeTuple(inoueData, 4)    #Right Wrist
inoue5 = storeTuple(inoueData, 5)    #Left Sholder
inoue6 = storeTuple(inoueData, 6)    #Left Elbow
inoue7 = storeTuple(inoueData, 7)    #Left Wrist
inoue8 = storeTuple(inoueData, 8)    #Right Hip
inoue11 = storeTuple(inoueData, 11)  #Left Hip

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)


#グラフに座標をプロット
#竹地データをプロット
plt.scatter(taketi0[0], taketi0[1], c='red')
plt.scatter(taketi1[0], taketi1[1], c='red')
plt.scatter(taketi2[0], taketi2[1], c='red', label='taketi')
plt.scatter(taketi3[0], taketi3[1], c='red')
plt.scatter(taketi4[0], taketi4[1], c='red')
plt.scatter(taketi5[0], taketi5[1], c='red')
plt.scatter(taketi6[0], taketi6[1], c='red')
plt.scatter(taketi7[0], taketi7[1], c='red')
plt.scatter(taketi8[0], taketi8[1], c='red')
plt.scatter(taketi11[0], taketi11[1], c='red')

#寺沢データをプロット
plt.scatter(terasawa0[0], terasawa0[1], c='blue')
plt.scatter(terasawa1[0], terasawa1[1], c='blue')
plt.scatter(terasawa2[0], terasawa2[1], c='blue', label='terasawa')
plt.scatter(terasawa3[0], terasawa3[1], c='blue')
plt.scatter(terasawa4[0], terasawa4[1], c='blue')
plt.scatter(terasawa5[0], terasawa5[1], c='blue')
plt.scatter(terasawa6[0], terasawa6[1], c='blue')
plt.scatter(terasawa7[0], terasawa7[1], c='blue')
plt.scatter(terasawa8[0], terasawa8[1], c='blue')
plt.scatter(terasawa11[0], terasawa11[1], c='blue')

#寺田データをプロット
plt.scatter(terada0[0], terada0[1], c='green')
plt.scatter(terada1[0], terada1[1], c='green')
plt.scatter(terada2[0], terada2[1], c='green', label='terada')
plt.scatter(terada3[0], terada3[1], c='green')
plt.scatter(terada4[0], terada4[1], c='green')
plt.scatter(terada5[0], terada5[1], c='green')
plt.scatter(terada6[0], terada6[1], c='green')
plt.scatter(terada7[0], terada7[1], c='green')
plt.scatter(terada8[0], terada8[1], c='green')
plt.scatter(terada11[0], terada11[1], c='green')

#井上データをプロット
plt.scatter(inoue0[0], inoue0[1], c='yellow')
plt.scatter(inoue1[0], inoue1[1], c='yellow')
plt.scatter(inoue2[0], inoue2[1], c='yellow', label='inoue')
plt.scatter(inoue3[0], inoue3[1], c='yellow')
plt.scatter(inoue4[0], inoue4[1], c='yellow')
plt.scatter(inoue5[0], inoue5[1], c='yellow')
plt.scatter(inoue6[0], inoue6[1], c='yellow')
plt.scatter(inoue7[0], inoue7[1], c='yellow')
plt.scatter(inoue8[0], inoue8[1], c='yellow')
plt.scatter(inoue11[0], inoue11[1], c='yellow')


#部位ごとに線で結びます(寺沢＆竹地)
#鼻→首
plt.plot([terasawa0[0], terasawa1[0]], [terasawa0[1], terasawa1[1]], c='blue')
plt.plot([taketi0[0], taketi1[0]], [taketi0[1], taketi1[1]], c='red')
#首→右肩
plt.plot([terasawa1[0], terasawa2[0]], [terasawa1[1], terasawa2[1]], c='blue')
plt.plot([taketi1[0], taketi2[0]], [taketi1[1], taketi2[1]], c='red')
#右肩→右ひじ
plt.plot([terasawa2[0], terasawa3[0]], [terasawa2[1], terasawa3[1]], c='blue')
plt.plot([taketi2[0], taketi3[0]], [taketi2[1], taketi3[1]], c='red')
#右ひじ→右手首
plt.plot([terasawa3[0], terasawa4[0]], [terasawa3[1], terasawa4[1]], c='blue')
plt.plot([taketi3[0], taketi4[0]], [taketi3[1], taketi4[1]], c='red')
#首→左肩
plt.plot([terasawa1[0], terasawa5[0]], [terasawa1[1], terasawa5[1]], c='blue')
plt.plot([taketi1[0], taketi5[0]], [taketi1[1], taketi5[1]], c='red')
#左肩→左ひじ
plt.plot([terasawa5[0], terasawa6[0]], [terasawa5[1], terasawa6[1]], c='blue')
plt.plot([taketi5[0], taketi6[0]], [taketi5[1], taketi6[1]], c='red')
#左ひじ→左手首
plt.plot([terasawa6[0], terasawa7[0]], [terasawa6[1], terasawa7[1]], c='blue')
plt.plot([taketi6[0], taketi7[0]], [taketi6[1], taketi7[1]], c='red')
#左腰→右腰
plt.plot([terasawa11[0], terasawa8[0]], [terasawa11[1], terasawa8[1]], c='blue')
plt.plot([taketi11[0], taketi8[0]], [taketi11[1], taketi8[1]], c='red')



#部位ごとに線で結びます(寺田＆井上)
#鼻→首
plt.plot([terada0[0], terada1[0]], [terada0[1], terada1[1]], c='green')
plt.plot([inoue0[0], inoue1[0]], [inoue0[1], inoue1[1]], c='yellow')
#首→右肩
plt.plot([terada1[0], terada2[0]], [terada1[1], terada2[1]], c='green')
plt.plot([inoue1[0], inoue2[0]], [inoue1[1], inoue2[1]], c='yellow')
#右肩→右ひじ
plt.plot([terada2[0], terada3[0]], [terada2[1], terada3[1]], c='green')
plt.plot([inoue2[0], inoue3[0]], [inoue2[1], inoue3[1]], c='yellow')
#右ひじ→右手首
plt.plot([terada3[0], terada4[0]], [terada3[1], terada4[1]], c='green')
plt.plot([inoue3[0], inoue4[0]], [inoue3[1], inoue4[1]], c='yellow')
#首→左肩
plt.plot([terada1[0], terada5[0]], [terada1[1], terada5[1]], c='green')
plt.plot([inoue1[0], inoue5[0]], [inoue1[1], inoue5[1]], c='yellow')
#左肩→左ひじ
plt.plot([terada5[0], terada6[0]], [terada5[1], terada6[1]], c='green')
plt.plot([inoue5[0], inoue6[0]], [inoue5[1], inoue6[1]], c='yellow')
#左ひじ→左手首
plt.plot([terada6[0], terada7[0]], [terada6[1], terada7[1]], c='green')
plt.plot([inoue6[0], inoue7[0]], [inoue6[1], inoue7[1]], c='yellow')
#左腰→右腰
plt.plot([terada11[0], terada8[0]], [terada11[1], terada8[1]], c='green')
plt.plot([inoue11[0], inoue8[0]], [inoue11[1], inoue8[1]], c='yellow')

#グラフのタイトルやラベル等の設定
ax.set_title('humanoid born')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.grid(True)
ax.legend(loc='upper left')
#プロット実行
fig.show()
plt.show()


#ここから計算パート