from tkinter import *
from tkinter import messagebox
from dao import userDao
import dashbord


window = Tk()
window.title("login au syteme")
window.geometry("950x550+180+50")
window.resizable(True, True)

#box pour ecrire ou take picture
logo = Canvas(window, width=950, height=550, bg="#46B8E1").place(x=0, y=10)
log = Label(logo, text="interface", font=('arial', 19, 'bold'))  # 46877F
log.place(x=20, y=10)

identifiant = StringVar()
mdp = StringVar()

Lidentifiant = Label(logo, text="E-mail ou telephone", bg="#46B8E1", font=('arial', 15, 'bold'), fg="#fff")
Lidentifiant.place(x=400, y=140)

Lmdp = Label(logo, text="Mot de passe", bg="#46B8E1", font=('arial', 15, 'bold'), fg="#fff")
Lmdp.place(x=430, y=200)

# fields entry
mdpentry = Entry(logo, textvariable=mdp, width=50, show="*", relief=FLAT, font=('arial', 12))
mdpentry.place(x=260, y=230)

identifiantentry = Entry(logo, textvariable=identifiant, width=50, relief=FLAT, font=('arial', 12))
identifiantentry.place(x=260, y=170)


##############
# check
##############

connexion = Button(logo, cursor="hand2", text="Se connecter",
                   bg="green", fg="white", relief=FLAT, font=('arial', 12),width=20,
                   command=lambda:popup())
connexion.place(x=400, y=280)

# mot de passe
oublie = Button(logo, text="Mot de passe oublié ?", bg="#46B8E1", fg="white", relief=FLAT, font=('arial', 12), width=20,
                )
oublie.place(x=490, y=350)


        # BOUTTON CONNEXION
def popup():
    if identifiant.get() != "" and mdp.get() != "":
        login = identifiant.get()
        password = mdp.get()
        userModel = userDao.UserDao()
        user = userModel.loginAndPasswordExist(login, password)
        if user is not None:
            window.destroy()
            dashbord.dashbord()
        else:
            messagebox.showerror("ERROR", "login ou mot de passe incorect", parent=window)
    else:
        messagebox.showerror("ERROR", "VEUILLEZ REMPLIR TOUS LES CHAMPS", parent=window)
window.mainloop()