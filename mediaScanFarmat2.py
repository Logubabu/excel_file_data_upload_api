import pandas as pd
import requests

input_data = r"D:\PEN INDIA\automation\Media Scan Tools & Tech 2023.xlsx"

post_url = "http://localhost:1337/api/media-scans"

xl = pd.ExcelFile(input_data)

sheet_names = xl.sheet_names  # see all sheet names

excel_sheets = pd.read_excel(input_data, sheet_name=None, header=1)
for sheet, df in excel_sheets.items():
    # sheet = sheet_names[0]
    print(sheet)
    date = pd.to_datetime(sheet)
    df = df.ffill(axis=0)
    df = df.to_dict('records')
    entries = []
    for item in df:
        entries.append({
            "data": {
                'entity': str(item["Party / Person"]),
                'link': str(item["News Header + Hyperlink"]),
                'constituency': str(item["Constituency"]),
                # 'summary': str(""),
                # 'publication': str(""),
                'reception': str(item["Proponent's Media Reception "]),
                'date': date.strftime("%Y-%m-%d"),
                # 'date': datetime.fromtimestamp(int(date.strftime("%Y/%m/%d"))),
            }
        })
    for data_item in entries:
        print(data_item)
        # headers = {'Content-Type': 'application/json'}
        res = requests.post(post_url, json=data_item)
        print(res.text)