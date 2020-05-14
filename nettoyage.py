





import xlrd
import django
import pandas as pd
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize ,word_tokenize
import re
list_statement_steemed=[]
list_statment_word=[]
lis=['hello word','how rae you']
for i in lis:
    list_statment_word.append(word_tokenize(i))
print(list_statment_word)
class nettoyage_class():

    def __init__(self):
        self.repeat_regexp = re.compile(r'(\w*)(\w)\2(\w*)')
        self.repl = r'\1\2\3'
        pass

    def stem(self,data):
        stop_words = set(stopwords.words("english"))

        ps = PorterStemmer()
        for i in data:
            a = word_tokenize(i)
            for y in a:
                list_statement_steemed.append(ps.stem(y))
        print("list steming",list_statement_steemed)
        return list_statement_steemed


    def replace(self, word):
        repl_word = self.repeat_regexp.sub(self.repl, word)
        if repl_word != word:
          return self.replace(repl_word)
        else:
          return repl_word
