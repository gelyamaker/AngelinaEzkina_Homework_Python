from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iPhone 17 Pro", "+79011111111"),
    Smartphone("Samsung", "Galaxy S26", "+79100000000"),
    Smartphone("Xiaomi", "Redmi Note 15", "+79255555555"),
    Smartphone("HUAWEI", "HUAWEI Pura 90", "+79777777777"),
    Smartphone("HONOR", "HONOR 600 Pro", "+79999999999"),
]

for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model}. {smartphone.phone}")
