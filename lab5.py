#!/usr/bin/env python
# coding: utf-8

# In[1]:


pwd


# In[4]:


get_ipython().run_cell_magic('writefile', 'first_group.txt', 'Name|Rating\nJohn;12\nBob;34\nAlice;56\nJulia;32')


# In[6]:


file = open('first_group.txt')


# In[7]:


data = file.read()
data


# In[8]:


print(data)


# In[9]:


get_ipython().run_cell_magic('writefile', 'second_group.txt', 'Name|Rating\nVanya;15\nOlga;31\nVika;44\nSasha;10\nAnatoliy;18')


# In[10]:


file = open('second_group.txt')
file.read()


# In[22]:


file.seek(0)


# In[23]:


data2 = file.read()
data2


# In[24]:


print(data2)


# In[26]:


file.close()


# In[27]:


print(file.closed)


# In[28]:


with open('first_group.txt') as first_file:
    first_data = first_file.read()


# In[29]:


print(first_data)


# In[ ]:




