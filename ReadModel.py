#masterまわりの関数まとめ
import numpy as np
import csv

def ReadMaster(key, i):
    master = [[]]
    if key == 1:
        master = []
        with open(r'\OpenPose_demo_1.0.1\examples\test_image\pose1-test\model{0}.csv'.format(i), 'r') as f:
            buf = csv.reader(f)
            for tmp in buf:
                master.append(tmp)
        print("key1 was read")
    elif key == 2:
        master = []
        with open(r'\OpenPose_demo_1.0.1\examples\test_image\pose2-test\model{0}.csv'.format(i), 'r') as f:
            buf = csv.reader(f)
            for tmp in buf:
                master.append(tmp)
        print("key2 was read")
    elif key == 3:
        master = []
        with open(r'\OpenPose_demo_1.0.1\examples\test_image\pose3-test\model{0}.csv'.format(i), 'r') as f:
            buf = csv.reader(f)
            for tmp in buf:
                master.append(tmp)
        print("key3 was read")
    elif key == 4:
        master = []
        with open(r'\OpenPose_demo_1.0.1\examples\test_image\pose4-test\model{0}.csv'.format(i), 'r') as f:
            buf = csv.reader(f)
            for tmp in buf:
                master.append(tmp)
        print("key4 was read")
    elif key == 5:
        master = []
        with open(r'\OpenPose_demo_1.0.1\examples\test_image\pose5-test\model{0}.csv'.format(i), 'r') as f:
            buf = csv.reader(f)
            for tmp in buf:
                master.append(tmp)
        print("key5 was read")
    elif key == 6:
        master = []
        with open(r'\OpenPose_demo_1.0.1\examples\test_image\pose6-test\model{0}.csv'.format(i), 'r') as f:
            buf = csv.reader(f)
            for tmp in buf:
                master.append(tmp)
        print("key6 was read")
    elif key == 7:
        master = []
        with open(r'\OpenPose_demo_1.0.1\examples\test_image\pose7-test\model{0}.csv'.format(i), 'r') as f:
            buf = csv.reader(f)
            for tmp in buf:
                master.append(tmp)
        print("key7 was read")
    elif key == 8:
        master = []
        with open(r'\OpenPose_demo_1.0.1\examples\test_image\pose8-test\model{0}.csv'.format(i), 'r') as f:
            buf = csv.reader(f)
            for tmp in buf:
                master.append(tmp)
        print("key8 was read")
    elif key == 9:
        master = []
        with open(r'\OpenPose_demo_1.0.1\examples\test_image\pose9-test\model{0}.csv'.format(i), 'r') as f:
            buf = csv.reader(f)
            for tmp in buf:
                master.append(tmp)
        print("key9 was read")
    return master


def ReadChild(key):
    if key == 1:
        with open(r'\OpenPose_demo_1.0.1\101_keypoints.json', 'r') as f:
            print(f)
            json1 = json.load(f)
        print("key1 was read")
    elif key == 2:
        
        with open(r'\OpenPose_demo_1.0.1\202_keypoints.json', 'r') as f:
            json1 = json.load(f)
        print("key2 was read")
    elif key == 3:
        
        with open(r'\OpenPose_demo_1.0.1\303_keypoints.json', 'r') as f:
            json1 = json.load(f)
        print("key3 was read")
    elif key == 4:
        
        with open(r'\OpenPose_demo_1.0.1\404_keypoints.json', 'r') as f:
            json1 = json.load(f)
        print("key4 was read")
    elif key == 5:

        with open(r'\OpenPose_demo_1.0.1\505_keypoints.json', 'r') as f:
            json1 = json.load(f)
        print("key5 was read")
    elif key == 6:
        
        with open(r'\OpenPose_demo_1.0.1\606_keypoints.json', 'r') as f:
            json1 = json.load(f)
        print("key6 was read")
    elif key == 7:
        
        with open(r'\OpenPose_demo_1.0.1\707_keypoints.json', 'r') as f:
            json1 = json.load(f)
        print("key7 was read")
    elif key == 8:
        
        with open(r'\OpenPose_demo_1.0.1\808_keypoints.json', 'r') as f:
            json1 = json.load(f)
        print("key8 was read")
    elif key == 9:

        with open(r'\OpenPose_demo_1.0.1\909_keypoints.json', 'r') as f:
            json1 = json.load(f)
        print("key9 was read")
    return json1