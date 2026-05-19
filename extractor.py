import requests

response = requests.get('https://jsonplaceholder.typicode.com/users')

estado = response.status_code

response_json = response.json()

print("El codigo de estado és:", estado)

print(response_json[0])