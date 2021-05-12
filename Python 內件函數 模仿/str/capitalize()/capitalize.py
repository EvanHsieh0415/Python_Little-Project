def capitalize(Str:str):
    out = ''
    for i in range(len(Str)):
        In = ord(Str[i])
        if i == 0 and In in range(90, 123):
            out += chr(In-32)
        else:
            if i == 0 or In not in range(65, 91):
                out += Str[i]
            else:
                out += chr(In+32)
    return out