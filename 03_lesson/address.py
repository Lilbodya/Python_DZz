class Address:
    index = "14200"
    city = "Воскресенск"
    street = "Светлая"
    house = "5"
    flat = "14"

    def __init__(self, index, city, street, house, flat):
        self.index = index
        self.city = city
        self.street = street
        self.house = house
        self.flat = flat


my_address = Address("140200", "Воскресенск", "Светлая", "5", "14")
print(my_address.index)
print(my_address.city)
print(my_address.street)
print(my_address.house)
print(my_address.flat)
