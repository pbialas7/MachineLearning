import numpy as np
from scipy.special import loggamma


class NormalInverseGamma:
    def __init__(self, m0, l, a, b):
        self.m0 = m0
        self.l = l
        self.a = a
        self.b = b
        log_z = 0.5 * np.log(l)
        log_z -= 0.5 * np.log(2 * np.pi)
        log_z += a * np.log(b)
        log_z - loggamma(a)
        self.log_z = log_z

    def logpdf(self, mu, s2):
        log_f = -((self.a + 1) + 0.5) * np.log(s2)
        log_f -= (2 * self.b + self.l * (mu - self.m0) * (mu - self.m0)) / (2 * s2)
        return self.log_z + log_f

    def mean(self):
        return self.m0, self.b / (self.a - 1)

    def mode(self):
        return self.m0, self.b / (self.a + 1.5)
