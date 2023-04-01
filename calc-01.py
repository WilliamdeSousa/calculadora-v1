opcoes = ["Soma", "Subtração", "Multiplicação", "Divisão", "Sair"]
BARRA = '-=' * 17


def mostrar_opcoes():
	print(BARRA)
	print('    Calculadora - versão texto')
	print(BARRA)
	for n, opcao in enumerate(opcoes):
		print(f'[{n}] {opcao}')
	while True:
		try:
			print(BARRA)
			escolha = int(input('   Qual operação deseja fazer? '))
			if opcoes[escolha] is not None:
				return escolha
		except:
			print(BARRA)
			print(' Opção inválida. Tente novamente!')

def soma(sub=False):
	a = float(input('Digite um número: '))
	b = float(input('Digite outro número: '))
	if sub:
		b *= -1
	print(f'A soma vale {a + b}')

def multi():
	a = float(input('Digite um número: '))
	b = float(input('Digite outro número: '))
	print(f'O produto vale {a * b}')

def div():
	a = float(input('Digite o divisor: '))
	b = float(input('Digite o dividendo: '))
	print(f'A divisão vale {a / b}')


while True:
	operacao = mostrar_opcoes()
	print(BARRA)
	if operacao != opcoes.__sizeof__:
		print(f'  Operação: {opcoes[operacao]}')
		print(BARRA)
	if operacao == 0:
		soma()
	elif operacao == 1:
		soma(True)
	elif operacao == 2:
		multi()
	elif operacao == 3:
		div()
	elif operacao == 4:
		break
