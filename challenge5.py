# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 04:44:24 2020

@author: paysd
"""
import numpy as np
import matplotlib.pyplot as plt
#
# On prépare les trois matrices à empiler 
R = 255 * np.ones((100, 100), dtype = np.uint8)
V = 255 * np.ones((100, 100), dtype = np.uint8)
B = 255 * np.ones((100, 100), dtype = np.uint8)
#
# Pour l'instant, la superposition donnerait du blanc.
# On mets à 0 les 100 premières lignes de chacune des matrices
R[:100, :] = 250
V[:100, :] = 109
B[:100, :] = 20
#
# On empile les trois matrices
carres = np.stack((R, V, B), axis = 2)
#
# visualisation avec imshow
plt.imshow(carres)
plt.show() # inutile en interactif
#
# Sauvegarde avec imsave
plt.imsave('envellope.png', carres)