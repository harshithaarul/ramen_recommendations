import os
import re
import pandas as pd
from nltk.stem.lancaster import LancasterStemmer
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import CountVectorizer


class KMeansRecSys:
    """
    K-means Clustering preprocessing and implementation

    Attributes:
        _query: user input composed as a query
        _features: all features including cluster ID ("label12")
    """

    def __init__(self, query):
        self.CONST_PATH = os.getcwd() + "/resources/"
        self._query = query
        self._features = pd.read_csv(self.CONST_PATH + "ramen-ratings.csv")
        self._features = self._features.iloc[:, 1:-2]

    def preprocess(self):
        train_data = pd.read_csv(self.CONST_PATH + "ramen-ratings.csv")
        train_data = train_data.iloc[:, 1:-1]

        train_data["Variety"] = train_data["Variety"] + " " + train_data["Brand"] + " " + train_data["Style"] + " " + \
                                train_data["Country"]
        train_data["Variety"] = train_data["Variety"].astype(str)

        # Processing the text
        stemmer = LancasterStemmer()

        def processing(text):
            text = re.sub(r'\@\S+', '', text)
            text = re.sub(r'http\:\/\/\S+', '', text)
            text = re.sub(r'[^\w\s]', '', text)
            tokens = text.lower().split(" ")
            stemmed_tokens = [stemmer.stem(x) for x in tokens]
            return ' '.join(stemmed_tokens)

        train_data["Variety"] = train_data["Variety"].apply(processing)

        vectorized = CountVectorizer(binary=True, min_df=5)

        # Fitting and processing countVectorized
        vectorized.fit(train_data["Variety"])
        train_vector = vectorized.transform(train_data["Variety"])

        kmeans_v = KMeans(n_clusters=10, random_state=0).fit(train_vector)

        self._features["label2"] = kmeans_v.labels_

    def predict(self):
        return self._features["label2"]
