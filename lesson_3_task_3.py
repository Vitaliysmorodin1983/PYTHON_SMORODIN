from address import Address
from mailing import Mailing

to_address = Address("633100", "Новосибирск", "Ленина", "10", "25")
from_address = Address("654321", "Санкт-Петербург", "Пушкина", "10", "30")

mailing = Mailing(
    to_address=to_address,
    from_address=from_address,
    cost=1800,
    track="BCJ_1234"
)

print(
    f"Отправление {mailing.track} из "
    f"{mailing.from_address.index}, {mailing.from_address.city}, {mailing.from_address.street}, {mailing.from_address.house} - {mailing.from_address.apartment} "
    f"в {mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.street}, {mailing.to_address.house} - {mailing.to_address.apartment}. "
    f"Стоимость {mailing.cost} рублей."
)