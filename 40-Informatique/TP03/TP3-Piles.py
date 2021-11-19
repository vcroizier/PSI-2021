#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#==============================================================================
# Fonctions de base
#==============================================================================

def pile_vide():
    return []

def est_vide(L):
    return L==[]

def depiler(L):
    L.pop()
    
def empiler(L,a):
    L.append(a)

def taille(L):
    return len(L)

def sommet(L):
    return L[taille(L)-1]
       
#==============================================================================
# Pour se chauffer
#==============================================================================

def Poulidor(L):
    depiler(L)
    return sommet(L)

def Poulidor2(L):
    a=sommet(L)
    depiler(L)
    b=sommet(L)
    empiler(L,a)
    return b

def Inv(L):
    P=pile_vide()
    while taille(L)>0:
        a=sommet(L)
        depiler(L)
        empiler(P,a)
    return P

def Copie(L):
    P=pile_vide()
    N=pile_vide()
    while taille(L)>0:
        a=sommet(L)
        depiler(L)
        empiler(P,a)
    while taille(P)>0:
        a=sommet(P)
        depiler(P)
        empiler(L,a)
        empiler(N,a)
    return N

def Inv2(L):
    N=Copie(L)
    return Inv(N)

#==============================================================================
# Expressions bien parenthésées
#==============================================================================
    
def Par(L):
    P=pile_vide()
    for c in L:
        if c=='(':
            empiler(P,c)
        if c==')':
            if taille(P)>0:
                depiler(P)
            else:
                return False
    if taille(P)>0:
        return False
    return True

#==============================================================================
# Permutation circulaire d'une pile
#==============================================================================
        
def Perm(W,k):
    P=Copie(W)
    n=k%taille(P)
    L=pile_vide()
    N=pile_vide()
    for i in range(n):
        a=sommet(P)
        depiler(P)
        empiler(L,a)
    while taille(P)>0:
        a=sommet(P)
        depiler(P)
        empiler(N,a)
    T=pile_vide()
    while taille(L)>0:
        a=sommet(L)
        depiler(L)
        empiler(T,a)
    while taille(N)>0:
        a=sommet(N)
        depiler(N)
        empiler(T,a)
    return T
    
        