##!/usr/bin/env python3
## -*- coding: utf-8 -*-
#"""
#Created on Mon Sep 10 20:50:22 2018
#
#@author: maximebailleul
#"""
#
#def ligne_complete(L,i):
#    ligne=L[i]
#    for k in range(1,10):
#        if k not in ligne:
#    	    return False
#    return True 
#
#def colonne_complete(L,j):
#    colonne=[L[i][j] for i in range(9)]
#    for i in range(0,9):
#        if i not in colonne:
#    	    return False
#    return True 
#
#def ligne(L,i):
#    chiffre =[]
#    for j in L[i]:
#        if (j not in chiffre) and j!=0:
#            chiffre.append(j)
#    return chiffre
#
#def colonne(L,j):
#    chiffre =[]
#    M=colonne=[L[i][j] for i in range(9)]
#    for j in M:
#        if (j not in chiffre) and j!=0:
#            chiffre.append(j)
#    return chiffre
#
#def carre(L,i,j):
#    icoin =3*(i//3)
#    jcoin =3*(j//3)
#    chiffre=[]
#    for i in range(icoin,icoin+3):
#        for j in range(jcoin,jcoin+3):
#            if (L[i][j] not in chiffre) and (L[i][j]!=0):
#                chiffre.append(L[i][j]) 
#    return chiffre
#
#def conflit(L,i,j):
#    return ligne(L,i)+colonne(L,j)+carre(L,i,j)
#
#def chiffres_ok(L,i,j):
#    ok=[]
#    conflits=conflit(L,i,j)
#    for k in range(1,10):
#        if k not in conflits:
#            ok.append(k)
#    return ok
#
#def nb_possibles(L,i,j):
#    return len(chiffres_ok(L,i,j))
#
#def liste_zero(L):
#    return [[i,j] for i in range(0,9) for j in range(0,9) if L[i][j]==0]
#
#def un_tour(L):
#    changement=False
#    for i in range(0,9):
#        for j in range(0,9):
#            if (L[i][j] == 0):
#                if (nb_possibles(L,i,j) == 1):
#                    L[i][j] = chiffres_ok(L,i,j)[0]
#                    changement=True
#    return changement
#
#def remplir(L,Lvide,k):
#    [i,j]=Lvide[k]
#    chiffre=L[i][j]+1
#    while chiffre not in chiffres_ok(L,i,j) and chiffre<10:
#        chiffre=chiffre+1
#    return chiffre 
#
#def complete(L):
#    bool=un_tour(L)
#    while bool:
#        bool=un_tour(L)
#    return L
#
#def resolution(L):
#    Lvide=liste_zero(L)
#    n=len(Lvide)
#    k=0
#    while k>=0 and k<n:
#        [i,j]=Lvide[k] 
#        chiffre=remplir(L,Lvide,k)
#        if chiffre==10:
#            k=k-1
#            L[i][j]=0
#        else:
#            L[i][j]=chiffre
#            k=k+1
#    return L 

M='maths'
P='physique'
C=''
for j in L:
    if j in P:
        C=j+C
        
def carre_complet(L,i):
    
        

    
        
        
    