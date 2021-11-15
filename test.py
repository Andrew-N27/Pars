import requests
import json

temp_json = "https://www.marvel.com/v1/pagination/grid_cards?offset=36&limit=36&entityType=character&sortField=title&sortDirection=asc"
#response = requests.get(temp_json)


with open('Parss/test.json', 'r') as json_file:
    content = json_file.read()
    json_data = json.loads(content)

print(type(json_data))

for json_i in json_data:
    try:
        print(json_i['headline'])
    except:
        print('***** NO KEY FOUND *****')


# j = json.load(response) 

# for item in j:
#     print(item['headline'])


#print(response.json()['headline'])