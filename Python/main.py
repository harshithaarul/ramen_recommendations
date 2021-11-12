from recommendation.recommendation_system import RecSystem

preferences = ["bowl", "spicy", "nissin"]


def print_hi(name):
    print(f'Hi, {name}')


def get_recommendations(p):
    rec_sys = RecSystem()
    rec_sys.set_preferences(p)
    rec_sys.process()

    recommendations = rec_sys.get_recommendations()
    return recommendations


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi(get_recommendations(preferences))
