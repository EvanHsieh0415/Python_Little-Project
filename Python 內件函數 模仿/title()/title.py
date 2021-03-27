def title(Str:str):
    listStr = list(Str)
    out = ''
    for i in range(len(listStr)):
        In = ord(listStr[i])
        if i == 0 and In in range(90, 123):
            out += chr(In-32)
        else:
            out += listStr[i]
    return out