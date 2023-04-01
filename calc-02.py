def checar_sintaxe():
    if expressao.count('(') != expressao.count(')'):
        print('A quantidade de parenteses está incorreta.')
    contador = 0
    for c in expressao:
        if c == '(':
            contador += 1
        if c == ')' and contador == 0:
            contador -= 1
        else:
            print('Fechamento de parenteses não aberto.')
        if c.isalpha():
            print('Não pode ter caracteres alfabéticos na expressão.')
    for i, c in enumerate(expressao):
        abertura = 0
        if c == '(':
            abertura = i
        if c == ')':
            e_atual = expressao[abertura:i]

expressao = str(input('Expressão matemática: '))
checar_sintaxe()
