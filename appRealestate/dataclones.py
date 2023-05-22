import requests,json

import requests

url = "https://bayut.p.rapidapi.com/properties/list"

querystring = {"locationExternalIDs":"5002,6020","purpose":"for-rent","hitsPerPage":"25","page":"0","lang":"en","sort":"city-level-score","rentFrequency":"monthly","categoryExternalID":"4"}

headers = {
	"X-RapidAPI-Key": "6cb10cae22mshe83ac21e4eb1de3p1897c1jsn0b3893d5488f",
	"X-RapidAPI-Host": "bayut.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)


with open("properties.json") as f:
  data = json.load(f)