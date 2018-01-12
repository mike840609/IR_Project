# Silhouette analysis
# http://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_silhouette_analysis.html
from __future__ import print_function

import sklearn

import plotly.plotly as py
import plotly.graph_objs as go
from plotly import tools

from sklearn import cluster, datasets, metrics
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_samples, silhouette_score

import matplotlib
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np


class Cluster :

    def __init__(self ):
        print(sklearn.__version__)
        print(__doc__)

        self.test()
    



    def test(self):
        
        # 讀入鳶尾花資料
        iris = datasets.load_iris()
        iris_X = iris.data

        for i in iris_X:
            print(i[0])
            print(i[1])
            print(i[2])
            break

        # # 迴圈
        # silhouette_avgs = []
        # ks = range(2, 11)

        # for k in ks:
        #     kmeans_fit = cluster.KMeans(n_clusters = k).fit(iris_X)
        #     cluster_labels = kmeans_fit.labels_
        #     silhouette_avg = metrics.silhouette_score(iris_X, cluster_labels)
        #     silhouette_avgs.append(silhouette_avg)


        # # 作圖並印出 k = 2 到 10 的績效
        # plt.bar(ks, silhouette_avgs)
        # plt.show()
        # print(silhouette_avgs)



        

    

