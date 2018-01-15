from  Model.Formatter import Formatter
from  Model.Cluster import Cluster
import json 
import os
import sys


import plotly 
import pickle

# pip freeze > requirements.txt

def main():
    plotly.tools.set_credentials_file(username='mike840609', api_key='1tjLWo3103p9bPcl6NN1')

    # '''
    formatter = Formatter()
    posts_dict = formatter.getPosts_dict()

    
    print (json.dumps(posts_dict["1"], indent=2))
    # print (json.dumps(posts_dict["2"], indent=2))
    # print (json.dumps(posts_dict["3"], indent=2))
    # print (json.dumps(posts_dict["4"], indent=2))
    # print (json.dumps(posts_dict["5"], indent=2))
    # print (json.dumps(posts_dict["6"], indent=2))


    # cluster_ope = Cluster()
    # cluster_ope.kmeans(posts_dict)

    rss = pickle.load(open("rss_score.p", 'rb'))
    print (rss)
    



if __name__ == '__main__':
    main()
    