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
        with open(r'\OpenPose_demo_1.0.1\examples\masterData\masterPoint1\master1.csv', "r", encoding='UTF-8') as f:
            buf = csv.reader(f)
            for tmp in buf:
                master.append(tmp)
    elif key == 2:
        master = []
        with open(r'\OpenPose_demo_1.0.1\examples\masterData\masterPoint2\master2.csv', "r", encoding='UTF-8') as f:
            buf = csv.reader(f)
            for tmp in buf:
                master.append(tmp)
    elif key == 3:
        master = []
        with open(r'\OpenPose_demo_1.0.1\examples\masterData\masterPoint3\master3.csv', "r", encoding='UTF-8') as f:
            buf = csv.reader(f)
            for tmp in buf:
                master.append(tmp)
    elif key == 4:
        master = []
        with open(r'\OpenPose_demo_1.0.1\examples\masterData\masterPoint4\master4.csv', "r", encoding='UTF-8') as f:
            buf = csv.reader(f)
            for tmp in buf:
                master.append(tmp)
    elif key == 5:
        master = []
        with open(r'\OpenPose_demo_1.0.1\examples\masterData\masterPoint5\master5.csv', "r", encoding='UTF-8') as f:
            buf = csv.reader(f)
            for tmp in buf:
                master.append(tmp)
    elif key == 6:
        master = []
        with open(r'\OpenPose_demo_1.0.1\examples\masterData\masterPoint6\master6.csv', "r", encoding='UTF-8') as f:
            buf = csv.reader(f)
            for tmp in buf:
                master.append(tmp)
    elif key == 7:
        master = []
        with open(r'\OpenPose_demo_1.0.1\examples\masterData\masterPoint7\master7.csv', "r", encoding='UTF-8') as f:
            buf = csv.reader(f)
            for tmp in buf:
                master.append(tmp)
    elif key == 8:
        master = []
        with open(r'\OpenPose_demo_1.0.1\examples\masterData\masterPoint8\master8.csv', "r", encoding='UTF-8') as f:
            buf = csv.reader(f)
            for tmp in buf:
                master.append(tmp)
    elif key == 9:
        master = []
        with open(r'\OpenPose_demo_1.0.1\examples\masterData\masterPoint9\master9.csv', "r", encoding='UTF-8') as f:
            buf = csv.reader(f)
            for tmp in buf:
                master.append(tmp)
    return master
