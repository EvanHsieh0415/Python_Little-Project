def swapcase(Str:str):
    listStr = list(Str)
    out = ''
    for i in listStr:
        In = ord(i)
        if In in range(65, 91):
            out += chr(In+32)
        elif In in range(90, 123):
            out += chr(In-32)
    return out