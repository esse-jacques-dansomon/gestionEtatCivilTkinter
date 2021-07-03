from tkinter import*
import tkinter as tkinter
from tkinter import messagebox
def __init__():
    window=Tk()         
    window.title("login system")
    window.geometry("950x550+180+50")
    window.resizable(False, False)
        ##box pour ecrire ou take picture
    logo=Canvas(self.window,width=950,height=550,bg="#46B8E1").place(x=0,y=10)

    log=Label(logo,text="interface",font=('arial',19,'bold'))   #46877F
    log.place(x=20,y=10)

    identifiant=StringVar()
    mdp=StringVar()
    Lidentifiant = Label(logo,text="E-mail ou telephone",bg="#46B8E1",font=('arial',15,'bold'),fg="#fff")
    Lidentifiant.place(x=400, y=140)


    Lmdp=Label(logo,text="Mot de passe",bg="#46B8E1",font=('arial',15,'bold'),fg="#fff") 
    Lmdp.place(x=430,y=200)


        #fields entry
    mdpentry=Entry(logo,textvariable=mdp,width=50,show="*",relief=FLAT,font=('arial',12))
    mdpentry.place(x=260,y=230)

    identifiantentry=Entry(logo,textvariable=identifiant,width=50,relief=FLAT,font=('arial',12))
    identifiantentry.place(x=260,y=170)

        
        ##############
        #check
        ##############
def popup():
    
        
   
    if identifiant.get()=="" or mdp.get()=="":
        messagebox.showerror("Error", "thks to respect ,all fields required",parent=self.window)
    elif identifiant.get()!="pds" or  mdp.get()!="123456":
        messagebox.showerror("Error", "thks to respect ,all fields requireds",parent=self.window)
    else:
        messagebox.showinfo("Welcome",f"Welcome {identifiant.get()}",parent=self.window)




        #BOUTTON CONNEXION
        connexion=Button(logo,cursor="hand2",text="Se connecter",bg="green",fg="white",relief=FLAT,font=('arial',12),width=20,command=lambda:popup())
        connexion.place(x=400,y=280)


        #mot de passe
        oublie=Button(logo,text="Mot de passe oublié ?",bg="#46B8E1",fg="white",relief=FLAT,font=('arial',12),width=20,command=lambda:forget_mdp())
        oublie.place(x=490,y=350)

        #creer compte
        CreerCompte=Button(logo,text="Creer un Compte",bg="#46B8E1",fg="white",relief=FLAT,font=('arial',12),width=20,command=lambda:creer_compte())
        CreerCompte.place(x=270,y=350)


window.mainloop()



