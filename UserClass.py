import sqlite3
import statistics
from functools import wraps, lru_cache
from Purchase import Purchase
def memoize(func):
    cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        key = str(args) + str(kwargs)

        if key not in cache:
            cache[key] = func(*args, **kwargs)

        return cache[key]

    return wrapper

class User:
    def __init__(self, uid, username=None, purchases: list = None,):
        self.username = username
        self.user_uid = uid
        self.purchases = purchases

    @lru_cache(256)
    def get_purchases(self, connector: sqlite3.Connection):
        with connector:
            cursor = connector.cursor()
            query = fr"Select * FROM Orders WHERE UserUID = '{self.user_uid}'"
            cursor.execute(query)
            purchases = cursor.fetchall()
            self.purchases = [
                Purchase(
                    purchase_id=order[0],
                    item=order[1],
                    quantity=order[2],
                    msrp=order[3],
                    amount=order[4],
                    category=order[5],
                    user_uid=order[6],
                    purchase_date=order[7]
                )
                for order in purchases
            ]
    @lru_cache(256)
    def get_purchases_by_category(self):
        purchases = {"Category1":[], "Category2":[], "Category3":[], "Category4":[],"Category5":[]}
        if self.purchases is not None:
            for purchase in self.purchases:
                if purchase not in purchases[purchase.category]:
                    purchases[purchase.category].append(purchase)
                else:
                    continue
        else:
            print("Get all purchases bu using user.get_purchases() first!!" )
            exit()
        self.purchases = purchases
        return purchases

    def get_mean_purchase_values(self):
        mean = {}
        for category in self.purchases.keys():
            prices = []
            for price in self.purchases[category]:
                 prices.append(price.msrp)
            mean[category] = round(statistics.mean(prices), 3)
        self.mean_values = mean


