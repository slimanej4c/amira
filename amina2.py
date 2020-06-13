
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename

import pandas as pd


from nettoyage import *
from pandastable import Table, TableModel


go_nettoyage=nettoyage_class()
import tf_idf1
import tf_idf2


class job:
    def __init__(self,root):



        self.root = root

        self.x=1000
        self.y=700
        self.root.geometry('%sx%s'%(self.x,self.y))
        self.id = []
        self.sentiment = []
        self.satatement = []

        self.frame()
        self.bautton([])



    def frame(self):

        self.positive=0
        self.nigative=0
        self.neutre=0


        self.global_frame=Frame(self.root ,height=self.y,width=self.x,bg='white')
        self.global_frame.grid(row=0,column=0)
        self.global_frame.grid_propagate(0)
        y1=self.y//20
        y2 = self.y // 14
        self.haut_frame1 = Frame(self.global_frame, height=y1, width=self.x,bg='#808B96')
        self.haut_frame1.grid(row=0, column=0,sticky=N)
        self.haut_frame1.grid_propagate(0)

        self.haut_frame2 = Frame(self.global_frame, height=y2/2, width=self.x, bg='#808B96')
        self.haut_frame2.grid(row=1, column=0, sticky=N)
        self.haut_frame2.grid_propagate(0)
        self.haut_frame2.grid_rowconfigure(0,weight=1)

        self.haut_frame3 = Frame(self.global_frame, height=y2/2, width=self.x, bg='#85C1E9')
        self.haut_frame3.grid(row=2, column=0, sticky=N)
        self.haut_frame3.grid_propagate(0)
        self.haut_frame3.grid_rowconfigure(0, weight=1)
        y3=self.y-y1-y2
        x3=self.x//5


        button_haut1=Button(self.haut_frame2,text='')
        self.gauche_frame= Frame(self.global_frame, height=y3, width=x3, bg='#154360')
        self.gauche_frame.grid(row=3, column=0,rowspan=2,sticky=W)
        self.gauche_frame.grid_propagate(0)


        self.droit_frame = Frame(self.global_frame, height=y3, width=x3, bg='#154360')
        self.droit_frame.grid(row=3, column=0,rowspan=2, sticky=E)
        self.droit_frame.grid_propagate(0)


        self.centre_frame1 = Frame(self.global_frame)
        self.centre_frame1.grid(row=3, column=0,sticky=N)

        self.bas_frame = Frame(self.global_frame, height=y2, width=3 * x3, bg='#85C1E9')
        self.bas_frame.grid(row=4, column=0,sticky=S)
        self.bas_frame.grid_propagate(0)


    def bautton(self,dataset):

        lper=Label(self.droit_frame,text='persontage')
        lper.grid(row=0,column=0)

        self.combo_per = ttk.Combobox(self.droit_frame, values=[5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100])

        self.combo_per.bind('<<ComboboxSelected>>', self.depart)



        self.combo_per.grid(column=1, row=0)




        self.btext_cleaning = Button(self.gauche_frame, text='text_cleaning', width=self.x // 60,bg='#1B2631',fg='white', relief=GROOVE,command=self.clean_text)

        self.btext_steming= Button(self.gauche_frame, text='stemming', width=self.x // 60, bg='#1B2631',
                                     fg='white', relief=GROOVE, command=self.stemming)





        self.btest_Data = Button(self.droit_frame, text='import data test', width=self.x // 60, bg='#1B2631',
                                  fg='white', relief=GROOVE, command=self.set_data2)


        self.bidf_tf1= Button(self.gauche_frame, text='tf*idf_train', width=self.x // 60, bg='#1B2631',
                                         fg='white', relief=GROOVE, command=self.tf_idf_1)

        self.bidf_tf2 = Button(self.gauche_frame, text='tf*idf_train', width=self.x // 60, bg='#1B2631',
                               fg='white', relief=GROOVE, command=self.tf_idf_2)














    def  depart( self,event):
            print('ok')
            self.btrain_Data = Button(self.droit_frame, text='import data train', width=self.x // 60, bg='#1B2631',
                                      fg='white', relief=GROOVE, command=self.set_data)
            self.btrain_Data.grid(row=1, column=0, sticky=S, padx=20)

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
        self.go=tf_idf2.tf_idf(li2[0:1000], self.centre_frame1, h, w)
        self.bafficheidf_test = Button(self.haut_frame3, text='afficher idf_tf test', command=self.go.afficher_idf, width=self.x // 60, bg='#1B2631',
                                         fg='white', relief=GROOVE,)

        self.bafficheidf_test.grid(row=0, column=3)
        import train_test
        go=train_test.train_test(self.data['statement'], self.data['sentiment'], self.data2['statement'], self.data2['sentiment'])
        vscore = StringVar()
        vscore.set('')
        butiliser_model=Button(self.haut_frame3,text='utilser le model',command=lambda:go.utiliser_svm(self.centre_frame1), width=self.x // 60, bg='#1B2631',
                                         fg='white', relief=GROOVE,)

        self.tester = Button(self.gauche_frame, text='tester',command=lambda:go.tester(vscore,butiliser_model), width=self.x // 60, bg='#1B2631',
                                         fg='white', relief=GROOVE,)


        self.lscore=Label(self.gauche_frame,textvariable=vscore)
        self.lscore.grid(row=6,column=0)
        self.entrainer = Button(self.gauche_frame, text='entrainer',command=lambda:go.entrainer(self.tester,self.root), width=self.x // 60, bg='#1B2631',
                                         fg='white', relief=GROOVE,)
        self.entrainer.grid(row=4, column=0)
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
        self.bafficheidf_train = Button(self.haut_frame3, text='afficher idf_tf train', command=self.go.afficher_idf, width=self.x // 60, bg='#1B2631',
                                         fg='white', relief=GROOVE,)

        self.bafficheidf_train.grid(row=0, column=2)
        self.bidf_tf2.grid(row=3, column=0, sticky=S)

    def set_data(self):
        self.FILETYPES = [("text files", "*.csv")]
        self.chemin11=(askopenfilename())
        #date_now = time.strftime('%d%m%Y')
        self.chemin=self.chemin11
        self.btest_Data.grid(row=2, column=0, sticky=S, padx=20)



    def set_data2(self):
        self.FILETYPES = [("text files", "*.csv")]
        self.chemin22=(askopenfilename())
        #date_now = time.strftime('%d%m%Y')
        self.chemin2=self.chemin22

        if self.chemin11 !='' and self.chemin22 !='':
            self.load_csv(self.chemin,self.chemin2)
        self.btext_cleaning.grid(row=0, column=0)

    def clean_text(self):
        self.data['statement']=self.data["statement"].apply(lambda x :" ".join(word.lower() for word in x.split()))

        self.data['statement']=self.data["statement"].str.replace(r"\W"," ")
        self.statement= list(self.data["statement"])
        self.statement = go_nettoyage.replace1(self.statement)
        y1 = self.y // 20
        y2 = self.y // 14
        y3 = self.y - y1 - y2
        x3 = self.x // 5

        pt = Table(self.centre_frame1, dataframe=self.data, height=y3 - y2, width=3 * x3 - 30)
        pt.show()

        self.btext_steming.grid(row=1, column=0)

        self.data2['statement'] = self.data2["statement"].apply(lambda x: " ".join(word.lower() for word in x.split()))

        self.data2['statement'] = self.data2["statement"].str.replace(r"\W", " ")
        self.statement2 = list(self.data2["statement"])
        self.statement2 = go_nettoyage.replace1(self.statement2)





    def load_csv(self,chemin,chemin2):
        header_list = ["id", "sentiment", "statement"]
        self.data=pd.read_csv(chemin,encoding = "ISO-8859-1",sep=',',names=header_list)

        self.data = self.data.dropna(axis=0)

        self.id=list(self.data["id"])
        self.sentiment=list(self.data["sentiment"])
        self.statement=list(self.data["statement"])



        self.data2 = pd.read_csv(chemin2, encoding="ISO-8859-1", sep=',', names=header_list)

        self.data2 = self.data2.dropna(axis=0)
        per_data=int(len(self.data)*int(self.combo_per.get())/100)
        per_data2=int(len(self.data2)*int(self.combo_per.get())/100)

        self.data=self.data[0:per_data]
        self.data2=self.data2[0:per_data2]

        self.btest = Button(self.haut_frame3, text='afficher test data', command=lambda:self.affiche_data(self.data2), width=self.x // 60, bg='#1B2631',
                                         fg='white', relief=GROOVE,)
        self.btest.grid(row=0, column=1)

        self.btrain = Button(self.haut_frame3, text='afficher train data', command=lambda:self.affiche_data(self.data), width=self.x // 60, bg='#1B2631',
                                         fg='white', relief=GROOVE,)
        self.btrain.grid(row=0, column=0)
        self.affiche_data(self.data)


    def affiche_data(self,data):
        f = Frame(self.root)
        f.grid(row=0, column=0)

        y1 = self.y // 20
        y2 = self.y // 14
        y3 = self.y - y1 - y2
        x3 = self.x // 5

        pt = Table(self.centre_frame1, dataframe=data, height=y3 - y2, width=3 * x3 - 30)
        pt.show()

    def percentage(self,part,all):
        return 100*part/all


    def analyse_data(self):

        pass

    def stemming (self):
        self.data['statement']=go_nettoyage.stem(self.statement)
        self.data2['statement']=go_nettoyage.stem(self.statement2)
        #self.data2['statement']=go_nettoyage.stem(self.statement2)
        y1 = self.y // 20
        y2 = self.y // 14
        y3 = self.y - y1 - y2
        x3 = self.x // 5
        print(self.data['statement'][0:10])
        pt = Table(self.centre_frame1, dataframe=self.data, height=y3 - y2, width=3 * x3 - 30)
        pt.show()
        self.bidf_tf1.grid(row=2, column=0, sticky=S)



if __name__ == '__main__':
     root=Tk()
     job(root)
     root.mainloop()