# Silhouette analysis
# http://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_silhouette_analysis.html
from __future__ import print_function

import sklearn
import sys

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
from scipy.spatial.distance import cdist

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score


class Cluster :

    def __init__(self ):
        print(sklearn.__version__)
        print(__doc__)

        
    def kmeans(self , posts_dict):

        documents = []
        for k,v in posts_dict.items():
            documents.append(v["text_filtered"])

        # print(len(documents))

        vectorizer = TfidfVectorizer(stop_words='english')
        X = vectorizer.fit_transform(documents)

        
        # model = KMeans(n_clusters=true_k, init='k-means++', max_iter=500, n_init=1)
        # model.fit(X)
        
        x = np.array(list(documents))

        # test 
        # Ks = range (1,9)
        # km = [KMeans(n_clusters = i, init='k-means++', max_iter=300, n_init=1) for i in Ks]
        # score = [abs(km[i].fit(X).score(X)) for i in range(len(km))]

        score = [] 
        K = [10,20,30,40,50,60,70,80,90,100] 
        for k in K: 
            KMeanModel = KMeans(n_clusters=k, init='k-means++', max_iter=300)
            KMeanModel.fit(X)
            score.append(KMeanModel.inertia_)


        print (score)
        plt.plot(Ks, score ,'bx-')
        plt.xlabel('k')
        plt.ylabel('Distortion')
        plt.title('The Elbow Method showing the optimal k')
        plt.show()


        # feature terms 
        '''
        print("Top terms per cluster:")
        order_centroids = model.cluster_centers_.argsort()[:, ::-1]
        terms = vectorizer.get_feature_names()
        
        for i in range(2):
            print("Cluster %d:" % i)
            for ind in order_centroids[i, :10]:
                print(' %s' % terms[ind]),
            print("=================")
        '''


        # print("\n")
        # print("Prediction")

        # Y = vectorizer.transform(["chrome browser to open."])
        # prediction = model.predict(Y)
        # print(prediction)

        # Y = vectorizer.transform(["My cat is hungry."])
        # prediction = model.predict(Y)
        # print(prediction)


        # Y = vectorizer.transform(["Google search  is good."])
        # prediction = model.predict(Y)
        # print(prediction)


        









    




        

        

    

