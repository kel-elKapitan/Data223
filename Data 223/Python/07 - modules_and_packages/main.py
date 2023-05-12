

# how to keep certain parts only for the module itself
print("For this module __name__ will be {}".format(__name__))
print('Before imports')

import second_module
from second_module import second_func

print('After imports')


print('before calling second_func() using second_module.second_func()')
print(second_module.second_func())


print('This is before calling second_main module directly using second_func()')

print(second_func())
print('End of second func() call')

print('End of program')


# code inside here can only be used for this module
# cannot be used by other modules
# this is useful for testing
# this is useful for running code only when the module is run directly
if __name__ == "__main__":
    print("for the second module __name__ will be {}".format(__name__))



def main():

    print("main is called")

    return 1