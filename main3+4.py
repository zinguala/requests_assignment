import requests


class SpeedUser:
    def __init__(self, d):
        self.__dict__ = d
        self.id = d['id']
        self.name = d['name']
        self.username = d['username']
        self.address = d['address']

    def lat(self):
        geo = self.address['geo']
        return float(geo['lat'])

    def __str__(self):
        return f'{self.__dict__}'


user_objects = []
i = 0
while True:
    i += 1

    res = requests.get('https://jsonplaceholder.typicode.com/users/' + str(i))
    downloaded_user_dict = res.json()
    if downloaded_user_dict:
        user_obj = SpeedUser(downloaded_user_dict)
        user_objects.append(user_obj)
    else:
        break


for i in range(len(user_objects)):
    print(user_objects[i])

while True:
    try:
        user_input = int((input("enter lat to check if exists in database : ")))
    except ValueError:
        print('wrong input ,lets try again!')
        continue

    counter = 0                              # counter for print if no matching user
    for user in user_objects:                # for checking
        counter += 1
        lat = user.lat()
        if user_input == lat:
            print(f'Matching lat found in the database {user.name}')
            print(user)
            counter = 0
        else:
            nearest_lat = lat = user.lat()
            nearest_user = user.__str__()

        if len(user_objects) == counter:
            print('no matching lat found in the database')
            print(f'the nearest is : {nearest_user}')
