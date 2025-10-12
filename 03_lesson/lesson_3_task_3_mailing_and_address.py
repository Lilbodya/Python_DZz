from mailing import Mailing
from address import Address

to_address = Address("140200", "Воскресенск", "Светлая", "5", "14")

from_address = Address("123456", "Москва", "Тёмная", "6", "13")

mailing = Mailing(to_address, from_address, 350, "TRACK1")

print(
    f"Отправление {mailing.track} из "
    f"{mailing.from_address.index}, {mailing.from_address.city}, "
    f"{mailing.from_address.street}, {mailing.from_address.house} - "
    f"{mailing.from_address.flat} "
    f"в {mailing.to_address.index}, {mailing.to_address.city}, "
    f"{mailing.to_address.street}, {mailing.to_address.house} - "
    f"{mailing.to_address.flat}. "
    f"Стоимость {mailing.cost} рублей."
)
