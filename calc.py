#誤差修正プログラム
#floatの座標データを取得し、正解のデータとの誤差を修正する

import csv

#csv_obj = csv.render(open('pointdata.csv', 'r'))
#data = [v for v in csv_obj]
#data_conved = [[float(elm) for elm in v] for v in data]

#data conversion section
#conversion string to float
data = [[float(elm) for elm in v] for v in csv.render(open("pointdata","r"))]
print(data)