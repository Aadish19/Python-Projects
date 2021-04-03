#!/usr/bin/env python
# coding: utf-8

# # Copy Paste Project

# In[1]:


pip install pyperclip


# In[2]:


import pyperclip 
pyperclip.copy('Hello Python')
pyperclip.paste()


# In[ ]:





# In[ ]:





# # STACK OVERFLOW SEARCH TOOL

# In[3]:


conda activate base


# In[4]:


pip install howdoi


# In[5]:


#It clears the doubts 


# In[6]:


howdoi install python


# In[8]:


howdoi declare a list in python


# In[ ]:





# In[ ]:





# # WIKIPEDIA SEARCH TOOL

# In[9]:


pip install wikipedia


# In[12]:


import wikipedia
query = wikipedia.page("Virat Kohli")
print(query.summary)


# In[ ]:





# In[ ]:





# # QR CODE GENERATOR

# In[13]:


pip install pyqrcode


# In[7]:


pip install pypng


# In[ ]:





# In[8]:


import pyqrcode
import png

def qrcode():
    q = pyqrcode.create(input())
    q.png('qrcode.png',scale=7)
    print('QR Generator ')

if __name__=='__main__':
    qrcode()
    
    
    
#Ye input maangega usme dena hai 'Python'
#Toh ye qr generated bolega aur file loctaion me i.e. =-->> C:\Users\adish
#isme jaake jis naam se png banayi hai use search karlo  qr code generated hoga 
#aur uss code ko scan karne pe Aayega ==>>'Python'  jo ki hamne output me daala tha


# In[ ]:





# In[ ]:





# # URL EXTRACTOR

# In[13]:


#We will use 'urllib' to make urls

from urllib.request import urlopen
page = urlopen("https://codewithharry.com")
print(page.headers)


# In[ ]:





# # URL EXTRACTOR-2

# In[14]:



from urllib.request import urlopen
page = urlopen("https://codewithharry.com")

sourcecode=page.read()
print(sourcecode)

#It will give the complete html source code 


# In[ ]:





# In[ ]:





# # URL SHORTENER

# In[17]:


pip install pyshorteners


# In[23]:


import pyshorteners
url = input("Enter The Url:")
shortener = pyshorteners.Shortener()
a = shortener.tinyurl.short(url)
print(a)


# In[ ]:





# In[ ]:





# # GOOGLE SEARCH TOOL

# In[25]:


pip install google


# In[2]:


from googlesearch import search
query = 'Aadish Jain'
for i in search(query,start=0,pause=2):
    print(i)


# In[ ]:





# In[ ]:





# # POCKET DICTIONARY

# In[3]:


pip install pydictionary


# In[7]:


from PyDictionary import PyDictionary
dictionary = PyDictionary()

print(dictionary.meaning("Indentation"))


# In[ ]:




