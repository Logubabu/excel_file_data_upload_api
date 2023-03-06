import pandas as pd
import requests
import json

input_data = r"D:\PEN INDIA\automation\Manifesto.xlsx"

post_url = "http://localhost:1337/api/manifesto-promises"
df = pd.read_excel(input_data)
df = df.to_dict('records')
new_df = []
for i in range(len(df)):
    # print(i)
    item = df[i]
    new_df.append({
        "data": {
            'number': str(int(item["Manifesto Number "])),
            'category': str(item["Manifesto Category "]),
            'poll_promise': str(item["Poll Promise"]),
            'department': str(item["Department"]),
            'status': str(item["Manifesto Status "]),
            'source': str(item["Source 1"])
        }
    })
new_df = pd.DataFrame(new_df)
final_data = dict()
final_data = new_df.to_dict("records")

for i in range(len(final_data)):
    # print(data)
    data_item = final_data[i]
    print(data_item)

    # headers = {'Content-Type': 'application/json'}
    res = requests.post(post_url, json=data_item)

    print(res.text)
