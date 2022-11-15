from random import *
import time
while True:
	print("O sorteio será de números INTEIROS ou DECIMAIS?")
	time.sleep(1)
	print("Digite o número para escolher")
	time.sleep(1)
	print("""
		0 - Para o sorteador
		1 - Inteiros
		2 - Decimais
		""")
	codigo=int(input())
	if(codigo==0):
		time.sleep(1)
		print("Obrigado por usar o sorteador do Victor")
		time.sleep(1)
		break
	if(codigo<0 or codigo>2):
		print("Codigo inválido")
		time.sleep(2)
		continue
	if(codigo==1):
		print("Escolha o menor número do sorteio")
		menor=float(input())
		print("Escolha o maior número do sorteio")
		maior=float(input())
		print("o numero sorteado é:")
		print(randint(menor,maior)) #faixa de inteiro
	if(codigo==2):
		print("Escolha o menor número do sorteio")
		menor=float(input())
		print("Escolha o maior número do sorteio")
		maior=float(input())
		print("o numero sorteado é:")
		print(uniform(menor,maior)) #faixa de ponto flutuante
	time.sleep(3)