import math


class Scores:
    def __init__(self, count_score=None, rating_score=None, price_score = None):
        self.scoreList = [count_score, rating_score, price_score]


    def weigh_scores(self, weights):
        self.scoreList = [score * weight for score, weight in zip(self.scoreList, weights)]
        score = round(sum(self.scoreList)/3, 3)
        return score