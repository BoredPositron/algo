class Purchase:
    def __init__(self, purchase_id, item, quantity, msrp, amount, category, user_uid, purchase_date):
        self.purchase_id = purchase_id
        self.item = item
        self.quantity = quantity
        self.msrp = msrp
        self.amount = amount
        self.category = category
        self.user_uid = user_uid
        self.purchase_date = purchase_date