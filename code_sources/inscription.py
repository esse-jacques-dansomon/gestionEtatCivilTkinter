from tkinter import messagebox

def creer_compte(self,window):
    self.window.window
    #self.window=Tk()         
    self.window.title("creer_compte")
    self.window.geometry("950x550+180+50")
    self.window.resizable(False, False)

    ##box pour ecrire ou take picture
    logo=Canvas(self,window,width=950,height=550,bg="#582900")
    logo.place(x=0,y=10)

    log=Label(logo,text="Creation Compte",font=('arial',19,'bold'))   #46877F
    log.place(x=20,y=10)

    identifiant=StringVar()
    mdp=StringVar()
    Lidentifiant = Label(logo,text="E-mail ou telephone",bg="#070505",font=('arial',15,'bold'),fg="#fff")
    Lidentifiant.place(x=400, y=80)

    LNom_Prenom = Label(logo,text="Nom & Prenom",bg="#070505",font=('arial',15,'bold'),fg="#fff")
    LNom_Prenom.place(x=425, y=140)


    Lmdp=Label(logo,text="Mot de passe",bg="#070505",font=('arial',15,'bold'),fg="#fff") 
    Lmdp.place(x=425,y=200)
    
    #fields entry
    self.mdpentry=Entry(logo,width=50,show="*",relief=FLAT,font=('arial',12))
    self.mdpentry.place(x=260,y=230)

    self.identifiantentry=Entry(logo,width=50,relief=FLAT,font=('arial',12))
    self.identifiantentry.place(x=260,y=170)

    self.Nom_Prenomentry=Entry(logo,width=50,relief=FLAT,font=('arial',12))
    self.Nom_Prenomentry.place(x=260,y=110)


    #BOUTTON CONNEXION
    connexion=Button(logo,text="VALIDER",relief=FLAT,font=('arial',12,'bold'),width=20,bg="#070505",fg="white")
    connexion.place(x=400,y=280)


        

    

