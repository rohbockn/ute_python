import math
import cmath
import random

def sqrt(x):
    res=x**0.5
    return(res)

def random_gauss(mu,sigma):
    return random.gauss(mu, sigma)

random.seed(100)
assert_almost_equal(random_gauss(24,2.6),25.746038650049936)

print(sys.float_info)
