# checkまわりの関数まとめ
import sys
from sys import argv

def checkKey(key1, key2, key3):
    if key1 is 0:
        if (key2 != 0 and key3 != 0):
            print("ERROR : 1st key is Wrong!!!!")
            sys.exit(1)
        elif (key2 is 0 and key3 != 0):
            print("ERROR : 1st and 2nd keys is Wrong!!!!")
            sys.exit(11)
    elif key2 is 0:
        if (key3 != 0):
            print("ERROR : 2nd key is Wrong!!!!")
            sys.exit(10)
        elif (key3 is 0):
            print("ERROR : 2nd and 3rd keys is Wrong!!!!")
            sys.exit(110)
    elif key3 is 0:
        if (key1 != 0 and key2 != 0):
            print("ERROR : 3rd key is Wrong!!!!")
            sys.exit(100)
        elif (key1 is 0 and key2 != 0):
            print("ERROE : 1st and 3rd key is Wrong!!!!")
            sys.exit(101)
    elif ((key1 is 0 and key2 is 0) and key3 is 0):
        print("ERROR : All keys is Wrong!!!!")
        sys.exit(111)

    return


def checkAns(cans1, cans2, cans3, key1, key2, key3):
    if abs(cans1) < 30000:
        if abs(cans2) < 30000:
            if abs(cans3) < 30000:
                collectAns(0, 0, key1)
            else:
                collectAns(1, 3, key3)
        else:
            collectAns(1, 2, key2)
    else:
        collectAns(1, 1, key1)


def collectAns(i, num, key):
    if i == 0:
        print("Pose Correct")
        print("The door will unlock")
        sys.exit(777)
    elif i == 1:
        if num == 1:
            print("1st Pose No.{0} Incorrect".format(key))
        elif num == 2:
            print("2nd Pose No.{0} Incorrect".format(key))
        elif num == 3:
            print("3rd Pose No.{0} Incorrect".format(key))
        print("Go Back To Your Home!!!")
        sys.exit(666)


if len(sys.argv) == 1:
    print("Argument is None")
    sys.exit(555)
