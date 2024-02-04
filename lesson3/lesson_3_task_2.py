from smartphone import Smartphone

phone1 = Smartphone("Samsung", "Galaxy S23", "+79123456789")
phone2 = Smartphone("Apple", "iPhone 13", "+79234567890")
phone3 = Smartphone("Google", "Pixel 7", "+79345678901")
phone4 = Smartphone("Huawei", "P70", "+79456789012")
phone5 = Smartphone("OnePlus", "12", "+79567890123")

catalog = [phone1, phone2, phone3, phone4, phone5]

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")
