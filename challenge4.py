#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 12:57:21 2020

@author: paysj
"""
import numpy as np
import matplotlib.pyplot as plt
#
# On prépare les trois matrices à empiler 
R = 255 * np.ones((400, 600), dtype = np.uint8)
V = 255 * np.ones((400, 600), dtype = np.uint8)
B = 255 * np.ones((400, 600), dtype = np.uint8)
# Pour l'instant, la superposition donnerait du blanc.
# On mets à 0 les 100 premières lignes de chacune des matrices

def etape1():
    #gris
    R[:600,:] = 96
    V[:600,:] = 96
    B[:600,:] = 96
    
    #bleu
    R[:,0:100] = 0
    V[:,0:100] = 0
    B[:,0:100] = 255
    
    #orange 
    #grande bar
    R[0:300,100:200] = 223
    V[0:300,100:200] =  109
    B[0:300,100:200] = 20
    #petit carré
    R[100:200,200:300] = 223
    V[100:200,200:300] =  109
    B[100:200,200:300] = 20
    
    #vert bar du haut
    R[200:300,400:600] = 0
    V[200:300,400:600] =127
    B[200:300,400:600] = 0
    #vert bar du bas
    R[300:400,300:500] = 0
    V[300:400,300:500] = 127
    B[300:400,300:500] = 0
    
    
    #
    # On empile les trois matrices
    carres = np.stack((R, V, B), axis = 2)
    
    # visualisation avec imshow
    #plt.imshow(carres)
    
    plt.imshow(carres)
    plt.show() # inutile en interactif
    
    #
    # Sauvegarde avec imsave
    plt.imsave('tetris1.png', carres)


etape1()

def etape2() :
    #gris
    R[:600,:] = 96
    V[:600,:] = 96
    B[:600,:] = 96
    
    #bleu
    R[:,0:100] = 0
    V[:,0:100] = 0
    B[:,0:100] = 255
    
    #orange 
    #grande bar
    R[100:200,100:400] = 223
    V[100:200,100:400] =  109
    B[100:200,100:400] = 20
    #petit carré
    R[200:300,200:300] = 223
    V[200:300,200:300] =  109
    B[200:300,200:300] = 20
    
    #vert bar du haut
    R[200:300,400:600] = 0
    V[200:300,400:600] =127
    B[200:300,400:600] = 0
    #vert bar du bas
    R[300:400,300:500] = 0
    V[300:400,300:500] = 127
    B[300:400,300:500] = 0
    
    
    #
    # On empile les trois matrices
    carres = np.stack((R, V, B), axis = 2)
    
    # visualisation avec imshow
    #plt.imshow(carres)
    
    plt.imshow(carres)
    plt.show() # inutile en interactif
    
    #
    # Sauvegarde avec imsave
    plt.imsave('tetris2.png', carres)
    
etape2()

def etape3() :
    #gris
    R[:600,:] = 96
    V[:600,:] = 96
    B[:600,:] = 96
        
    #bleu
    R[:,0:100] = 0
    V[:,0:100] = 0
    B[:,0:100] = 255
    #orange 
    #grande bar
    R[200:300,100:400] = 223
    V[200:300,100:400] =  109
    B[200:300,100:400] = 20
    #petit carré
    R[300:400,200:300] = 223
    V[300:400,200:300] =  109
    B[300:400,200:300] = 20
    
    #vert bar du haut
    R[200:300,400:600] = 0
    V[200:300,400:600] =127
    B[200:300,400:600] = 0
    #vert bar du bas
    R[300:400,300:500] = 0
    V[300:400,300:500] = 127
    B[300:400,300:500] = 0
    
    
    #
    # On empile les trois matrices
    carres = np.stack((R, V, B), axis = 2)
    
    # visualisation avec imshow
    #plt.imshow(carres)
    
    plt.imshow(carres)
    plt.show() # inutile en interactif
    
    #
    # Sauvegarde avec imsave
    plt.imsave('tetris3.png', carres)
    
etape3()
