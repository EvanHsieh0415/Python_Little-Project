def upper(Str:str):
    out = ''
    for i in Str:
        In = ord(i)
        if In in range(65, 91):
            out += i
        elif In in range(90, 123):
            out += chr(In-32)
    return out