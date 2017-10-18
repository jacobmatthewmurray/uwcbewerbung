import random
import string
import json
from datetime import date

# Function to Generate Random Text


def getRandomText(l):
    s = string.letters
    s += '       '
    t = ''
    for i in range(random.randrange(1, l, 1)):
        t += random.choice(s)
    return t

# Function to Generate Random Date


def getRandomDate():
    start_date = date.today().replace(day=1, month=date.today().month - 1).toordinal()
    end_date = date.today().toordinal()
    return date.fromordinal(random.randint(start_date, end_date))

# Fixture for Kontakt


d = []
for i in range(1, 1000):
    data = {}
    data['model'] = 'orgmgm.kontakt'
    data['pk'] = i
    data['fields'] = {
        'vorname': 'Vorname' + str(i),
        'nachname': 'Nachname' + str(i),
        'email': 'name' + str(i) + '@host.com',
        'organisation': random.randrange(1, 400, 1)
    }
    d.append(data)

with open('kontakt.json', 'w') as f:
    json.dump(d, f, indent=4)


# Fixture for Activity

d = []
for i in range(1, 1000):
    data = {}
    data['model'] = 'orgmgm.activity'
    data['pk'] = i
    data['fields'] = {
        'titel': 'Titel' + str(i),
        'activitydate': str(getRandomDate()),
        'description': getRandomText(300),
        'activitytype': random.randrange(1, 4, 1),
        'organisation': random.randrange(1, 400, 1),
        'kontakt': random.randrange(1, 1000, 1),
    }
    d.append(data)

with open('activity.json', 'w') as f:
    json.dump(d, f, indent=4)


# Fixture Update for Organisation

d = json.loads(open('organisation.json').read())

for i in d:
    i['fields']['organisationtype'] = 1
with open('organisation.json', 'w') as f:
    json.dump(d, f, indent=4)

