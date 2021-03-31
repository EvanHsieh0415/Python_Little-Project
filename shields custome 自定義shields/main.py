import urllib 
sL = ['plastic', 'flat', 'flat-square', 'for-the-badge', 'social']
url_startswith = ['https://', 'http://']

print(r'[![ {Name} ](https://img.shields.io/badge/ {Title} - {Index} - {Color} ?style= {Style} )]( {URL} )')
print(f'/nStyle: {sL}')

def URL_encode(url:str):
    return urllib.parse.quote(url)

while True:
    url_t = False
    Name = input('img name> ')
    Title = URL_encode(input('Title> '))
    Index = URL_encode(input('Index> '))
    Color = input('Color> ')
    while True:
        Style = input('Style> ')
        if Style not in sL:
            print(f'style {Style} is not found')
        else:
            break
    while True:
        URL = input('URL> ')
        for i in url_startswith:
            if URL.startswith(i) is True:
                url_t = True
                break
        if url_t == True:
            break
        else:
            print('URL format wrong')
    out = f'[![{Name}](https://img.shields.io/badge/{Title}-{Index}-{Color}?style={Style})]({URL})'
    print(out)
    print('\n','='*50,'\n', sep='')
    input()