import requests
from pathlib import Path

#без функции

# path = 'C:\Yand_final_sprint\myconverter\mysite\files'
path = 'C:\\Yand_final_sprint\\myconverter\\mysite\\files'
# path2 = fr"{path}".replace('\\','\\\\')
# print(path, path2, path2==path)

files = []
for p in Path(path).rglob('*'):
    i = 1
    print(f' {i:} eto p : {str(p)}, type: {type(str(p))}')
    files.append(str(p.parent)+p.name)
    file_path = str(p.parent)+p.name
    ans_file = requests.post("http://127.0.0.1:8000/filmwork/",
                             {'title': f"test_api_{i}", 'certificate': f"test_api_{i}"},
                             files={'file_path': file_path})
    print(f"Answer is with load_file_to_model {ans_file.status_code}: {ans_file.json()}")
    i += 1



def load_file_to_model(path):
    #get path for all files in path directory
    files = []
    for p in Path(path).rglob('*'):
        # print(f' eto p : {str(p)}, type: {type(str(p))}')
        files.append(str(p.parent) + p.name)

    #write file to model
    # print(f' start write : {files}')
    try:
        for file in files:
            # print(str(file.replace("\\","\\\\")))
            i = 1
            fd = open(str(file), "rb")
            # print(f' etp fd : {fd}, eto str(file) : {str(file)}')
            # fields = ['id', 'title', 'certificate', 'file_path']

            ans_file = requests.post("http://127.0.0.1:8000/filmwork/", {'title': f"test_api_{i}", 'certificate': f"test_api_{i}"},
                                     files={'file_path': fd})
            print(f"Answer is with load_file_to_model {ans_file.status_code}: {ans_file.json()}")
            i +=1
            return True
    except Exception as e:
        print(f'  Exception in load_file_to_model : {e.args}')


if __name__ == '__main__':
    path = 'C:\\Yand_final_sprint\\myconverter\\mysite\\files'
    ## Функция не работает
    # load_file_to_model(path)

    files = []
    i = 1
    for p in Path(path).rglob('*'):
        print(f' {i:} eto p : {str(p)}, type: {type(str(p))}')

        file_path = str(p.parent) + p.name
        print(f'eto file_path :')
        print(file_path)
        ans_file = requests.post("http://127.0.0.1:8000/filmwork/",
                                 {'title': f"test_api_{i}", 'certificate': f"test_api_{i}"},
                                 files={'file_path': file_path})
        print(f"Answer is with load_file_to_model {ans_file.status_code}: {ans_file.json()}")
        i += 1

