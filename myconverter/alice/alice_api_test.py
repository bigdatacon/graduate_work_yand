import requests
string = 'Зеленая миля'


answer = requests.get(f"http://127.0.0.1:8002/api/v1/alice_api/find_actor_in_fake_db/?input_actor={string}")
print(f' eto answer.json for actor : {answer.json()}')

# не работает
# answer = requests.get(f"http://127.0.0.1:8002/api/v1/alice_api/find_actor_in_fake_db_json/?input_actor={string_dict}")
# print(f' eto answer.json for actor : {answer.json()}')

string_dict = {'actor' : 'Зеленая миля'}
url = 'http://127.0.0.1:8002/api/v1/alice_api/find_actor_in_fake_db_json/'
response = requests.request("GET", url,  params=string_dict)
print(f' eto response.json for actor : {response.json()}')

#2 просто возвращаю fake_films_db
answer = requests.get(f"http://127.0.0.1:8002/api/v1/alice_api/return_film_data/")
print(f' eto answer.json all objects: {answer.json()}: {answer.json()}')