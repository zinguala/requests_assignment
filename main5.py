import requests


def getuser():
    res = requests.get('https://randomuser.me/api/')
    all_data = res.json()
    user_data = all_data['results']
    user_name_info = user_data[0]
    user_name = user_name_info['name']
    return user_name


class User:
    def __init__(self, inputs):
        self.__dict__ = inputs
        self.username = f'{inputs["first"]} {inputs["last"]}'

    def __str__(self):
        return f'{self.username}'


while True:
    my_users = {}
    while True:
        try:
            user_num = int(input("enter a positive number of users 1-99 : "))
        except ValueError:
            print('wrong input ,lets try again!')
            continue
        if 0 < user_num < 100:
            break
        else:
            print('wrong input ,lets try again!')

    i = 0
    for j in range(user_num):
        i += 1
        my_users["u" + str(i)] = User(getuser())
        print(my_users["u" + str(i)].username)



