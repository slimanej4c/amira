
import pandas as pd
import matplotlib.pyplot as plt



class tf_idf():
    def __init__(self):
        doc1="the cat sat in my face"
        doc2="the dog sat in my bed"


        bow1=doc1.split(" ")
        bow2=doc2.split(" ")
        l=[set(bow1),set(bow2)]
        wordset=frozenset().union(*l)


        worddic1=dict.fromkeys(wordset,0)
        print(worddic1)
        worddic2=dict.fromkeys(wordset,0)

        print("wordict1",worddic1)

        for word in bow1:
            worddic1[word]+=1
        for word in bow2:
            worddic2[word]+=1

        data=pd.DataFrame([worddic1,worddic2])
        print("dattta",data)
        tfbow1 = self.count_tf(worddic1, bow1)
        print("tf1",tfbow1)
        tfbow2 = self.count_tf(worddic2, bow2)
        idfs = self.count_idf([worddic1, worddic2])
        print('her idf', idfs)

        tf_idf1 = self.count_tf_idf(tfbow1, idfs)
        tf_idf2 = self.count_tf_idf(tfbow2, idfs)

        data=pd.DataFrame([tf_idf1,tf_idf2])
        print(data)

    def count_tf(self,wordict,bow):
            tf_dict={}
            bow_count=len(bow)

            for word ,count in wordict.items():
                tf_dict[word]=count/float(bow_count)
            return tf_dict


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
            for word , val in tfblow.items():
                tf_idf[word]=val*idfs[word]

            return tf_idf

list_text=[["hello word"],["how are you hello you"]]

tf_idf()
