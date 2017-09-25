import math
def gausse(mu, sigma, x):
	y = 1.0 / math.sqrt(2*math.pi * sigma * sigma) * math.exp(-0.5 * (x - mu) * (x - mu) / (sigma * sigma))
	return y


print gausse(10, 2, 8)
