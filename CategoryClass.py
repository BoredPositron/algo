import ScoresClass


class Category:
    def __init__(self, no_items,items: list, category, mean_purchase = None ):
        self.number_of_items = no_items
        self.items = items
        self.user_mean_purchase_value = mean_purchase
        self.category = category


    def calculate_score(self):
        for item in self.items:
            view_score = round(float(item.sales/item.views), 3)
            price_score_not_final = round(abs(item.price - self.user_mean_purchase_value)/self.user_mean_purchase_value, 3)
            price_score = 1- price_score_not_final
            rating_score = round(item.rating/5, 3)
            score = ScoresClass.Scores(view_score, rating_score, price_score)
            item.score = score.weigh_scores([0.7, 0.8, 1])

    def display_items(self):
        inventory = []
        for item in self.items:
            item_property = {}
            item_property["name"] = item.name
            item_property["price"] = item.price
            item_property["score"] = item.score
            inventory.append(item_property)
        return inventory



