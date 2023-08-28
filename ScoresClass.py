
class Scores():
    def __init__(self, count_score=None, rating_score=None):
        self.scoreList = [count_score, rating_score]

    def Count_Score(self, sales, views):
        count_score = float(sales / views)
        self.scoreList[0] = count_score

    def rating_score(self, ratings):
        self.scoreList[1] = ratings / 5

    def weigh_scores(self, weights):
        self.scoreList = [score * weight for score, weight in zip(self.scoreList, weights)]
        score = round(sum(self.scoreList), 3)
        return score