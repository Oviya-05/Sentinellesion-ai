import requests

url = 'http://127.0.0.1:5000/predict'
# Replace 'test_image.jpg' with the name of an actual image in your folder
files = {'file': open('test_image.jpg', 'rb')}

response = requests.post(url, files=files)
print(response.json())