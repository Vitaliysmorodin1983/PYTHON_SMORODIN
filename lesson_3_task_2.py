from smartphone import Smartphone

catalog = [
    Smartphone("Samsung", "Galaxy S25", "+79133456789"),
    Smartphone("Apple", "iPhone 15", "+79234567890"),
    Smartphone("Xiaomi", "Redmi Note 12", "+79835678901"),
    Smartphone("Google", "Pixel 7", "+79136789012"),
    Smartphone("OnePlus", "11 Pro", "+79527890123")
]

for phone in catalog:
    print(f"{phone.brand} - {phone.model} {phone.phone_number}")