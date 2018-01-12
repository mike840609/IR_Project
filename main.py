from  Model.Formatter import Formatter
import json 
import os
import sys

# pip freeze > requirements.txt


def main():
    
    formatter = Formatter()
    posts_dict = formatter.getPosts_dict()

    # print (json.dumps(posts_dict, indent=2))

    print (len(posts_dict))




if __name__ == '__main__':
    main()
    