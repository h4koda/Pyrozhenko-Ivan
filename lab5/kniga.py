#!/usr/bin/env python
# coding: utf-8

# In[2]:


from nltk.metrics import BigramAssocMeasures
from nltk.collocations import BigramCollocationFinder
from nltk.util import ngrams
import nltk
import random
import os

book = "kniga.txt"
filename = book


def count_total_amout_of_chars_with_spaces():

    file = open(filename, 'r')

    data = file.read()
    total_amount = len(data)

    file.close()

    return total_amount

    
    
def count_total_amout_of_chars_without_spaces():

    num_chars = 0

    with open(filename, 'r') as f:
        for line in f:
            for letter in line:
                for i in letter:
                    if(i != ' ' and i != '\n'):
                        num_chars += 1

    return num_chars


def total_amout_of_words_in_file():
    num_words = 0
    words_set = set() 
    one_time_words = set()
    words_array = []

    with open(filename, 'r') as f:
        for line in f:

            words = line.split()
            num_words += len(words)

            for word in words:
                words_set.add(word)
                words_array.append(word)

    for i in range(0, len(words_array)):
        if(words_array.count(words_array[i]) == 1):
            one_time_words.add(words_array[i])

    print(f'Total amount of different words {len(words_set)}')
    print(f'Total amount of unique words {len(one_time_words)}')

    return num_words


print(f'With spaces {count_total_amout_of_chars_with_spaces()}')
print(f'Without spaces {count_total_amout_of_chars_without_spaces()}')
print(f'Amout of words {total_amout_of_words_in_file()}')


# In[ ]:





# In[ ]:




