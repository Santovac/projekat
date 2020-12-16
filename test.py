from datetime import date

receipt = {
"id": "123",
  "seller": "S",
  "date": date(2020, 12, 16)
}

if(receipt['date'] >= date.today()): #.strftime("%d/%m/%Y")
  print(receipt)


#datetime_object = datetime.now()
#print(datetime_object)

'''
new_user = {
    "username": "",
    "password": "",
    "name": "",
    "lastname": ""
}'''