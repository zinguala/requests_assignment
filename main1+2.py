import requests                                            # for downloading the users list with .get(url) and .jason()


class MyUser:
    def __init__(self, _id, name, username, email):                        # inputs for MyUser's class
        self.id = _id                                                      # saves the id of the user in the class
        self.name = name                                                   # saves the name of the user in the class
        self.username = username                                           # saves the username of the user in the class
        self.email = email                                                 # saves the email of the user in the class

    def __str__(self):                           # to define what will be printed when we print the user in class MyUser
        return f'id: {self.id}, name: {self.name}, email: {self.email}'


res = requests.get('https://jsonplaceholder.typicode.com/users')          # used to request the users data from the url
downloaded_users_dict = res.json()                                  # for storing the list of dictionaries of the users.
user_objects = []                                                              # for storing list of our MyUser objects.

for user in downloaded_users_dict:              # for creating our MyUser objects and storing them at user_objects list.
    user_obj = MyUser(user['id'], user['name'], user['username'], user['email'])
    user_objects.append(user_obj)

while True:                                                                              # while for continues checking
    user_input = (input("enter name to check if exists in database : "))
    counter = 0                                                       # reset the counter for print if no matching user
    for user in user_objects:                    # for checking if one of the objects contain the name we want to check
        counter += 1                                                        # count 1 up  for print if no matching user
        if user_input.lower() in user.name.lower().split():  # to check if the input is equal to the first or last name
            print(f'Matching user found in the database {user.name}')
            print(user)
            counter = 0          # if one or more found equal reset the counter for not printing 'no matching user found

        elif len(user_objects) == counter:                             # if we checked all names and no equal name found
            print('no matching user found in the database')

    while True:                                                         # while for input if players want to check again
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
