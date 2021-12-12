from Python.recommendation.k_means import KMeansRecSys
from Python.recommendation.gmm import GMMRecSys
import numpy as np
import pandas as pd


class RecSystem:
    """
    RecSystem is a collection of hashing / clustering algorithms and computes recommended results based on
    the algorithms.

    Attributes:
        _recommendations: system output n common recommendations (n = 10)
        _k_means: recommendation using k_means
    """

    def __init__(self):
        self._recommendations = []
        self._k_means = KMeansRecSys()
        self._gmm = GMMRecSys()

    def get_recommendations(self):
        return self._recommendations

    def process(self, preference):
        self._k_means.preprocess(preference)
        self._gmm.preprocess(preference)

        k_means_rec = self._k_means.predict()
        gmm_rec = self._gmm.predict()

        intersection = np.intersect1d(k_means_rec.index, gmm_rec.index)
        # self._features = self._features.sort_values(by=["distance"])
        if len(intersection) > 10:
            intersection = intersection[:10]

        n = 0
        for i in intersection:
            if n < 10:
                self._recommendations.append(k_means_rec[k_means_rec.index == i].sort_values(by=["distance"]).values.tolist()[0])
                n += 1
