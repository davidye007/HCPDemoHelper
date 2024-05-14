from datetime import datetime
from store import Store
from item import Item

class Receipt:

    #TODO: add a field to store receipt image, and proper way to make it into dict/json form
    def __init__(self, store, date, category, purchases, total):
        self.store = store
        self.date = date
        self.purchases = purchases
        self.category = category
        self.total = total

    #TODO: create an exception for handling failure to create receipt from dict
    @staticmethod
    def from_dict(dict):
        store = Store.from_dict(dict.get('store')) # store dict -> store object
        date_value = dict.get('date')
        if isinstance(date_value, str):
            date = datetime.strptime(date_value, "%Y-%m-%d") # YYYY-MM-DD -> datetime object
        else:
            date = datetime.fromisoformat(str(date_value))
        purchases = dict.get('purchases')
        items = []
        for purchase in purchases:
            items.append(Item.from_dict(purchase)) # item dict -> item object
        category = dict.get('category')
        total = dict.get('total')
        return Receipt(store=store, date=date, purchases=items, category=category, total = total)


    def to_dict(self):
        storeDict = self.store.to_dict() # store object -> store dict
        purchasesDict = [item.to_dict() for item in self.purchases] # item object -> item dict
        date = self.date.strftime('%Y-%m-%d')
        return {
        'store': storeDict,
        'date': date,
        'purchases': purchasesDict,
        'category' : self.category,
        'total' : self.total
        }

    #TODO: verify input
    @staticmethod
    def verify_receipt(dict):
        pass
