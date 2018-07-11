# Listまわりの関数まとめ
# 座標データを格納する関数
import numpy as np

def storeList(dataStr, data):
    for i in range(len(dataStr)):
        for j in range(len(dataStr[i])):
            data.append(float(dataStr[i][j]))
    return data

# xy座標を二重リストに格納する関数
def storeDoubleList(data):
    array = np.zeros((8, 2))
    k = 0
    i = 0
    j = 0
    for i in range(8):
        for j in range(3):
            if k % 3 != 2:
                array[i][j] = data[k]
                k += 1
            else:
                k += 1
    # print(array)
    return array
