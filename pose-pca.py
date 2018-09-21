import numpy as np
from matplotlib import pyplot as plt
from sklearn.decomposition import PCA
import csv
from sklearn import datasets


def main():
    new = []
    targets = np.zeros(50)
    master = np.zeros(((50, 8, 2)))
    for i in range(1, 51):
        with open(r'\OpenPose_demo_1.0.1\examples\test_image\pose9-test\model{0}.csv'.format(i), 'r') as f:
            buf = csv.reader(f)
            for tmp in buf:
                new.append(tmp)
            for j in range(8):
                for k in range(2):
                    targets[i-1] = 0
                    master[i-1][j][k] = new[j][k]
    #print(new[0])
    #print(master)
    features = new
    # 主成分分析を実行
    pca = PCA(n_components=2)
    pca.fit(features)

    # 分析結果を元にデータセットを主成分に変換する
    transformed = pca.fit_transform(features)
    # 主成分をプロット
    for label in np.unique(targets):
        plt.scatter(transformed[targets == label, 0], transformed[targets == label, 1])
        #plt.scatter(transformed[0], transformed[1])

    plt.title('principal component')
    plt.xlabel('PC1')
    plt.ylabel('PC2')

    # 寄与率とはざっくり言えば各次元の重要度
    print('各次元の寄与率: {0}'.format(pca.explained_variance_ratio_))
    print('累積寄与率: {0}'.format(sum(pca.explained_variance_ratio_)))

    plt.show()


if __name__ == '__main__':
    main()
