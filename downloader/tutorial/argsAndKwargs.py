#!/usr/bin/env python
"""
Args and Kwargs - Intermediate Python Programming p.25  By ---- sentdex
"""
def function(arg1,*args,**kwargs): 
    """
    args : []
    kwargs: key word args {}
    """
    pass

"""
args:
"""
title = "Youzark's blog"
blog1 = "I am so awesome"
blog2 = "It makes me so happy"
def blogPosts(title , *args):
    print(title + " :")
    for post in args:
        print(post)
blogPosts(title,blog1,blog2)


"""
kwargs:
"""
def keywordPosts(title, **kwargs):
    print(title + " :")
    for postKw,post in kwargs.items():
        print(postKw,":",post)

keywordPosts(title = "Youzark's blog",
        blog1 = "I am so awesome",
        blog2 = "It makes me so happy")


"""
Unpacking lists as arguments
"""
title = "Youzark's blog"
blog1 = "I am so awesome"
blog2 = "It makes me so happy"
infoList = [title, blog1, blog2]
blogPosts(*infoList) ## unpack the infoList into positional arguments

