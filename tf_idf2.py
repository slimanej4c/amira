
import pandas as pd
import matplotlib.pyplot as plt


from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename

import pandas as pd
from pandastable import Table, TableModel


from nettoyage import *

class tf_idf():
    def __init__(self,args,root,h,w):
        centre_frame1 = Frame(root, bg='white', width=630, height=700)
        centre_frame1.grid(row=3, column=0, sticky=N)
        centre_frame1.grid_propagate(0)
        self.f = centre_frame1
        self.h=h
        self.w=w
        list_golbal=[]
        bow=[]
        for i in args:
            for ii in i :
                a=str(ii).split(" ")
                list_golbal.append(set(a))
                bow.append(a)

        wordset=list(frozenset().union(*list_golbal))

        #wordict=dict.fromkeys(wordset,0)


        list_global_dic=[]
        for i in bow:
            wordict = dict.fromkeys(wordset, 0)
            for word in i :
                wordict[word]+=1
            list_global_dic.append(wordict)


        data=pd.DataFrame([list_global_dic[0],list_global_dic[1]])


        self.tfbow = self.count_tf(list_global_dic, bow)


        self.idfs = self.count_idf(list_global_dic)


        self.tf_idf2 = self.count_tf_idf(self.tfbow, self.idfs)

        #tf_idf2 = self.count_tf_idf(tfbow2, idfs)
        self.afficher_idf(root)


    def afficher_idf(self,root):
        centre_frame1 = Frame(root, bg='white', width=630, height=700)
        centre_frame1.grid(row=3, column=0, sticky=N)
        centre_frame1.grid_propagate(0)
        self.data = pd.DataFrame(self.tf_idf2, columns=list(self.tf_idf2[0].keys()))
        pt = Table(centre_frame1, dataframe=self.data, height=self.h, width=self.w)
        pt.show()




    def count_tf(self,wordict,bow):
            tf_dict={}
            list_tf=[]

            for i ,j in zip(wordict,bow):
                bow_count = len(j )
                tf_dict = {}
                for word ,count in i.items():
                    tf_dict[word]=count/float(bow_count)
                list_tf.append(tf_dict)
            return list_tf


    def count_idf(self,doclist):
            import math
            idf_dict={}
            n=len(doclist)
            idf_dict=dict.fromkeys(doclist[0].keys(),0)
            print(idf_dict)
            for doc in doclist:
                for word , val in doc.items():
                    if val> 0:
                        idf_dict[word]+=1
            print(idf_dict)
            for word ,val in idf_dict.items():
                idf_dict[word]=math.log(n/float(val))

            return idf_dict

    def count_tf_idf(self,tfblow,idfs):
            tf_idf={}
            lts_tf_idf=[]
            for i in tfblow:
                tf_idf = {}
                for word , val in i.items():
                    tf_idf[word]=val*idfs[word]
                lts_tf_idf.append(tf_idf)

            return lts_tf_idf


list_text=[["the cat sat in my 1 2 ... @face"],["the dog sat in my bed..... 1 . ;;;;"],["the dog sat in my bed"],["the dog sat in my bed"]]

#tf_idf(list_text)