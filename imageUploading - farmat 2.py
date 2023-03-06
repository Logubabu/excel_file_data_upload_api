import requests

# img_path = r"D:\PEN INDIA\automation\image upload\IMG_7289.jpg"
# img1 = r"D:\PEN INDIA\automation\image upload\24.jpg.jpg"
# img2 = r"D:\PEN INDIA\automation\image upload\karunanidhi.jpg"
img_path = [
    r"D:\PEN INDIA\automation\image upload\24.jpg.jpg",
    r"D:\PEN INDIA\automation\image upload\karunanidhi.jpg"
]

upload_url = 'http://localhost:1337/api/upload'
post_url = 'http://localhost:1337/api/party-wings/294'
_id = []
for img in img_path:

    files = {'files': (img, open(img, 'rb'), 'image', {'uri': ''})}
    res = requests.post(upload_url, files=files)
    # id = res.json()[0]["id"]
    _id.append(res.json()[0]["id"])
    print(res.status_code)
payload = {
    "data": {
        "image": _id,
    }
}
resp = requests.put(post_url, json=payload)

print(resp.status_code)
print(resp.text)
print("finish")
