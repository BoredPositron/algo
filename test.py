import math
import random
import sqlite3

conn = sqlite3.connect("data.db")
cursor = conn.cursor()
data = []
def price(category):
    d = {"1": [300, 500], "2": [500, 1000], "3": [1000, 4000], "4": [4000, 10000], "5":[10000, 100000]}
    v = d[category[-1]]
    price = random.randint(v[0],v[1])
    return price
for i in range(301, 100000):
    print(i+1)
    purchase_id = ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(8))
    user_uid = random.choice(['043HRMGC', '13G45QOM', '28MYNW5P', 'M5OKGAK6'])
    brand_imp = random.choice("Alpha", "Beta", "Gamma", "Delta")
    brand_meh = random.choice("ABC", "XYZ", "PQR")
    brand = random.choice(brand_meh, brand_imp)
    item = f'Product {random.randint(1,8)}'
    quantity = random.randint(1, 10)
    category = random.choice(['Category1', 'Category2', 'Category3', 'Category4', 'Category5'])
    msrp = price(category)
    amount = quantity * msrp
    purchase_date = f'2023-08-{random.randint(1, 31)}'

    data.append([purchase_id, item, quantity, msrp, amount, category, user_uid, purchase_date])

for order in data:
    query = f"INSERT INTO Orders Values {tuple(order)}"
    cursor.execute(query)
    conn.commit()
#

# cursor = conn.cursor()
#
# for i in range(10000):
#     itemuid = i
#     itemName = f"Product{i + 1}"
#     itemPrice = random.randint(1000, 4000)
#     itemViews = random.randint(100, 1000)
#     itemSales = random.randint(math.ceil(0.5*itemViews), itemViews)
#     customerRating = round(random.uniform(1,5), 2)
#
#     cursor.execute(
#         f"INSERT INTO Category3 VALUES ({itemuid}, '{itemName}', {itemPrice}, {itemViews}, {itemSales}, {customerRating});")
#
# conn.commit()
