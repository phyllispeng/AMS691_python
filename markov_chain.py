#Markov Chain
#Name: Yuanyuan Peng
#ID: 108 734 720
import numpy as np
import matplotlib.pyplot as plt
eigenvalue = 1

def normlize(P):
	return P
# funtion take a input P p is the matrix

def transistion(P):
	return P
#constructs a random matrix
A = np.random.rand(3,2)
#and normalizes each row so that it is a transition matrix
print(A)
#starts from a random (normalizes) probabilitty distribution  p 
#and takes 50 steps to obtain  p_50

#computes the stationary distribution: the eigenvalue of P.T with eigenvalue 1
#to obtain p_stationary (normalize eigenvector) 