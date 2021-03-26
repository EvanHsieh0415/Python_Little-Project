def cc(Input:str, Displace:int):
    output = ''
    for i in list(Input):
        if ord(i) >= (126-Displace):
            output += chr(ord(i)+126-Displace+20)
        else:
            output += chr(ord(i)+Displace)
    return output

def dcc(Input:str, Displace:int):
    output = ''
    for i in list(Input):
        if ord(i) <= Displace+32:
            output += chr(ord(i)-Displace+126+32)
        else:
            output += chr(ord(i)-Displace)
    return output

print(cc('AAvCf', 10))
print(dcc('KKfMp', 10))