import numpy as np
import re

def storeList(dataStr, data):
    for i in range(len(dataStr)):
        for j in range(len(dataStr[i])):
            data.append(float(dataStr[i][j]))
    return data


#xy座標を二重リストに格納する関数
def storeDoubleList(data):
    array = np.zeros((8, 2))
    k = 0
    for i in range(8):
        for j in range(3):
            if k % 3 != 2:
                array[i][j] = data[k]
                k += 1
            else:
                k += 1
    return array


#首基準の相対座標に直す関数
def reCoord(data):
    neckx = data[1][0]
    necky =data[1][1]

    for i in range(0, 8):
        data[i][0] -= neckx
        data[i][1] -= necky
    return data


new_data = open(r'\OpenPose_demo_1.0.1\examples\masterData\masterPoint9\proto2_pose.yml', "r", encoding='UTF-8')
lines1 = new_data.readlines()

mas1DataStr = []
mas1Data = []
pattern = r"0\.|[0-9]*\.[0-9]*e[\+-\-][0-9]*"
for line in lines1:
    mas1DataStr.append(re.findall(pattern, line))
mas1Data = storeList(mas1DataStr, mas1Data)
mas1 = [[]]
mas1 = reCoord(storeDoubleList(mas1Data))
print(mas1)