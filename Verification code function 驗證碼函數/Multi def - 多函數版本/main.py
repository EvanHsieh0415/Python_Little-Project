import random
import json

def verify_setting(ctx, setType:str, limit:int):
    with open('.\\settings\\verification.json', mode='r', encoding='utf8') as verifySetFile:
        verifySetData = json.load(verifySetFile)
    if setType == 'longer':
        verifySetData[ctx.guild.id]['longe'] = limit
    elif setType == 'digit':
        verifySetData[ctx.guild.id]['digit'] = limit
    print(f'{ctx.member.name} - {ctx.member.id} Set {setType}: {limit}')
    fb = f'Set {setType}: {limit}'
    return fb

def get_verifyCode(ctx):
    with open('.\\verification_data\\data.json', mode='r', encoding='utf8') as verifyFile:
        verifyData = json.load(verifyFile)
    with open('.\\settings\\verification.json', mode='r', encoding='utf8') as verifySetFile:
        verifySetData = json.load(verifySetFile)
    longer = verifySetData[ctx.guild.id]['longer']
    digit = verifySetData[ctx.guild.id]['digit']

    ch_l = []
    digit_num = int('F'*digit, 16)
    for i in range(longer):
        ch_l.append(str(hex(random.randint(0, digit_num)).replace('0x', '')).zfill(digit))
    fb = '-'.join(ch_l)

    try:
        verifyData[ctx.member.id]['count'] += 1
    except:
        verifyData[ctx.member.id]['count'] = 1
    else:
         verifyData[ctx.member.id]['verCode'] = fb
    finally:
        with open('.\\verification_data\\data.json', mode='w', encoding='utf8') as verifyDataFile:
            json.dump(verifyDataFile, verifyData, sort_keys=True, indent=4)

    print(f'{ctx.member.name} - {ctx.member.id} Get VerCode: {fb}')
    return fb

def enter_verifyCode(ctx, enterCode):
    with open('.\\verification_data\\data.json', mode='r', encoding='utf8') as verifyDataFile:
        verifyData = json.load(verifyDataFile)
    cc = verifyData[ctx.member.id]['verCode']
    if cc == enterCode:
        fb = True
        print(f'{ctx.member.name} - {ctx.member.id} successfully verified -\n>>> Verification code')
    else:
        print(f'{ctx.member.name} - {ctx.member.id} enter error -\n>> correct code: {cc}\n>> enter code: {enterCode}')
        get_verifyCode()
        fb = False
    return fb