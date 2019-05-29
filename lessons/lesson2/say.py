from logging import logging

@logging(level="DEBUG")
def say(something):
    print("say {}".format(something))


if __name__ == "__main__":
    say("Good bye")
