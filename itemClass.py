import ScoresClass
import sqlite3


class Item:
    def __init__(self, name, price, views, sales, rating, score = None):
        self.name = name
        self.price = price
        self.views = views
        self.sales = sales
        self.rating = rating
        self.score: ScoresClass.Scores = score

    # def get_scores(self):
    #     self.score.Count_Score(self.sales, self.views)
    #     self.score.rating_score(self.rating)
    #     self.score.price_score(self.price, self.category_mean)
    #     final_score = self.score.weigh_scores([0.7, 8, 1])
    #     return {"name": self.name, "score": final_score}

    def update_attr(self, attribute, value):
        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()
        query = f"UPDATE Category1 SET {attribute} = {value} WHERE itemName = '{self.name}'"
        cursor.execute(query)
        conn.commit()
