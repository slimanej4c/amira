from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from time import time, sleep
import pandas as pd
from PIL import ImageTk , Image
from nettoyage import *
from pandastable import Table, TableModel

go_nettoyage = nettoyage_class()
import tf_idf1
import tf_idf2

import train_test

from abré import *


class job:
    def __init__(self, root):
        self.root = root
        self.z = '0'
        self.x = 1000
        self.y = 700
        self.root.geometry('%sx%s' % (self.x, self.y))
        self.id = []
        self.sentiment = []
        self.satatement = []
        self.d1=False
        self.d2=False
        self.frame1()

    def set_data(self, v):
        if v == 'train':
            self.FILETYPES = [("text files", "*.csv")]
            self.chemin1 = (askopenfilename())
            # date_now = time.strftime('%d%m%Y')



        if v == 'test':
            self.FILETYPES = [("text files", "*.csv")]
            self.chemin2 = (askopenfilename())
            # date_now = time.strftime('%d%m%Y')




    def load_csv(self, chemin, v):
        if v=='train':
            header_list = ["id", "sentiment", "statement"]
            self.data1 = pd.read_csv(chemin, encoding="ISO-8859-1", sep=',', names=header_list)
            self.data1 = self.data1.dropna(axis=0)
            self.id1 = list(self.data1["id"])
            self.sentiment1 = list(self.data1["sentiment"])
            self.statement1 = list(self.data1["statement"])
            self.per1 = StringVar()
            self.per1.set(self.combo_percentage1.get())
            per_data1 = int(len(self.data1) * int(self.per1.get()) / 100)
            self.data1 = self.data1[0:per_data1]

            self.affiche_data(self.data1,'train')
            self.d1=True


        if v == 'test':


            header_list2 = ["id","sentiment", "statement"]

            self.data2 = pd.read_csv(chemin, encoding="ISO-8859-1", sep=',', names=header_list2)

            self.data2 = self.data2.dropna(axis=0)
            self.per2 = StringVar()
            self.per2.set(self.combo_percentage2.get())
            per_data2 = int(len(self.data2) * int(self.per2.get()) / 100)
            self.data2 = self.data2[0:per_data2]
            self.statement2 = list(self.data2["statement"])


            self.affiche_data(self.data2, 'test')
            self.d2 = True

    def clean_text(self, v):
        y1 = self.y // 20
        y2 = self.y // 14
        y3 = self.y - y1 - y2
        x3 = self.x // 5
        if v == 'train':

            self.data1['statement'] = self.data1["statement"].apply(
                lambda x: " ".join(word.lower() for word in x.split()))

            self.data1['statement'] = self.data1["statement"].str.replace(r"\W", " ")



            l_filter = list(self.data1['statement'])
            l_filter2 = []
            for d in l_filter:
                # d=d.split(' ')
                d = d.split(' ')
                for i in l2:
                    if i[0].strip().upper() in d:
                        d[d.index(i[0].strip().upper())] = i[1]
                    if i[0].strip().lower() in d:
                        d[d.index(i[0].strip().lower())] = i[1]

                sent = ''
                for s in d:
                    sent += s + ' '
                l_filter2.append(sent)

            self.data1['statement'] = l_filter2

            self.statement1 = list(self.data1["statement"])
            self.statement1 = go_nettoyage.replace1(self.statement1)

            self.pt1 = Table(self.centre_frame1, dataframe=self.data1, height=y3 - y2, width=3 * x3 - 30)
            self.pt1.show()
            # self.btext_steming.grid(row=1, column=0)




        if v == 'test':

            self.data2['statement'] = self.data2["statement"].apply(
                lambda x: " ".join(word.lower() for word in x.split()))

            self.data2['statement'] = self.data2["statement"].str.replace(r"\W", " ")

            l_filter = list(self.data2['statement'])

            l_filter2 = []
            for d in l_filter:
                # d=d.split(' ')
                d = d.split(' ')
                for i in l2:
                    if i[0].strip().upper() in d:
                        d[d.index(i[0].strip().upper())] = i[1]
                    if i[0].strip().lower() in d:
                        d[d.index(i[0].strip().lower())] = i[1]

                sent = ''
                for s in d:
                    sent += s + ' '
                l_filter2.append(sent)

            self.data2['statement'] = l_filter2

            self.statement2 = list(self.data2["statement"])
            self.statement2 = go_nettoyage.replace1(self.statement2)
            self.pt2 = Table(self.centre_frame1, dataframe=self.data2, height=y3 - y2, width=3 * x3 - 30)
            self.pt2.show()


    def affiche_data(self,data,v):
                y1 = self.y // 20
                y2 = self.y // 14
                y3 = self.y - y1 - y2
                x3 = self.x // 5
                if v=='train':

                    f = Frame(self.root)
                    f.grid(row=0, column=0)

                    self.pt1 = Table(self.centre_frame1, dataframe=data, height=y3 - y2, width=3 * x3 - 30)
                    self.pt1.show()
                if v=='test':

                    f = Frame(self.root)
                    f.grid(row=0, column=0)

                    self.pt2 = Table(self.centre_frame1, dataframe=data, height=y3 - y2, width=3 * x3 - 30)
                    self.pt2.show()


    def stemming (self,v):
        y1 = self.y // 20
        y2 = self.y // 14
        y3 = self.y - y1 - y2
        x3 = self.x // 5
        if v=='train':

            self.data1['statement']=go_nettoyage.stem(self.statement1)


            self.pt1 = Table(self.centre_frame1, dataframe=self.data1, height=y3 - y2, width=3 * x3 - 30)
            self.pt1.show()
            #self.bidf_tf1.grid(row=2, column=0, sticky=S)
        if v=='test':

            self.data2['statement'] = go_nettoyage.stem(self.statement2)
            # self.data2['statement']=go_nettoyage.stem(self.statement2)

            self.pt2 = Table(self.centre_frame1, dataframe=self.data2, height=y3 - y2, width=3 * x3 - 30)
            self.pt2.show()

            #self.bidf_tf1.grid(row=2, column=0, sticky=S)
    def frame1(self):

        self.positive = 0
        self.nigative = 0
        self.neutre = 0

        self.global_frame = Frame(self.root, height=self.y, width=self.x, bg='white')
        self.global_frame.grid(row=0, column=0)
        self.global_frame.grid_propagate(0)
        y1 = self.y // 6
        y2 = self.y // 2
        y3 = self.y // 5
        self.haut_frame1 = Frame(self.global_frame, height=y1, width=self.x, bg='#85C1E9')
        self.haut_frame1.grid(row=0, column=0)
        self.haut_frame1.grid_propagate(0)
        self.haut_frame1.grid_columnconfigure(0, weight=1)

        self.haut_frame2 = Frame(self.global_frame, height=y2 , width=self.x, bg='#0000FF')
        self.haut_frame2.grid(row=1, column=0)
        self.haut_frame2.grid_propagate(0)


        self.haut_frame3 = Frame(self.global_frame, height=y3 , width=self.x,bg='#85C1E9',)
        self.haut_frame3.grid(row=2, column=0, sticky=N)
        self.haut_frame3.grid_propagate(0)
        self.haut_frame3.grid_rowconfigure(0, weight=1)
        self.haut_frame3.grid_columnconfigure(0, weight=1)

        ltitre = Label(self.haut_frame1, text='analyse des sentiments', font=('arian',30),bg='#85C1E9')
        ltitre.grid(row=0, column=0,pady=25)

        img = Image.open('header.jpg')
        self.limage = ImageTk.PhotoImage(img)

        limage = Label(self.haut_frame2, text='démarer',image=self.limage)
        limage.grid(row=0, column=0)

        img = Image.open('button.jpg')
        self.bimage = ImageTk.PhotoImage(img)

        bdemarer=Button(self.haut_frame3,command=self.frame2,text='démarer',image=self.bimage)
        bdemarer.grid(row=0,column=0)


    def frame2(self):

        self.positive = 0
        self.nigative = 0
        self.neutre = 0

        self.global_frame = Frame(self.root, height=self.y, width=self.x, bg='white')
        self.global_frame.grid(row=0, column=0)
        self.global_frame.grid_propagate(0)
        y1 = self.y // 20
        y2 = self.y // 14
        self.haut_frame1 = Frame(self.global_frame, height=y1, width=self.x, bg='#85C1E9')
        self.haut_frame1.grid(row=0, column=0, sticky=N)
        self.haut_frame1.grid_propagate(0)

        self.haut_frame2 = Frame(self.global_frame, height=y2 / 2, width=self.x, bg='#85C1E9')
        self.haut_frame2.grid(row=1, column=0, sticky=N)
        self.haut_frame2.grid_propagate(0)
        self.haut_frame2.grid_rowconfigure(0, weight=1)

        self.haut_frame3 = Frame(self.global_frame, height=y2 / 2, width=self.x,bg='#0000FF',)
        self.haut_frame3.grid(row=2, column=0, sticky=N)
        self.haut_frame3.grid_propagate(0)
        self.haut_frame3.grid_rowconfigure(0, weight=1)
        y3 = self.y - y1 - y2
        x3 = self.x // 5

        button_haut1 = Button(self.haut_frame2, text='')
        self.gauche_frame = Frame(self.global_frame, height=y3, width=x3, bg='#85C1E9')
        self.gauche_frame.grid(row=3, column=0, rowspan=2, sticky=W)
        self.gauche_frame.grid_propagate(0)


        self.droit_frame = Frame(self.global_frame, height=y3, width=x3, bg='#85C1E9')
        self.droit_frame.grid(row=3, column=0, rowspan=2, sticky=E)
        self.droit_frame.grid_propagate(0)


        self.centre_frame1 = Frame(self.global_frame)
        self.centre_frame1.grid(row=3, column=0, sticky=N)

        self.bas_frame = Frame(self.global_frame, height=y2, width=3 * x3, bg='#85C1E9')
        self.bas_frame.grid(row=4, column=0, sticky=S)
        self.bas_frame.grid_propagate(0)

        self.bpretraitement= Button(self.haut_frame2, text='prétraitement', command=self.btrain)
        self.bpretraitement.grid(row=0, column=0)
        self.bclassification = Button(self.haut_frame2, text='classification', command=self.btest)
        self.bclassification.grid(row=0, column=1)

    def btrain(self):
        self.update_frame_gauche()
        if self.d1:
            self.affiche_data(self.data1,'train')


        self.bimport_data1 = Button(self.droit_frame, text='import data train ', width=self.x // 40,bg='#0000FF', fg='white', command=lambda:self.set_data('train'))

        self.bimport_data1.grid(row=0, column=0,pady=15)


        self.lper1 = Label(self.droit_frame, text='percentage',width=self.x // 40,bg='#0000FF', fg='white')
        self.lper1.grid(row=1, column=0)
        self.combo_percentage1 = ttk.Combobox(self.droit_frame, values=[5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100])

        self.combo_percentage1.grid(row=2, column=0)

        self.valide1 = Button(self.droit_frame, text='valider ', width=self.x // 40, bg='#0000FF',
                                    fg='white', command=lambda: self.load_csv(self.chemin1, 'train'))

        self.valide1.grid(row=3,column=0,pady=10)


        self.btrain_cleaning1 = Button(self.gauche_frame, text='cleaning', width=self.x // 40,
                                      bg='#0000FF', fg='white', relief=GROOVE,command=lambda:self.clean_text('train') )




        self.bimport_data1.grid(row=0, column=0, pady=15)

        self.btrain_steming1 = Button(self.gauche_frame, text='stemming', width=self.x // 40, bg='#0000FF',
                                     fg='white', relief=GROOVE,command=lambda:self.stemming('train'))
        def affiche_traitement():
            self.btrain_cleaning1.grid(row=2,column=0,sticky=W)
            self.btrain_steming1.grid(row=3,column=0,sticky=W)


        self.btraitement1=Button(self.gauche_frame, text='traitement', width=self.x // 40, bg='#0000FF',fg='white', command=affiche_traitement)
        self.btraitement1.grid(row=1,column=0,pady=5)

        self.bafficher_data1 = Button(self.gauche_frame, text='afficher data', width=self.x // 40, bg='#0000FF', fg='white',)
        self.bafficher_data1.grid(row=0, column=0, pady=5)

        self.bidf_tf1 = Button(self.gauche_frame, text='tf*idf_train', width=self.x // 40, bg='#0000FF',fg='white')
        self.bidf_tf1.grid(row=4,column=0,pady=20)

        self.bafficheidf_train1 = Button(self.gauche_frame, text='afficher idf_tf train', width=self.x // 40, bg='#0000FF', fg='white' )

        self.bafficheidf_train1.grid(row=5, column=0,pady=20)

        self.bentrainer1 = Button(self.gauche_frame, text='entrainer', width=self.x // 40,bg='#0000FF',fg='white',  )
        self.bentrainer1.grid(row=6, column=0,pady=20)



    def update_frame_gauche(self):
        y1 = self.y // 20
        y2 = self.y // 14
        y3 = self.y - y1 - y2
        x3 = self.x // 5
        self.gauche_frame = Frame(self.global_frame, height=y3, width=x3, bg='#85C1E9')
        self.gauche_frame.grid(row=3, column=0, rowspan=2, sticky=W)
        self.gauche_frame.grid_propagate(0)

        self.centre_frame1 = Frame(self.global_frame)
        self.centre_frame1.grid(row=3, column=0, sticky=N)

    def btest(self):
        self.update_frame_gauche()
        if self.d2:
            self.affiche_data(self.data2,'test')


        self.bimport_data2 = Button(self.droit_frame, text='import data test', width=self.x // 40, bg='#0000FF',
                                    fg='white', command=lambda:self.set_data('test') )

        self.bimport_data2.grid(row=0, column=0, pady=15)

        self.lper2 = Label(self.droit_frame, text='percentage', width=self.x // 40, bg='#0000FF', fg='white')
        self.lper2.grid(row=1, column=0)
        self.combo_percentage2 = ttk.Combobox(self.droit_frame,
                                              values=[5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85,
                                                      90, 95, 100])

        self.combo_percentage2.grid(row=2, column=0)

        self.valide2 = Button(self.droit_frame, text='valider ', width=self.x // 40, bg='#0000FF',
                              fg='white', command=lambda: self.load_csv(self.chemin2, 'test'))

        self.valide2.grid(row=3, column=0, pady=10)
        self.btrain_cleaning2 = Button(self.gauche_frame, text='cleaning', width=self.x // 40,
                                       bg='#0000FF', fg='white', relief=GROOVE,command=lambda:self.clean_text('test') )

        self.btrain_steming2 = Button(self.gauche_frame, text='stemming', width=self.x // 40, bg='#0000FF',
                                      fg='white', relief=GROOVE,command=lambda:self.stemming('test'))

        def affiche_traitement():
            self.btrain_cleaning2.grid(row=2, column=0, sticky=W)
            self.btrain_steming2.grid(row=3, column=0, sticky=W)

        self.btraitement2 = Button(self.gauche_frame, text='traitement', width=self.x // 40, bg='#0000FF', fg='white',
                                   command=affiche_traitement)
        self.btraitement2.grid(row=1, column=0, pady=5)

        self.bafficher_data2 = Button(self.gauche_frame, text='afficher data test', width=self.x // 40, bg='#0000FF',
                                      fg='white', )
        self.bafficher_data2.grid(row=0, column=0, pady=5)

        self.bidf_tf2 = Button(self.gauche_frame, text='tf*idf test', width=self.x // 40, bg='#0000FF', fg='white')
        self.bidf_tf2.grid(row=4, column=0, pady=20)

        self.bafficheidf_train2 = Button(self.gauche_frame, text='afficher idf_tf test', width=self.x // 40,
                                         bg='#0000FF', fg='white')

        self.bafficheidf_train2.grid(row=5, column=0, pady=20)

        self.bentrainer2 = Button(self.gauche_frame, text='calculer les resultats', width=self.x // 40, bg='#0000FF', fg='white', )
        self.bentrainer2.grid(row=6, column=0, pady=20)




    def tf_idf_1(self):


        li2=[]

        for i in  self.statement:
            li1=[]
            li1.append(i)
            li2.append(li1)
        y1 = self.y // 20
        y2 = self.y // 14
        y3 = self.y - y1 - y2
        x3 = self.x // 5
        h = y3 - y2
        w= 3 * x3 - 30
        self.go=tf_idf1.tf_idf(li2[0:1000], self.centre_frame1, h, w)
        self.bafficheidf_train = Button(self.haut_frame3, text='afficher idf_tf train', command=self.go.afficher_idf,
                                        width=self.x // 40, bg='#0000FF',
                                        fg='white', relief=GROOVE, )






    def tf_idf_2(self):


        li2=[]

        for i in  self.statement2:
            li1=[]
            li1.append(i)
            li2.append(li1)
        y1 = self.y // 20
        y2 = self.y // 14
        y3 = self.y - y1 - y2
        x3 = self.x // 5
        h = y3 - y2
        w= 3 * x3 - 30
        self.goo=tf_idf2 .tf_idf(li2[0:1000], self.centre_frame1, h, w)







if __name__ == '__main__':
    root = Tk()
    job(root)
    root.mainloop()