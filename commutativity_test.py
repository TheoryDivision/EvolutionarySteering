#==============================================================================#
# Daniel Nichol - 08/06/2015.
#
# We generate 10,000 pairs of markov chain transition matrices for NK landscapes, 
# take the limits under multiplications and test if they commute. Each landscape is 
# generated by first randomly selecting K from {0,...,N-1} and then using the 
# NK algorithm to generate an NK landscape.
#==============================================================================#

from markovModel import generateNKLandscape
import random
import markovModel

num_samples = 100
commuting_pairs = []
N = 5

for i in range(num_samples):

	K_1 = random.randint(0,N-1)
	K_2 = random.randint(0,N-1)

	l_1 = generateNKLandscape(N,K_1)
	l_2 = generateNKLandscape(N,K_2)

	limit_1 = markovModel.limitMatrix(markovModel.buildTransitionMatrix(l_1))
	limit_2 = markovModel.limitMatrix(markovModel.buildTransitionMatrix(l_2))

	if (limit_1*limit_2 == limit_2*limit_1).all():
		commuting_pairs.append((l_1, l_2))

print len(commuting_pairs)

