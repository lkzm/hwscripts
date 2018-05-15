#! /bin/python3
import os
import sys
from os.path import join, split, isfile


cur = split(os.path.realpath(__file__))[0]



def count (path):
    i = 0
    for x in os.listdir(path):
        if isfile(join(path, x)):
            i=i+1
        else:
            count(join(path, x))
    
                    
    print (path, ' ----- ', i)


count(cur)

