import sys
import re
import json


class Formatter:

    stopWord_list = []

    #  { id : dict }  user dictionary 
    posts_dic = {}

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

    
    #  tokenization
    def tokenize(self):

        for key , post in  self.posts_dic.items() : 

            text = post["text"].encode('utf-8').lower()
            text = re.sub('[^a-zA-Z]+', ' ', text)
            text_arr = text.split()
            
            #  stopword operation 
            text_arr = [x for x in text_arr if x not in self.stopWord_list ]
            
            #  add to dict
            self.posts_dic[key]["stem_arr"] = text_arr
            print (json.dumps(self.posts_dic[key] , indent=4))   

            break

            