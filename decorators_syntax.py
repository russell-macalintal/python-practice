# Write basic Python function using Decorators
# Writing DECORATOR FUNCTIONS for '@' syntax use -- can easily be commented out to add/remove the decorator
def new_decorator(simple_func):
    def wrap_func():
        print('This is extra code BEFORE the wrapped function')
        simple_func()
        print('This is extra code AFTER the wrapped function')
    return wrap_func


if __name__ == '__main__':
    @new_decorator                          # This line can easily be commented out to add/remove the decorator
    def undecorated_func():
        print('This is the simple function that will be decorated.')

    undecorated_func()
    print('Success')