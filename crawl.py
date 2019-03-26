#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
from urllib.request import urlopen
import re


def url_generator(search, page):
    if page==1:
        return "https://arxiv.org/search/?query="+search+"&searchtype=all&abstracts=show&order=-announced_date_first&size=50"
    else:
        return "https://arxiv.org/search/?query="+search+"&searchtype=all&source=header&order=-announced_date_first&size=50&abstracts=show&start="+str((page-1)*50)



def url2soup(url):
    html = urlopen(url).read()
    soup = BeautifulSoup(html,"html.parser")
    return soup



def paper_link(paper_soup):
    manylink = paper_soup.find('ol')('p','list-title')
    link = [L.a['href'] for L in manylink]
    return link


def title_author_abs(link):
    soup = url2soup(link)
    title = soup.find('h1',"title mathjax").text[6:]
    
    author = soup.find('div', 'authors').text
    author = author[8:]               #change format
    author = author.split(',')
    author[-1] = re.sub('[\n\t]','',author[-1])
    
    abst = soup.find('blockquote').text[11:]
    
    return title, author, abst
    
    
    

#pass argument
import sys
arg = sys.argv
keyword = arg[1]



link = []



for i in range(1,3):
    link.extend(paper_link(url2soup(url_generator(keyword,i))))
print("find all the link")


import time
title, author, abst = [], [], []
for L in link:
    A, B, C = title_author_abs(L)
    title.append(A)
    author.append(B)
    abst.append(C)
    time.sleep(0.1)

print("find all the info")


with open('paper_info.txt','w',encoding = 'utf8') as f:
    for i in range(100):

        f.write(link[i]+'\n')

        f.write(title[i]+'\n')

        for name in author[i]:
            f.write(name+';')
        f.write('\n')
f.close()

print("finish writing info")




abstr = []
for ele in abst:
    rep = (re.sub('[;~!@#$%^&*_?()\\//{}~'',.><"|=+_\n]','',ele))
    rep = rep.replace('\\','')
    rep = rep.split(' ')
    abstr.extend(rep)
for i in range(len(abstr)):
    abstr[i] = abstr[i].lower()
    




stop_word = []
with open('stop_words.txt','r') as stop:
    for line in stop:
        stop_word.append(stop.readline().replace('\n',''))
        



from collections import Counter
most_words = Counter(abstr).most_common(50+len(stop_word))



fw = []
for e in most_words:
    if not(e[0] in stop_word):
        fw.append(e)
fw = fw[:50]



with open('frequent_words.txt', 'w') as p2:
    for pair in fw:
        p2.write(pair[0]+' '+str(pair[1])+'\n')
p2.close()

print("finish writing frequent_words")





