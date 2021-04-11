from copy import deepcopy
from Pile import *

#definition d'une fonction pour récupérer les parenthèses
def analyseur(exp):
    #Conversion de l'expression entrée en liste
    list_exp=[i for i in exp]
    #Création de listes pour répertorier les parenthèses, ainsi que leurs indexs en fonction de si elles sont
    #ouvrantes (=Ipo) ou fermantes (=Ipf)
    parenthèses=[]
    Ipo=[]
    Ipf=[]
    #Récupération des parenthèses et leurs indexs
    for k in range (len(list_exp)) :
        if list_exp[k]=="(":
            parenthèses.append(list_exp[k])
            Ipo.append(k)
        if list_exp[k]==")":
            parenthèses.append(list_exp[k])
            Ipf.append(k)
    #Création de piles et inversions des listes de parenthèses et de leurs indexs
    P0=creer_pile()
    Pi=creer_pile()
    parenthèses=reverse_pile(parenthèses)
    Ipo=reverse_pile(Ipo)
    Ipf=reverse_pile(Ipf)
    a_couple=[]
    #Désempilage des listes de parenthèses et indexs et empilage dans deux piles, une pour les parenthèses
    #et l'autre pour leurs indexs respectifs.
    while len(parenthèses)!=0:
        empiler(P0,depiler(parenthèses))
        #Si la parenthèse est ouvrante, on cherche son index dans la liste "Ipo"
        if P0[(len(P0)-1)]=="(":
            empiler(Pi,depiler(Ipo))
        #Si la parenthèse est fermante, on cherche son index dans la liste "Ipf"
        elif P0[(len(P0)-1)]==")":
            empiler(Pi,depiler(Ipf))
            #On vérifie si la parenthèse avant dans la pile est ouvrante
            if P0[(len(P0)-2)]=="(":
                couple=[]
                #Si la parenthèse est ouvrante, on dépile celle-ci en plus de la dernière parenthèse de P0
                #et on ajoute leurs index+1 donc leurs places à une liste de couples de parenthèses
                for loop in range (2):
                    depiler(P0)
                    couple.append(depiler(Pi)+1)
                couple=reverse_pile(couple)
                a_couple.append(str(couple))
    Pnf=[]
    #Transforme la liste de couples en chaine de caractère
    strA_couple="".join(a_couple)
    #Si la liste d'index n'est pas vide, donc qu'il reste une parenthèse non fermée, on retourne son index+1 donc sa place
    if len(Pi)!=0:
        if len(Pi)==1:
            Pi=Pi[0]+1
            print("L'expression est incorrecte, la parenthèse non-fermée est la parenthèse à la place",Pi,", les couples de parenthèses sont : ",strA_couple)
        elif len(Pi)>1:
            for i in range (len(Pi)):
                Pnf.append(str((Pi[i])+1))
            strPnf=", ".join(Pnf)
            print("L'expression est incorrecte, les parenthèses non-fermées sont les parenthèses aux places",strPnf,"les couples de parenthèses sont : ",strA_couple)
    else:    
        print("L'expression est correcte, les parenthèses sont toutes fermées et les couples de parenthèses sont : ",strA_couple)
    
    return
    
exp=str(input("Insérez une expression à analyser : "))
analyseur(exp)
