#
# TP d'info n°2 - Manipulation des images.
#

# ! ATTENTION : modifier le chemin ci-dessous pour qu'il corresponde
# !             à l'emplacement des fichiers images du TP.
##
#%%
path = "H:/Informatique/TP2-2021"

#
# 2) Traitement des images.
#    a) Les bases de la manipulation d'images.
#

# Changement de répertoire de travail :
import os
os.chdir(path)

# Chargement des librairies nécessaires au TP :
import numpy as np
import matplotlib.image as img
import matplotlib.pyplot as plt
##
#%%
# Chargement du fichier image :
A = img.imread("Chloroplastes.png")
# Enregistrement de l'image dans un fichier :
img.imsave("Chloroplastes_bis.png",A)
# Affichage de l'image :
plt.imshow(A, interpolation='none')
plt.show()
##
#%%
print(type(A))
n,p,c=A.shape
print((n,p,c))
print(A[10,40])
##
#%%
A=np.array([[ [0,0,0] , [0.5,0.5,0.5] , [1,1,1] ]
           ,[ [0,0,0.5] , [0,0.5,0.5] , [0,0.5,0]]])

plt.imshow(A,interpolation='none')
plt.show()
##
#%%
# +------------+
# | Exercice 1 |
# +------------+
def nbconvert(image,seuil) :
    """ Convertit l'image en noir et blanc selon le seuil.
    """
    n,p,c = image.shape
    resultat = np.zeros((n,p,c))

    # *** A compléter ***
        
    return(resultat)

# Test
A = img.imread("Chloroplastes.png")
B = nbconvert(A , 1.5)
plt.imshow(B, interpolation='none')
plt.show()
img.imsave("Chloroplastes_NB.png",B)
##
#%%
# +------------+
# | Exercice 2 |
# +------------+



# Test
A = img.imread("Chloroplastes.png")
B = ngconvert(A)
plt.imshow(B, interpolation='none')
plt.show()
img.imsave("Chloroplastes_gris.png",B)
##
#%%
# +------------+
# | Exercice 3 |
# +------------+
def filtre_bleu(image) :
    """ Redonne l'image après lui avoir appliqué un filtre bleu.
    """
    n,p,c = image.shape
    resultat = np.zeros((n,p,c))

    # *** A compléter ***
        
    return(resultat)
# Test
A = img.imread("Chloroplastes.png")
B = filtre_bleu(A)
plt.imshow(B, interpolation='none')
plt.show()
##
#%%
# +------------+
# | Exercice 4 |
# +------------+



# Test
A = img.imread("Chloroplastes.png")
# négatif
B = negatif(A)
plt.imshow(B, interpolation='none')
plt.show()
# négatif du négatif
C = negatif(B)
plt.imshow(C, interpolation='none')
plt.show()
##
#%%
# +------------+
# | Exercice 5 |
# +------------+



# Test
A = img.imread("Chloroplastes.png")
# effet miroir
B = miroir(A)
plt.imshow(B, interpolation='none')
plt.show()
##
#%%



# Test
A = img.imread("Chloroplastes.png")
# une rotation
B = rotation(A)
plt.imshow(B, interpolation='none')
plt.show()
# deuxième rotation
C = rotation(B)
plt.imshow(C, interpolation='none')
plt.show()
##
#%%
# +------------+
# | Exercice 6 |
# +------------+



# Test
A = img.imread("Chloroplastes.png")
# Foncer
B = luminosite(A,0.5)
plt.imshow(B, interpolation='none')
plt.show()
#Eclaircir
C = luminosite(A,2)
plt.imshow(C, interpolation='none')
plt.show()
##
#%%




# Test
A = img.imread("Chloroplastes.png")
# Diminuer le contraste
B = contraste(A,0.5)
plt.imshow(B, interpolation='none')
plt.show()
#E Augmenter le contraste
C = contraste(A,2)
plt.imshow(C, interpolation='none')
plt.show()
##
#%%
# +------------+
# | Exercice 7 |
# +------------+

from math import floor
#exemple d'usage de floor :
floor(2.72)
##
#%%



# Test
A = img.imread("Chloroplastes.png")
# réduction coeff 2
B = reduire(A,2)
plt.imshow(B, interpolation='none')
plt.show()
# réduction coeff 5
C = reduire(A,5)
plt.imshow(C, interpolation='none')
plt.show()
##
#%%
# +------------+
# | Exercice 8 |
# +------------+



# Test
A = img.imread("Chloroplastes.png")
# agrandir coeff 2
B = agrandir(A,2)
plt.imshow(B, interpolation='none')
plt.show()
# agrandir coeff 3
C = agrandir(A,3)
plt.imshow(C, interpolation='none')
plt.show()
##
#%%
# +------------+
# | Exercice 9 |
# +------------+



# Test
A = img.imread("Chloroplastes.png")
# flouter
B = flou(A)
plt.imshow(B, interpolation='none')
plt.show()
# flouter 10 fois
for k in range(9):
    B = flou(B)
plt.imshow(B, interpolation='none')
plt.show()
##
#%%
# +-------------+
# | Exercice 10 |
# +-------------+



# Test
A = img.imread("Chloroplastes.png")
# détection de contours
B = contour(A,1) # le coefficient est à ajuster
plt.imshow(B, interpolation='none')
plt.show()

