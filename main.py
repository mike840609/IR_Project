from  Model.Formatter import Formatter
import os

def main():
    formatter = Formatter('StaticDoc/trump_posts_test.json')
    # formatter = Formatter('StaticJson/trump_posts.json')
    formatter.tokenize()

if __name__ == '__main__':
    main()
    