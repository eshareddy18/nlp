#!/usr/bin/env python
# coding: utf-8

# In[1]:


import nltk
from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')
lemmatizer = WordNetLemmatizer()
print(lemmatizer.lemmatize("pizzas"))


# In[2]:


import nltk    
get_ipython().system('pip install textblob')
from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')
lemmatizer = WordNetLemmatizer()
text = "pizzas"
res = lemmatizer.lemmatize(text)
print(res)


# In[3]:


import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))
text = ['This','is','a','sample','sentence']
res = [word for word in text if word.lower() not in stop_words]
print(res)


# In[ ]:



project 1
calculate the lemenstin distance between START and STARE
project 2 
clean a dirty sentence for a search engine
input is: "The quick,Brown foxes...
    they are JUMPING over
    10 lazy dogs!"
Output is:["quick","brown","fox","jump","lazy","dogs"]
project 3:
A spam trigger
build a simple logic based filter 
challenge: create list of 3 spam words example:["win","cash","free","prize"]
        input is:"you are winning a free prize now!"
            output should be ike spam or not


# In[4]:



def levenshtein_distance(a, b):
    m, n = len(a), len(b)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i - 1] == b[j - 1]:
                cost = 0
            else:
                cost = 1

            dp[i][j] = min(
                dp[i - 1][j] + 1,      # deletion
                dp[i][j - 1] + 1,      # insertion
                dp[i - 1][j - 1] + cost # substitution
            )

    return dp[m][n]


word1 = "START"
word2 = "STARE"

print("Levenshtein Distance:", levenshtein_distance(word1, word2))


# In[7]:


import re
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import nltk

nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('stopwords')

sentence = "The quick,Brown foxes...\n    they are JUMPING over\n    10 lazy dogs!"

sentence = sentence.lower()

sentence = re.sub(r'[^a-z\s]', ' ', sentence)

words = sentence.split()

stop_words = set(stopwords.words('english'))
words = [word for word in words if word not in stop_words]

lemmatizer = WordNetLemmatizer()
clean_words = [lemmatizer.lemmatize(word) for word in words]

print(clean_words)


# In[6]:


spam_words = ["win", "free", "prize"]

message = "you are winning a free prize now!"

def spam_filter(text, spam_list):
    text = text.lower()
    for word in spam_list:
        if word in text:
            return "spam"
    return "not spam"


result = spam_filter(message, spam_words)
print(result)


# In[ ]:




