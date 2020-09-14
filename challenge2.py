#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 12:16:58 2020

@author: paysj
"""
import matplotlib.pyplot as plt
knight = plt.imread('/home/ann2/paysj/Model_math/dark-knight.png', 'PNG')
import numpy as np
knight2= knight[::-1,:]
plt.imshow(knight2)
 knight3= np.concatenate((knight,knight2))
 plt.imshow(knight3)
 knight4= np.concatenate((knight3,knight3),axis=1)
plt.imshow(knight4)

