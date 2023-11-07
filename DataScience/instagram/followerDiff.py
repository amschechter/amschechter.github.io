import requests
import json

#this is called 'instagram' cuz i was gonna try to use their API but it is too private so I just did some light potter stuff

print('helfwflo')

print('ok i will try to do some kind of follower diff project here i guess?? having trouble with API access.')

x = 6
y = 7
print (x * y)



response = requests.get("https://marauderapi.fr/api/characters")

characterDataJson = response.json()

characterDataJson = json.dumps(characterDataJson)

serialized = json.loads(characterDataJson)

charData = serialized["items"]

#print (serialized["items"])
print (charData)
print (serialized['items'][0]["house"])


#birthdates = serialized['items']['birthdate']

for id in charData:
    print (id['firstName'])