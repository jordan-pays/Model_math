# -*- coding: utf-8 -*-
"""
Éditeur de Spyder
Ceci est un script temporaire.
"""
import matplotlib.pyplot as plt
knight = plt.imread('./dark-knight.png', 'PNG')
import numpy as np

def etape1(): 
    knight1 = np.concatenate((knight,knight))
    plt.imshow(knight1)
    plt.show()
    plt.imsave('KnihtVerticale.png', knight1)
etape1()

def etape2() :
    knight1= np.concatenate((knight,knight),axis=1)
    plt.imshow(knight1)
    plt.show()
    plt.imsave('KnightHorizontale.png', knight1)
etape2()

def etape3():
    knight1= np.concatenate((knight,knight),axis=1)
    knight2=np.concatenate((knight1,knight1))
    plt.imshow(knight2)
    plt.show()
    plt.imsave('4Kngiht.png', knight2)
etape3()