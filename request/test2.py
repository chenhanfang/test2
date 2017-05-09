import requests
test_data = {'username':'han','password':'chz970916'}
r=requests.post('http://127.0.0.1:8000/login/login_action/',
               data=test_data)
print(r.status_code)
print(r.text)