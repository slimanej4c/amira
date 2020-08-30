from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from time import time, sleep
import pandas as pd

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
        self.z='0'

        self.x = 1000
        self.y = 700
        self.root.geometry('%sx%s' % (self.x, self.y))
        self.id = []
        self.sentiment = []
        self.satatement = []




        self.frame()
        self.bautton()

    def frame(self):

        self.positive = 0
        self.nigative = 0
        self.neutre = 0

        self.global_frame = Frame(self.root, height=self.y, width=self.x, bg='white')
        self.global_frame.grid(row=0, column=0)
        self.global_frame.grid_propagate(0)
        y1 = self.y // 20
        y2 = self.y // 14
        self.haut_frame1 = Frame(self.global_frame, height=y1, width=self.x, bg='#808B96')
        self.haut_frame1.grid(row=0, column=0, sticky=N)
        self.haut_frame1.grid_propagate(0)

        self.haut_frame2 = Frame(self.global_frame, height=y2 / 2, width=self.x, bg='#808B96')
        self.haut_frame2.grid(row=1, column=0, sticky=N)
        self.haut_frame2.grid_propagate(0)
        self.haut_frame2.grid_rowconfigure(0, weight=1)

        self.haut_frame3 = Frame(self.global_frame, height=y2 / 2, width=self.x, bg='#85C1E9')
        self.haut_frame3.grid(row=2, column=0, sticky=N)
        self.haut_frame3.grid_propagate(0)
        self.haut_frame3.grid_rowconfigure(0, weight=1)
        y3 = self.y - y1 - y2
        x3 = self.x // 5

        button_haut1 = Button(self.haut_frame2, text='')
        self.gauche_frame = Frame(self.global_frame, height=y3, width=x3, bg='#154360')
        self.gauche_frame.grid(row=3, column=0, rowspan=2, sticky=W)
        self.gauche_frame.grid_propagate(0)

        self.droit_frame = Frame(self.global_frame, height=y3, width=x3, bg='#154360')
        self.droit_frame.grid(row=3, column=0, rowspan=2, sticky=E)
        self.droit_frame.grid_propagate(0)

        self.centre_frame1 = Frame(self.global_frame)
        self.centre_frame1.grid(row=3, column=0, sticky=N)

        self.bas_frame = Frame(self.global_frame, height=y2, width=3 * x3, bg='#85C1E9')
        self.bas_frame.grid(row=4, column=0, sticky=S)
        self.bas_frame.grid_propagate(0)




    def bautton(self):



        self.lper = Label(self.haut_frame2, text='percentage')
        self.lper.grid(row=0, column=0)
        # pour choiser la quantité de data train qui va utiliser par ce que a chaque ordinateur et sa puissance d'analyse 32 ou bien 64 bits
        self.combo_percentage = ttk.Combobox(self.haut_frame2, values=[5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95,100])
        #self.combo_percentage.bind('<<ComboboxSelected>>', self.depart)
        self.combo_percentage.grid( row=0,column=1)


        self.lmethod = Label(self.haut_frame2, text='method')
        self.lmethod.grid(row=0, column=3)
        # pour choiser la quantité de data train qui va utiliser par ce que a chaque ordinateur et sa puissance d'analyse 32 ou bien 64 bits
        self.combo_method= ttk.Combobox(self.haut_frame2,
                                             values=['svm','MultinomialNB'])
        # self.combo_percentage.bind('<<ComboboxSelected>>', self.depart)
        self.combo_method.grid(row=0,column=4)
        self.bvalider = Button(self.haut_frame2, text='ok', command=self.depart)
        self.bvalider.grid(row=0, column=5)

        self.btrain_cleaning = Button(self.gauche_frame, text='text train cleaning', width=self.x // 40,bg='#0000FF',
                                      fg='white', relief=GROOVE,
                                      command=lambda: self.clean_text('train'))

        self.btest_cleaning = Button(self.gauche_frame, text='text test cleaning', width=self.x // 40, bg='#008000',
                                     fg='white', relief=GROOVE, command=lambda: self.clean_text('test'))

        self.btrain_steming = Button(self.gauche_frame, text='stemming train', width=self.x // 40, bg='#0000FF',
                                    fg='white', relief=GROOVE, command=lambda:self.stemming('train'))

        self.btest_steming = Button(self.gauche_frame, text='stemming test', width=self.x // 40, bg='#008000',
                                    fg='white', relief=GROOVE, command=lambda:self.stemming('test'))

        self.bidf_tf1 = Button(self.gauche_frame, text='tf*idf_train', width=self.x // 40, bg='#0000FF',
                               fg='white', relief=GROOVE, command=self.tf_idf_1)

        self.bidf_tf2 = Button(self.gauche_frame, text='tf*idf_test', width=self.x // 40, bg='#008000',
                               fg='white', relief=GROOVE,command=self.tf_idf_2)

        self.banalyse= Button(self.gauche_frame, text='analyse data test', width=self.x // 40, bg='#008000',fg='white', relief=GROOVE)
        self.bexport= Button(self.gauche_frame, text='export data', width=self.x // 40, bg='#008000',fg='white', relief=GROOVE)
        self.baffiche= Button(self.haut_frame3, text='afficher test final', width=self.x // 40, bg='#008000',fg='white', relief=GROOVE)














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

        self.bafficheidf_train.grid(row=0, column=1)

        self.go_train = train_test.train_test(self.data['statement'], self.data['sentiment'], self.vmethod.get(),
                                   None)
        vscore = StringVar()
        vscore.set('')
        def tester():
            self.btest_data.grid(row=2, column=0)

        self.butiliser_model = Button(self.haut_frame3, text='tester',
                                 command=tester,width=self.x // 40, bg='#1B2631',fg='white', relief=GROOVE, )


        self.bscore = Button(self.gauche_frame, text='afficher le score', command=lambda: self.go_train.tester(vscore, self.butiliser_model),
                             width=self.x // 40, bg='#0000FF',
                             fg='white', relief=GROOVE, )

        self.lscore = Label(self.gauche_frame, textvariable=vscore)
        self.lscore.grid(row=9, column=0)
        v='entrainer avec '+self.vmethod.get()
        self.bentrainer = Button(self.gauche_frame, text=v,
                                command=lambda: self.go_train.entrainer(self.bscore, self.root), width=self.x // 40, bg='#0000FF',
                                fg='white', relief=GROOVE, )
        self.bentrainer.grid(row=4, column=0)
        self.z='1'
        self.hide_show('train','0')



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

        self.bafficheidf_test = Button(self.haut_frame3, text='afficher idf_tf test', command=self.goo.afficher_idf,width=self.x // 40, bg='#008000',fg='white', relief=GROOVE, )


        self.bafficheidf_test.grid(row=0, column=3)

        self.banalyse.configure(command=lambda: self.go_train.utiliser_svm(self.centre_frame1,self.data2,self.bexport,self.baffiche))













    def depart(self):
        self.per=StringVar()
        self.per.set(self.combo_percentage.get())

        self.vmethod = StringVar()
        self.vmethod.set(self.combo_method.get())

        self.btrain_Data1 = Button(self.droit_frame, text='import data train', width=self.x // 40, bg='#0000FF', fg='white', relief=GROOVE, command=lambda:self.set_data('train'))
        self.btrain_Data1.grid(row=1, column=0, sticky=S)
        self.combo_percentage.destroy()
        self.bvalider.destroy()
        self.lper.destroy()
        self.combo_method.destroy()

        self.lmethod.destroy()

    def set_data(self,v):
        if v=='train':
            self.FILETYPES = [("text files", "*.csv")]
            self.chemin11 = (askopenfilename())
            # date_now = time.strftime('%d%m%Y')
            self.chemin = self.chemin11
            if self.chemin11 != '':
                self.load_csv(self.chemin,'train')

            self.btrain_cleaning.grid(row=0, column=0)

        if v=='test':
            self.FILETYPES = [("text files", "*.csv")]
            self.chemin11 = (askopenfilename())
            # date_now = time.strftime('%d%m%Y')
            self.chemin = self.chemin11
            if self.chemin11 != '':
                self.load_csv(self.chemin,'test')

            self.btest_cleaning.grid(row=0, column=0)
            self.butiliser_model.destroy()

    def load_csv(self, chemin, v):
        if v=='train':
            header_list = ["id", "sentiment", "statement"]
            self.data = pd.read_csv(chemin, encoding="ISO-8859-1", sep=',', names=header_list)
            self.data = self.data.dropna(axis=0)
            self.id = list(self.data["id"])
            self.sentiment = list(self.data["sentiment"])
            self.statement = list(self.data["statement"])
            self.btrain = Button(self.haut_frame3, text='afficher train data',command=lambda: self.affiche_data(self.data,'train'), width=self.x // 40, bg='#0000FF',
                                 fg='white', relief=GROOVE, )
            per_data = int(len(self.data) * int(self.per.get()) / 100)
            self.data = self.data[0:per_data]
            self.btrain.grid(row=0, column=0)
            self.affiche_data(self.data,'train')


        if v == 'test':


            header_list2 = ["id","sentiment", "statement"]

            self.data2 = pd.read_csv(chemin, encoding="ISO-8859-1", sep=',', names=header_list2)

            self.data2 = self.data2.dropna(axis=0)

            per_data2 = int(len(self.data2) * int(self.per.get()) / 100)

            self.data2 = self.data2[0:1000]
            self.statement2 = list(self.data2["statement"])

            self.btest = Button(self.haut_frame3, text='afficher test data', command=lambda: self.affiche_data(self.data2,'test'),
                                width=self.x // 40, bg='#008000',
                                fg='white', relief=GROOVE, )
            self.btest.grid(row=0, column=2)
            self.affiche_data(self.data2, 'test')


    def hide_show(self,v,z):
        if v=='train':
            self.btest_cleaning.grid_forget()
            self.btest_steming.grid_forget()
            self.bidf_tf2.grid_forget()
            self.banalyse.grid_forget()
            self.bexport.grid_forget()
            self.btrain_cleaning.grid(row=2, column=0)
            self.btrain_steming.grid(row=3, column=0)
            self.bidf_tf1.grid(row=4, column=0)

            if self.z=='1':
                self.bentrainer.grid(row=5, column=0)
                self.bscore.grid(row=8, column=0)
                self.lscore.grid(row=9, column=0)

        if v=='test':
            self.btrain_cleaning.grid_forget()
            self.btrain_steming.grid_forget()
            self.bidf_tf1.grid_forget()
            self.bentrainer.grid_forget()
            self.bscore.grid_forget()
            self.lscore.grid_forget()
            self.btest_cleaning.grid(row=2, column=0)
            self.btest_steming.grid(row=3, column=0)
            self.bidf_tf2.grid(row=4,column=0)
            self.banalyse.grid(row=5,column=0)
            self.bexport.grid()














    def affiche_data(self,data,v):
                y1 = self.y // 20
                y2 = self.y // 14
                y3 = self.y - y1 - y2
                x3 = self.x // 5
                if v=='train':
                    self.hide_show('train','0')
                    self.btrain_cleaning.grid()
                    f = Frame(self.root)
                    f.grid(row=0, column=0)



                    pt = Table(self.centre_frame1, dataframe=data, height=y3 - y2, width=3 * x3 - 30)
                    pt.show()
                if v=='test':
                    self.hide_show('test','1')
                    self.btrain_cleaning.grid_forget()
                    self.btest_cleaning.grid()
                    f = Frame(self.root)
                    f.grid(row=0, column=0)



                    pt = Table(self.centre_frame1, dataframe=data, height=y3 - y2, width=3 * x3 - 30)
                    pt.show()
    def clean_text(self,v):
        y1 = self.y // 20
        y2 = self.y // 14
        y3 = self.y - y1 - y2
        x3 = self.x // 5
        if v=='train':

            self.data['statement']=self.data["statement"].apply(lambda x :" ".join(word.lower() for word in x.split()))

            self.data['statement']=self.data["statement"].str.replace(r"\W"," ")

            """for n, i in enumerate(list(self.data['statement'])):

                

                    if j[0] in i:
                        k = i.replace(j[0], " " + j[1] + " ")

                        self.data['statement'][n] = k"""

            l_filter = list(self.data['statement'])
            l_filter2=[]
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



            self.data['statement'] = l_filter2

            self.statement= list(self.data["statement"])
            self.statement = go_nettoyage.replace1(self.statement)


            pt = Table(self.centre_frame1, dataframe=self.data, height=y3 - y2, width=3 * x3 - 30)
            pt.show()
            #self.btext_steming.grid(row=1, column=0)
            self.btest_data = Button(self.droit_frame, text='import data test', width=self.x // 40, bg='#008000',
                                      fg='white', relief=GROOVE, command=lambda: self.set_data('test'))


            self.hide_show('train','0')

        if v=='test':


            self.data2['statement'] = self.data2["statement"].apply(lambda x: " ".join(word.lower() for word in x.split()))

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
            pt = Table(self.centre_frame1, dataframe=self.data2, height=y3 - y2, width=3 * x3 - 30)
            pt.show()
            self.hide_show('test','1')

            #self.btext_steming.grid(row=1, column=0)












    def stemming (self,v):
        y1 = self.y // 20
        y2 = self.y // 14
        y3 = self.y - y1 - y2
        x3 = self.x // 5
        if v=='train':

            self.data['statement']=go_nettoyage.stem(self.statement)


            pt = Table(self.centre_frame1, dataframe=self.data, height=y3 - y2, width=3 * x3 - 30)
            pt.show()
            #self.bidf_tf1.grid(row=2, column=0, sticky=S)
        if v=='test':

            self.data2['statement'] = go_nettoyage.stem(self.statement2)
            # self.data2['statement']=go_nettoyage.stem(self.statement2)

            pt = Table(self.centre_frame1, dataframe=self.data2, height=y3 - y2, width=3 * x3 - 30)
            pt.show()
            #self.bidf_tf1.grid(row=2, column=0, sticky=S)


if __name__ == '__main__':
    root = Tk()
    job(root)
    root.mainloop()