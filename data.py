import time
time1 = time.time()
import sqlite3
import itemClass
import UserClass
import Functions

connect = sqlite3.connect("data.db")
cursor = connect.cursor()

query = "SELECT * FROM Category2"
cursor.execute(query)
items = cursor.fetchall()
user = UserClass.User(uid='M5OKGAK6')
user.get_purchases(connect)
purchases = user.get_purchases_by_category()
print(user.get_mean_purchase_value(2))
itemList = [
    itemClass.Item(
        name=item[1],
        price=item[2],
        views=item[3],
        sales= item[4],
        rating=item[5],
        user_mean=user.get_mean_purchase_value(1)
     )
    for item in items
]
print(items)
#
scores = list(map(itemClass.Item.get_scores, itemList))
sortedlist = sorted(scores, key=lambda i: i['score'])
sortedlist.reverse()
print(sortedlist)
print(len(sortedlist))
time2 = time.time()
print(time2-time1)