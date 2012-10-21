# 6.00x Problem Set 3
#
# Successive Approximation: Newton's Method
#


# Problem 1: Polynomials
def evaluatePoly(poly, x):
    '''
    Computes the value of a polynomial function at given value x. Returns that
    value as a float.
 
    poly: list of numbers, length > 0
    x: number
    returns: float
    '''
    # FILL IN YOUR CODE HERE...
    res=0
    iterator=0
    for e in poly:
        res += e * pow(x,iterator)
        iterator +=1
    return float(res)



# Problem 2: Derivatives
def computeDeriv(poly):
    '''
    Computes and returns the derivative of a polynomial function as a list of
    floats. If the derivative is 0, returns [0.0].
 
    poly: list of numbers, length &gt; 0
    returns: list of numbers (floats)
    '''
    # FILL IN YOUR CODE HERE...
    res=[]
    iterator=0
    for e in poly:
	res=res+[float(e*iterator)]
	iterator +=1
    if len(res)==1:
	return res
    else:
	return res[1:]
		
		

# Problem 3: Newton's Method
def computeRoot(poly, x_0, epsilon):
    '''
    Uses Newton's method to find and return a root of a polynomial function.
    Returns a list containing the root and the number of iterations required
    to get to the root.
 
    poly: list of numbers, length > 1.
         Represents a polynomial function containing at least one real root.
         The derivative of this polynomial function at x_0 is not 0.
    x_0: float
    epsilon: float > 0
    returns: list [float, int]
    '''
    iterator=0
    x_n=x_0
    x_n1=x_0
    while abs(evaluatePoly(poly,x_n1))>epsilon or x_n1==x_0:
    	x_n=x_n1
    	x_n1=x_n-(evaluatePoly(poly,x_n)/evaluatePoly(computeDeriv(poly),x_n))
    	iterator +=1
    return [x_n1,iterator]
print computeRoot([-13.39, 0.0, 17.5, 3.0, 1.0], 0.1,  .0001)
print computeRoot([1, 9, 8], -3, .01)
print computeRoot([1, -1, 1, -1], 2, .001)
