import requests
print("Getting the list of all questions")
ans = requests.get("http://127.0.0.1:8000/polls/question/")
print(f"Answer is {ans.status_code}: {ans.json()}")
print("Adding a new question")
ans = requests.post("http://127.0.0.1:8000/polls/question/", json={'question_text': "New question"})
print(f"Answer is {ans.status_code}: {ans.json()}")


# fd = open("myconverter/mysite/files/тест.mp4", "rb")
fd = open("C:\\Yand_final_sprint\\myconverter\\mysite\\files\\тест.mp4", "rb")

ans_file = requests.post("http://127.0.0.1:8000/questions/", {'question_text': "With file"}, files={'file_path': fd})
print(f"Answer is {ans_file.status_code}: {ans_file.json()}")