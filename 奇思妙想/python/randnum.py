# randomnum.py in school

# initialize
# Import Random
from random import randint as ri
# max
max = 62
min = 1

login = input('请按回车键继续...\n')
if login != 'login account':
    while True:
        account_name = input('Please input the name for account')
        if (account_name == 'root') or (account_name == 'admin'):
            account_password = input(f'please input the password of the admin account {account_name} ')
            if account_password == 'randnum.py':
                print(f'Login successful!\n\nYou can change the var of max and min.\n\nmax: {max}\nmin: {min}\n')
                input('Input ri to generate random numbers, or\nInput max to change max num, or\nInput min to change min num.\n')
                pass
            else:
                print('Worng Password!')
                login = False

n = int(input('请输入抽取人数:'))

# Pemissions

for i in range(1,n+1):
    t = ri(min,max)
    while (t == 46) or (t == 19):
        t=ri(min,max)
    print(f'恭喜 {t} 号成为第 {i} 个抽中的同学!')
