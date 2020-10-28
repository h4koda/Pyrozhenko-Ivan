#!/usr/bin/env python
# coding: utf-8

# In[5]:


from nltk.metrics import BigramAssocMeasures
from nltk.collocations import BigramCollocationFinder
from nltk.util import ngrams
import nltk
import random
import os

first_list = ['1', '2', '3', '4', '5', '6', '7', '8']
second_list = ['9', '10', '11', '12',
               '13', '14', '15', '16']
third_list = ['17', '18', '19', '20', '21', '22', '23', '24']

list_of_strings_list = [first_list, second_list, third_list]


def random_phrase():
    result_string = ""
    for i in range(0, 3):
        random_index = random.randrange(0, 7)
        result_string = result_string +             list_of_strings_list[i][random_index] + " "

    return result_string

print(random_phrase())


# In[ ]:




