def betterPrint(string: str):
    if type(string) != str: string = str(string)
    tab = 0
    tabstr = '    ' #  '	'
    for index in range(len(string)):
        char = string[index]
        if char in '([{':
            print(char, end='')
            tab += 1
            print('\n', end=tabstr * tab)
        elif char in '}])':
            print()
            tab -= 1
            print(tabstr * tab, end=char)
        elif char == ',' and string[index + 1] == ' ':
            print(char)
            print(tabstr * tab, end='')
        elif char == ',':
            print(char)
            print(tabstr * tab, end='')
        else: print(char, end='')

if __name__ == '__main__':
    egdict = {
        i:{
            j:{
                k:0 for k in range(10)
            } for j in range(10)
        } for i in range(10)
    }
    betterPrint(str(egdict))