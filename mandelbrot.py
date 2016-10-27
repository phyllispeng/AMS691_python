#Mandelbrot Set
#Name: Yuanyuan Peng
#ID: 108 734 720
import numpy as np
import matplotlib.pyplot as plt

N_max = 300
some_threshold = 50

x = np.linspace(-2, 1, N_max,endpoint=True)
y = np.linspace(-1.5, 1.5, N_max,endpoint=True)
xv,yv = np.meshgrid(x,y)
c = xv+ 1j*yv
print('c',c)
mask = np.zeros_like(c,dtype = np.bool)


for y1 in range(N_max):
	for x1 in range(N_max):
		z = 0
		for j in range(N_max):
			#c = xv[x1]+1j*yv[y1]
			z = z**2 + c[y1,x1]
		if np.any(np.absolute(z) < some_threshold):
			mask[x1,y1] = j
		
		#print(z)

plt.imshow(mask.T, extent = [-2,1,-1.5,1.5])
plt.gray()
plt.savefig('mandelbrot.png')
plt.show()