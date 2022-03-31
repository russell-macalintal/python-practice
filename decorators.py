# Write basic Python function using Decorators
# Brute force way of writing DECORATOR FUNCTIONS
def new_decorator(simple_func):
    def wrap_func():
        print('This is extra code BEFORE the wrapped function')
        simple_func()
        print('This is extra code AFTER the wrapped function')
    return wrap_func                                        # returns wrapped function

def undecorated_func():
    print('This is the simple function that will be decorated.')


if __name__ == '__main__':
    decorated_func = new_decorator(undecorated_func)        # assigns returned wrap_func to pointer variable
    decorated_func()                                        # runs pointer function
    print('Success')