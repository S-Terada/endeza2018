from sys import argv
import glob
import re
import csv

master = []
with open(r'\OpenPose_demo_1.0.1\examples\masterData\masterPoint2\master2.csv', "r", encoding='UTF-8') as f:
    buf = csv.reader(f)
    for tmp in buf:
        print(tmp)
        master.append(tmp)
