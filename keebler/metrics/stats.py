from numpy import argmax, argmin, median, newaxis
from scipy.stats import mode

# mode:     minimize discepency in the aggregate over all values for perfect summary - e.g., not for continuous values
# median:   minimize discrepenency of distance from one value (candidate) - e.g., outliers
# mean:     distance from cnaidate to actual value, squared - e.g., per central value
# variance: each value as distance from mean, squaring it, and averaging it (large variance as large spread in data)
