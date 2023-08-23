from mymodule.register import funcs

@funcs.register
def p():
    print('p')

@funcs.register('Hello World')
def hello_world():
    print('Hello World')
