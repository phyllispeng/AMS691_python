#Mandelbrot Set
#Name: Yuanyuan Peng
#ID: 108 734 720

import numpy as np
import matplotlib.pyplot as plt

def mandelbrot():
	 N_max = 50
	 some_threshold = 50
	 x = np.linspace(-2,1)
	 y = np.linspace(-1.5,1.5)
	 c = x + 1j*y
	 z = c


	 #loop
	 for j in range(N_max):
	 	z = z**2 + c
	 	#abs of z should be smaller than some_threshold
	 	if np.absolute(z) <  some_threshold:
	 		#argument here
	 		return j


mask = mandelbrot()

plt.imshow(mask.T, extent=[-2,1,-1.5,1.5])
plt.gray()
plt.savefig('mandelbrot.png')