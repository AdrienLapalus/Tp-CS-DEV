"""
Header

Jeu du pendu 
Créeateur du code : Lapalus Adrien
Le 27/11/2020
ToDO:
    fonction meilleurScore
"""        
       
import random


def ListeMot():
    """ 
    Fonction permettant d'acceder au fichier contenant tous les mots
    puis de les mettre dans une liste
    """
    Mot=[]
    fic= open("ListeMot.txt","r")
    for ligne in fic :
        ligne=ligne[:-1]
        Mot.append(ligne)
    fic.close
    return Mot

def ChoisirMot(ListeMot):
    """
    Fonction permettant de Chosir un mot aléatoirement
    """
    ListeLettre=[]
    print(ListeMot)
    i = random.randint(0,len(ListeMot)-1)
    Mot=ListeMot[i]
    ListeLettre.append(Mot[0])
    return Mot,ListeLettre



def CreationMot(Mot,ListeLettre):
    """
    Fonction créant une liste avec des tirets pour les lettres non trouvé 
    et les lettres trouvées du mot chosi
    """
    AffichMot=[]
    for lettre in Mot:
            if lettre in ListeLettre:
                AffichMot.append(lettre)
            else:
                AffichMot.append("_")
    return  AffichMot           



def AfficherMot(AffichMot):
    """
    Affiche le mot
    """
    for l in AffichMot:
        print(l , end = " ")
    print("")    

def DemanderLettre(Mot,ListeLettre,chance,LettreDonnee):
    """
    Fonction permettant de demander un lettre à l'utilisateur 
    et de la comparer au mot choisi puis de l'afficher si il est bonne 
    ou d'enlever une vie si elle n'est pas bonne
    """
    Lettre=input("Lettre choisie ?")
    Lettre=Lettre.lower()
    if Lettredonnee(LettreDonnee,Lettre) == True:      
        if VerifLettre(Lettre) == True:
            if Lettre in Mot:
                ListeLettre.append(Lettre)
                AffichMot = CreationMot(Mot,ListeLettre)
                AfficherMot(AffichMot) 
            else:
                print("Votre lettre n'est pas dans le mot")
                chance-=1
               
    return chance


def VerifLettre(L):
    """
    Verfie si la variable est bien une lettre
    """
    if len(L) == 1 and L.isalpha():
        return True
    else :
        print("erreur")
        DemanderLettre(Mot,ListeLettre,chance,LettreDonnee)


def Victoire(Mot,ListeLettre):
    """
    Regarde si toutes les lettres du mot ont été trouvées
    """
    Vict =[]
    for l in Mot:
        if l not in Vict :
            Vict.append(l)
    if len(Vict) == len(ListeLettre):
        print("Mot trouvé !!")
        return True   
    else:
        return False
            
def Defaite(chance):
    """
    Regarde si le nombre de chance n'est pas tombé à 0
    """
    if chance > 0:
        print("Il vous reste ",chance," chance")
        return False
    else:
        print("Vous n'avez plus de chance disponible")
        print("Vous avez perdu...")
        return True

def Lettredonnee(LettreDonnée,Lettre):
    """
    verfie si la lettre choisie n'a pas déja et donnée
    """
    if Lettre not in LettreDonnée:
        LettreDonnée.append(Lettre)
        return True
    else:
        print("Vous avez déjà donné cette lettre")
        DemanderLettre(Mot,ListeLettre,chance,LettreDonnee)

def Rejouer():
    """
    Demande a l'utilisateur s'il veut rejouer
    """
    Choix = input("Voulez vous rejouer ?")
    if Choix == "oui":
        return True
    else:
        return False
        
def MeilleurScore(chance):
    """
    Fonction permettant de donner le meilleur score
    """
    fic=open("MeilleurScore.txt","r")
    for ligne in fic:
        Best = int(ligne)
    fic.close
    print(Best)
    fic=open("MeilleurScore.txt","w")
    if Best<=chance:
        fic.write(str(Best))
    fic.close
    fic=open("MeilleurScore.txt","r")
    print(Best)
    for ligne in fic:   
        print("Votre meilleur score est de ",ligne)
    fic.close



ListeMot=ListeMot()
while Rejouer() == True:
    chance = 8     
    LettreDonnee=[]  
    Mot,ListeLettre=ChoisirMot(ListeMot)
    AffichMot=CreationMot(Mot,ListeLettre)
    AfficherMot(AffichMot)
    while Defaite(chance) == False and Victoire(Mot,ListeLettre) == False :
        chance = DemanderLettre(Mot,ListeLettre,chance,LettreDonnee)
    MeilleurScore(chance)    

