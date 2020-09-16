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
import train_test2

class job:
    def __init__(self, root):
        self.root = root
        self.root.title('Analyse des Sentiments sur Twitter basées sur Svm')
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
            self.data = self.data1.dropna(axis=0)
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


            header_list2 = [ "id","statement"]

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

                self.centre_frame1 = Frame(self.root)
                self.centre_frame1.grid(row=3, column=0, sticky=N)

                if v=='train':



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


        y1 = self.y // 6
        y2 = self.y // 2
        y3 = self.y // 5
        self.haut_frame1 = Frame(self.root, height=y1, width=self.x, bg='#85C1E9')
        self.haut_frame1.grid(row=0, column=0)
        self.haut_frame1.grid_propagate(0)
        self.haut_frame1.grid_columnconfigure(0, weight=1)

        self.haut_frame2 = Frame(self.root, height=y2, width=self.x, bg='#0000FF')
        self.haut_frame2.grid(row=1, column=0)
        self.haut_frame2.grid_propagate(0)


        self.haut_frame3 = Frame(self.root, height=y3, width=self.x, bg='#85C1E9', )
        self.haut_frame3.grid(row=2, column=0, sticky=N)
        self.haut_frame3.grid_propagate(0)
        self.haut_frame3.grid_rowconfigure(0, weight=1)
        self.haut_frame3.grid_columnconfigure(0, weight=1)

        ltitre = Label(self.haut_frame1, text='Analyse des Sentiments sur Twitter basées sur Svm', font=('arian',30),bg='#85C1E9')
        ltitre.grid(row=0, column=0,pady=25)

        img = Image.open('mira/face1.jpg')
        self.limage = ImageTk.PhotoImage(img)

        limage = Label(self.haut_frame2, text='',image=self.limage)
        limage.grid(row=0, column=0)

        img = Image.open('button.jpg')
        self.bimage = ImageTk.PhotoImage(img)

        bdemarer=Button(self.haut_frame3,command=self.frame2,text='',image=self.bimage, compound="center",font=('arial',15))
        bdemarer.grid(row=0,column=0)


    def frame2(self):

        self.positive = 0
        self.nigative = 0
        self.neutre = 0

        self.root = Frame(self.root, height=self.y, width=self.x, bg='white')
        self.root.grid(row=0, column=0)
        self.root.grid_propagate(0)
        y1 = self.y // 20
        y2 = self.y // 14
        self.haut_frame1 = Frame(self.root, height=y1, width=self.x, bg='#85C1E9')
        self.haut_frame1.grid(row=0, column=0, sticky=N)
        self.haut_frame1.grid_propagate(0)

        self.haut_frame2 = Frame(self.root, height=y2 * 2 / 2, width=self.x, bg='#85C1E9')
        self.haut_frame2.grid(row=1, column=0, sticky=N)
        self.haut_frame2.grid_propagate(0)
        self.haut_frame2.grid_rowconfigure(0, weight=1)

        self.haut_frame3 = Frame(self.root, height=y2 / 2, width=self.x, bg='gray', )
        self.haut_frame3.grid(row=2, column=0, sticky=N)
        self.haut_frame3.grid_propagate(0)
        self.haut_frame3.grid_rowconfigure(0, weight=1)
        y3 = self.y - y1 - y2
        x3 = self.x // 5

        button_haut1 = Button(self.haut_frame2, text='')
        self.gauche_frame = Frame(self.root, height=y3, width=x3, bg='#85C1E9')
        self.gauche_frame.grid(row=3, column=0, rowspan=2, sticky=W)
        self.gauche_frame.grid_propagate(0)


        self.droit_frame = Frame(self.root, height=y3, width=x3, bg='#85C1E9')
        self.droit_frame.grid(row=3, column=0, rowspan=2, sticky=E)
        self.droit_frame.grid_propagate(0)


        self.centre_frame1 = Frame(self.root)
        self.centre_frame1.grid(row=3, column=0, sticky=N)

        self.bas_frame = Frame(self.root, height=y2, width=3 * x3, bg='#85C1E9')
        self.bas_frame.grid(row=4, column=0, sticky=S)
        self.bas_frame.grid_propagate(0)

        self.button_color = 'white'
        self.button_colorf = 'black'
        img = Image.open('mira/pretraitement.png')
        self.bimage10= ImageTk.PhotoImage(img)

        self.bpretraitement= Button(self.haut_frame2, text='Prétraitement', command=self.btrain,bg=self.button_color, fg=self.button_colorf,image=self.bimage10, compound="right",font=('arial',12))
        self.bpretraitement.grid(row=0, column=0,padx=4)

        self.bpretraitement.bind("<Enter>", lambda event: self.on_enter(self.bpretraitement))
        self.bpretraitement.bind("<Leave>", lambda event: self.on_leave(self.bpretraitement))

        img = Image.open('mira/classification.jpg')
        self.bimage111= ImageTk.PhotoImage(img)

        self.bclassification = Button(self.haut_frame2, text='Classification', command=self.btest,bg=self.button_color, fg=self.button_colorf,image=self.bimage111, compound="right",font=('arial',12))
        self.bclassification.grid(row=0, column=1)
        self.bclassification.bind("<Enter>", lambda event: self.on_enter(self.bclassification))
        self.bclassification.bind("<Leave>", lambda event: self.on_leave(self.bclassification))

    def on_enter(self,event):

        event['background'] = '#85C1E9'

    def on_leave(self,event):
        event['background'] = 'white'




    def btrain(self):
        self.button_color='white'
        self.button_colorf='black'
        self.update_frame_gauche()
        self.update_frame_droit()
        if self.d1:
            self.affiche_data(self.data1,'train')

        img = Image.open('mira/import-data.png')
        self.bimage1 = ImageTk.PhotoImage(img)
        self.bimport_data1 = Button(self.gauche_frame, text='Import Data train ',width=self.x // 5.5 ,bg=self.button_color, fg=self.button_colorf,image=self.bimage1, compound="right",font=('arial',12), command=lambda:self.set_data('train'))

        self.bimport_data1.grid(row=0, column=0,pady=15)

        self.bimport_data1.bind("<Enter>",lambda event:  self.on_enter(self.bimport_data1))
        self.bimport_data1.bind("<Leave>",lambda event:  self.on_leave(self.bimport_data1))

        img = Image.open('mira/pourcentage.jpg')
        self.bimage2 = ImageTk.PhotoImage(img)

        self.lper1 = Label(self.gauche_frame, text='Taille Data %',width=self.x // 5.5 ,bg=self.button_color,fg=self.button_colorf,image=self.bimage2, compound="right",font=('arial',12),)
        self.lper1.grid(row=1, column=0)
        self.combo_percentage1 = ttk.Combobox(self.gauche_frame, values=[5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100])

        self.combo_percentage1.grid(row=2, column=0)

        self.valide1 = Button(self.gauche_frame, text='Valider ', width=self.x // 40, bg=self.button_color,height=2,font=('arial',9),
                                    fg=self.button_colorf, command=lambda: self.load_csv(self.chemin1, 'train'))

        self.valide1.grid(row=3,column=0,pady=10)

        self.valide1.bind("<Enter>", lambda event: self.on_enter(self.valide1))
        self.valide1.bind("<Leave>", lambda event: self.on_leave(self.valide1))

        img = Image.open('mira/stemming.png')
        self.bimage4 = ImageTk.PhotoImage(img)

        self.btrain_cleaning1 = Button(self.droit_frame, text=' Stemming ',width=self.x // 7,bg=self.button_color, fg=self.button_colorf,image=self.bimage4, compound="right",
                                       relief=GROOVE,command=lambda:self.clean_text('train') )

        self.btrain_cleaning1.bind("<Enter>", lambda event: self.on_enter(self.btrain_cleaning1))
        self.btrain_cleaning1.bind("<Leave>", lambda event: self.on_leave(self.btrain_cleaning1))


        img = Image.open('mira/clean.png')
        self.bimage5 = ImageTk.PhotoImage(img)

        self.btrain_steming1 = Button(self.droit_frame, text='Néttoyage ',width=self.x // 7,bg=self.button_color, fg=self.button_colorf,image=self.bimage5, compound="right",
                                      relief=GROOVE,command=lambda:self.stemming('train'))

        self.btrain_steming1.bind("<Enter>", lambda event: self.on_enter(self.btrain_steming1))
        self.btrain_steming1.bind("<Leave>", lambda event: self.on_leave(self.btrain_steming1))
        def affiche_traitement():
            self.btrain_cleaning1.grid(row=2,column=0,sticky=W,padx=10)
            self.btrain_steming1.grid(row=3,column=0,sticky=W,padx=10)

        img = Image.open('mira/traitement_data.jpg')
        self.bimage3 = ImageTk.PhotoImage(img)
        self.btraitement1=Button(self.droit_frame, text='Traitement ',width=self.x // 5.5, command=affiche_traitement,bg=self.button_color, fg=self.button_colorf,image=self.bimage3, compound="right",font=('arial',12))
        self.btraitement1.grid(row=1,column=0,pady=5,padx=10)

        self.btraitement1.bind("<Enter>", lambda event: self.on_enter(self.btraitement1))
        self.btraitement1.bind("<Leave>", lambda event: self.on_leave(self.btraitement1))


        img = Image.open('mira/afficher_data.jpg')
        self.bimage6= ImageTk.PhotoImage(img)

        self.bafficher_data1 = Button(self.droit_frame, text=' Afficher data train ',width=self.x // 5.5,bg=self.button_color, fg=self.button_colorf,image=self.bimage6, compound="right",font=('arial',12) ,
                                      command=lambda :self.affiche_data(self.data1,'train'))
        self.bafficher_data1.grid(row=9, column=0)

        self.bafficher_data1.bind("<Enter>", lambda event: self.on_enter(self.bafficher_data1))
        self.bafficher_data1.bind("<Leave>", lambda event: self.on_leave(self.bafficher_data1))

        img = Image.open('mira/idf.jpg')
        self.bimage7 = ImageTk.PhotoImage(img)
        self.bidf_tf1 = Button(self.droit_frame, text='Calcul Tf*Idf_train ',width=self.x // 5.5,command=self.tf_idf_1,bg=self.button_color, fg=self.button_colorf,image=self.bimage7, compound="right",font=('arial',12) ,)
        self.bidf_tf1.grid(row=4,column=0,pady=2)

        self.bidf_tf1.bind("<Enter>", lambda event: self.on_enter(self.bidf_tf1))
        self.bidf_tf1.bind("<Leave>", lambda event: self.on_leave(self.bidf_tf1))

        img = Image.open('mira/afficher_data.jpg')
        self.bimage8 = ImageTk.PhotoImage(img)
        self.bafficheidf_train1 = Button(self.droit_frame, text='Afficher idf_tf train ',width=self.x // 5.5,command=lambda:self.go.afficher_idf(self.root),bg=self.button_color, fg=self.button_colorf,image=self.bimage8, compound="right",font=('arial',12)  )

        self.bafficheidf_train1.grid(row=10, column=0,pady=2)

        self.bafficheidf_train1.bind("<Enter>", lambda event: self.on_enter(self.bafficheidf_train1))
        self.bafficheidf_train1.bind("<Leave>", lambda event: self.on_leave(self.bafficheidf_train1))
        def go():
            if self.d1:

                   self.go_train = train_test2.train_test(self.data1['statement'], self.data1['sentiment'],
                                                  None)
                   self.go_train.entrainer(self.root)

        img = Image.open('mira/model.png')
        self.bimage9 = ImageTk.PhotoImage(img)
        self.bentrainer1 = Button(self.droit_frame, text=' Aprentissage (svm)',width=self.x // 5.5, command=lambda:go() ,bg=self.button_color, fg=self.button_colorf,image=self.bimage9, compound="right",font=('arial',12) )
        self.bentrainer1.grid(row=6, column=0,pady=2)
        self.bentrainer1.bind("<Enter>", lambda event: self.on_enter(self.bentrainer1))
        self.bentrainer1.bind("<Leave>", lambda event: self.on_leave(self.bentrainer1))


    def btest(self):


        self.update_frame_gauche()
        self.update_frame_droit()
        if self.d2:
            self.affiche_data(self.data2,'test')


        img = Image.open('mira/import-data.png')
        self.bimage1 = ImageTk.PhotoImage(img)

        self.bimport_data2 = Button(self.gauche_frame, text=' Import data test ',width=self.x // 5.5, bg=self.button_color, fg=self.button_colorf,image=self.bimage1, compound="right",font=('arial',12),
                                     command=lambda:self.set_data('test') )

        self.bimport_data2.grid(row=0, column=0, pady=15)

        self.bimport_data2.bind("<Enter>", lambda event: self.on_enter(self.bimport_data2))
        self.bimport_data2.bind("<Leave>", lambda event: self.on_leave(self.bimport_data2))

        img = Image.open('mira/pourcentage.jpg')
        self.bimage2 = ImageTk.PhotoImage(img)
        self.lper2 = Label(self.gauche_frame, text='     Taille Data  %     ',width=self.x // 5.5,  bg=self.button_color, fg=self.button_colorf,image=self.bimage2, compound="right",font=('arial',12),)
        self.lper2.grid(row=1, column=0)
        self.combo_percentage2 = ttk.Combobox(self.gauche_frame,
                                              values=[5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85,
                                                      90, 95, 100])

        self.combo_percentage2.grid(row=2, column=0)

        self.valide2 = Button(self.gauche_frame, text='Valider ', width=self.x // 40, bg=self.button_color,height=2,font=('arial',9),
                                    fg=self.button_colorf,
                              command=lambda: self.load_csv(self.chemin2, 'test'))

        self.valide2.grid(row=3, column=0, pady=10)

        self.valide2.bind("<Enter>", lambda event: self.on_enter(self.valide2))
        self.valide2.bind("<Leave>", lambda event: self.on_leave(self.valide2))

        img = Image.open('mira/stemming.png')
        self.bimage4 = ImageTk.PhotoImage(img)
        self.btrain_cleaning2 = Button(self.droit_frame, text='  Stemming   ',width=self.x // 7, relief=GROOVE,command=lambda:self.clean_text('test'),  bg=self.button_color, fg=self.button_colorf,image=self.bimage4, compound="right",font=('arial',12), )

        img = Image.open('mira/clean.png')
        self.bimage5 = ImageTk.PhotoImage(img)

        self.btrain_cleaning2.bind("<Enter>", lambda event: self.on_enter(self.btrain_cleaning2))
        self.btrain_cleaning2.bind("<Leave>", lambda event: self.on_leave(self.btrain_cleaning2))

        self.btrain_steming2 = Button(self.droit_frame, text='  Néttoyage ',width=self.x // 7,  bg=self.button_color, fg=self.button_colorf,image=self.bimage5, compound="right",font=('arial',12),
                                       relief=GROOVE,command=lambda:self.stemming('test'))

        self.btrain_steming2.bind("<Enter>", lambda event: self.on_enter(self.btrain_steming2))
        self.btrain_steming2.bind("<Leave>", lambda event: self.on_leave(self.btrain_steming2))

        def affiche_traitement():
            self.btrain_cleaning2.grid(row=2, column=0, sticky=W,padx=5)
            self.btrain_steming2.grid(row=3, column=0, sticky=W,padx=5)

        img = Image.open('mira/traitement_data.jpg')
        self.bimage3 = ImageTk.PhotoImage(img)

        self.btraitement2 = Button(self.droit_frame, text='      Traitement       ',width=self.x // 5.5,  bg=self.button_color, fg=self.button_colorf,image=self.bimage3, compound="right",font=('arial',12),
                                   command=affiche_traitement)
        self.btraitement2.grid(row=1, column=0,padx=10)

        self.btraitement2.bind("<Enter>", lambda event: self.on_enter(self.btraitement2))
        self.btraitement2.bind("<Leave>", lambda event: self.on_leave(self.btraitement2))

        img = Image.open('mira/afficher_data.jpg')
        self.bimage8 = ImageTk.PhotoImage(img)
        self.bafficher_data2 = Button(self.droit_frame, text='Afficher data test ',width=self.x // 5.5, command=lambda :self.affiche_data(self.data2,'test'), bg=self.button_color, fg=self.button_colorf,image=self.bimage8, compound="right",font=('arial',12),
                                       )
        self.bafficher_data2.grid(row=9, column=0)

        self.bafficher_data2.bind("<Enter>", lambda event: self.on_enter(self.bafficher_data2))
        self.bafficher_data2.bind("<Leave>", lambda event: self.on_leave(self.bafficher_data2))

        img = Image.open('mira/idf.jpg')
        self.bimage7 = ImageTk.PhotoImage(img)

        self.bidf_tf2 = Button(self.droit_frame, text='       Calcul Tf*Idf test       ',width=self.x // 5.5, command=self.tf_idf_2 , bg=self.button_color, fg=self.button_colorf,image=self.bimage7, compound="right",font=('arial',12),)
        self.bidf_tf2.grid(row=4, column=0,pady=2)

        self.bidf_tf2.bind("<Enter>", lambda event: self.on_enter(self.bidf_tf2))
        self.bidf_tf2.bind("<Leave>", lambda event: self.on_leave(self.bidf_tf2))

        img = Image.open('mira/afficher_data.jpg')
        self.bimage82 = ImageTk.PhotoImage(img)
        self.bafficheidf_train2 = Button(self.droit_frame, text='Afficher idf_tf test',width=self.x // 5.5, command=self.tf_idf_2 ,bg=self.button_color, fg=self.button_colorf,image=self.bimage82, compound="right",font=('arial',12),
                                         )

        self.bafficheidf_train2.grid(row=11, column=0, pady=2)

        self.bafficheidf_train2.bind("<Enter>", lambda event: self.on_enter(self.bafficheidf_train2))
        self.bafficheidf_train2.bind("<Leave>", lambda event: self.on_leave(self.bafficheidf_train2))





        img = Image.open('mira/afficher_data.jpg')
        self.bimage81 = ImageTk.PhotoImage(img)
        self.btester2 = Button(self.droit_frame, text='   Afficher Data test       \n classé',width=self.x // 5.5, command=lambda:self.go_train.affi_test(self.root),bg=self.button_color, fg=self.button_colorf,image=self.bimage81, compound="right",font=('arial',12), )
        self.btester2.grid(row=12, column=0, pady=2)
        self.btester2.bind("<Enter>", lambda event: self.on_enter(self.btester2))
        self.btester2.bind("<Leave>", lambda event: self.on_leave(self.btester2))

        img = Image.open('mira/test.png')
        self.bimage15 = ImageTk.PhotoImage(img)
        self.bresultat_tester2 = Button(self.droit_frame, text='   Afficher les   \n   resultat de test  ',width=self.x // 5.5,bg=self.button_color, fg=self.button_colorf,image=self.bimage15, compound="right",font=('arial',12),
                                        command=lambda: self.go_train.tester(self.root,self.data2['statement'],self.data1['sentiment']))


        self.bresultat_tester2.grid(row=13, column=0, pady=5)

        self.bresultat_tester2.bind("<Enter>", lambda event: self.on_enter(self.bresultat_tester2))
        self.bresultat_tester2.bind("<Leave>", lambda event: self.on_leave(self.bresultat_tester2))

        img = Image.open('mira/classification.jpg')
        self.bimage11 = ImageTk.PhotoImage(img)
        self.bclasser2 = Button(self.droit_frame, text='        Classification       ' ,width=self.x // 5.5,bg=self.button_color, fg=self.button_colorf,image=self.bimage11, compound="right",font=('arial',12),
                                  command=lambda: self.go_train.utiliser_svm(self.root, self.data2))
        self.bclasser2.grid(row=6, column=0, pady=2)

        self.bclasser2.bind("<Enter>", lambda event: self.on_enter(self.bclasser2))
        self.bclasser2.bind("<Leave>", lambda event: self.on_leave(self.bclasser2))

    def tf_idf_1(self):


        li2=[]

        for i in  self.statement1:
            li1=[]
            li1.append(i)
            li2.append(li1)
        y1 = self.y // 20
        y2 = self.y // 14
        y3 = self.y - y1 - y2
        x3 = self.x // 5
        h = y3 - y2
        w= 3 * x3 - 30

        self.go=tf_idf1.tf_idf(li2[0:1000], self.root, h, w)



        """def tester():
            self.btest_data.grid(row=2, column=0)

        self.butiliser_model = Button(self.haut_frame3, text='tester',
                                 command=tester,width=self.x // 40, bg='#1B2631',fg='white', relief=GROOVE, )"""



    def update_frame_gauche(self):
        y1 = self.y // 20
        y2 = self.y // 14
        y3 = self.y - y1 - y2
        x3 = self.x // 5
        self.gauche_frame = Frame(self.root, height=y3, width=x3, bg='#85C1E9')
        self.gauche_frame.grid(row=3, column=0, rowspan=2, sticky=W)
        self.gauche_frame.grid_propagate(0)

        self.centre_frame1 = Frame(self.root)
        self.centre_frame1.grid(row=3, column=0, sticky=N)


    def update_frame_droit(self):
        y1 = self.y // 20
        y2 = self.y // 14
        y3 = self.y - y1 - y2
        x3 = self.x // 5


        self.droit_frame = Frame(self.root, height=y3, width=x3, bg='#85C1E9')
        self.droit_frame.grid(row=3, column=0, rowspan=2, sticky=E)
        self.droit_frame.grid_propagate(0)



    def update_frame2(self):
        y1 = self.y // 20
        y2 = self.y // 14
        y3 = self.y - y1 - y2
        x3 = self.x // 5
        self.gauche_frame = Frame(self.root, height=y3, width=x3, bg='#85C1E9')
        self.gauche_frame.grid(row=3, column=0, rowspan=2, sticky=W)
        self.gauche_frame.grid_propagate(0)

        self.centre_frame1 = Frame(self.root)
        self.centre_frame1.grid(row=3, column=0, sticky=N)

    def tf_idf_2(self):

        li2 = []

        for i in self.statement2:
            li1 = []
            li1.append(i)
            li2.append(li1)
        y1 = self.y // 20
        y2 = self.y // 14
        y3 = self.y - y1 - y2
        x3 = self.x // 5
        h = y3 - y2
        w = 3 * x3 - 30

        self.go2 = tf_idf2.tf_idf(li2[0:1000], self.root, h, w)


if __name__ == '__main__':
    root = Tk()
    job(root)
    root.mainloop()