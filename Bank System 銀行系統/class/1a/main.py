class bank:
    def __init__(self):
        self.accountDict = {}
    
    def check(self, email, password):
        if email not in self.accountDict:
            return 'EmailNotFound'
        if self.accountDict[email]['password'] != password:
            return 'PasswrodError'
        return None

    def create(self, email, password, name):
        if email in self.accountDict:
            return 'EmailUsed'
        if not name:
            return 'NameNull'
        self.accountDict[email] = {'name': name, 'password': password, 'deposit': 0}
        return 'CreateSuccessful'
    
    def delete(self, email, password):
        check = bank.check(email, password)
        if check:
            return check
        confirm = input(f'是否確定刪除{self.accountDict[email]["name"]}( True/False ): ')
        if confirm == 'True':
            del self.accountDict[email]
            return 'ActionSuccessful'
        if confirm == 'False':
            return 'ActionCancel'
        return 'UnknowAction'
    
    def save(self, email, password, amount):
        check = bank.check(email, password)
        if check:
            return check
        if amount.isdigit():
            amount = int(amount)
            self.accountDict[email]['deposit'] += amount
            return 'SaveSuccessful'
        return 'AmountEnterError'
    
    def take(self, email, password, amount):
        check = bank.check(email, password)
        if check:
            return check
        if amount.isdigit():
            amount = int(amount)
            if self.accountDict[email]['deposit'] < amount:
                return 'DepositNotEnough'
            self.accountDict[email]['deposit'] -= amount
            return 'TakeSuccessful'
        return 'AmountEnterError'
    
    def balance(self, email, password):
        check = bank.check(email, password)
        if check:
            return check
        return self.accountDict[email]['deposit']

bank = bank()

def output(string:str):
    stringDict = {
        # Null
        'EmailNull': '[Error] 請輸入E-mail',
        'PasswordNull': '[Error] 請輸入密碼',
        'NameNull': '[Error] 請輸入帳戶名稱',
        'AmountNull': '[Error] 請輸入金額',
        
        # Account Error
        'EmailNotFound': '[Error] 資料庫內無此E-mail',
        'EmailUsed': '[Error] E-mail已使用',
        'PasswrodError': '[Error] 密碼輸入錯誤',

        # Action
        'ActionSuccessful': '操作成功',
        'ActionCancel': '[Error] 操作取消',
        'UnknowAction': '[Error] 未知的操作',
        'SaveSuccessful': '成功存入銀行帳戶',
        'TakeSuccessful': '取款成功',

        # Amount
        'AmountEnterError': '[Error] 金額輸入錯誤',

        # Deposit
        'DepositNotEnough': '[Error] 存款不足',

        # Account
        'CreateSuccessful': '帳戶創建成功'
    }
    return stringDict[string]

def line():
    print('='*100)

line()
print('歡迎來到芒果銀行！！！\n若您是新用戶，請先創建帳戶 輸入"create"）\n刪除帳戶 請輸入"delete"\n存款 請輸入"save"\n取款 請輸入"take"\n離開此系統 請輸入"leave"')
line()

tragger = True
while tragger:
    action = input('輸入您要進行的操作: ')
    if not action:
        print('[Error] 請輸入操作名稱')
        line()
        continue
    if action not in ('create', 'delete', 'save', 'take', 'leave'):
        print('[Error] 請輸入正確的操作')
        line()
        continue
    if action == 'leave':
        print('程式關閉')
        tragger = False
    if action in ('create', 'delete', 'save', 'take'):
        email = input('請輸入E-mail: ')
        if not email:
            print(output('EmailNull'))
            line()
            continue
        password = input('請輸入密碼: ')
        if not password:
            print(output('PasswordNull'))
            line()
            continue
        if action in ('save', 'take'):
            amount = input('請輸入金額: ')
            if not amount:
                print(output('AmountNull'))
                line()
                continue
        if action == 'create':
            name = input('請輸入使用者名稱: ')
            out = bank.create(email, password, name)
        elif action == 'delete':
            out = bank.delete(email, password)
        elif action == 'save':
            out = bank.save(email, password, amount)
        elif action == 'take':
            out = bank.take(email, password, amount)
        print(output(out))
        if out in ('SaveSuccessful', 'TakeSuccessful', 'DepositNotEnough'):
            print(f'存款餘額: {bank.balance(email, password)}')
    line()

input('Press any key to continue . . .')