# -*- coding: utf-8 -*-
"""
Created on Sat May  4 13:55:56 2019
FIR (ventanas frecuencia)
Tecnológico Nacional de México
Tecnológico de Estudios Superiores de Ixtapaluca
División de Ingeniería Electrónica
@author: M. en C. Rogelio Manuel Higuera Gonzalez
"""
from scipy import signal
from scipy.fftpack import fft, fftshift
import matplotlib.pyplot as plt
import numpy as np
window1 = signal.barthann(51)
window2 = signal.bartlett(51)
window3 = signal.blackman(51)
window4 = signal.bohman(51)
window5 = signal.hanning(51)
window6 = signal.tukey(51)
A1 = fft(window1, 2048) / (len(window1)/2.0)
A2 = fft(window2, 2048) / (len(window2)/2.0)
A3 = fft(window3, 2048) / (len(window3)/2.0)
A4 = fft(window4, 2048) / (len(window4)/2.0)
A5 = fft(window5, 2048) / (len(window5)/2.0)
A6 = fft(window6, 2048) / (len(window6)/2.0)
response1 = 20 * np.log10(np.abs(fftshift(A1 / abs(A1).max())))
response2 = 20 * np.log10(np.abs(fftshift(A2 / abs(A2).max())))
response3 = 20 * np.log10(np.abs(fftshift(A3 / abs(A3).max())))
response4 = 20 * np.log10(np.abs(fftshift(A4 / abs(A4).max())))
response5 = 20 * np.log10(np.abs(fftshift(A5 / abs(A5).max())))
response6 = 20 * np.log10(np.abs(fftshift(A6 / abs(A6).max())))
freq = np.linspace(-0.5, 0.5, len(A1))
fig,axes=plt.subplots()
axes.plot(window1,label='Bartlett-Hann')
axes.plot(window2,label='Bartlett')
axes.plot(window3,label='Blackman')
axes.plot(window4,label='Bohman')
axes.plot(window5,label='Hanning')
axes.plot(window6,label='Tukey')
axes.set_ylabel('Amplitude')
axes.set_xlabel('Sample')
plt.legend(bbox_to_anchor=(0.35,0.45),loc=2,borderaxespad=0.1)
plt.grid(True)
plt.savefig('ventanasample1.eps',dpi=1000,bbox_inches='tight')
fig,axes1=plt.subplots()
axes1.plot(freq,response1,label='Bartlett-Hann')
axes1.plot(freq,response2,label='Bartlett')
axes1.plot(freq,response3,label='Blackman')
axes1.plot(freq,response4,label='Bohman')
axes1.plot(freq,response5,label='Hanning')
axes1.plot(freq,response6,label='Tukey')
axes1.set_ylabel('Normalized magnitude [dB]')
axes1.set_xlabel('Normalized frequency [cycles per sample]')
plt.legend(bbox_to_anchor=(0.35,0.45),loc=2,borderaxespad=0.1)
plt.grid(True)
plt.savefig('ventanasfreq1.eps',dpi=1000,bbox_inches='tight')


