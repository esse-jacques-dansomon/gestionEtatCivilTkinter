################################################################################################
#forget mdp
##############
def forget_mdp():
    window=Tk()         
    window.title("interface")
    window.geometry("950x550+180+50")
    window.resizable(False, False)

    ##box pour ecrire ou take picture
    logo=Canvas(window,width=950,height=550,bg="#46B8E1")
    logo.place(x=0,y=10)

    log=Label(logo,text="Redefine mdp",font=('arial',19,'bold'))   #46877F
    log.place(x=20,y=10)

    identifiant = Label(logo,text="E-mail ou telephone",bg="#46B8E1",font=('arial',15,'bold'),fg="#fff")
    identifiant.place(x=400, y=80)

    Nom_Prenom = Label(logo,text="Nom & Prenom",bg="#46B8E1",font=('arial',15,'bold'),fg="#fff")
    Nom_Prenom.place(x=425, y=140)


    mdp=Label(logo,text="Enter the new password",bg="#46B8E1",font=('arial',15,'bold'),fg="#fff") 
    mdp.place(x=400,y=200)
    
    #fields entry
    mdpentry=Entry(logo,width=50,show="*",relief=FLAT,font=('arial',12))
    mdpentry.place(x=260,y=230)

    identifiantentry=Entry(logo,width=50,relief=FLAT,font=('arial',12))
    identifiantentry.place(x=260,y=170)

    Nom_Prenomentry=Entry(logo,width=50,relief=FLAT,font=('arial',12))
    Nom_Prenomentry.place(x=260,y=110)


    #BOUTTON CONNEXION
    connexion=Button(logo,text="VALIDER",bg="green",fg="white",relief=FLAT,font=('arial',12),width=20)
    connexion.place(x=400,y=280)

window.mainloop()
