from __future__ import division
'''Simple Example Using Gaussian Variables'''
import numpy as np

from bayesian.gaussian_bayesian_network import gaussian, conditional_gaussian
from bayesian.gaussian_bayesian_network import build_graph
from bayesian.gaussian_node import *

'''
This example comes from page 3 of
http://people.cs.aau.dk/~uk/papers/castillo-kjaerulff-03.pdf

Note that to create a Guassian Node
we supply mean and standard deviation,
this differs from the example in the
above paper which uses variance (=std. dev.) ** 2

Note in the paper they specify variance,
wheres as this example we are  using std. dev.
instead hence for A the variance is 4 and std_dev is 2.
'''

@gaussian(3, 2)
def f_a(a):
    '''represents point A in the river system'''
    pass


@conditional_gaussian(4, 1, 1)
def f_b(a, b):
    '''Point b is a conditional Guassian
    with parent a.
    '''
    pass


@conditional_gaussian(9, 2, 1)
def f_c(a, c):
    '''Point c is a conditional Guassian
    with parent a'''
    pass


@conditional_gaussian(14, 1, betas=dict(b=1, c=1))
def f_d(b, c, d):
    pass


means = np.matrix([[f_a.mean], [f_b.mean], [f_c.mean], [f_d.mean]])

#std_devs = [f.std_dev for f in [f_a, f_b, f_c, f_d]]
std_devs = [f.std_dev for f in [f_a, f_b, f_c, f_d]]
sigma = build_sigma_from_std_devs(std_devs)
sigma = np.matrix([[4, 4, 8, 12],
                   [4, 5, 8, 13],
                   [8, 8, 20, 28],
                   [12, 13, 28, 42]])


N = 4
q = 3

#splits = split(means, sigma)
betas = {
    (1, 0): 1, # BA
    (2, 0): 2, # CA
    (3, 1): 1, # DB
    (3, 2): 1, # DC
}


variances = [s ** 2 for s in std_devs]


variances = [4, 4, 3]
betas = {
    (1, 0): 0.5,
    (2, 1): -1
}
C = {
    1: [],
    2: [1],
    3: [2]
}


betas = {
    (2, 1): 0.5,
    (3, 2): -1
}


sigma = conditional_to_joint_sigma_2([1, 2, 3], C, variances, betas)
print sigma


# Now for the river example first we have to modify the
# args called with...
C = {
    1: [],
    2: [1],
    3: [1],
    4: [2, 3]
}

betas = {
    (2, 1): 1, # BA
    (3, 1): 2, # CA
    (4, 2): 1, # DB
    (4, 3): 1, # DC
}


variances = [s ** 2 for s in std_devs]

import ipdb; ipdb.set_trace()
sigma = conditional_to_joint_sigma_2([1,2,3,4], C, variances, betas)
print sigma