from tkinter import*
from tkinter import messagebox

def certification_mariage():
    window=Tk()         
    window.title("Certification_Mariage")
    window.geometry("950x500+180+50")
    window.resizable(False, False)

    ##box pour ecrire ou take picture
    logo = Canvas(window,width=2950,height=5550,bg="#46B8E1")
    logo.place(x=0,y=10)

    log=Label(logo,text="Certification_Mariage",font=('arial',10,'bold'))   #46877F
    log.place(x=40,y=10)
    #BOUTTON IMPRIMER
    connexion=Button(logo,text="IMPRIMER",bg="black",fg="white",relief=FLAT,font=('arial',9),width=8,command=lambda:joke())
    connexion.place(x=798,y=10)
    

    NAMEgars = Label(logo,text="Nom Du Messieur",bg="#46B8E1",font=('arial',12,'bold'),fg="#fff")
    NAMEgars.place(x=40, y=45)
    NAMEgarsentry=Entry(logo,width=9,relief=FLAT,font=('arial',12))
    NAMEgarsentry.place(x=30,y=75)

    NAMEgo = Label(logo,text="Nom De la Femme",bg="#46B8E1",font=('arial',12,'bold'),fg="#fff")
    NAMEgo.place(x=40, y=95)
    NAMEgoentry=Entry(logo,width=9,relief=FLAT,font=('arial',12))
    NAMEgoentry.place(x=30,y=125)


    place=Label(logo,text="Lieu  de Mariage",bg="#46B8E1",font=('arial',12,'bold'),fg="#fff") 
    place.place(x=40,y=145)
    #fields entry
    placeentry=Entry(logo,width=9,relief=FLAT,font=('arial',12))
    placeentry.place(x=30,y=175)

######################
#....2eme box
#################
    celebrepar = Label(logo,text="celebrer_par",bg="#46B8E1",font=('arial',12,'bold'),fg="#fff")
    celebrepar.place(x=700, y=35)
    celebreparentry=Entry(logo,width=9,relief=FLAT,font=('arial',12))
    celebreparentry.place(x=700,y=65)

    TH = Label(logo,text="TEMOINS_HOMME",bg="#46B8E1",font=('arial',12,'bold'),fg="#fff")
    TH.place(x=700, y=93)
    THentry=Entry(logo,width=9,relief=FLAT,font=('arial',12))
    THentry.place(x=700,y=120)

    TF = Label(logo,text="TEMOINS_FEMME",bg="#46B8E1",font=('arial',12,'bold'),fg="#fff")
    TF.place(x=700, y=138)
    TFentry=Entry(logo,width=9,relief=FLAT,font=('arial',12))
    TFentry.place(x=700,y=172)

    #BOUTTON CONNEXION
    connexion=Button(logo,text="VALIDER",bg="black",fg="white",relief=FLAT,font=('arial',12),width=20)
    connexion.place(x=400,y=280)

    window.mainloop()


