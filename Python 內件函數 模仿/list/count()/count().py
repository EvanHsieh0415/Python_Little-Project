def count(l:list=None, v=None):
    if l == None:
        out = '[Input Error] list has not been entered'
    elif v == None:
        out = '[Input Error] Value has not been entered'
    else:
        out = 0
        for i in l:
            if i == v:
                out+=1
    return out