class Smartphone:
    def __init__(self, brand, model, phone_number):
        self.brand = brand
        self.model = model
        self.phone_number = phone_number


catalog = [
    Smartphone("Apple", "iphone 15 PRO MAX", "+79999760621"),
    Smartphone("Samsung", "s21", "+79987775555"),
    Smartphone("Apple", "iphone 15", "+79998887766"),
    Smartphone("Samsung", "S3", "+79995554433"),
    Smartphone("Apple", "iphone SE", "+79992221111")
]

for phone in catalog:
    print(phone.brand, "-", phone.model + "-", phone.phone_number)
