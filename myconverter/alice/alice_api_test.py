import requests
string = 'Зеленая миля'
answer = requests.get(f"http://127.0.0.1:8002/api/v1/alice_api/find_actor_in_fake_db/?{string}")
# answer = requests.get(f"http://127.0.0.1:8002/api/v1/alice_api/find_actor_in_fake_db/", string)
print(f' eto answer.json : {answer.json()}')