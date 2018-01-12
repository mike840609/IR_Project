import sys
import os
import re
import json
import pickle

from Model.Poter_Algo.PorterStemmer import *
from nltk.stem import WordNetLemmatizer


class Formatter:

    def __init__(self ):
        #  { id : dict }  user dictionary 
        self.posts_dict = {}
        self.term_dictionay = {}
        self.stopWord_list = []

        self.stemmer = PorterStemmer()
        self.wnl = WordNetLemmatizer()

    def genarate_dict(self):
        # with open("StaticDoc/trump_simple.json", 'r') as f:
        with open("StaticDoc/trump_simple_test.json", 'r') as f:
            posts = json.load(f)
        
        #  convert to  {id : dict } dict 
        for idx , post in enumerate( posts ) :
            self.posts_dict[str(idx+1)] = post
    
        # print (self.posts_dic['1']['text']) 

        #  stop word array
        stop_temp = open('StaticDoc/stopList.txt').read()
        self.stopWord_list = stop_temp.lower().split()

    #  tokenization
    def tokenize(self):

        for key , post in  self.posts_dict.items() : 

            # text = post["text"].encode('utf-8').lower()
            text = post["text"].lower()

            text = re.sub(r"http\S+", "", text)

            print(text)

            text = re.sub('[^a-zA-Z]+', ' ', text)
            
            print ("\n")
            self.posts_dict[key]["text"]
            text_arr = text.split()
            
            #  stopword operation 
            text_arr = [x for x in text_arr if x not in self.stopWord_list ]

            for idx , word in enumerate( text_arr ):
                # stemming or lemmatization

                # after_stm = self.stemmer.stem(word , 0 , len(word)-1)
                after_stm = self.wnl.lemmatize(word)

                text_arr[idx] = after_stm

            #  add to dict
            self.posts_dict[key]["stem_arr"] = text_arr
            self.posts_dict[key]["af_text"] = text
    
    def saveToPickle(self):
        pickle.dump(self.posts_dict , open("posts_dict.p","wb"))
    
    def loadPickle(self):
        self.posts_dict = pickle.load(open("posts_dict.p", 'rb'))

    # def genDictionary (self):
    #     pass

    def getPosts_dict(self):
        if os.path.isfile("posts_dict.p"):

            print("load posts dict")
            self.loadPickle()

            # self.genarate_dict()
            # self.tokenize()
            # self.saveToPickle()

            
        else:
            
            print("create posts dict")
            self.genarate_dict()
            self.tokenize()
            self.saveToPickle()
        
        return self.posts_dict
            
        
        
