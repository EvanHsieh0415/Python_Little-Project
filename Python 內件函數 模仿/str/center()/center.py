def center(Str:str, fillchar:int, char:str=' '):
    out = char*(fillchar//2) + Str + char*(fillchar//2)
    return out