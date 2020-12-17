from datetime import date
import json
from json import JSONEncoder

path = 'database/json_test.json'

def load():
    with open(path, encoding='utf-8') as f:
        return json.load(f)

def save(bundles_new):
    with open(path, "w", encoding='utf-8') as f:
        json.dump(bundles_new, f, ensure_ascii=False, indent=4, cls=DateTimeEncoder)

test = load()
#test[0]['expiry'] = date(2020, 12, 16)

# subclass JSONEncoder
class DateTimeEncoder(JSONEncoder):
    # Override the default method
    def default(self, obj):
        if isinstance(obj, (date)):
            return obj.isoformat()

print("Printing to check how it will look like")
print(DateTimeEncoder().encode(test))

#print("Encode DateTime Object into JSON using custom JSONEncoder")
#testJSONData = json.dumps(test, indent=4, cls=DateTimeEncoder)
#print(testJSONData)

save(test)
test = load()
print('after changes: ',test)

'''
receipt = {
"id": "123",
  "seller": "S",
  "date": date(2021, 12, 16),
 "expiry": date(2021, 12, 16)
}

if(receipt['date'] >= date.today()): #.strftime("%d/%m/%Y")
  print(receipt['date'])
  print(receipt['expiry'])

#datetime_object = datetime.now()
#print(datetime_object)
'''