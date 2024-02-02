#import requests

#url = 'http://127.0.0.1:8000/upload-image'
#files = [('files', open('twopeople.jpg', 'rb')), ('files', open('fivepeople.jpg', 'rb'))]
#files = ['file', open('twopeople.jpg', 'rb')]
#resp = requests.post(url=url, files=files) 
#print(resp.json())


import requests

url = 'http://127.0.0.1:8000/upload-image'
file_path = "twopeople.jpg"

# Open the file and send a POST request with the file attached
with open(file_path, "rb") as file:
    files = {"file": (file_path, file)}
    response = requests.post(url, files=files)

# Print the response
print(response.status_code)
print(response.json())