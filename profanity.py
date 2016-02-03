# -*- coding: utf-8 -*-
import os
import urllib

def read_text():
    path = os.path.expanduser(r"~/Desktop/movie_quotes.txt")
    quotes = open(path)
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)

def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdyl.com/profanity?q="+text_to_check)
    output = connection.read()
    print(output)
    connection.close()

    if "true" in output:
        print("Profanity Alert!")
    elif "false" in output:
        print("This document has no curse words!")
    else:
        print("Could not scan the document properly.")
        
    
read_text()
