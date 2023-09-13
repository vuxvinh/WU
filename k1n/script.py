import requests
import time

server = ''
file_path=''

while True:
    try:
        with open(file_path, 'rb') as file:
            files = {'file': (file_path, file)}
            response = requests.post(server, files=files)
            if response.status_code == 200:
                print(response.text)
            else:
                print("false")
    except FileNotFoundError:
        print(f"Tệp tin {file_path} không tồn tại.")
    except Exception as e:
        print(f"Lỗi: {str(e)}")

    time.sleep(5)