# Silhouette analysis
# http://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_silhouette_analysis.html
from __future__ import print_function
import sys 
import sklearn
import sys

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

import pickle as pk

import sys

class Cluster :

    def __init__(self ):
        print(sklearn.__version__)
        print(__doc__)

        
    def kmeans(self , posts_dict):

        documents = []
        for k,v in posts_dict.items():
            documents.append(v["text_filtered"])

        # print(len(documents))

        vectorizer = TfidfVectorizer(stop_words='english' , min_df=10)
        X = vectorizer.fit_transform(documents)

<<<<<<< HEAD
        score = [] 
        #K = [10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100] 

=======
        
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

>>>>>>> e062c78ee4f5bc0034934c3af4731d56de3082c4

        model_13 = KMeans(n_clusters=13, init='k-means++', max_iter= sys.maxsize, random_state= 5 , n_jobs=-1).fit(X)
        pk.dump(model_13 ,  open("model_13.p","wb"))
        print(" 13 : " +   str(model_13.inertia_))

        model_33 = KMeans(n_clusters=33, init='k-means++', max_iter= sys.maxsize, random_state= 5 , n_jobs=-1).fit(X)
        pk.dump(model_33 ,  open("model_33.p","wb"))
        print( " 33  : " +  str(model_33.inertia_))


        # K = list(range(2,61))
        # for k in K: 
        #     KMeanModel_1 = KMeans(n_clusters=k, init='k-means++', max_iter=300, random_state= 5,tol=1 , n_jobs=-1).fit(X)

        #     KMeanModel_2 = KMeans(n_clusters=k, init='k-means++', max_iter=300 , random_state=7 , tol=1, n_jobs=-1).fit(X)

        #     rss = min(KMeanModel_1.inertia_ , KMeanModel_2.inertia_)
        #     score.append(rss)

        #     print(str(k) + " : " + str(rss))

        # print (score)
        # plt.plot(K, score ,'bx-')
        # plt.xlabel('k')
        # plt.ylabel('Distortion')
        # plt.title('The Elbow Method showing the optimal k')
        # plt.xticks(range(2,61,1))
        # plt.savefig('final.png')
        # plt.show()
    


        # feature terms ===================================================

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


        









    




        

        

    

