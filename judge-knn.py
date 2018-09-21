import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn import neighbors, datasets

n_neighbors = 80

iris = datasets.load_iris()

#xにはがく片の長さとがく片の幅を格納
x = iris.data[:, :2]
#yには品種のコードを格納、データは150件
y = iris.target

print(y)
#print(y)

h = .02

cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF'])
cmap_bold = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])

cnt = 0

for weights in ['uniform', 'distance']:
    #重みづけとkの数を決める
    clf = neighbors.KNeighborsClassifier(n_neighbors, weights=weights)
    #モデルの作成
    clf.fit(x, y)

    #描画する範囲の選択
    #x,yの最大値+1と最小値-1を限度にする
    x_min, x_max = x[:, 0].min() - 1, x[:, 0].max() + 1
    y_min, y_max = x[:, 1].min() - 1, x[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])

    Z = Z.reshape(xx.shape)
    plt.figure()
    plt.pcolormesh(xx, yy, Z, cmap=cmap_light)

    plt.scatter(x[:, 0], x[:, 1], c=y, cmap=cmap_bold, edgecolors='k', s=20)
    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())
    plt.title("3-Class classification (k = %i, weights = '%s)" % (n_neighbors, weights))

    plt.show()
