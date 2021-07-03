from tkinter import*
#import tkinter as tkinter
from tkinter import messagebox

def etat_civil():
    window=Tk()         
    window.title("interface")
    window.geometry("950x700+180+50")
    window.resizable(False, False)

    ##box pour ecrire ou take picture
    logo=Canvas(window,width=2950,height=5550,bg="#46B8E1")
    logo.place(x=0,y=10)

    log=Label(logo,text="Redefine mdp",font=('arial',10,'bold'))   #46877F
    log.place(x=40,y=10)
    

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
etat_civil()
