import pandas as pd
import numpy as np
import tkinter
from tkinter import *
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
# from sklearn.cross_validation import train_test_split
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn import svm
from tkinter import messagebox
from pandastable import Table, TableModel
from pathlib import Path
from tkinter.filedialog import askopenfilename,askdirectory

class train_test():

    def __init__(self, df_x_train, df_y_train, df_y_test):
        self.x = 1000
        self.y = 700


        self.df_x_test = df_x_train[int(len(df_x_train) * 9 / 10):]
        self.df_y_test = df_y_train[int(len(df_x_train) * 9 / 10):]
        self.df_x_train = df_x_train[0:int(len(df_x_train)*9.5/10)]
        self.df_y_train = df_y_train[0:int(len(df_x_train)*9.5/10)]
        print("hii",self.df_x_train)


        # cv=CountVectorizer()
       # self.df_x_train,self.df_x_test,self.df_y_train,self.df_y_test=train_test_split(df_x_train,df_y_train,test_size=0.2,random_state=2)





    def entrainer(self,root):
        self.cv = TfidfVectorizer(min_df=1, stop_words='english')
        self.x_train = self.cv.fit_transform(self.df_x_train.apply(lambda x: np.str_(x)))

        self.x_test = self.cv.transform(self.df_x_test.apply(lambda x: np.str_(x)))

        self.mb = svm.SVC()
        try:
            self.mb.fit(self.x_train, self.df_y_train)
            print("entrinement terminé")

        except MemoryError:
            messagebox.showerror('la mémoire est insuffisante ',message=' baisser le pourcentage et ressayer')
            root.destroy()



    def tester(self,lscore):
        x_test = self.cv.transform(self.df_x_test.apply(lambda x: np.str_(x)))
        pred = self.mb.predict(x_test)

        actual = np.array(self.df_y_test)
        count = 0
        zero = 0
        un = 0

        for i in range(len(pred)):
            if pred[i] == str(actual[i]):
                count += 1
            else:
              print(pred[i])
              if  pred[i]=='0':
                 zero+=1
              if  pred[i]=='1':
                 un+=1

        print(count / len(pred))
        lscore['text']='score :\n '+'les vrai :'+str(round(count *100/ len(pred),2))+'%\n'+'faux neg :'+str(round(zero*100/ len(pred),2))+'%\n'+'faux pos'+str(round(un*100/ len(pred),2))
        lscore.grid(row=14,column=0)





    def affi_test(self,center_frame):
        y1 = self.y // 20
        y2 = self.y // 14
        y3 = self.y - y1 - y2
        x3 = self.x // 5
        pt = Table(center_frame, dataframe=self.df, height=y3 - y2, width=3 * x3 - 30)
        pt.show()
    def utiliser_svm(self,center_frame,data2):


            k= self.cv.transform(list(data2['statement']))

            a = self.mb.predict(k)

            dict={'id':data2['id'],'sentiment':a,'statement':data2['statement']}
            self.df = pd.DataFrame(dict)


            def export():
                import time
                self.FILETYPES = [("text files", "*.xlsx")]
                chemin1 = (askdirectory())
                date_now = time.strftime('%d%m%Y')


                if chemin1 != '':
                    self.chemin = chemin1 + '/' + 'amira' + date_now + '.csv'
                    my_file = Path(self.chemin)
                    if my_file.exists():
                        answer = messagebox.askquestion('file exists',
                                                        'The file already exists. Do you want to replace it? ')
                        if answer == 'yes':
                            self.df.to_csv(my_file)


                        else:None


                    else:
                        self.df.to_csv(my_file)


            #bexport.grid(row=5,column=0)
            #bexport.configure(command=export)
            self.affi_test(center_frame)











