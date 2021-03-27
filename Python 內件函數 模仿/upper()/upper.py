def upper(Str:str):
    listStr = list(Str)
    out = ''
    for i in listStr:
        In = ord(i)
        if In in range(65, 91):
            out += i
        elif In in range(90, 123):
            out += chr(In-32)
    return out