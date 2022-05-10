import wavio
import numpy as np

s = input("Enter your data: ")
s += '.'
filename = "h"
print((''.join(map(bin,bytearray(s, 'utf-8')))))
binout = ((''.join(map(bin,bytearray(s, 'utf-8')))).replace("b", "")).replace(" ", "")
print(binout)


rate = 44100  # samples per second, every second 44100 samples are used, for 100ms --> 44100/(1000/100)
T = 1         # sample duration for each bit (seconds), can be changed using the ms down below
f1 = 1200.0   # sound frequency (Hz) for 0 bit
f2 = 2400.0   # sound frequency (Hz) for 1 bit
start_sequence = 1800.0   # start frequencies
stop_sequence = 3600.0    # stop frequency


ms = 10; #milliseconds between each bit
samples = 44100//(1000//ms)

x = []
l = []

#------------------------------------------------------------------------------
#start sequence with 1800hz
t = np.linspace(0, T, T*rate, endpoint=False)
x.append(np.sin(2*np.pi * start_sequence * t[:samples]))


for i in binout:
	t = np.linspace(0, T, T*rate, endpoint=False)
	if i == '0':
		x.append(np.sin(2*np.pi * f1 * t[:samples]))
	if i == '1':
		x.append(np.sin(2*np.pi * f2 * t[:samples]))


#end sequence with 4000hz
t = np.linspace(0, T, T*rate, endpoint=False)
x.append(np.sin(2*np.pi * stop_sequence * t[:samples]))
t = np.linspace(0, T, T*rate, endpoint=False)
x.append(np.sin(2*np.pi * stop_sequence * t[:samples]))
t = np.linspace(0, T, T*rate, endpoint=False)
x.append(np.sin(2*np.pi * stop_sequence * t[:samples]))
#------------------------------------------------------------------------------

for i in x:
	for j in i:
		l.append(j);

l = np.array(l)

wavio.write(filename+".wav", l, rate, sampwidth=2)
