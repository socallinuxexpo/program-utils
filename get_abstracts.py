import xmltodict
import requests
from html.parser import HTMLParser

class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.strict = False
        self.convert_charrefs= True
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()

url='http://socallinuxexpo.org/scale/19x/sign.xml'
schedule = requests.get(url).content

doc = xmltodict.parse(schedule)

for talk in doc['nodes']['node']:
  if talk['Topic'] != "BoFs":
    print('##')
    print(talk['Title'])
    print(strip_tags(talk['Time']),"-",talk['Room'])
    if talk['Speakers'] != "None" and talk['Speakers'] != None:
        print(talk['Speakers'])
    else:
        print("")

    if talk['Topic'] != None:
        print(talk['Topic'])
    else:
        print("")
    print(strip_tags(talk['Short-abstract']).strip())