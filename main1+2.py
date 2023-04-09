import requests


class MyUser:
    def __init__(self, _id, name, username, email):
        self.id = _id
        self.name = name
        self.username = username
        self.email = email

    def __str__(self):
        return f'id: {self.id}, name: {self.name}, email: {self.email}'


res = requests.get('https://jsonplaceholder.typicode.com/users')
downloaded_users_dict = res.json()
user_objects = []

for user in downloaded_users_dict:
    user_obj = MyUser(user['id'], user['name'], user['username'], user['email'])
    user_objects.append(user_obj)

for i in range(len(user_objects)):
    print(user_objects[i])

while True:
    try:
        user_input = (input("enter name to check if exists in database : "))
    except ValueError:
        print('wrong input ,lets try again!')
        continue

    for user in user_objects:
        if user_input.lower() in user.name.lower().split():
            print(f'there is user name in the databas {user.name}')

