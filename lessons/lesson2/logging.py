#! /usr/bin/env python3

class logging(object):

    def __init__(self, level="INFO"):
        self.level = level

    def __call__(self, func):
        def wrapper(*k,**kw):
            print("[{}]: This is function {}".format(self.level,func.__name__))
            return func(*k, **kw)
        return wrapper

