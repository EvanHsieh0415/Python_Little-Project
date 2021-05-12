def index(l:list=None, v=None):
    if l == None:
        out = '[Input Error] list has not been entered'
    elif v == None:
        out = '[Input Error] Value has not been entered'
    else:
        il = []
        for i in range(len(l)):
            if v == l[i]:
                il.append(i)
        if len(il) == 0:
            out = f'Could not find {v} in {l}'
        else:
            if len(il) == 1:
                out = il[0]
            elif len(il) >= 2:
                out = il
            else:
                out = 'Function Error: Exceptional output'
    return out