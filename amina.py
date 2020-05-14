
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename

import pandas as pd


from nettoyage import *

go_nettoyage=nettoyage_class()


class job:
    def __init__(self,root):



        self.root = root

        self.x=900
        self.y=700
        self.root.geometry('%sx%s'%(self.x,self.y))
        self.id = []
        self.sentiment = []
        self.satatement = []

        self.frame()
        self.bautton()



    def frame(self):

        self.positive=0
        self.nigative=0
        self.neutre=0
        self.polarité=0

        self.global_frame=Frame(self.root ,height=self.y,width=self.x,bg='red')
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
        self.gauche_frame.grid_rowconfigure(0, weight=2)
        self.gauche_frame.grid_rowconfigure(6, weight=2)
        self.gauche_frame.grid_rowconfigure(4, weight=2)

        self.droit_frame = Frame(self.global_frame, height=y3, width=x3, bg='#154360')
        self.droit_frame.grid(row=3, column=0,rowspan=2, sticky=E)
        self.droit_frame.grid_propagate(0)
        self.droit_frame.grid_rowconfigure(0, weight=1)
        self.droit_frame.grid_rowconfigure(1, weight=1)
        self.droit_frame.grid_rowconfigure(2, weight=1)
        self.droit_frame.grid_rowconfigure(3, weight=1)

        self.centre_frame1 = Frame(self.global_frame, height=y3-y2, width=3*x3, bg='#808B96')
        self.centre_frame1.grid(row=3, column=0,sticky=N)
        self.centre_frame1.grid_propagate(0)
        self.bas_frame = Frame(self.global_frame, height=y2, width=3 * x3, bg='#85C1E9')
        self.bas_frame.grid(row=4, column=0,sticky=S)
        self.bas_frame.grid_propagate(0)


    def bautton(self):
        self.bpretreatement=Button(self.haut_frame2,text='Pretreatement',width=self.x//80,bg='#1B2631',fg='white', relief=GROOVE )
        self.bpretreatement.grid(row=0,column=0,sticky=S)

        self.bclassification = Button(self.haut_frame2, text='Classification',width=self.x//80,bg='#1B2631',fg='white', relief=GROOVE )
        self.bclassification.grid(row=0, column=1,sticky=S)

        self.ltext_data = Label(self.haut_frame3, text='text_data', width=self.x // 80,bg='#154360',fg='white', relief=FLAT)
        self.ltext_data.grid(row=0, column=0, sticky=S)



        self.btext_cleaning = Button(self.gauche_frame, text='text_cleaning', width=self.x // 60,bg='#1B2631',fg='white', relief=GROOVE,command=self.clean_text)
        self.btext_cleaning.grid(row=0, column=0)
        self.btext_cleaning = Button(self.gauche_frame, text='stemmingng', width=self.x // 60, bg='#1B2631',
                                     fg='white', relief=GROOVE, command=self.stemming)
        self.btext_cleaning.grid(row=0, column=1)

        self.cbn_gran=ttk.Combobox (self.gauche_frame,values=['1','2'],width=self.x//150)
        self.cbn_gran.grid(row=1, column=1,sticky=W)

        self.rngram = Radiobutton(self.gauche_frame, text='N_GRAM..', value=1,width=self.x//100,bg='#154360',fg='white', relief=GROOVE)
        self.rngram.grid(row=1, column=0, sticky=W)

        self.rbag_of_word = Radiobutton(self.gauche_frame, text='Bag Of Word', value=2,width=self.x//100,bg='#154360',fg='white', relief=GROOVE)
        self.rbag_of_word.grid(row=2, column=0, sticky=W)

        self.rsteming = Radiobutton(self.gauche_frame, text='Steming', value=3,width=self.x//100,bg='#154360',fg='white', relief=GROOVE)
        self.rsteming.grid(row=3, column=0, sticky=W)

        self.btext_representation = Button(self.gauche_frame, text='Text representation', width=self.x // 60,bg='#1B2631',fg='white', relief=GROOVE)
        self.btext_representation.grid(row=4, column=0)

        self.rtfn = Radiobutton(self.gauche_frame, text='TFN', value=4,bg='#154360',fg='white', relief=GROOVE)
        self.rtfn.grid(row=5, column=0, sticky=W)

        self.rtf_idf = Radiobutton(self.gauche_frame, text='TF*IDF', value=5,bg='#154360',fg='white', relief=GROOVE)
        self.rtf_idf.grid(row=5, column=1, sticky=W)

        self.bcoding_text = Button(self.gauche_frame, text='Coding Text', width=self.x // 60,bg='#1B2631',fg='white', relief=GROOVE)
        self.bcoding_text.grid(row=6, column=0)



        self.bunstructured_Data = Button(self.droit_frame, text='Unstructured Data', width=self.x // 60,bg='#1B2631',fg='white', relief=GROOVE,command=self.set_data)
        self.bunstructured_Data .grid(row=0, column=0,sticky=S)

        self.bcollection_tweets = Button(self.droit_frame, text='Collection des tweets', width=self.x // 60,bg='#1B2631',fg='white', relief=GROOVE)
        self.bcollection_tweets.grid(row=1, column=0)

        self.b1 = Button(self.droit_frame, text='Collection des tweets', width=self.x // 60,
                                         bg='#1B2631', fg='white', relief=GROOVE)
        self.b1.grid(row=2, column=0)

        self.b2 = Button(self.droit_frame, text='Collection des tweets', width=self.x // 60,
                                         bg='#1B2631', fg='white', relief=GROOVE)
        self.b2.grid(row=3, column=0)



        self.listbox = Listbox(self.centre_frame1,width=86,height=34)
        self.listbox.grid(row=0, column=0)
        self.scrollbarv = Scrollbar(self.centre_frame1,orient=VERTICAL)
        self.scrollbarv.grid(row=0,column=1,sticky=N+S)
        self.scrollbarh = Scrollbar(self.centre_frame1,orient=HORIZONTAL)
        self.scrollbarh.grid(row=2, column=0,columnspan=2,sticky=W+E)

        self.listbox.insert(END, "id                  " + "  sentiment            " + "                                                   text")
        for i in range(len(self.id)):

            self.listbox.insert(END,str(self.id[i])+"   "+"                 " +str(self.sentiment[i])+"                         "+str(self.statement[i]))

        self.listbox.config(yscrollcommand=self.scrollbarv.set)
        self.listbox.config(xscrollcommand=self.scrollbarh.set)

        self.scrollbarv.config(command=self.listbox.yview)
        self.scrollbarh.config(command=self.listbox.xview)


    def set_data(self):
        self.FILETYPES = [("text files", "*.csv")]
        self.chemin1=(askopenfilename())
        #date_now = time.strftime('%d%m%Y')
        self.chemin=self.chemin1

        if self.chemin1 !='':
            self.load_csv(self.chemin)

    def clean_text(self):
        self.data['statement']=self.data["statement"].apply(lambda x :" ".join(word.lower() for word in x.split()))
        self.data['statement']=self.data["statement"].str.replace(r"\W"," ")
        self.statement= list(self.data["statement"])

        self.bautton()
        self.analyse_data()


    def load_csv(self,chemin):
        header_list = ["id", "sentiment", "statement"]
        self.data=pd.read_csv(chemin,encoding = "ISO-8859-1",sep=',',names=header_list)
        print(self.data.shape)
        self.data = self.data.dropna(axis=0)
        print(self.data.shape)

        self.id=list(self.data["id"])
        self.sentiment=list(self.data["sentiment"])
        self.statement=list(self.data["statement"])

        self.bautton()
        self.analyse_data()
        print(self.data["statement"][0])


    def percentage(self,part,all):
        return 100*part/all


    def analyse_data(self):

        pass

    def stemming (self):

        self.satatement=go_nettoyage.stem(self.satatement)
        self.bautton()








if __name__ == '__main__':
     root=Tk()
     job(root)
     root.mainloop()