import random, math

def withProb(p):
	return random.random() < p
	
def runGeneration(v,p):
	"""Runs a generation of change. Returns the bit in v after it's had a chance p to flip"""
	return not v if withProb(p) else v
	
def runGenerations(v,p,n):
	"""Given an initial value v, a probability to change during a generation p, and n generations, return the transformed value of v"""
	for i in range(n):
		v = runGeneration(v,p)
	return v
	
def binomialProbability(n,p,k):
	""" get probability of X~B(n,p) having result X=k """
	binomCoeff = math.factorial(n) / (math.factorial(k) * math.factorial(n-k))
	return p**k * (1-p)**(n-k) * binomCoeff
	
if __name__ == "__main__":
	print("Running sample:")
	omega = False
	p = 0.0001
	n = 1000
	trials = 1000
	
	numSuccesses = 0
	
	for trial in range(trials):
		alpha = runGenerations(omega,p,n)
		#print("The result was",alpha)
		if alpha != omega:
			numSuccesses += 1
		
	print("In",trials,"trials,",numSuccesses,"times the bit was incorrect. (",numSuccesses/trials,")")
	
	# calculate the theoretical probability based on binomial distribution
	theoreticalProb = 0.0
	for k in range(1,n+1,2): # get all odds (the n+1 is necc. to force the value of n, if odd, to be in the list too)
		theoreticalProb += binomialProbability(n,p,k)
		
	print("Theoretical probability of this:",theoreticalProb)
	