import scipy.stats as st
import numpy as np


class Gaussian1D:

    @staticmethod
    def FromGaussianMixture(gm):
        return Gaussian1D(gm.means_.ravel(), np.sqrt(gm.covariances_.ravel()), gm.weights_)

    def __init__(self, means, stds, pis):
        self.n_components = len(means)
        self.dists_ = st.norm(means, stds)
        self.pis_ = np.asarray(pis) / np.sum(pis)
        self.cmp_dist_ = st.rv_discrete(values=(np.arange(len(pis)).astype('int32'), self.pis_))

    def pdf(self, x, sep=False):
        if sep:
            return self.pis_ * self.dists_.pdf(np.atleast_2d(x).reshape(-1, 1))
        else:
            return np.sum(self.pis_ * self.dists_.pdf(np.atleast_2d(x).reshape(-1, 1)), 1)

    def proba(self, x):
        p = self.pdf(x, sep=True)
        return p[:, 1] / np.sum(p, axis=1)

    def rvs(self, size):
        cmp = self.cmp_dist_.rvs(size=size)
        return np.stack((self.dists_.rvs(size=(size, self.n_components))[range(size), cmp], cmp), axis=1)
