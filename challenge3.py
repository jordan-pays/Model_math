#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 12:29:13 2020

@author: paysj
"""
import numpy as np
import matplotlib.pyplot as plt
#
# On prépare les trois matrices à empiler 
R = 255 * np.ones((100, 100), dtype = np.uint8)
V = 255 * np.ones((100, 100), dtype = np.uint8)
B = 255 * np.ones((100, 100), dtype = np.uint8)
# Pour l'instant, la superposition donnerait du blanc.
# On mets à 0 les 100 premières lignes de chacune des matrices

R[:100,:] = 223
V[:100,:] = 109
B[:100,:] = 20

R[80:100,80:100] = 0
V[80:100,80:100] = 127
B[80:100,80:100] = 0

#
# On empile les trois matrices
carres = np.stack((R, V, B), axis = 2)

# visualisation avec imshow
#plt.imshow(carres)

carres2= carres[::-1,:]
carres3=np.concatenate((carres,carres2))
carres4=carres3[:,::-1]
carres5=np.concatenate((carres3,carres4),axis=1)
carres6=np.concatenate((carres5,carres5))
carres7=np.concatenate((carres6,carres6,carres6),axis=1)
plt.imshow(carres7)
plt.show() # inutile en interactif

#
# Sauvegarde avec imsave
plt.imsave('carres.png', carres7)
           
