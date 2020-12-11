from datetime import datetime

racun = {
"sifra": "123",
  "prodavac": "S",
  "datum_vreme": ""
}
racun['datum_vreme'] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
print(racun)

'''
new_user = {
    "username": "",
    "password": "",
    "name": "",
    "lastname": ""
}'''