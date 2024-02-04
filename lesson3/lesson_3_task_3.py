from address import Address
from mailing import Mailing

to_address = Address("101000", "Москва", "Сретинский бульвар", "11", "10")
from_address = Address("191186", "Санкт-Петербург", "Малая морская улица", "11", "5")

mailing = Mailing(to_address, from_address, 150, "RU321123")

print(f"Отправление {mailing.track} из {mailing.from_address.index}, {mailing.from_address.city}, {mailing.from_address.street}, {mailing.from_address.house} - {mailing.from_address.apartment} в {mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.street}, {mailing.to_address.house} - {mailing.to_address.apartment}. Стоимость {mailing.cost} рублей.")
