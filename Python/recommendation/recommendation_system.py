from Python.recommendation.k_means import KMeansRecSys


class RecSystem:
    """
    RecSystem is a collection of hashing / clustering algorithms and computes recommended results based on
    the algorithms.

    Attributes:
        preferences: user input preferences
        recommendations: system output n common recommendations
    """

    def __init__(self):
        self._preferences = []
        self._recommendations = []
        self._k_means = KMeansRecSys("bowl, mild, nissin")
        self._k_means.preprocess()

    def set_preferences(self, p):
        self._preferences = p

    def get_recommendations(self):
        return self._recommendations

    def process(self):
        self._recommendations = self._k_means.predict()
