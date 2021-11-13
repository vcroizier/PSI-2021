# coding: utf-8

#
# TP d'info n°2 - Manipulation des images.
#

#
# 1) Très court aperçu du type ARRAY de Numpy.
#    a) Construction d'un ARRAY.
#
##
#%%

import numpy as np
##
#%%
a = np.array([[1,2],[3,4],[5,6]])
print(a)
##
#%%
print(a.shape)
n,p = a.shape
print(n)
print(p)
##
#%%
b = np.zeros((2,5))
print(b)
##
#%%
#
#    b) Accéder et modifier les éléments d'un ARRAY.
#

print(a)
print('a[1]    donne',a[1])
print('a[1][0] donne',a[1][0])
print('a[1,0]  donne',a[1,0])
print('a[1,:]  donne',a[1,:])
print('a[:,1]  donne',a[:,1])
##
#%%
a[1,0]=30
print(a)
##
#%%
a[1,:]=[8,9]
print(a)
##
#%%
a[:,1]=[-1,-2,-3]
print(a)
