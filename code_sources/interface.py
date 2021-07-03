from tkinter import*
#import tkinter as tkinter
from tkinter import messagebox
import mysql.connector


window=Tk()
window.title("login system")
window.geometry("950x550+180+50")
window.resizable(False, False)


##box pour ecrire ou take picture
logo=Canvas(window,width=950,height=550,bg="#46B8E1").place(x=0,y=10)
log=Label(logo,text="interface",font=('arial',19,'bold'))   #46877F
log.place(x=20,y=10)

identifiant=StringVar()
mdp=StringVar()
NomPrenom=StringVar()

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
        messagebox.showerror("Error", "all fields required",parent=window)
    elif identifiant.get()!="pds" or  mdp.get()!="123456":
        messagebox.showerror("Error", "thks to respect ,all fields requireds",parent=window)
    else:
        messagebox.showinfo("Welcome",f"Welcome {identifiant.get()}",parent=window)


    




        #BOUTTON CONNEXION
connexion=Button(logo,cursor="hand2",text="Se connecter",bg="green",fg="white",relief=FLAT,font=('arial',12),width=20,command=lambda:creer_compte())
connexion.place(x=400,y=280)


        #mot de passe
oublie=Button(logo,text="Mot de passe oublié ?",bg="#46B8E1",fg="white",relief=FLAT,font=('arial',12),width=20,command=lambda:forget_mdp())
oublie.place(x=490,y=350)

        #creer compte
#CreerCompte=Button(logo,text="Creer un Compte",bg="#46B8E1",fg="white",relief=FLAT,font=('arial',12),width=20,command=lambda:creer_compte())
#CreerCompte.place(x=270,y=350)


        

##########################################################################################################
#register user
##############

#data=RecupDonneFromUsersapp(db,"amate")
#print(data)



    




################################################################################################
#creeer compte
##############
    
def creer_compte():
    global window
    global identifiant
    global identifiantentry
    global mdp
    global mdpentry
    identifiant=StringVar()
    mdp=StringVar()

    window=Tk()         
    window.title("creer_compte")
    window.geometry("950x550+180+50")
    window.resizable(False, False)

        ##box pour ecrire ou take picture
    logo=Canvas(window,width=950,height=550,bg="#582900")
    logo.place(x=0,y=10)

    log=Label(logo,text="Creation Compte",font=('arial',19,'bold'))   #46877F
    log.place(x=20,y=10)


    
    Lidentifiant = Label(logo,text="E-mail ou telephone",bg="#070505",font=('arial',15,'bold'),fg="#fff")
    Lidentifiant.place(x=400, y=80)

    Lmdp=Label(logo,text="Mot de passe",bg="#070505",font=('arial',15,'bold'),fg="#fff") 
    Lmdp.place(x=425,y=200)

    #LNomPrenom = Label(logo,text="Nom & Prenom",bg="#070505",font=('arial',15,'bold'),fg="#fff")
    #LNomPrenom.place(x=425, y=140)
        
        #fields entry
    mdpentry=Entry(logo,textvariable=mdp,width=50,show="*",relief=FLAT,font=('arial',12))
    mdpentry.place(x=260,y=230)

    identifiantentry=Entry(logo,textvariable=identifiant,width=50,relief=FLAT,font=('arial',12))
    identifiantentry.place(x=260,y=170)

    #NomPrenomentry=Entry(logo,width=50,relief=FLAT,font=('arial',12))
    #NomPrenomentry.place(x=260,y=110)


        #BOUTTON CONNEXION
    connexion=Button(logo,text="VALIDER",relief=FLAT,font=('arial',12,'bold'),width=20,bg="#070505",fg="white",command=lambda:connexion())
    connexion.place(x=400,y=280)
       #creer compte
    DeclarerEnfant=Button(logo,text="Declaration Administrative",bg="#070505",fg="white",relief=FLAT,font=('arial',12,'bold'),width=20,command=lambda:etat_civil())
    DeclarerEnfant.place(x=270,y=350)
    #EXTRAIT DE NAISSANCE
    RETRAITEXTRAIT=Button(logo,text="RETRAIT_EXTRAIT",bg="#070505",fg="white",relief=FLAT,font=('arial',12,'bold'),width=20,command=lambda:Extrait_naissance())
    RETRAITEXTRAIT.place(x=520,y=350)
     #Declaration mariage
    Declaration_mariage=Button(logo,text="Declaration_mariage",bg="#070505",fg="white",relief=FLAT,font=('arial',12,'bold'),width=20,command=lambda:Certification_Mariage())
    Declaration_mariage.place(x=350,y=400)
        
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

    NomPrenom = Label(logo,text="Nom & Prenom",bg="#46B8E1",font=('arial',15,'bold'),fg="#fff")
    NomPrenom.place(x=425, y=140)


    mdp=Label(logo,text="Enter the new password",bg="#46B8E1",font=('arial',15,'bold'),fg="#fff") 
    mdp.place(x=400,y=200)
    
    #fields entry
    mdpentry=Entry(logo,width=50,show="*",relief=FLAT,font=('arial',12))
    mdpentry.place(x=260,y=230)

    identifiantentry=Entry(logo,width=50,relief=FLAT,font=('arial',12))
    identifiantentry.place(x=260,y=170)

    NomPrenomentry=Entry(logo,width=50,relief=FLAT,font=('arial',12))
    NomPrenomentry.place(x=260,y=110)


    #BOUTTON CONNEXION
    connexion=Button(logo,text="VALIDER",bg="green",fg="white",relief=FLAT,font=('arial',12),width=20)
    connexion.place(x=400,y=280)
################################################################################################
#DECLARATION ETAT CIVIL
##############
def etat_civil():    
    window=Tk()         
    window.title("interface")
    window.geometry("950x700+180+50")
    window.resizable(False, False)

    ##box pour ecrire ou take picture
    logo=Canvas(window,width=2950,height=5550,bg="#46B8E1")
    logo.place(x=0,y=10)

    log=Label(logo,text="ETAT_CIVIL",font=('arial',10,'bold'))   #46877F
    log.place(x=40,y=10)
     #BOUTTON IMPRIMER
    connexion=Button(logo,text="IMPRIMER",bg="black",fg="white",relief=FLAT,font=('arial',9),width=8,command=lambda:joke())
    connexion.place(x=798,y=10)
    

    Region = Label(logo,text="Region",bg="#46B8E1",font=('arial',12,'bold'),fg="#fff")
    Region.place(x=40, y=40)

    Departement = Label(logo,text="Departement",bg="#46B8E1",font=('arial',12,'bold'),fg="#fff")
    Departement.place(x=40, y=90)


    Arrondissement=Label(logo,text="Arrondissement",bg="#46B8E1",font=('arial',12,'bold'),fg="#fff") 
    Arrondissement.place(x=40,y=140)

    Collectivite_Locale=Label(logo,text="Collectivite Locale(commune de)",bg="#46B8E1",font=('arial',12,'bold'),fg="#fff") 
    Collectivite_Locale.place(x=40,y=190)


    
    #fields entry
    Collectivite_Localeentry=Entry(logo,width=9,relief=FLAT,font=('arial',12))
    Collectivite_Localeentry.place(x=30,y=170)

    Departemententry=Entry(logo,width=9,relief=FLAT,font=('arial',12))
    Departemententry.place(x=30,y=120)

    Regionentry=Entry(logo,width=9,relief=FLAT,font=('arial',12))
    Regionentry.place(x=30,y=70)

    Collectivite_Localeentry=Entry(logo,width=9,relief=FLAT,font=('arial',12))
    Collectivite_Localeentry.place(x=30,y=220)

######################
#....2eme box
#################
    ETAT_CIVIL=Label(logo,text="ETAT CIVIL",font=('arial',14,'bold'))   #46877F
    ETAT_CIVIL.place(x=430,y=10)

    Centre_de = Label(logo,text="Centre de ",bg="#46B8E1",font=('arial',12,'bold'),fg="#fff")
    Centre_de.place(x=385, y=48)

    Centre_deentry=Entry(logo,width=9,relief=FLAT,font=('arial',12))
    Centre_deentry.place(x=480,y=49)

####################
#....3eme box
#################

    ETAT_CIVIL=Label(logo,text="EXTRAIT DU REGISTRE DES ACTES DE NAISSANCE",font=('arial',14,'bold'))   #46877F
    ETAT_CIVIL.place(x=40,y=249)

    an =Label(logo,text="Pour l'année (2)",bg="#46B8E1",font=('arial',12,'bold'),fg="#fff")
    an.place(x=40, y=284)

    anentry=Entry(logo,width=9,relief=FLAT,font=('arial',14))
    anentry.place(x=199,y=284)
    antext =Label(logo,text="(En lettre)",bg="#46B8E1",font=('arial',8),fg="#fff")
    antext.place(x=228, y=310)
    ###num registre
    num =Label(logo,text="Nº dans le Registre",bg="#46B8E1",font=('arial',12,'bold'),fg="#fff")
    num.place(x=40, y=324)

    numentry=Entry(logo,width=9,relief=FLAT,font=('arial',14))
    numentry.place(x=199,y=328)
    antext =Label(logo,text="(En lettre)",bg="#46B8E1",font=('arial',8),fg="#fff")
    antext.place(x=228, y=354)
  
#####
    date =Label(logo,text="Le",bg="#46B8E1",font=('arial',12,'bold'),fg="#fff")
    date.place(x=40, y=370)
    numentry=Entry(logo,width=18,relief=FLAT,font=('arial',14))
    numentry.place(x=199,y=372)

    datea =Label(logo,text="a",bg="#46B8E1",font=('arial',12,'bold'),fg="#fff")
    datea.place(x=40, y=404)
    dateaentry=Entry(logo,width=18,relief=FLAT,font=('arial',14))
    dateaentry.place(x=199,y=408)
    
    sex =Label(logo,text=" Un enfant de sexe ",bg="#46B8E1",font=('arial',12,'bold'),fg="#fff")
    sex.place(x=40, y=442)
    sexentry=Entry(logo,width=9,relief=FLAT,font=('arial',14))
    sexentry.place(x=200,y=442)

    PRENOM =Label(logo,text=" PRENOMS ",bg="#46B8E1",font=('arial',12,'bold'),fg="#fff")
    PRENOM.place(x=409, y=284)
    PRENOMentry=Entry(logo,width=10,relief=FLAT,font=('arial',14))
    PRENOMentry.place(x=509,y=284)

    NOMFAM =Label(logo,text=" NOMS DE FAMILLE ",bg="#46B8E1",font=('arial',12,'bold'),fg="#fff")
    NOMFAM.place(x=640, y=284)
    NOMFAMentry=Entry(logo,width=10,relief=FLAT,font=('arial',14))
    NOMFAMentry.place(x=803,y=284)

    prenompere =Label(logo,text=" PRENOMS DU PERE ",bg="#46B8E1",font=('arial',12,'bold'),fg="#fff")
    prenompere.place(x=409, y=324)
    prenompereentry=Entry(logo,width=16,relief=FLAT,font=('arial',14))
    prenompereentry.place(x=685,y=322)

    prenommere =Label(logo,text=" PRENOMS ET NOMS DE LA MERE ",bg="#46B8E1",font=('arial',12,'bold'),fg="#fff")
    prenommere.place(x=409, y=372)
    prenomMereentry=Entry(logo,width=16,relief=FLAT,font=('arial',14))
    prenomMereentry.place(x=685,y=372)


    DELI =Label(logo,text=" Délivre par le juge de Paix de  ",bg="#46B8E1",font=('arial',12,'bold'),fg="#fff")
    DELI.place(x=40, y=480)
    DELIentry=Entry(logo,width=35,relief=FLAT,font=('arial',14))
    DELIentry.place(x=422,y=480)

                    
    numm =Label(logo,text=" Sous le numero",bg="#46B8E1",font=('arial',12,'bold'),fg="#fff")
    numm.place(x=40, y=515)
    nummentry=Entry(logo,width=35,relief=FLAT,font=('arial',14))
    nummentry.place(x=422,y=516)

    
    Inscrit=Label(logo,text=" Insrit le ",bg="#46B8E1",font=('arial',12,'bold'),fg="#fff")
    Inscrit.place(x=40, y=546)
    Inscritentry=Entry(logo,width=35,relief=FLAT,font=('arial',14))
    Inscritentry.place(x=422,y=549)

    Extrait=Label(logo,text=" EXTRAIT DELIVRE PAR LE CENTRE DE ",bg="#46B8E1",font=('arial',12,'bold'),fg="#fff")
    Extrait.place(x=40, y=580)
    Extraitentry=Entry(logo,width=35,relief=FLAT,font=('arial',14))
    Extraitentry.place(x=422,y=580)
   
 
    
    #BOUTTON CONNEXION
    #connexion=Button(logo,text="VALIDER",bg="green",fg="white",relief=FLAT,font=('arial',12),width=20)
    #connexion.place(x=400,y=280)
################################################################################################
#EXTRAIT DE NAISSANCE
##############
def Extrait_naissance():
    window=Tk()         
    window.title("interface")
    window.geometry("950x500+180+50")
    window.resizable(False, False)

    ##box pour ecrire ou take picture
    logo=Canvas(window,width=2950,height=5550,bg="#46B8E1")
    logo.place(x=0,y=10)

    log=Label(logo,text="Extrait de naissance",font=('arial',10,'bold'))   #46877F
    log.place(x=40,y=10)
    #BOUTTON IMPRIMER
    connexion=Button(logo,text="IMPRIMER",bg="black",fg="white",relief=FLAT,font=('arial',9),width=8,command=lambda:joke())
    connexion.place(x=798,y=10)
    

    Region = Label(logo,text="Region",bg="#46B8E1",font=('arial',12,'bold'),fg="#fff")
    Region.place(x=40, y=40)

    Departement = Label(logo,text="Departement",bg="#46B8E1",font=('arial',12,'bold'),fg="#fff")
    Departement.place(x=40, y=90)


    Arrondissement=Label(logo,text="Arrondissement",bg="#46B8E1",font=('arial',12,'bold'),fg="#fff") 
    Arrondissement.place(x=40,y=140)

    Collectivite_Locale=Label(logo,text="Collectivite Locale(commune de)",bg="#46B8E1",font=('arial',12,'bold'),fg="#fff") 
    Collectivite_Locale.place(x=40,y=190)


    
    #fields entry
    Collectivite_Localeentry=Entry(logo,width=9,relief=FLAT,font=('arial',12))
    Collectivite_Localeentry.place(x=30,y=170)

    Departemententry=Entry(logo,width=9,relief=FLAT,font=('arial',12))
    Departemententry.place(x=30,y=120)

    Regionentry=Entry(logo,width=9,relief=FLAT,font=('arial',12))
    Regionentry.place(x=30,y=70)

    Collectivite_Localeentry=Entry(logo,width=9,relief=FLAT,font=('arial',12))
    Collectivite_Localeentry.place(x=30,y=220)

######################
#....2eme box
#################
    ETAT_CIVIL=Label(logo,text="EXTRAIT DE NAISSANCE",font=('arial',14,'bold'))   #46877F
    ETAT_CIVIL.place(x=430,y=10)

    Centre_de = Label(logo,text="Centre de ",bg="#46B8E1",font=('arial',12,'bold'),fg="#fff")
    Centre_de.place(x=385, y=48)

    Centre_deentry=Entry(logo,width=9,relief=FLAT,font=('arial',12))
    Centre_deentry.place(x=480,y=49)

####################
#....3eme box
#################

    ETAT_CIVIL=Label(logo,text="INFORMATION EXTRAIT DE NAISSANCE",font=('arial',14,'bold'))   #46877F
    ETAT_CIVIL.place(x=40,y=249)

    an =Label(logo,text="Pour l'année (2)",bg="#46B8E1",font=('arial',12,'bold'),fg="#fff")
    an.place(x=40, y=284)

    anentry=Entry(logo,width=9,relief=FLAT,font=('arial',14))
    anentry.place(x=199,y=284)
    antext =Label(logo,text="(En lettre)",bg="#46B8E1",font=('arial',8),fg="#fff")
    antext.place(x=228, y=310)
    ###num registre
    num =Label(logo,text="Nº dans le Registre",bg="#46B8E1",font=('arial',12,'bold'),fg="#fff")
    num.place(x=40, y=324)

    numentry=Entry(logo,width=9,relief=FLAT,font=('arial',14))
    numentry.place(x=199,y=328)
    antext =Label(logo,text="(En lettre)",bg="#46B8E1",font=('arial',8),fg="#fff")
    antext.place(x=228, y=354)
  
#####
    date =Label(logo,text="Le",bg="#46B8E1",font=('arial',12,'bold'),fg="#fff")
    date.place(x=90, y=370)
    numentry=Entry(logo,width=18,relief=FLAT,font=('arial',14))
    numentry.place(x=199,y=372)

    datea =Label(logo,text="à",bg="#46B8E1",font=('arial',12,'bold'),fg="#fff")
    datea.place(x=90, y=404)
    dateaentry=Entry(logo,width=18,relief=FLAT,font=('arial',14))
    dateaentry.place(x=199,y=408)
    
    sex =Label(logo,text=" Un enfant de sexe ",bg="#46B8E1",font=('arial',12,'bold'),fg="#fff")
    sex.place(x=40, y=442)
    sexentry=Entry(logo,width=9,relief=FLAT,font=('arial',14))
    sexentry.place(x=200,y=442)

    PRENOM =Label(logo,text=" PRENOMS ",bg="#46B8E1",font=('arial',12,'bold'),fg="#fff")
    PRENOM.place(x=409, y=284)
    PRENOMentry=Entry(logo,width=10,relief=FLAT,font=('arial',14))
    PRENOMentry.place(x=509,y=284)

    NOMFAM =Label(logo,text=" NOMS DE FAMILLE ",bg="#46B8E1",font=('arial',12,'bold'),fg="#fff")
    NOMFAM.place(x=640, y=284)
    NOMFAMentry=Entry(logo,width=10,relief=FLAT,font=('arial',14))
    NOMFAMentry.place(x=803,y=284)

    prenompere =Label(logo,text=" PRENOMS DU PERE ",bg="#46B8E1",font=('arial',12,'bold'),fg="#fff")
    prenompere.place(x=409, y=324)
    prenompereentry=Entry(logo,width=16,relief=FLAT,font=('arial',14))
    prenompereentry.place(x=685,y=322)

    prenommere =Label(logo,text=" PRENOMS ET NOMS DE LA MERE ",bg="#46B8E1",font=('arial',12,'bold'),fg="#fff")
    prenommere.place(x=409, y=372)
    prenomMereentry=Entry(logo,width=16,relief=FLAT,font=('arial',14))
    prenomMereentry.place(x=685,y=372)


   

    
   
   
 
    
    #BOUTTON CONNEXION
    #connexion=Button(logo,text="VALIDER",bg="green",fg="white",relief=FLAT,font=('arial',12),width=20)
    #connexion.place(x=400,y=280)

def joke():
    print("PAS D ENCRE MERCI DE RECHARGER")



################################################################################################
#int 1 mariage
##############
def Certification_Mariage():
    window=Tk()         
    window.title("Certification_Mariage")
    window.geometry("950x500+180+50")
    window.resizable(False, False)

    ##box pour ecrire ou take picture
    logo=Canvas(window,width=2950,height=5550,bg="#46B8E1")
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
def joke():
    print("PAS D ENCRE MERCI DE RECHARGER")



    
window.mainloop()
Mydb=connexion()

    


            


