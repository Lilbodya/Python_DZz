class Smartphone:
    def __init__(self, brand, model, phone_number):
        self.brand = brand
        self.model = model
        self.phone_number = phone_number

    def info(self):
        return (
          f"Марка: {self.brand}, "
          f"Модель: {self.model}, "
          f"Номер: {self.phone_number}"
            )


my_phone = Smartphone("Apple", "iphone 15 PRO MAX", "+79999760621")
print(my_phone.info())
