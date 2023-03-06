import pandas as pd
import requests
import json

input_data = r"D:\PEN INDIA\automation\Party Frontal Members\Party Frontals - English.xlsx"

df = pd.read_excel(input_data)
df = df.to_dict('records')
failed = []
for i, item in enumerate(df, 1):
    print(i, item)
    post_url = f'http://localhost:1337/api/party-wings/{item["ID"]}/localizations'

    entry = {
        "locale": "en",
        "name": item["Name"],
        "position": item["Party Position"],
        "wing_name": item["Wing"]
    }
    # print(entry)
    res = requests.post(post_url, json=entry)
    # print(res.text)
    if res.status_code != 200:
        failed.append(item['ID'])

    # print("finish")
print(failed)
