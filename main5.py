import requests                                            # for downloading the users list with .get(url) and .jason()


def getuser():                           # function for getting user with get request from 'https://randomuser.me/api/'
    res = requests.get('https://randomuser.me/api/')                       # request for download and save the user data
    all_data = res.json()                                                     # to store the dictionary of the user data
    user_data = all_data['results']                                           # to save the list value of the result key
    user_name_info = user_data[0]                                                          # to save the dictionary info
    user_name = user_name_info['name']                                             # to save the 'name' dictionary value
    return user_name                                                               # return the username dictionary info


class User:
    def __init__(self, inputs):                                                          # inputs for SpeedUser's class
        self.username = f'{inputs["first"]} {inputs["last"]}'                           # saves the username of the user

    def __str__(self):                                                           # print the username for print function
        return f'{self.username}'


user_num = int                                                                        # initialize the variable user_num
while True:                                                                                            # while for input
    my_users = {}                                                              # dictionary for storing the User objects
    while True:                                                        # while for check if player placed a num in range
        try:                                                                             # input the num of user we want
            user_num = int(input("enter a positive number of users 1-99 : "))
        except ValueError:                                        # exception for value check, for wrong input try again
            print('wrong input ,lets try again!')
            continue
        if 0 < user_num < 100:                                      # check if player placed a num in range if yes break
            break
        else:
            print('wrong input ,lets try again!')

    i = 0                             # index for adding str to the variable name saved in the key in my_user dictionary
    for j in range(user_num):                                                            # for creating the User objects
        i += 1                                                                           # index 1 up
        my_users["u" + str(i)] = User(getuser())                        # saves key and creating User object for the Key
        print(my_users["u" + str(i)])                                                                # print the object
