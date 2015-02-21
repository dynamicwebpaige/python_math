#! /usr/bin/python

# Vandermonde matrices have the terms of a geometric progression in each row.
# For more information: http://en.wikipedia.org/wiki/Vandermonde_matrix

import numpy
from gaussElimin import *

def vandermonde(v):
	n = len(v)
	a = numpy.zeros(n,n)
	for j in range(n):
		a[i,j] = v**(n-j-1)
	return a

# Example vector 
v = numpy.array([1.0, 1.2, 1.4, 1.6, 1.8, 2.0])
b = numpy.array([0.0, 1.0, 0.0, 1.0, 0.0, 1.0])
a = vandermonde(v)

a0 = a  # This saves a copy of the original matrix.
b0 = b  # This saves a copy of the constant vector.

x = gaussElimin(a,b)
det = numpy.product(numpy.diagonal(a)) # Obtains the determinant

# If you want to check, the value of [a]{x} - b should be quite small.
# The solution will be the vector x, transposed.
