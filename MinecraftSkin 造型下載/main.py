from json import loads
from requests import get
from base64 import b64decode

while True:
    mcid = input('Minecraft ID:') or -1
    try:
        uuid = loads(get(url=f'https://api.mojang.com/users/profiles/minecraft/{mcid}').content.decode('UTF-8'))
    except:
        print('ID 不存在')
    else:
        skinbase64 = loads(get(url=f'https://sessionserver.mojang.com/session/minecraft/profile/{uuid["id"]}').content.decode('UTF-8'))['properties'][0]['value']
        skin = loads(b64decode(skinbase64))
        filename = f'{mcid}.png'
        with open(filename, mode='wb') as pic:
            pic.write(get(skin['textures']['SKIN']['url']).content)
        print(f'{filename} 已成功創建')