from tkinter import *
from tkinter import messagebox
import extrait_de_naissance
import declaration_de_naissance
import declaration_de_mariage

def dashbord():

    window = Tk()
    window.title("creer_compte")
    window.geometry("950x550+180+50")
    window.resizable(False, False)

    #variables
    identifiant = StringVar()
    mdp = StringVar()
    nom = StringVar()

    ##box pour ecrire ou take picture
    logo = Canvas(window, width=950, height=550, bg="#582900")
    logo.place(x=0, y=10)

    log = Label(logo, text="Creation Compte", font=('arial', 19, 'bold'))  # 46877F
    Lidentifiant = Label(logo, text="E-mail", bg="#070505", font=('arial', 15, 'bold'), fg="#fff")
    Lmdp = Label(logo, text="Mot de passe", bg="#070505", font=('arial', 15, 'bold'), fg="#fff")
    LNomPrenom = Label(logo,text="Nom & Prenom",bg="#070505",font=('arial',15,'bold'),fg="#fff")

    log.place(x=20, y=10)
    Lidentifiant.place(x=400, y=80)
    Lmdp.place(x=425, y=200)
    LNomPrenom.place(x=425, y=140)


    # fields entry
    mdpentry = Entry(logo, textvariable=mdp, width=50, show="*", relief=FLAT, font=('arial', 12))
    identifiantentry = Entry(logo, textvariable=identifiant, width=50, relief=FLAT, font=('arial', 12))
    NomPrenomentry=Entry(logo, textvariable=nom, width=50,relief=FLAT,font=('arial',12))

    mdpentry.place(x=260, y=230)
    identifiantentry.place(x=260, y=170)
    NomPrenomentry.place(x=260,y=110)

    # Buttons
    valider = Button(logo, text="VALIDER", relief=FLAT, font=('arial', 12, 'bold'), width=20, bg="#070505",fg="white", command=lambda:popup())
    DeclarerEnfant = Button(logo, text="Declaration Administrative", bg="#070505", fg="white", relief=FLAT,font=('arial', 12, 'bold'), width=20, command=declaration_de_naissance.declaration_naissance)
    RETRAITEXTRAIT = Button(logo, text="Acte De Naissance ", bg="#070505", fg="white", relief=FLAT, font=('arial', 12, 'bold'), width=20, command=extrait_de_naissance.extrait_naissance)
    Declaration_mariage = Button(logo, text="Declaration De Mariage", bg="#070505", fg="white", relief=FLAT, font=('arial', 12, 'bold'), width=20, command=declaration_de_mariage.certification_mariage)

    valider.place(x=400, y=280)
    DeclarerEnfant.place(x=270, y=350)
    RETRAITEXTRAIT.place(x=520, y=350)
    Declaration_mariage.place(x=350, y=400)

    def popup():
        if identifiant.get() != "" and mdp.get() != "":
            login = identifiant.get()
            password = mdp.get()
            userModel = userDao.UserDao()
            user = userModel.loginAndPasswordExist(login, password)
            if user is not None:
                window.destroy()
            else:
                messagebox.showerror("ERROR", "login ou mot de passe incorect", parent=window)
        else:
            messagebox.showerror("ERROR", "VEUILLEZ REMPLIR TOUS LES CHAMPS", parent=window)
    window.mainloop()



