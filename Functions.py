import statistics


def get_mean_price_by_category(sorted_purchases: dict):
    mean_prices = dict()
    for category in sorted_purchases.keys():
        values = []
        for purchase in sorted_purchases[category]:
            values.append(purchase.msrp)
        mean_prices[category] = round(statistics.mean(values), 3)
    return mean_prices
