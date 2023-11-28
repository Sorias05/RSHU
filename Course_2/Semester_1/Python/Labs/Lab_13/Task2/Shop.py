class Shop:
    def __init__(self, shop_name, store_type):
        self.shop_name = shop_name
        self.store_type = store_type
        self.number_of_units = 0
    
    def describe_shop(self):
        print(f"Shop name: {self.shop_name}\nStore type: {self.store_type}")

    def open_shop(self):
        print(f"{self.shop_name} has been opened!")
        
    def set_number_of_units(self, data):
        self.number_of_units = data

    def increment_number_of_units(self, n):
        self.number_of_units += n