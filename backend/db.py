import requests

url = 'https://reservation.documents.azure.com/dbs/outDatabase/colls/MyCollection/docs'
accessKey = 'type=master&ver=1.0&sig=J36LlamrQCVNgAuqMXxjc2h4XJv33ry3c5MYaGKHCQ6l8tGrUWrCSVFNyONKMHbMYCVLREsEQyYR33EtvXk7Sw=='
headers = {'Authorization': accessKey}

response = requests.post(url, headers=headers)

print(response.text)