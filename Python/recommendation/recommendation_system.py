from Python.recommendation.k_means import KMeansRecSys


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

    def get_recommendations(self):
        return self._recommendations

    def process(self, preference):
        self._k_means.preprocess(preference)
        self._recommendations = self._k_means.predict()
