"""
Interface Graphique du pendu


Créeateur du code : Lapalus Adrien
Le 11/12/2020
ToDO:
    écran victoire/defaite
    
"""        
from tkinter import Tk, Label, Button, Entry, StringVar, messagebox
from tkinter import Canvas, PhotoImage
import random


chance = 8 

def ListeMot():
    """ 
    Fonction permettant d'acceder au fichier contenant tous les mots
    puis de les mettre dans une liste
    """
    Mots=[]
    fic= open("ListeMot.txt","r")
    for ligne in fic :
        ligne=ligne[:-1]
        Mots.append(ligne)
    fic.close
    return Mots

def ChoisirMot(ListeMot):
    """
    Fonction permettant de Chosir un mot aléatoirement
    """
    ListeLettre=[]
    i = random.randint(0,len(ListeMot)-1)
    Mot=ListeMot[i]
    ListeLettre.append(Mot[0])
    return Mot,ListeLettre



def CreationMot(Mot,ListeLettre):
    """
    Fonction permettant d'afficher le mot avec des tirets pour les lettres non trouvé 
    et les lettres trouvées
    """
    global mot
    mot.set("")
    AffichMot=""
    for lettre in Mot:
            if lettre in ListeLettre:
                AffichMot = AffichMot + lettre
            else:
                AffichMot = AffichMot + "-"            
    mot.set(AffichMot)        
              




def TraitementLettre(Lettre,Mot,ListeLettre,chance,LettreDonnee):
    """
    Fonction permettant de comparer la lettre au mot choisi puis de l'afficher si il est bonne 
    ou d'enlever une vie si elle n'est pas bonne
    """
    global lettre
    Lettre=Lettre.lower()
    if Lettredonnee(LettreDonnee,ListeLettre) == True:      
        if Lettre in Mot:
            ListeLettre.append(Lettre)
            print(ListeLettre)
            CreationMot(Mot,ListeLettre)
            lettre.set("")
            Victoire(Mot,ListeLettre)
        else:
            messagebox.showwarning('Dommage','Votre lettre n est pas dans le mot')
            lettre.set("")
            Perdu()
    
     
    


def VerifLettre(Mot,ListeLettre,chance,LettreDonnee):
    """
    Verfie si la variable est bien une lettre
    """
    if len(lettre.get()) == 1 and lettre.get().isalpha():
        TraitementLettre(lettre.get(),Mot,ListeLettre,chance,LettreDonnee)
    else :
        messagebox.showwarning('Attention','Vous n avez pas rentrer un lettre\n Veuillez recommencer')
        lettre.set("")


def Victoire(Mot,ListeLettre):
    """
    Regarde si toutes les lettres du mot ont été trouvées puis affiche une fenètre
    (la fenètre n'est pas fonctionnel)
    """
    Vict =[]
    for l in Mot:
        if l not in Vict :
            Vict.append(l)
    if len(Vict) == len(ListeLettre):
        print("Mot trouvé !!")
        Gagner = Tk()
        TexteGagne = Label(Gagner, text = "Bravo vous avez trouvé le mot\nVous avez gagné")
        Rejouer = Label(Gagner, text = "Rejouer ?")
        BoutonQ = Button(Gagner, text="Quitter",command = Fermer(Gagner))
        
        TexteGagne.grid(row = 1,column=1,columnspan=1)
        Rejouer.grid(row=2,column=1)
        BoutonQ.grid(row=3,column=2)
        
        Gagner.mainloop()
              
    else:
        return False
            


def Lettredonnee(LettreDonnée,ListeLettre):
    """
    verfie si la lettre choisie n'a pas déja et donnée
    """
    print("Lettre donnée : ",LettreDonnée)
    if lettre.get() not in LettreDonnée:
        LettreDonnée.append(lettre.get())
        return True
    else:
        messagebox.showwarning('Attention',"Vous avez déjà donné cette lettre\nVeuillez redonner une lettre")
        lettre.set('')

def Rejouer():
    """
    Demande a l'utilisateur s'il veut rejouer
    """
    Choix = input("Voulez vous rejouer ?")
    if Choix == "oui":
        return True
    else:
        return False
        

def Perdu():
    """
    Fonction permettant de changer l'image si le jouer s'est trompé de lettre
    puis si le joueur n'as plus de vie créer une nouvelle fenetre pour lui demander s'il
    veut rejouer (la fenètre n'est pas fonctionnel)
    """
    global chance
    chance-=1
    if chance >0 :
        Image = PhotoImage(file = "bonhomme" + str(chance) + ".gif")
        print(Image)
        can1.itemconfigure(item, image=Image)
        can1.image = Image
    else:
        Perdu = Tk()
        TextePerdu = Label(Perdu, text = "Vous n avez plus de chance\nVous avez perdu")
        Rejouer = Label(Perdu, text = "Rejouer ?")
        BoutonQ = Button(Perdu, text="Quitter",command = Fermer(Perdu))
        
        TextePerdu.grid(row = 1,column=1,columnspan=1)
        Rejouer.grid(row=2,column=1)
        BoutonQ.grid(row=3,column=2)
        
        Perdu.mainloop()
        

def Fermer(fenetre):
    """
    fonction pour fermer les fenetre lorsque le joueuer veut arretter de jouer
    """
    fenetre.destroy
    Fen.destroy      
            
    
    

#ListeMot=ListeMot()
#while Rejouer() == True:
#    chance = 8     
#    LettreDonnee=[]  
#    Mot,ListeLettre=ChoisirMot(ListeMot)
#    AffichMot=CreationMot(Mot,ListeLettre)
#    AfficherMot(AffichMot)
#    while Defaite(chance) == False and Victoire(Mot,ListeLettre) == False :
#        chance = DemanderLettre(Mot,ListeLettre,chance,LettreDonnee)
#    MeilleurScore(chance)


   
ListeMot=ListeMot()

   
LettreDonnee=[]  
Mot,ListeLettre=ChoisirMot(ListeMot)


Fen = Tk()
Texte = Label(Fen, text="Proposer une lettre")

lettre = StringVar()
ProposerLettre = Entry(Fen, bd = 5, textvariable = lettre)


mot=StringVar()
CreationMot(Mot,ListeLettre)
MotAfficher = Label(Fen, textvariable = mot)

BoutonProposer = Button(Fen, text = 'Proposer', command =lambda : VerifLettre(Mot,ListeLettre,chance,LettreDonnee))


can1 = Canvas(Fen, width = 300 , height = 300)
photo = PhotoImage(file = "bonhomme8.gif")
item = can1.create_image(0,0, anchor ='nw', image=photo)


BoutonProposer.grid(row = 2, column = 2, sticky = 'E')
ProposerLettre.grid(row = 2, column = 1, sticky = 'W')
Texte.grid(row = 3, column = 1, sticky ='N')
MotAfficher.grid(row=1,rowspan=1,column=1,columnspan=1)
can1.grid(row=1, column= 3, rowspan = 4)

Fen.mainloop()
