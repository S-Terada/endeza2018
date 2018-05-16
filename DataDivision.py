import re
import csv

test_data = open(r'\OpenPose_demo_1.0.1\examples\test_image\PointData\camerat_pose.yml', "r")
lines = test_data.readlines()
i = 0
PointDataStr = []
PointData = []

#正規表現のパターンをセット
pattern = r"0\.|[0-9]*\.[0-9]*e[\+-\-][0-9]*"

#配列にデータを追加 1行を読み込んでパターンとマッチしたものを二次元配列に追加
for line in lines:
    PointDataStr.append(re.findall(pattern, line))

#一次元配列にfloat型で格納しなおす
for i in range(len(PointDataStr)):
        for j in range(len(PointDataStr[i])):
            PointData.append(float(PointDataStr[i][j]))

#csvファイルにデータを出力
with open(r'\OpenPose_demo_1.0.1\examples\test_image\PointData\pointdata.csv', 'w', newline="") as wri:
    writer = csv.writer(wri, lineterminator='\n')
    writer.writerow(PointData)

test_data.close()
