from copy import deepcopy
def creer_pile():
    pile=[]
    return pile

def empiler(p,x):
    p.append(x)
    
def depiler(p):
    element=p[len(p)-1]
    p.pop()
    return element

def reverse_pile(s):
    rs=creer_pile()
    if len(s)!=0:
        #Attention ici à la copie ou au pointeur
        #sc=s[:] ou
        sc=deepcopy(s)
        for i in range(len(sc)):
            elt=depiler(sc)
            empiler(rs,elt)
    return rs

def permut_circ_pile(s,n):
    if len(s)!=0 and n!=0:
        sc=deepcopy(s)
        P1=creer_pile()
        P2=creer_pile()
        if n>len(s):
            n=n-len(s)
        for loop in range(n):
            empiler(P1, depiler(s))
        for loop in range(len(sc)-n):
            empiler(P2, depiler(s))
        for loop in range (n):
            empiler(s,depiler(P1))
        for loop in range (len(sc)-n):
            empiler(s,depiler(P2))
    return s
