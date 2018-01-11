from  Model.Formatter import Formatter
import json 
import os
import sys

# pip freeze > requirements.txt


def main():
    
    # formatter = Formatter('StaticDoc/trump_simple.json')
    formatter = Formatter('StaticDoc/trump_simple_test.json')
    # formatter.tokenize()
    # formatter.saveToPickle()
    formatter.loadPickle()
    posts_dict = formatter.getPosts_dict()
    

    print (json.dumps(posts_dict, indent=2))
    # print (json.dumps(formatter.getPosts_dict(), indent=2))




if __name__ == '__main__':
    main()
    