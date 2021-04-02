import random, time, os

def loading():
    per = 0
    while per < 100: 
        print(f'載入中 {per}%')
        time.sleep(random.choice([0.1, 0.3, 0.5]))
        per += random.randint(1, 7)
        os.system('cls')
    os.system('cls')
    print('載入完畢 100%')