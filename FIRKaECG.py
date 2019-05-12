# -*- coding: utf-8 -*-
"""
Created on Fri May 10 01:15:27 2019
Filtro FIR (Prueba2)
Tecnológico Nacional de México
Tecnológico de Estudios Superiores de Ixtapaluca
División de Ingeniería Electrónica
@author: M. en C. Rogelio Manuel Higuera Gonzalez
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from scipy.fftpack import fft
import matplotlib as mpl
params = {'xtick.labelsize': 14, 'ytick.labelsize': 14}
mpl.rcParams.update(params)
datos=np.loadtxt("ECG2.csv",usecols=(0,1,),skiprows=1,delimiter=',') 
Tiempo=(datos[:,0]) 
n=len(Tiempo)
Tm=Tiempo[11]-Tiempo[10]
fs=1/Tm
fc1=0.1
fc2=100
wn1=fc1/(fs/2)
wn2=fc2/(fs/2)
taps1 = signal.firwin(11,[wn1,wn2],pass_zero=False, window=('kaiser',2))
taps2 = signal.firwin(31,[wn1,wn2],pass_zero=False, window=('kaiser',2))
taps4 = signal.firwin(71,[wn1,wn2],pass_zero=False, window=('kaiser',2))
taps6 = signal.firwin(111,[wn1,wn2],pass_zero=False, window=('kaiser',2))
w_1, h_1 = signal.freqz(taps1, worN=8000)
w_2, h_2 = signal.freqz(taps2, worN=8000)
w_4, h_4 = signal.freqz(taps4, worN=8000)
w_6, h_6 = signal.freqz(taps6, worN=8000)
noise1=0.2*np.sin(2*np.pi*105*Tiempo)
noise2=0.1*np.sin(2*np.pi*115*Tiempo)                                                
Amplitud=(datos[:,1])    
x_noise=Amplitud+noise1+noise2
filtered_x = signal.lfilter(taps4, 1.0,x_noise)   
x_freq1=fft(x_noise)
x_freq2=fft(filtered_x)
freq=np.linspace(0.0, 1.0/(2.0*Tm), n//2)                                   
############################################################################################
fig,axes2=plt.subplots(figsize=(11, 5))
axes2.plot((w_1/np.pi)*(fs/2), 20 * np.log10(np.absolute(h_1)), label='M=11', linewidth=2)
axes2.plot((w_2/np.pi)*(fs/2), 20 * np.log10(np.absolute(h_2)), label='M=31', linewidth=2)
axes2.plot((w_4/np.pi)*(fs/2), 20 * np.log10(np.absolute(h_4)), label='M=71', linewidth=2)
axes2.plot((w_6/np.pi)*(fs/2), 20 * np.log10(np.absolute(h_6)), label='M=111', linewidth=2)
axes2.set_ylabel('Normalized magnitude [dB]',fontsize=16)
axes2.set_xlabel('Frequency [Hz]',fontsize=16)
axes2.tick_params(direction='out', length=2, width=1)
texto1 = plt.text(1, -70, r'$\beta=2$', fontsize=16)
plt.legend(bbox_to_anchor=(0.24,0),loc='lower right',borderaxespad=0.1,fontsize=16)
plt.grid(True)
plt.savefig('FIRECG1.png',dpi=1000,bbox_inches='tight')
############################################################################################
fig = plt.figure(figsize=(11, 6))
axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8]) # main axes
axes2 = fig.add_axes([0.2, 0.58, 0.4, 0.3]) # inset axes
axes1.plot(Tiempo, x_noise,linewidth = 2)
axes1.set_ylim([min(x_noise)-0.1,5.5])
axes1.set_xlabel('Time(s)',fontsize = 16)
axes1.set_ylabel('Voltage(mV)',fontsize = 16)
axes1.tick_params(direction='out', length=2, width=1)
texto2 = plt.text(150, 0.15, r'$Signal \; ECG + noise$', fontsize=20)
axes2.plot(freq, 2.0/n * np.abs(x_freq1[0:n//2]),'r',linewidth = 2)
axes2.set_xlabel('Frequency(Hz)', fontsize = 16)
axes2.set_ylabel('Amplitude', fontsize = 16)
plt.grid(True)
plt.savefig('FIRECG_signalnoise.png',dpi=500)
############################################################################################
fig = plt.figure(figsize=(11, 6))
axes3 = fig.add_axes([0.1, 0.1, 0.8, 0.8]) # main axes
axes4 = fig.add_axes([0.2, 0.58, 0.4, 0.3]) # inset axes
axes3.plot(Tiempo, filtered_x,linewidth = 2)
axes3.set_ylim([min(filtered_x)-0.1,4.8])
axes3.set_xlabel('Time(s)',fontsize = 16)
axes3.set_ylabel('Voltage(mV)',fontsize = 16)
axes3.tick_params(direction='out', length=2, width=1)
texto1 = plt.text(180, 0.1, r'$\beta=2$', fontsize=20)
texto2 = plt.text(155, 0.15, r'$Window=Kaiser$', fontsize=20)
texto3 = plt.text(178, 0.05, r'$M=71$', fontsize=20)
axes4.plot(freq, 2.0/n * np.abs(x_freq2[0:n//2]),'r',linewidth = 2)
axes4.set_xlabel('Frequency(Hz)', fontsize = 16)
axes4.set_ylabel('Amplitude', fontsize = 16)
plt.grid(True)
plt.savefig('FIRECG_filtered.png',dpi=500)