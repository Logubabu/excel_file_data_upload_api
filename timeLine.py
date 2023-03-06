import pandas as pd
import requests

input_data = r"D:\PEN INDIA\automation\Timeline for Dravida Munnetra Kazhagam.xlsx"
resp_df = pd.read_excel(input_data)
df = resp_df.dropna(subset=['Description'])


def upload_images(df):
    # Upload images to strapi server and add respective ids to input file and save
    df = df.to_dict('records')

    _id = []
    upload_url = 'http://localhost:1337/api/upload'
    for data in df:
        if pd.isna(data["Image Link"]):
            _id.append(None)
        else:
            path = r'./Timeline - Gallery/' + data["Image Link"]

            files = {'files': (path, open(path, 'rb'), 'image', {'uri': ''})}
            res = requests.post(upload_url, files=files)
            _id.append(res.json()[0]["id"])
            print(res.status_code)

    df = pd.DataFrame(df)
    df["id"] = _id

    df.to_excel("./new_file.xlsx")

    return df


def upload_entries(df):
    entries = []
    df['Year'] = df['Year'].ffill()
    df = df.fillna("")
    df = df.to_dict('records')
    for _i, item in enumerate(df, 1):
        entries.append({
            "data": {
                'title': str(item["Headline"]),
                'year': str(int(item["Year"])),
                'description': str(item["Description"]),
                "image": str(item['id'])
            }
        })
    for data_item in entries:
        post_url = "http://localhost:1337/api/timeline"
        res = requests.post(post_url, json=data_item)
    return res


img = upload_images(df)
newfile_df = pd.read_excel("./new_file.xlsx")
entry_df = upload_entries(newfile_df)
