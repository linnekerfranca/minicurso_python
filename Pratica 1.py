#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 11:31:18 2017

@author: labsim
"""
#Importar bibliotecas
import numpy as np
import matplotlib.pyplot as plt

#Definir variaveis
i1,i2 = 0.8,0.3

theta = np.linspace(-10,10,1000)

L11 = (3 + np.cos(2*theta))*10e-3
L22 = 0.3*np.cos(theta)
L12 = (30+10*np.cos(2*theta))

#Operaçoes
w = 0.5*L11*i1**2 + L12*i1*i2 + 0.5*L22*i2**2

T_total = np.diff(w)                                    #Funçao para derivar

w_relutancia = 0.5*L11*i1**2 + 0.5*L22*i2**2
w_mutuo = L12*i1*i2

T_r = np.diff(w_relutancia)
T_m = np.diff(w_mutuo)

#Plotagem 

plt.figure(1,[10,7])
plt.subplot(311)
plt.plot(theta[0:len(theta)-1],T_total, 'r')
plt.title("Torque Total")
plt.ylabel("Torque [N*m]")
plt.xlabel("$\Theta$ [Radianos]")
plt.grid()

plt.subplot(312)
plt.plot(theta[0:len(theta)-1],T_r, 'g')
plt.title("Torque de Relutancia")
plt.ylabel("Torque [N*m]")
plt.xlabel("$\Theta$ [Radianos]")
plt.grid()

plt.subplot(313)
plt.plot(theta[0:len(theta)-1],T_m, 'b')
plt.title("Torque Mutuo")
plt.ylabel("Torque [N*m]")
plt.xlabel("$\Theta$ [Radianos]")
plt.grid()

plt.tight_layout()
plt.show()                                              #Mostrar grafico
