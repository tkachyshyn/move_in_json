'''
this module helps the user to move
in the json file
'''
import json

def open_file(path):
    '''
    open file and convert data into
    dictionary
    '''
    f = open(path)
    data = json.load(f)
    return data

lst = []

def keys(data):
    '''
    help the user to choose keys and to
    move within them in the dictionary
    '''
    for key in data:
        print(key)
    choice = str(input())
    lst.append(choice)
    try:
        new_data = data[lst[-1]]
        try:
            if type(new_data) == dict or\
            type(new_data[0]) == dict:
                if type(new_data[0]) == dict:
                    new_data = new_data[0]
                print("This is a dictionary. Do you want to continue?(y/n):")
                yes_no_option = str(input())
                if yes_no_option == 'y':
                    try:
                        keys(new_data)
                    except TypeError:
                        return new_data[lst[-1]]
        except TypeError:
            return new_data
        return new_data
    except KeyError:
        print("That is a wrong key. Please, enter the right one:\n")
        keys(data)
print(keys(open_file('move_in_json/friends.json')))
