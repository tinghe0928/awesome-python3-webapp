#! /usr/bin/env python3

from datetime import datetime


def get_time():
    print(datetime.now())


def log(func):
    def deco(*args,**kw):
        print(func.__name__)
        get_time()
        return func(*args, **kw)
    return deco

def log_with_level(level):
    def wrapper(func):
        def innner_wrapper(*args,**kw):
            print("[{}]: Enter function {}".format(level, func.__name__))
            return func(*args,**kw)
        return innner_wrapper
    return wrapper
    


@log_with_level(level="INFO")
def say_hello():
    print("this is a hello")

@log_with_level(level="DEBUG") 
def say_hi():
    print("this is a hello")



if __name__ == "__main__":
    say_hi()
    say_hello()
