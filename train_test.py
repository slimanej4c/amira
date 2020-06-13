import pandas as pd
import numpy as np
import tkinter
from tkinter import *
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
# from sklearn.cross_validation import train_test_split
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from tkinter import messagebox


class train_test():

    def __init__(self, df_x_train, df_y_train, df_x_test, df_y_test):
        self.df_x_train = df_x_train
        self.df_y_train = df_y_train
        self.df_x_test = df_x_test
        self.df_y_test = df_y_test

        # cv=CountVectorizer()
        self.cv = TfidfVectorizer(min_df=1, stop_words='english')
        self.x_train = self.cv.fit_transform(self.df_x_train.apply(lambda x: np.str_(x)))

        self.x_test = self.cv.transform(self.df_x_test.apply(lambda x: np.str_(x)))

        self.mb = MultinomialNB()



    def entrainer(self,button,root):
        try:
            self.mb.fit(self.x_train, self.df_y_train)
            button.grid(row=5, column=0)
        except MemoryError:
            messagebox.showerror('la mémoire est insuffisante ',message=' baisser le pourcentage et ressayer')
            root.destroy()



    def tester(self,vscore,butiliser_model):
        pred = self.mb.predict(self.x_test)

        actual = np.array(self.df_y_test)
        count = 0
        print(actual)
        print('p', pred)
        for i in range(len(pred)):
            if pred[i] == str(actual[i]):
                count += 1

        print(count / len(pred))
        vscore.set('score : '+str(count / len(pred)))


        butiliser_model.grid(row=0, column=4)

    def utiliser_svm(self,center_frame):
         def clac(model, ):
            vresult=''
            print(self.estatement.get())
            k= self.cv.transform([str(self.estatement.get())])
            print(k)
            a = model.predict(k)
            print(a[0])
            if a[0] == '1':
                vresult='sentiment : POSITIVE'

            if a[0] == '0':
                  vresult='sentiment : NIGATIVE'

            print('vvvvvvvvv',vresult)
            lresulte = Label(top, text=vresult)
            lresulte.grid(row=1, column=0)
         top=Toplevel()
         top.geometry('400x300')

         lstratement=Label( top,text='enter text (en anglais) :')
         lstratement.grid(row=0,column=0,pady=20)
         self.vstatement=StringVar()
         self.vsresulte=StringVar()
         self.vsresulte.set('')
         self.estatement=Entry( top)
         self.estatement.grid(row=0,column=1,pady=20)





         bvalider = Button( top, text='check sentiment', command=lambda:clac(self.mb))
         bvalider.grid(row=0, column=2, pady=10)









