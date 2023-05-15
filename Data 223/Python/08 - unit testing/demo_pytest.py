# expected string input "1,000"
# remove comma and convert to int


def convert_string_to_int(string):
    # convert string to int removing any commas in the string
    my_number = int(string.replace(',', ''))
    return my_number



def add(a, b):
    return a + b


# input is dict, return the keys of the dictionary
# if input is not dictionary, then return an error message

def get_dict_keys(my_dict):
    '''
    Function to get the keys from a dictionary
    input = dict
    output = list of keys or error message if dictionary


    '''
    if type(my_dict) is not dict:
        return "Error: NOT A DICTIONARY"
    
    
    return list(my_dict.keys())

