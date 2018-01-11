import sys
import re
import json
import pickle

from Model.Poter_Algo.PorterStemmer import *
from nltk.stem import WordNetLemmatizer


class Formatter:

    stopWord_list = []

    #  { id : dict }  user dictionary 
    posts_dic = {}
    term_dictionay = {}

    def __init__(self , json_path = None):
        with open(json_path, 'r') as f:
            posts = json.load(f)
        
        #  convert to  {id : dict } dict 
        for idx , post in enumerate( posts ) :
            self.posts_dic[str(idx+1)] = post
    
        # print (json.dumps(self.posts_dic , indent=4))   
        # print (self.posts_dic['1']['text']) 

        #  stop word array
        stop_temp = open('StaticDoc/stopList.txt').read()
        self.stopWord_list = stop_temp.lower().split()

    
    stemmer = PorterStemmer()
    wnl = WordNetLemmatizer()

    #  tokenization
    def tokenize(self):

        for key , post in  self.posts_dic.items() : 

            # text = post["text"].encode('utf-8').lower()
            text = post["text"].lower()

            text = re.sub('[^a-zA-Z]+', ' ', text)
            text_arr = text.split()
            
            #  stopword operation 
            text_arr = [x for x in text_arr if x not in self.stopWord_list ]

            for idx , word in enumerate( text_arr ):
                # stemming or lemmatization

                # after_stm = self.stemmer.stem(word , 0 , len(word)-1)
                after_stm = self.wnl.lemmatize(word)

                text_arr[idx] = after_stm

            #  add to dict
            self.posts_dic[key]["stem_arr"] = text_arr

    
    def saveToPickle(self):
        pickle.dump(self.posts_dic , open("posts_dict.p","wb"))
    
    def loadPickle(self):
        self.posts_dic = pickle.load(open("posts_dict.p", 'rb'))

    def genDictionary (self):
        pass

    def getPosts_dict(self):
        return self.posts_dic
        
