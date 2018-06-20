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

key = argv[1] #実行時のコマンドライン引数としてpose番号を渡す
              #argv[]の第一引数は実行ファイル名，第二引数をkeyとして受け取る

#keyによって開くmasterファイルを決定する辞書
dict_master = {
    1: open(r'master1.yml', "r", encoding='UTF-8'),
    2: open(r'master2.yml', "r", encoding='UTF-8'),
    3: open(r'master3.yml', "r", encoding='UTF-8'),
    4: open(r'master4.yml', "r", encoding='UTF-8'),
    5: open(r'master5.yml', "r", encoding='UTF-8'),
    6: open(r'master6.yml', "r", encoding='UTF-8'),
    7: open(r'master7.yml', "r", encoding='UTF-8'),
    8: open(r'master8.yml', "r", encoding='UTF-8'),
    9: open(r'master9.yml', "r", encoding='UTF-8')
}

if key in dict_master:
    master_data = dict_master[key]
else:
    print("do not work")

new_data = open(r'new.yml', "r", encoding='UTF-8')

lines = new_data.readlines()
lines2 = master_data.readlines()
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

mas = [[]]
new = [[]]


mas = reCoord(storeDoubleList(masterData))
new = reCoord(storeDoubleList(newData))

#ここから計算パート
#pose番号から実行する判定関数を決定する辞書
dict_pose = {
    1: p1(mas, new),
    2: p2(mas, new),
    3: p3(mas, new),
    4: p4(mas, new),
    5: p5(mas, new),
    6: p6(mas, new),
    7: p7(mas, new),
    8: p8(mas, new),
    9: p9(mas, new)
    }

#keyを辞書に投げて関数を実行し，その結果をcansへ代入する
if key in dict_pose:
    cans = dict_pose[key]
else:
    print("do not work")


if abs(cans) < 3000 :
    print("Pose Correct")
    print("The door will unlock")
    sys.exit(777)
else:
    print("Pose Incorrect")
    print("Go Back to your Home")
    sys.exit(666)
