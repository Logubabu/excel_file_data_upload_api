import pandas as pd
import requests
import json

input_data = r"D:\PEN INDIA\automation\Party Frontal Members\Party Frontals - English.xlsx"

post_url = f'http://localhost:1337/api/party-wings'
df = pd.read_excel(input_data)
df = df.to_dict('records')
entries = []
for i in range(len(df)):
    # print(i)
    item = df[i]
    entries.append({
        "data": {
            'number': str(int(item["Manifesto Number "])),
            'category': str(item["Manifesto Category "]),
            'poll_promise': str(item["Poll Promise"]),
            'department': str(item["Department"]),
            'status': str(item["Manifesto Status "]),
            'source': str(item["Source 1"])
        }
    })
    entry = {
        "locale": "en",
        "name": item["Name"],
        "position": item["Party Position"],
        "wing_name": item["Wing"]
    }

for data_item in entries:
    res = requests.post(post_url, json=data_item)
