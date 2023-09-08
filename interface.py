from functools import wraps, lru_cache
import sqlite3
from CategoryClass import Category
import UserClass
from itemClass import Item
from time import perf_counter


def memoize(func):
    cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        key = str(args) + str(kwargs)

        if key not in cache:
            cache[key] = func(*args, **kwargs)

        return cache[key]

    return wrapper


def get_user_details():
    uid = input("Enter User Unique Id: ")
    category = input("Enter Preferred Category: ")
    return [uid, category]


def asign_to_object(items: list):
    itemList = [
        Item(
            name=item[1],
            price=item[2],
            views=item[3],
            sales=item[4],
            rating=item[5],
        )
        for item in items
    ]
    return itemList


@lru_cache(256)
def get_data(category):
    connect = sqlite3.connect("data.db")
    cursor = connect.cursor()
    query = f"SELECT * FROM Category{category}"
    cursor.execute(query)
    items = assign_to_object(cursor.fetchall())
    category_obj = Category(len(items), items, category)
    return category_obj


def assign_to_object(items: list):
    itemList = [
        Item(
            name=item[1],
            price=item[2],
            views=item[3],
            sales=item[4],
            rating=item[5],
        )
        for item in items
    ]
    return itemList


def main():
    connector = sqlite3.connect("data.db")
    input_data = get_user_details()
    t1 = perf_counter()
    user = UserClass.User(input_data[0])
    user.get_purchases(connector)
    user.get_purchases_by_category()
    user.get_mean_purchase_values()
    inventory = get_data(input_data[1])
    inventory.user_mean_purchase_value = user.mean_values[f"Category{input_data[1]}"]
    inventory.calculate_score()
    print(user.mean_values)
    sortedlist = sorted(inventory.display_items(), key=lambda i: i['score'], reverse=True)
    print(sortedlist[0:10])
    t2 = perf_counter()
    print(t2-t1)


if __name__ == "__main__":
    main()
