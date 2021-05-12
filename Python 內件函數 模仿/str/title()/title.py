def title(Str:str):
    out = ''
    for i in range(len(Str)):
        if ord(Str[i]) in range(90, 123):
            out += chr(ord(Str[i]-32))
        else:
            out += Str[i]
    return out