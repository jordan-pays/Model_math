#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 12:16:58 2020

@author: paysj
"""
import matplotlib.pyplot as plt
knight = plt.imread('./dark-knight.png', 'PNG')
import numpy as np

def etape1():
    knight1= knight[::-1,:]
    plt.imshow(knight1)
    plt.show()
    plt.imsave('KnihtInverser.png', knight1)
etape1()

def etape2():
     knight1= np.concatenate((knight,knight[::-1,:]))
     plt.imshow(knight1)
     plt.show()
     plt.imsave('KnihtVerticaleInverser.png', knight1)
etape2()

def etape3():
    knight1= np.concatenate((knight,knight[::-1,:]))
    knight2= np.concatenate((knight1,knight1),axis=1)
    plt.imshow(knight2)
    plt.show()
    plt.imsave('4KnihtInverser.png', knight2)
etape3()

