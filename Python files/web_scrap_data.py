#!/usr/bin/env python
# coding: utf-8

# In[37]:


from bs4 import BeautifulSoup
import requests
import pandas as pd
import re


# In[79]:


url_df = pd.read_csv("Input.csv")


# In[80]:


for i in url_df.index:
    link = requests.get(url_df['URL'][i])
    data = BeautifulSoup(link.content,'html.parser')
    if i != 0 :
        paragraph_0 = data.find('div',attrs={"class":"td-post-content tagdiv-type"})
        try:
            paragraph = paragraph_0.find_all('p')
            paragragh = paragraph.append(paragraph_0.find_all('li'))
            heading = data.find('h1',attrs={"class":"entry-title"})
        except:
            print(paragraph)
    else:
        paragraph = data.find('div',attrs={"data-td-block-uid":"tdi_130"}).find_all('p')
        heading = data.find('h1',attrs={"class":"tdb-title-text"})
    
    def remove_tag(text):
        if not isinstance(text, str):
            text = str(text)
        clean = re.compile('<.*?>')
        return re.sub(clean, '', text)
    
    print(i)
    head = remove_tag(heading)
    para = remove_tag(paragraph)
    url_id = str(url_df['URL_ID'][i])
    f = open(url_id + ".txt","w+")
    f.write(head)
    f.write(para)
    f.close()


# In[ ]:





# In[ ]:




