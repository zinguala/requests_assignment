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

    counter = 0                              # counter for print if no matching user
    for user in user_objects:                # for checking
        counter += 1
        if user_input.lower() in user.name.lower().split():
            print(f'Matching user found in the database {user.name}')
            counter = 0

        elif len(user_objects) == counter:
            print('no matching user found in the database')






