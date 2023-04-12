import requests                # for downloading the users list with .get(url) and .jason()


class SpeedUser:
    def __init__(self, d):     # input for SpeedUser's class
        self.name = d['name']
        self.username = d['username']
        self.address = d['address']

    def lat(self):                           # for calling the .lat() function to receive float for checking the object
        geo = self.address['geo']              # geo is help variable because lat is inside another value of dictionary
        return float(geo['lat'])           # return the float value of lat, so we can do math functions with the output

    def __str__(self):                       # to define what will be printed when we print the user in class SpeedUser
        return f'name: {self.name}, username: {self.username}, address: {self.address} '


def nearestuser(input_lat, objects):                                 # near user function to check the nearest user,lat
    nearest_lat = objects[0].lat()                           # loading the first user's lat in the nearest lat variable
    nearest_user = objects[0]                                     # loading the first user in the nearest user variable
    counter = 0                              # counter for print the nearest user and lat  if no equal user's lat found
    for user in objects:                                           # for checking all SpeedUser objects for nearest lat
        counter += 1                                               # counter 1 up
        if input_lat == user.lat():                        # if input lat = user checked lat print the lat and the user
            print(f'Matching lat found in the database {user.lat()}')
            print(user)
            counter = 1            # if matching lat found reset the counter for not printing 'no matching lat found'

        elif abs(user_input - user.lat()) < abs(user_input - nearest_lat):  # if no matching lat found check the nearest
            nearest_lat = user.lat()                 # save the current lat if he is more close than the saved user lat
            nearest_user = user                      # save the current user if he is more close than the saved user

    if len(user_objects) == counter:                       # when finish checking if no matching found print the nearest
        print('no matching lat found in the database')
        print(f'the nearest lat is : {nearest_lat}')
        print(nearest_user)


user_objects = []    # for storing list of our SpeedUser objects.
i = 0          # counter for adding number to the url to go over all the users one by one
while True:
    i += 1          # start from one, and 1 up every round
    res = requests.get('https://jsonplaceholder.typicode.com/users/' + str(i))  # request for download the user data
    downloaded_user_dict = res.json()      # to store the dictionary of the user data
    if downloaded_user_dict:       # if downloaded_user_dict contains data --> true
        user_obj = SpeedUser(downloaded_user_dict)     # if true store SpeedUser object of the user
        user_objects.append(user_obj)                  # if true add the object we just stored to the objects list
    else:
        break            # if the downloaded_user_dict is empty--->false and stop the while with break

while True:            # while for continues checking until the user want to stop checking
    try:               # input the name we want to check
        user_input = float((input("enter lat to check if exists in database : ")))
    except ValueError:                 # exception for value check, for wrong input try again
        print('wrong input ,lets try again!')
        continue

    nearestuser(user_input, user_objects)    # executing the lat check with user input and list of all objects

    while True:  # while for input if players want to check again
        recheck = input('want to check again? y/n : ')
        if recheck in ['y', 'n']:
            break
        else:
            print('Type y or n')
            continue
    if recheck == 'n':
        break
    elif recheck == 'y':
        continue
