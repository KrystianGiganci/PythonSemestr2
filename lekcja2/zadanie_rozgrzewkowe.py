from uzytkownik import Uzytkownik

user1 = Uzytkownik()
user1.imie = 'Jan'
user1.nazwisko = 'Kowalski'
user1.wiek = 32

user2 = Uzytkownik()
user2.imie = 'Adam'
user2.nazwisko = 'Nowak'
user2.wiek = 45

user3 = Uzytkownik()
user3.imie = 'Piotr'
user3.nazwisko = 'Murarz'
user3.wiek = 12

user4 = Uzytkownik()
user4.imie = 'Marek'
user4.nazwisko = 'Kowal'
user4.wiek = 73

user5 = Uzytkownik()
user5.wyswietl_info()
user5.zmien_wiek(33)
user5.wyswietl_info()
# user1.wyswietl_info()
# user2.wyswietl_info()
# user3.wyswietl_info()
# user4.wyswietl_info()

# user1.zmien_wiek(23)
# user1.wyswietl_info()