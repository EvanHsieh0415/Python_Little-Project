def pop(l:list=None, index:int=None):
    if l == None:
        out = '[Input Error] list has not been entered'
    elif index == None:
        out = '[Input Error] Index has not been entered'
    else:
        out = []
        for i in range(len(l)):
            if i == index:
                continue
            else:
                out.append(l[i])
    return out