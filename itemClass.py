import ScoresClass
import sqlite3


class Item:
    def __init__(self, name, price, views, sales, rating):
        self.name = name
        self.price = price
        self.views = views
        self.sales = sales
        self.rating = rating

    def get_scores(self):
        score = ScoresClass.Scores()
        score.Count_Score(self.sales, self.views)
        score.rating_score(self.rating)
        final_score = score.weigh_scores([1, 0.8])
        return {"name": self.name, "score": final_score}

    def update_attr(self, attribute, value):
        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()
        query = f"UPDATE Category1 SET {attribute} = {value} WHERE itemName = '{self.name}'"
        cursor.execute(query)
        conn.commit()
