import time
time1 = time.time()
import sqlite3
import itemClass

connect = sqlite3.connect("data.db")
cursor = connect.cursor()

query = "SELECT * FROM Category1"
cursor.execute(query)
items = cursor.fetchall()

itemList = [
    itemClass.Item(
        name=item[1],
        price=item[2],
        views=item[3],
        sales= item[4],
        rating=item[5]
     )
    for item in items
]
print(items)

scores = list(map(itemClass.Item.get_scores, itemList))
sortedlist = sorted(scores, key=lambda i: i['score'])

print(scores)
print(sortedlist)
time2 = time.time()
print(time2-time1)
