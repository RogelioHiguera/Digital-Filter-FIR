# -*- coding: utf-8 -*-
"""
Created on Sat May  4 18:46:21 2019
FIR (ventana Kaiser)
Tecnológico Nacional de México
Tecnológico de Estudios Superiores de Ixtapaluca
División de Ingeniería Electrónica
@author: M. en C. Rogelio Manuel Higuera Gonzalez
"""
import numpy as np
import matplotlib.pyplot as plt 
from scipy import signal
from scipy.fftpack import fft, fftshift
window1 = signal.kaiser(51, beta=0)
window2 = signal.kaiser(51, beta=5)
window3 = signal.kaiser(51, beta=6)
window4 = signal.kaiser(51, beta=8.6)
window5 = signal.kaiser(51, beta=14)
A1 = fft(window1, 2048) / (len(window1)/2.0)
A2 = fft(window2, 2048) / (len(window2)/2.0)
A3 = fft(window3, 2048) / (len(window3)/2.0)
A4 = fft(window4, 2048) / (len(window4)/2.0)
A5 = fft(window5, 2048) / (len(window5)/2.0)
response1 = 20 * np.log10(np.abs(fftshift(A1 / abs(A1).max())))
response2 = 20 * np.log10(np.abs(fftshift(A2 / abs(A2).max())))
response3 = 20 * np.log10(np.abs(fftshift(A3 / abs(A3).max())))
response4 = 20 * np.log10(np.abs(fftshift(A4 / abs(A4).max())))
response5 = 20 * np.log10(np.abs(fftshift(A5 / abs(A5).max())))
freq = np.linspace(-0.5, 0.5, len(A1))
fig,axes=plt.subplots()
axes.plot(window1,label='Beta=0')
axes.plot(window2,label='Beta=5')
axes.plot(window3,label='Beta=6')
axes.plot(window4,label='Beta=8.6')
axes.plot(window5,label='Bata=14')
axes.set_ylabel('Amplitude')
axes.set_xlabel('Sample')
plt.legend(bbox_to_anchor=(0.35,0.45),loc=2,borderaxespad=0.1)
plt.grid(True)
plt.savefig('ventanak1.eps',dpi=1000,bbox_inches='tight')
fig,axes1=plt.subplots()
axes1.plot(freq,response1,label='Beta=0')
axes1.plot(freq,response2,label='Beta=5')
axes1.plot(freq,response3,label='Beta=6')
axes1.plot(freq,response4,label='Beta=8.6')
axes1.plot(freq,response5,label='Beta=14')
axes1.set_ylabel('Normalized magnitude [dB]')
axes1.set_xlabel('Normalized frequency [cycles per sample]')
axes1.set_ylim([-220,1])
plt.legend(bbox_to_anchor=(0.38,0.31),loc=2,borderaxespad=0.1)
plt.grid(True)
plt.savefig('ventanak2.eps',dpi=1000,bbox_inches='tight')

