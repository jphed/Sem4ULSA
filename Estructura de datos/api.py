import requests

response = requests.get('https://randomuser.me/api/')
data = response.json()

# Access the first result
user = data['results'][0]

# Print the required details
print('Name:', user['name']['first'], user['name']['last'])
print('Gender:', user['gender'])
print('Nationality:', user['nat'])