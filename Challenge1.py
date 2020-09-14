# -*- coding: utf-8 -*-
"""
Éditeur de Spyder
Ceci est un script temporaire.
"""
import matplotlib.pyplot as plt
knight = plt.imread('/home/ann2/paysj/Model_math/dark-knight.png', 'PNG')
import numpy as np
knight2 = np.concatenate((knight,knight))
plt.imshow(knight2)
knight3= np.concatenate((knight,knight),axis=1)
plt.imshow(knight3)
knight4=np.concatenate((knight3,knight3))
plt.imshow(knight4)