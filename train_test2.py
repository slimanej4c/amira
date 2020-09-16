import pandas as pd
import numpy as np
import tkinter
from tkinter import *
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
# from sklearn.cross_validation import train_test_split
import matplotlib.pyplot as plt
from PIL import ImageTk , Image
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn import svm
from tkinter import messagebox
from pandastable import Table, TableModel
from pathlib import Path
from tkinter.filedialog import askopenfilename,askdirectory
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

class train_test():

    def __init__(self, df_x_train, df_y_train, df_y_test):
        self.x = 1000
        self.y = 700


        self.df_x_test = df_x_train[int(len(df_x_train) * 9 / 10):]
        self.df_y_test = df_y_train[int(len(df_x_train) * 9 / 10):]
        self.df_x_train = df_x_train[0:int(len(df_x_train)*9.5/10)]
        self.df_y_train = df_y_train[0:int(len(df_x_train)*9.5/10)]

        self.long = len(self.df_x_train)


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



    def tester(self,root,df_x_test,df_y_test):
        print('long :',self.long)

        self.df_x_test2 = df_x_test[0:self.long-1 ]
        self.df_y_test2 = df_y_test[0:self.long-1 ]

        print(self.df_x_test2)
        print(self.df_x_train)

        self.x_test2 = self.cv.transform(self.df_x_test2.apply(lambda x: np.str_(x)))

        pred = self.mb.predict(self.x_test2)

        actual = np.array(self.df_y_test2)
        pcount = 0
        ncount = 0
        zero = 0
        un = 0


        # Plot


        for i in range(len(pred)):
            if pred[i] == str(actual[i]):
                if pred[i] == '0':
                    ncount += 1
                if pred[i] == '1':

                    pcount += 1
            else:

              if  pred[i]=='0':
                 zero+=1
              if  pred[i]=='1':
                 un+=1
###############################################################
        fig = Figure(figsize=(2.5, 2.5))
        plt = fig.add_subplot(111)
        labels = '   vrai\n positive', 'faux \n positive'
        sizes = [ pcount, un]
        colors = [ 'lightcoral', 'lightskyblue']
        explode = (0.1, 0)  # explode 1st slice

        # Plot
        plt.pie(sizes, explode=explode, labels=labels, colors=colors,
                autopct='%1.1f%%', shadow=True, startangle=140)

        plt.axis('equal')
        centre_frame1 = Frame(root,bg='white',width=630,height=700)
        centre_frame1.grid(row=3, column=0, sticky=N)
        centre_frame1.grid_propagate(0)

        f1 = Frame(centre_frame1, bg='white', width=315, height=700)
        f1.grid(row=0, column=0)
        f1.grid_propagate(0)

        f2 = Frame(centre_frame1, bg='white', width=315, height=700)
        f2.grid(row=0, column=1)
        f2.grid_propagate(0)

        canvas = FigureCanvasTkAgg(fig, master=f1)
        canvas.get_tk_widget().grid(row=3,column=1)
        canvas.draw()

        fig2 = Figure(figsize=(2.5, 2.5))
        plt= fig2.add_subplot(111)
        labels = ' vrai \n negative', '  faux \n negative'
        sizes = [ncount, zero]
        colors = ['gold', 'yellowgreen']
        explode = (0.1, 0)  # explode 1st slice

        # Plot
        plt.pie(sizes, explode=explode, labels=labels, colors=colors,
                autopct='%1.1f%%', shadow=True, startangle=140)

        plt.axis('equal')

        canvas = FigureCanvasTkAgg(fig2, master=f2)
        canvas.get_tk_widget().grid(row=3, column=1)
        canvas.draw()

##############################################################

        #+'%\n'+'faux neg :'+str(round(zero*100/ len(pred),2))+'%\n'+'faux pos'+str(round(un*100/ len(pred),2))
        self.button_color='white'
        self.button_colorf='black'
        img = Image.open('mira/pos.png')
        self.bimage100 = ImageTk.PhotoImage(img)


        lscore = Label(f1, text="", bg=self.button_color, width=self.x // 5.5, fg=self.button_colorf,
                       image=self.bimage100, compound="right", font=('arial', 10), borderwidth=2, relief="ridge" )

        img = Image.open('mira/neg.png')
        self.bimage101 = ImageTk.PhotoImage(img)

        lscore2 = Label(f2, text="", bg=self.button_color, width=self.x // 5.5, fg=self.button_colorf,
                        image=self.bimage101,
                        compound="right", font=('arial', 10), borderwidth=2, relief="ridge" )

        img = Image.open('mira/false.jpg')
        self.bimage102 = ImageTk.PhotoImage(img)

        lscore3 = Label(f1, text="", bg=self.button_color, width=self.x // 5.5, fg=self.button_colorf,
                        image=self.bimage102,
                        compound="right", font=('arial', 10), borderwidth=2, relief="ridge" )

        img = Image.open('mira/false.jpg')
        self.bimage103 = ImageTk.PhotoImage(img)

        lscore4 = Label(f2, text="", bg=self.button_color, width=self.x // 5.5, fg=self.button_colorf,
                        image=self.bimage103,
                        compound="right", font=('arial', 10), borderwidth=2, relief="ridge" )
        img = Image.open('mira/vrai.jpg')
        self.bimage99 = ImageTk.PhotoImage(img)
        lscore5 = Label(f1, text="", bg=self.button_color, width=self.x // 5.5, fg=self.button_colorf,
                        image=self.bimage99,
                        compound="right", font=('arial', 10), borderwidth=2, relief="ridge" )

        lscore6 = Label(f2, text="", bg=self.button_color, width=self.x // 5.5, fg=self.button_colorf,
                        image=self.bimage99,
                        compound="right", font=('arial', 10), borderwidth=2, relief="ridge" )
        lscore.grid(row=0,column=1)
        lscore2.grid(row=0,column=1)
        lscore3.grid(row=1,column=1)
        lscore4.grid(row=1,column=1)
        lscore5.grid(row=2,column=1)
        lscore6.grid(row=2,column=1)

        lscore['text'] = 'total des sentiment \n positive:' + str(pcount+un )

        lscore2['text'] = 'total des sentiment \n negative:' + str(ncount+zero )

        lscore3['text'] = '  faux positive : ' + str(un )

        lscore4['text'] = '  faux  negative   : ' + str(zero )

        lscore5['text'] = '  vrai positive  : ' + str(pcount)
        lscore6['text'] = '  vrai negative   : ' + str(ncount )





    def affi_test(self,root):
        y1 = self.y // 20
        y2 = self.y // 14
        y3 = self.y - y1 - y2
        x3 = self.x // 5
        centre_frame1 = Frame(root, bg='white', width=630, height=700)
        centre_frame1.grid(row=3, column=0, sticky=N)
        centre_frame1.grid_propagate(0)
        pt = Table(centre_frame1, dataframe=self.df, height=y3 - y2, width=3 * x3 - 30)
        pt.show()
    def utiliser_svm(self,root,data2):



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
            self.affi_test(root)











