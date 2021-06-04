import random

def verify(length=16):
    codes = ''
    for i in range(int(length)):
        codes += str(random.randint(0,9))
    return codes