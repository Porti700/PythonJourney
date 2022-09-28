import requests

dict = {
    "name" : "Kevin",
    "job" : "Programmer"
}
r_example = requests.post('https://reqres.in/api/users', json = dict)
print(f"Status Code: {r_example.status_code}, Response: {r_example.json()}")