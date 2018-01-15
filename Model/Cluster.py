# Silhouette analysis
# http://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_silhouette_analysis.html
from __future__ import print_function
import sys 
import sklearn

from sklearn import cluster, datasets, metrics
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_samples, silhouette_score

import matplotlib
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np


from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score
# import pickle as pk

class Cluster :

    def __init__(self ):
        print(sklearn.__version__)
        print(__doc__)

        
    def kmeans(self , posts_dict):

        # documents = ["This little kitty came to play when I was eating at a restaurant.",
        #      "Merley has the best squooshy kitten belly.",
        #      "Google Translate app is incredible.",
        #      "If you open 100 tab in google you get a smiley face.",
        #      "Best cat photo I've ever taken.",
        #      "Climbing ninja cat.",
        #      "Impressed with google map feedback.",
        #      "Key promoter extension for Google Chrome."]

        documents = []
        for k,v in posts_dict.items():
            documents.append(v["text_filtered"])

        print(len(documents))

        vectorizer = TfidfVectorizer(stop_words='english' , min_df=10)
        X = vectorizer.fit_transform(documents)

        score = [] 
        #K = [10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100] 
        K = list(range(2,61))
        for k in K: 
            KMeanModel_1 = KMeans(n_clusters=k, init='k-means++', max_iter=300, random_state= 5,tol=1e-1 , n_jobs=-1).fit(X)

            KMeanModel_2 = KMeans(n_clusters=k, init='k-means++', max_iter=300 , random_state=7 , tol=1e-1, n_jobs=-1).fit(X)

            rss = min(KMeanModel_1.inertia_ , KMeanModel_2.inertia_)
            score.append(rss)

            print(str(k) + " : " + str(rss))

        print (score)
        plt.plot(K, score ,'bx-')
        plt.xlabel('k')
        plt.ylabel('Distortion')
        plt.title('The Elbow Method showing the optimal k')
        plt.xticks(range(2,61,1))
        plt.savefig('final.png')
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


        









    




        

        

    

