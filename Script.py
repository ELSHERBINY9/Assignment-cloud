#!/usr/bin/env python
# coding: utf-8

# In[17]:


import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter


# In[11]:


# Download NLTK resources
nltk.download('punkt')
nltk.download('stopwords')


# In[18]:


# Read the contents of the "random_paragraphs.txt" file
file_path = '/app/random_paragraphs.txt'
with open(file_path, 'r') as file:
    text = file.read()


# In[19]:


# Tokenize the text into words
words = nltk.word_tokenize(text)


# In[20]:


# Remove stop words
stop_words = set(stopwords.words('english'))
filtered_words = [word for word in words if word.lower() not in stop_words]


# In[21]:


# Count the frequency of each word
word_frequency = Counter(filtered_words)


# In[22]:


# Display word frequency count to the console
for word, count in word_frequency.items():
    print(f'{word}: {count}')

