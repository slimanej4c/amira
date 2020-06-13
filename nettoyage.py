





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
a=''
list2=[]




class nettoyage_class(object):

    def __init__(self):
        self.repeat_regexp = re.compile(r'(\w*)(\w)\2(\w*)')
        self.repl = r'\1\2\3'
        pass

    def stem(self,data):
        list_statement_steemed = []
        stop_words = set(stopwords.words("english"))

        ps = PorterStemmer()
        for i in data:


            a = word_tokenize(i)
            s=""
            for y in a:

                s+=ps.stem(y)+" "
            list_statement_steemed.append(s)

        return list_statement_steemed

    def replace(self,word):
        repl_word = self.repeat_regexp.sub(self.repl, word)
        if repl_word != word:
            return self.replace(repl_word)
        else:
            return repl_word
    def replace1(self,data):
        list_remove_char = []
        for i in data:
            k = re.sub(r"http\S+", "", i)
            a = word_tokenize(k)
            s=""
            for word in a:
                word = ''.join([i for i in word if not i.isdigit()])
                s+=self.replace(word)+" "

            list_remove_char.append(s)

        return list_remove_char





