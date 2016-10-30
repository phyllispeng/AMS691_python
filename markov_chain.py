#Markov Chain
#Name: Yuanyuan Peng
#ID: 108 734 720
import numpy as np


#normlize function 
def normalizes(P):
	row_num = 0
	R =  np.zeros_like(P)

	for row in P:

		R[row_num] = row/np.sum(row)
		row_num = row_num + 1
	
	return R
# funtion take a input P p is the matrix

def transistion(P,time,p):
	for i in range(time):
		p = (P.transpose()).dot(p)
	return p
# compare function see if p_50 equals to p_stationary
def compare(p_time, p_station):
	boo = np.allclose(p_time, p_station,0.00001)
	return boo

#construct a random matrix
P = np.random.rand(5,5)

normal_P = normalizes(P)
#starts from a random (normalizes) probabilitty distribution  p 
p = np.random.rand(5,1)
p_stationary=np.zeros_like(p)
normal_pt = normalizes(p.transpose())
normal_p = normal_pt.transpose()
 
#and takes 50 steps to obtain  p_50
p_50 = transistion(normal_P,50,normal_p)
 
#and normalizes each row so that it is a transition matrix
#w is the eigenvalue
#v is the normalized eigenvectors
w,v = np.linalg.eig(normal_P.transpose())

p_stationaryt = v[:,(np.abs(w-1)).argmin()]
 
#normalize p stationary
normal_p_stationary = p_stationaryt/np.sum(p_stationaryt)

p_stationary[:,0] = normal_p_stationary 
print('p_50', p_50)
print('p_stationary', p_stationary)
result = compare(p_50, p_stationary)

if result == True:
	print ('p_50 and p_stationary are equal')
else:
	print('p_50 and p_stationary are not equal')
 