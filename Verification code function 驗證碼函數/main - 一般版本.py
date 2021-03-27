import random

def verify_func(longer, digit):
    try:
        longer = int(longer)
        digit = int(digit)
    except:
        print('數值輸入錯誤')
    else:
        while True:
            ch_l = []
            digit_long = digit
            digit_num = int('F'*digit, 16)
            for i in range(longer):
                ch_l.append(str(hex(random.randint(0, digit_num)).replace('0x', '')).zfill(digit_long))
            code = '-'.join(ch_l)
            print(code)
            input_code = input('請輸入驗證碼 > ')
            if input_code == code:
                print('輸入正確')
                return True
            else:
                print('輸入錯誤 將重新生成驗證碼')