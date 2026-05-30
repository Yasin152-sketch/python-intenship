def My_decorator(fucn) :
    def wrapper() :
       return fucn().upper()
    return wrapper


@My_decorator
def Upper_case() :
    return "hello world!"

print(Upper_case())
