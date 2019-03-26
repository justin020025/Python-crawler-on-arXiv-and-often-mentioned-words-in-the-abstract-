# Python-crawler-on-arXiv-and-often-mentioned-words-in-the-abstract-
This is a python program that crawls from Cornell University's essay archive https://arxiv.org/search/?query=cache&searchtype=all&source=header and analyzes the popular words mentioned in the abstracts.
## Purpose
Given a topic, something of interest is how this topic is being dicussed in academic community. For example, given the topic "medicine", you may wonder what kinds of bacteria or virus scientist are trying to dealing with. This program takes what you wanna search on arXiv as the input, and will return the first 100 essays(sorted by time) and the top 50 often-mentioned words in the abstracts of those.
## Installation
```
pip install beautifulsoup4
```

## Usage
<ul>
<li>Open the command window and direct to the "crawl" folder</li>
<li>Enter the following command
  
  ```
  python crawler.py search_word

  ```
  , where search_word is what you want to search on arXiv.org<br>
  Note that if there is any space in search_word, replace it with '+'.(e.g. face+detection)</li>

<li>The program takes some time to run. After finishing, you will get the first 100 essays in paper_info.txt and top 50 oftened-mentioned words in frequent_words.txt</li>.
<li>stop_word.txt contains the words that are commonly-used but are of no importance, such as "we", "is", "has", etc. If you find frequent words.txt contains too many unwanted words, add those words to stop_words.txt and run the program again.</li> 
<li>Alternatively, open crawl.ipynb on jupyter notebook.</li>
</ul>
