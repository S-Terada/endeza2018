#masterまわりの関数まとめ
import numpy as np
import csv

def storeMasterList(data):
    array = np.zeros((8, 2))
    k = 0
    i = 0
    j = 0
    for i in range(8):
        for j in range(2):
                array[i][j] = data[k]
                k += 1
    # print(array)
    return array

def selectMaster(key):
    master = [[]]
    if key == 1:
        master = []
        with open(r'master1.csv', "r", encoding='UTF-8') as f:
            buf = csv.reader(f)
            for tmp in buf:
                master.append(tmp)
    elif key == 2:
        master = []
        with open(r'master2.csv', "r", encoding='UTF-8') as f:
            buf = csv.reader(f)
            for tmp in buf:
                master.append(tmp)
    elif key == 3:
        master = []
        with open(r'master3.csv', "r", encoding='UTF-8') as f:
            buf = csv.reader(f)
            for tmp in buf:
                master.append(tmp)
    elif key == 4:
        master = []
        with open(r'master4.csv', "r", encoding='UTF-8') as f:
            buf = csv.reader(f)
            for tmp in buf:
                master.append(tmp)
    elif key == 5:
        master = []
        with open(r'master5.csv', "r", encoding='UTF-8') as f:
            buf = csv.reader(f)
            for tmp in buf:
                master.append(tmp)
    elif key == 6:
        master = []
        with open(r'master6.csv', "r", encoding='UTF-8') as f:
            buf = csv.reader(f)
            for tmp in buf:
                master.append(tmp)
    elif key == 7:
        master = []
        with open(r'master7.csv', "r", encoding='UTF-8') as f:
            buf = csv.reader(f)
            for tmp in buf:
                master.append(tmp)
    elif key == 8:
        master = []
        with open(r'master8.csv', "r", encoding='UTF-8') as f:
            buf = csv.reader(f)
            for tmp in buf:
                master.append(tmp)
    elif key == 9:
        master = []
        with open(r'master9.csv', "r", encoding='UTF-8') as f:
            buf = csv.reader(f)
            for tmp in buf:
                master.append(tmp)
    return master