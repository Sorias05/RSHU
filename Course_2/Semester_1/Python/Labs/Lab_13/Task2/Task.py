from Shop import Shop 

# a
store = Shop("Store", "Online")
print(f"{store.shop_name} {store.store_type}")
store.describe_shop()
store.open_shop()

# b
Shop("Store1", "Online").describe_shop()
Shop("Store2", "Online").describe_shop()
Shop("Store3", "Online").describe_shop()

# c
print(f"Number of units: {store.number_of_units}")
store.number_of_units += 5
print(f"Number of units: {store.number_of_units}")

# d
store.set_number_of_units(7)
store.increment_number_of_units(3)

# e
class Discount(Shop):
    def __init__(self, shop_name, store_type, discount_products):
        self.shop_name = shop_name
        self.store_type = store_type
        self.number_of_units = 0
        self.discount_products = discount_products
    
    def get_discount_products(self):
        return self.discount_products
    
store_discount = Discount("Store", "Online", ["Laptop", "Smartphone", "Jeans"])
print(store_discount.get_discount_products())

# f
all_store = Shop("AllStore", "Online")
all_store.describe_shop()
all_store.open_shop()
