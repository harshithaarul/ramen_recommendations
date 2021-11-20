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
        _features: all features including cluster ID ("label12")
    """

    def __init__(self):
        self.CONST_PATH = os.getcwd() + "/resources/"
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

        mock_v = "cup noodl chick veget nissin cup us"
        dict = {"Brand": "Nissin",
                "Variety": "Cup Noodles Chicken Vegetable",
                "Style": "Cup",
                "Country": "USA",
                "Stars": "2.25"
                }
        preference_data = pd.DataFrame(dict, [0])

        preference_data["Variety"] = preference_data["Variety"] + " " + preference_data["Brand"] + " " + preference_data["Style"] + " " + \
                                preference_data["Country"]
        preference_data["Variety"] = preference_data["Variety"].astype(str)

        preference_data["Variety"] = preference_data["Variety"].apply(processing)
        preference_vector = vectorized.transform(preference_data["Variety"])

        one = train_vector[2]
        print(kmeans_v.predict(preference_vector))

    # def recommend_util(str_input):
    #     # match on the basis course-id and form whole 'Description' entry out of it.
    #     temp_df = course_df.loc[course_df['CourseId'] == str_input]
    #     temp_df['InputString'] = temp_df.CourseId.str.cat(
    #         " " + temp_df.CourseTitle.str.cat(" " + temp_df['Description']))
    #     str_input = list(temp_df['InputString'])
    #
    #     # Predict category of input string category
    #     prediction_inp = cluster_predict(str_input)
    #     prediction_inp = int(prediction_inp)
    #     # Based on the above prediction 10 random courses are recommended from the whole data-frame
    #     # Recommendation Logic is kept super-simple for current implementation.
    #     temp_df = course_df.loc[course_df['ClusterPrediction'] == prediction_inp]
    #     temp_df = temp_df.sample(10)
    #
    #     return list(temp_df['CourseId'])

    def predict(self, preference):

        return self._features["label2"]
