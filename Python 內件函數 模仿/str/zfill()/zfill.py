def zfill(Str:str, width:int):
    out = '0'*(width-len(Str)) + Str
    return out