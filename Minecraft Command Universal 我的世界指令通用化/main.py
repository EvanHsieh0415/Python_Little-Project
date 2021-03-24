yes = ['y', 'yes']
no = ['n', 'no']
while True:
    command = input('Command > ')
    if command.startswith('/'):
        command = command.replace('/', '')
    command = '/execute run ' + command
    print('轉換完成')
    print(command)
    while True:
        keep = input('繼續修改?(Y/N) > ')
        if keep.lower() in yes or keep.lower() in no:
            break
        else:
            print('請輸入Yes 或是 No (無視大小寫)')
    if keep.lower() in no:
        break