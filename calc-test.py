#誤差修正プログラム
#floatの座標データを取得し、正解のデータとの誤差を修正する

import re
from sys import argv
import sys
import numpy as np

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
#以下p1からp9はpose判定関数
def p1(mas, new):
    mas1x = mas[4][0] - mas[3][0]
    mas1y = mas[4][1] - mas[3][1]
    mas2x = mas[3][0] - mas[2][0]
    mas2y = mas[3][1] - mas[2][1]
    mas3x = mas[7][0] - mas[5][0]
    mas3y = mas[7][1] - mas[5][1]

    new1x = new[4][0] - new[3][0]
    new1y = new[4][1] - new[3][1]
    new2x = new[3][0] - new[2][0]
    new2y = new[3][1] - new[2][1]
    new3x = new[7][0] - new[5][0]
    new3y = new[7][1] - new[5][1]

    #mpans : mas pre ans
    mpans1 = (mas1x * mas2x) + (mas1y * mas2y)  #dot
    mpans2 = (mas2x * mas3y) - (mas2y * mas3x)  #cross

    #npans : new pre ans
    npans1 = (new1x * new2x) + (new1y * new2y)  #dot
    npans2 = (new2x * new3y) - (new2y * new3x)  #cross

    ans = (abs((mpans1 - npans1)) + abs((mpans2 - npans2))) / 2

    return ans
def p2(mas, new):
    mas1x = mas[7][0] - mas[6][0]
    mas1y = mas[7][1] - mas[6][1]
    mas2x = mas[6][0] - mas[5][0]
    mas2y = mas[6][1] - mas[5][1]
    mas3x = mas[4][0] - mas[2][0]
    mas3y = mas[4][1] - mas[2][1]

    new1x = new[7][0] - new[6][0]
    new1y = new[7][1] - new[6][1]
    new2x = new[6][0] - new[5][0]
    new2y = new[6][1] - new[5][1]
    new3x = new[4][0] - new[2][0]
    new3y = new[4][1] - new[2][1]

    #mpans : mas pre ans
    mpans1 = (mas1x * mas2x) + (mas1y * new2y)  #dot
    mpans2 = (mas2x * mas3y) - (mas2y * mas3x)  #cross

    #npans : new pre ans
    npans1 = (new1x * new2x) + (new1y * new2y)  #dot
    npans2 = (new2x * new3y) - (new2y * new3x)  #cross
    ans = (abs((mpans1 - npans1)) + abs((mpans2 - npans2))) / 2

    return ans
def p3(mas, new):
    mas1x = mas[4][0] - mas[2][0]
    mas1y = mas[4][1] - mas[2][1]
    mas2x = mas[7][0] - mas[5][0]
    mas2y = mas[7][1] - mas[5][1]
    new1x = new[4][0] - new[2][0]
    new1y = new[4][1] - new[2][1]
    new2x = new[7][0] - new[5][0]
    new2y = new[7][1] - new[5][1]

    #mpans : mas pre ans
    mpans = (mas1x * mas2y) - (mas1y * mas2x)  #cross

    #npans : new pre ans
    npans = (new1x * new2y) - (new1y * new2x)  #cross

    #additional condition determination
    if new[7][1] > new[6][1] and new[3][1] > new[4][1] and new[6][1] > new[3][1]:
        constant = 0
    else:
        constant = 9999

    ans = (abs(mpans + npans) + constant) / 2

    return ans
def p4(mas, new):
    mas1x = mas[4][0] - mas[3][0]
    mas1y = mas[4][1] - mas[3][1]
    mas2x = mas[3][0] - mas[2][0]
    mas2y = mas[3][1] - mas[2][1]
    mas3x = mas[7][0] - mas[6][0]
    mas3y = mas[7][1] - mas[6][1]
    mas4x = mas[6][0] - mas[5][0]
    mas4y = mas[6][1] - mas[5][1]
    
    new1x = new[4][0] - new[3][0]
    new1y = new[4][1] - new[3][1]
    new2x = new[3][0] - new[2][0]
    new2y = new[3][1] - new[2][1]
    new3x = new[7][0] - new[6][0]
    new3y = new[7][1] - new[6][1]
    new4x = new[6][0] - new[5][0]
    new4y = new[6][1] - new[5][1]

    #mpans : mas pre ans
    mpans1 = (mas1x * mas2x) + (mas1y * mas2y)  #dot
    mpans2 = (mas3x * mas4x) + (mas3y * mas4y)  #dot

    #npans : new pre ans
    npans1 = (new1x * new2x) + (new1y * new2y)  #dot
    npans2 = (new3x * new4x) + (new3y * new4y)  #dot

    #additional condition determination
    if new[3][1] > new[4][1] and new[6][1] > new[7][1]:
        constant = 0
    else:
        constant = 9999

    ans = (abs((mpans1 - npans1)) + abs((mpans2 - npans2)) + constant) / 2

    return ans
def p5(mas, new):
    mas1x = mas[4][0] - mas[2][0]
    mas1y = mas[4][1] - mas[2][1]
    mas2x = mas[7][0] - mas[5][0]
    mas2y = mas[7][1] - mas[5][1]
    new1x = new[4][0] - new[2][0]
    new1y = new[4][1] - new[2][1]
    new2x = new[7][0] - new[5][0]
    new2y = new[7][1] - new[5][1]

    #mpans : mas pre ans
    mpans = (mas1x * mas2y) - (mas1y * mas2x)  #cross

    #npans : new pre ans
    npans = (new1x * new2y) - (new1y * new2x)  #cross

    #additional condition determination
    if new[7][1] > new[5][1] and new[4][1] > new[2][1] and new[3][1] > new[5][1]:
        constant = 0
    else:
        constant = 9999

    ans = (abs(mpans + npans) + constant) / 2

    return ans
def p6(mas, new):
    mas1x = mas[4][0] - mas[2][0]
    mas1y = mas[4][1] - mas[2][1]
    mas2x = mas[7][0] - mas[5][0]
    mas2y = mas[7][1] - mas[5][1]
    new1x = new[4][0] - new[2][0]
    new1y = new[4][1] - new[2][1]
    new2x = new[7][0] - new[5][0]
    new2y = new[7][1] - new[5][1]

    #mpans : mas pre ans
    mpans = (mas1x * mas2y) - (mas1y * mas2x)  #cross

    #npans : new pre ans
    npans = (new1x * new2y) - (new1y * new2x)  #cross

    #additional condition determination
    if new[4][1] > new[3][1] and new[3][1] > new[6][1] and new[6][1] > new[7][1]:
        constant = 0
    else:
        constant = 9999

    ans = (abs(mpans + npans) + constant) / 2

    return ans
def p7(mas, new):
    mas1x = mas[4][0] - mas[3][0]
    mas1y = mas[4][1] - mas[3][1]
    mas2x = mas[3][0] - mas[2][0]
    mas2y = mas[3][1] - mas[2][1]
    mas3x = mas[7][0] - mas[6][0]
    mas3y = mas[7][1] - mas[6][1]
    mas4x = mas[6][0] - mas[5][0]
    mas4y = mas[6][1] - mas[5][1]

    new1x = new[4][0] - new[3][0]
    new1y = new[4][1] - new[3][1]
    new2x = new[3][0] - new[2][0]
    new2y = new[3][1] - new[2][1]
    new3x = new[7][0] - new[6][0]
    new3y = new[7][1] - new[6][1]
    new4x = new[6][0] - new[5][0]
    new4y = new[6][1] - new[5][1]

    # mpans : mas pre ans
    mpans1 = (mas1x * mas2x) + (mas1y * mas2y)  # dot
    mpans2 = (mas3x * mas4x) + (mas3y * mas4y)  # dot

    # npans : new pre ans
    npans1 = (new1x * new2x) + (new1y * new2y)  # dot
    npans2 = (new3x * new4x) + (new3y * new4y)  # dot

    # additional condition determination
    if new[4][1] > new[3][1] and new[6][1] > new[7][1]:
        constant = 0
    else:
        constant = 9999

    ans = (abs((mpans1 - npans1)) + abs((mpans2 - npans2)) + constant) / 2

    return ans
def p8(mas, new):
    mas1x = mas[4][0] - mas[3][0]
    mas1y = mas[4][1] - mas[3][1]
    mas2x = mas[3][0] - mas[2][0]
    mas2y = mas[3][1] - mas[2][1]
    mas3x = mas[7][0] - mas[6][0]
    mas3y = mas[7][1] - mas[6][1]
    mas4x = mas[6][0] - mas[5][0]
    mas4y = mas[6][1] - mas[5][1]

    new1x = new[4][0] - new[3][0]
    new1y = new[4][1] - new[3][1]
    new2x = new[3][0] - new[2][0]
    new2y = new[3][1] - new[2][1]
    new3x = new[7][0] - new[6][0]
    new3y = new[7][1] - new[6][1]
    new4x = new[6][0] - new[5][0]
    new4y = new[6][1] - new[5][1]

    # mpans : mas pre ans
    mpans1 = (mas1x * mas2x) + (mas1y * mas2y)  # dot
    mpans2 = (mas3x * mas4x) + (mas3y * mas4y)  # dot

    # npans : new pre ans
    npans1 = (new1x * new2x) + (new1y * new2y)  # dot
    npans2 = (new3x * new4x) + (new3y * new4y)  # dot

    # additional condition determination
    if new[3][1] > new[4][1] and new[6][1] > new[7][1]:
        constant = 0
    else:
        constant = 9999

    ans = (abs((mpans1 - npans1)) + abs((mpans2 - npans2)) + constant) / 2

    return ans
def p9(mas, new):
#判定用ベクトル生成
    mas1x = mas[7][0] - mas[4][0]
    mas1y = mas[7][1] - mas[4][1]
    mas2x = mas[6][0] - mas[3][0]
    mas2y = mas[6][1] - mas[3][1]
    new1x = new[7][0] - new[4][0]
    new1y = new[7][1] - new[4][1]
    new2x = new[6][0] - new[3][0]
    new2y = new[6][1] - new[3][1]
#外積計算
    preans1 = (mas1x * new1y) - (mas1y * new1x)
    preans2 = (mas2x * new2y) - (mas2y * new2x)

    ans = (preans1 + preans2) / 2

    return ans

def selectPose(mas, new, key):
    ans = 0
    if key == 1:
        ans = p1(mas, new)
    elif key == 2:
        ans = p2(mas, new)
    elif key == 3:
        ans = p3(mas, new)
    elif key == 4:
        ans = p4(mas, new)
    elif key == 5:
        ans = p5(mas, new)
    elif key == 6:
        ans = p6(mas, new)
    elif key == 7:
        ans = p7(mas, new)
    elif key == 8:
        ans = p8(mas, new)
    elif key == 9:
        ans = p9(mas, new)

    return ans

def selectMaster(key):
    master = [[]]
    if key == 1:
        master = open(r'master1.csv', "r", encoding='UTF-8')
    elif key == 2:
        master = open(r'master2.csv', "r", encoding='UTF-8')
    elif key == 3:
        master = open(r'master3.csv', "r", encoding='UTF-8')
    elif key == 4:
        master = open(r'master4.csv', "r", encoding='UTF-8')
    elif key == 5:
        master = open(r'master5.csv', "r", encoding='UTF-8')
    elif key == 6:
        master = open(r'master6.csv', "r", encoding='UTF-8')
    elif key == 7:
        master = open(r'master7.csv', "r", encoding='UTF-8')
    elif key == 8:
        master = open(r'master8.csv', "r", encoding='UTF-8')
    elif key == 9:
        master = open(r'master9.csv', "r", encoding='UTF-8')

    return master

def checkAns(cans1, cans2, cans3, key1, key2, key3):
    if abs(cans1) < 3000:
        if abs(cans2) < 3000:
            if abs(cans3) < 3000:
                collectAns(0, 0)
            else:
                collectAns(1, key3)
        else:
            collectAns(1, key2)
    else:
        collectAns(1, key1)

def collectAns(i, key):
    if i == 0:
        print("Pose Correct")
        print("The door will unlock")
        sys.exit(777)
    elif i == 1:
        print("Pose {0} Incorrect".format(key))
        print("Go Back to your Home")
        sys.exit(666)

key1 = (int)(argv[1] / 100) #先頭一桁
key2 = (int)((argv[1]%100) / 10)     #二桁目
key3 = (int)((argv[1]%100)%10)     #三桁目
               #実行時のコマンドライン引数としてpose番号を3桁で渡す
               #argv[]の第一引数は実行ファイル名，第二引数をkeyとして受け取る

#keyによって開くmasterファイルを決定する辞書
if (key1 or key2 or key3) == None:
    print("key Wrong!!!! FU*KI'N S*IT!!")

new1_data = open(r'new1.yml', "r", encoding='UTF-8')
new2_data = open(r'new2.yml', "r", encoding='UTF-8')
new3_data = open(r'new3.yml', "r", encoding='UTF-8')

"""masterのフォーマット変換に関わる部分は，calc-Master.pyで既に終わっているので不要
"""
lines4 = new1_data.readlines()
lines5 = new2_data.readlines()
lines6 = new3_data.readlines()

new1DataStr = []
new2DataStr = []
new3DataStr = []
new1Data = []
new2Data = []
new3Data = []

#正規表現のパターンをセット
pattern = r"0\.|[0-9]*\.[0-9]*e[\+-\-][0-9]*"

#配列にデータを追加 1行を読み込んでパターンとマッチしたものを二次元配列に追加
for line in lines4:
    new1DataStr.append(re.findall(pattern, line))
for line in lines5:
    new2DataStr.append(re.findall(pattern, line))
for line in lines6:
    new3DataStr.append(re.findall(pattern, line))

#新規データを一次元配列にfloat型で格納しなおす
new1Data = storeList(new1DataStr, new1Data)
new2Data = storeList(new2DataStr, new2Data)
new3Data = storeList(new3DataStr, new3Data)

mas1 = selectMaster(key1)
mas2 = selectMaster(key2)
mas3 = selectMaster(key3)

new1 = [[]]
new2 = [[]]
new3 = [[]]

new1 = reCoord(storeDoubleList(new1Data))
new2 = reCoord(storeDoubleList(new2Data))
new3 = reCoord(storeDoubleList(new3Data))

#ここから計算パート
#pose番号から実行する判定関数を決定する辞書

#keyを辞書に投げて関数を実行し，その結果をcansへ代入する
cans1 = selectPose(mas1, new1, key1)
cans2 = selectPose(mas2, new2, key2)
cans3 = selectPose(mas3, new3, key3)

checkAns(cans1, cans2, cans3, key1, key2, key3)
