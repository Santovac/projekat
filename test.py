from datetime import date,datetime
import json

now = datetime.now().isoformat()
print('DATETIME:', now)
print('DATE:', date.today())
print('DATETIME:', datetime.fromisoformat(now))

'''
path = 'database/json_test.json'

def load():
    with open(path, encoding='utf-8') as f:
        return json.load(f)

def save(bundles_new):
    with open(path, "w", encoding='utf-8') as f:
        json.dump(bundles_new, f, ensure_ascii=False, indent=4)

test = load()
x = date.fromisoformat(test[0]['expiry'])
y = date.fromisoformat(test[1]['expiry'])
z = date.fromisoformat(test[2]['expiry'])

print('Test loaded = ', test)
xy = int(input('year='))
xm = int(input('month='))
xd = int(input('day='))
x=date(xy, xm, xd)
y=date(2021, 1, 31)
z=date(2020, 12, 25)
test[0]['expiry'] = x.isoformat()
test[1]['expiry'] = y.isoformat()
test[2]['expiry'] = z.isoformat()

save(test)
#test = load()
#print('after changes: ',test)
'''


'''
from datetime import date
import json
from json import JSONEncoder
import dateutil.parser


# custom Decoder
def DecodeDateTime(empDict):
   if 'expiry' in empDict:
      empDict["expiry"] = dateutil.parser.parse(empDict["expiry"])
      return empDict

path = 'database/json_test.json'

def load():
    with open(path, encoding='utf-8') as f:
        return json.load(f, object_hook=DecodeDateTime)

def save(bundles_new):
    with open(path, "w", encoding='utf-8') as f:
        json.dump(bundles_new, f, ensure_ascii=False, indent=4, cls=DateTimeEncoder)

test = load()
print('Test loaded = ', test)
test[0]['expiry'] = date(2021, 12, 16)
test[1]['expiry'] = date(2020, 12, 31)
# subclass JSONEncoder
class DateTimeEncoder(JSONEncoder):
    # Override the default method
    def default(self, obj):
        if isinstance(obj, (date)):
            return obj.isoformat()

save(test)
#test = load()
#print('after changes: ',test)
'''