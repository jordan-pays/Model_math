#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 12:18:20 2020

@author: paysj
"""

import numpy as np
import matplotlib.pyplot as plt

def etape1():
    # definition des couleurs utilisées, codées en R, V, B
    bleu = np.array([0, 0, 255], dtype = np.uint8)
    orange = np.array([237, 127, 16], dtype = np.uint8)
    vert = np.array([0, 255, 0], dtype = np.uint8)
    gris = np.array([96, 96, 96], dtype = np.uint8)
    hauteur =500 
    largeur = 1000
    
    # Initialisation de l'image. On pourrait aussi créer les 3 plans R, V, B
    # et les empiler ensuite avec la fonction stack.
    triangles = np.zeros((hauteur, largeur, 3), dtype = np.uint8)
    #
    # Création des matrices d'indices lignes et colonnes (déjà vu)
    I, J = np.meshgrid(\
                        np.arange(hauteur, dtype=np.int64),\
                        np.arange(largeur, dtype = np.int64),\
                        indexing = 'ij')
    #
    # Affectation des couleurs en respectant les conditions :
    triangles[ ((largeur/hauteur)*I <= J) &  ((largeur/hauteur)*I <= (largeur - J)) ] = bleu
    triangles[ ((largeur/hauteur)*I <= J) & ((largeur/hauteur)*I > (largeur - J)) ] = orange
    triangles[ ((largeur/hauteur)*I >= J) &  ((largeur/hauteur)*I > (largeur - J)) ] = vert
    triangles[ ((largeur/hauteur)*I >= J) &  ((largeur/hauteur)*I <= (largeur - J)) ] = gris
    #
    # Voilà le résultat :
    plt.imshow(triangles)
    plt.show() # inutile en interactif
    #
    # Ça mérite une sauvegarde :
    plt.imsave('enveloppe.png', triangles)
etape1()

def etape2():
     bleu = np.array([0, 0, 255], dtype = np.uint8)
     jaune = np.array([255, 255, 0], dtype = np.uint8)
     rouge = np.array([255, 0, 0], dtype = np.uint8)
     blanc = np.array([0, 0, 0], dtype = np.uint8)
     vert = np.array([0, 255, 0], dtype = np.uint8)
     hauteur =500 
     largeur = 1000
     
     triangles = np.zeros((hauteur, largeur, 3), dtype = np.uint8)
     
     I, J = np.meshgrid(\
                        np.arange(hauteur, dtype=np.int64),\
                        np.arange(largeur, dtype = np.int64),\
                        indexing = 'ij')
     
    triangles[ (np.cos(largeur)*I <= J) &  (np.cos(largeur)*I <= (largeur - J)) ] = bleu
    triangles[ (np.cos(9)*I <= J) & (np.cos(9)*I > (largeur - J)) ] = jaune
    triangles[ (np.cos(9)*I >= J) &  (np.cos(9)*I > (largeur - J)) ] = rouge
    triangles[ (np.cos(9)*I >= J) &  (np.cos(9)*I <= (largeur - J)) ] = blanc
    triangles[ (np.cos(9)*I >= J) &  (np.cos(9)*I <= (largeur - J)) ] = vert
    #
    # Voilà le résultat :
    plt.imshow(triangles)
    plt.show() # inutile en interactif
    #
    # Ça mérite une sauvegarde :
    plt.imsave('Seychelles.png', triangles)
etape2()