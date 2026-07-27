from address import Address
from mailing import Mailing

to_address = Address(119019, "г. Москва", "ул. Арбат", "д. 500", "кв. 999")
from_address = Address(630000, "г. Новосибирск",
                       "ул. Ленина", "д. 999", "кв. 9")

mail = Mailing(to_address, from_address, 57.60, "63000012345678")

print(mail)
