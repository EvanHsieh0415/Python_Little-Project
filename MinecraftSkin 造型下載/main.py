from json import loads
from requests import get
from base64 import b64decode
from datetime import datetime
from time import sleep

def now(): return datetime.now().strftime("%Y%m%d%H%M%S")

print('='*100, '輸入-1關閉系統', '本系統由芒果凍布丁製作', '有問題請至Discord找本作者: YT Mango#4092', 'Github: https://github.com/EvanHsieh0415', '本著作使用創用CC授權 CC BY-NC-ND 3.0 TW', '='*100, sep='\n')

while True:
    mcid = input('Minecraft ID:') or 0
    if not mcid:
        print('請輸入ID')
        continue
    if mcid == '-l':
        print('已關閉系統')
        break
    try:
        uuid = loads(get(url=f'https://api.mojang.com/users/profiles/minecraft/{mcid}').content.decode('UTF-8'))
    except:
        print('ID 不存在')
    else:
        skinbase64 = loads(get(url=f'https://sessionserver.mojang.com/session/minecraft/profile/{uuid["id"]}').content.decode('UTF-8'))['properties'][0]['value']
        skin = loads(b64decode(skinbase64))
        filename = f'{now()}_{mcid}.png'
        with open(filename, mode='wb') as pic:
            pic.write(get(skin['textures']['SKIN']['url']).content)
        print(f'{filename} 已成功創建')
    sleep(1)