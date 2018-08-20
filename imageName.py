import re
from sys import argv
import sys
import numpy as np

dataName = open(r'\OpenPose_demo_1.0.1\examples\analysisData\imageName.txt', "r")
lines = dataName.readlines()
pattern = r"[0-9]{3}"

PNameStr = []
PName = []

#配列にデータを追加 1行を読み込んでパターンとマッチしたものを二次元配列に追加
for line in lines:
    PNameStr.append(re.findall(pattern, line))

#一次元配列にfloat型で格納しなおす
for i in range(len(PNameStr)):
        for j in range(len(PNameStr[i])):
            PName.append(int(PNameStr[i][j]))

reNum = int((PName[0] % 100) % 10)*100 + int((PName[1] % 100) % 10)*10 + int((PName[2] % 100) % 10)

print(PName)
print(reNum)
sys.exit(reNum)
