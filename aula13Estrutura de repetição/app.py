# print('oi')
# print('oi')
# print('oi')
# print('oi')
# print('oi')
# print('oi')
# para simplifica em laço de repetição darei os seguintes comando:
# for c in range(1,6): #repetição de 5x repetição de 5x ou seja ele vai de 1 até 5
#     print('oi') #repetindo o print ('oi')
# print('fim') # o fim do laço de repetição 

# # Colocando 0 ao invés de 1
# for c in range(0,6): #repetição de 5x repetição de 5x ou seja ele vai de 1 até 5
#     print('oi') #repetindo o print ('oi')
# print('fim') # o fim do laço de repetição 

# Outra forma 
# Colocando 0 ao invés de 1
# for c in range(0, 6): #repetição de 5x ou seja ele vai de 1 até 5
#     print(c) # Se no lugar de oi colocarmos C ele dara de 0 a 5 em números 
# print('fim') # o fim do laço de repetição


# for c in range(6, 0, -1): #Fazendo contagem regressiva de 6 a 1 
#     print(c) # Se no lugar de oi colocarmos C ele dara de 0 a 5 em números 
# print('fim') # o fim do laço de repetição

# for c in range(6, 0, 2): #Fazendo contagem de 0 até 7 pulando de 2 em 2 ou seja ficará 0, 2, 4, 6 fim 
#     print(c) # Se no lugar de oi colocarmos C ele dara de 0 a 5 em números 
# print('fim') # o fim do laço de repetição

# Outro exemplo:
# n = int(input('Digite um número: '))
# for c in range(0, n+1): #Utilizo o N como parte de passgem opara o for. 
#     print(c)
# print('FIM')

# Outro exemplo:
# i = int(input('Inicio: ')) # começando a ler o inicio 
# f = int(input('Fim: ')) # Leio o Fim 
# p = int(input('Passo: ')) # leio o passo. 
# for c in range(i, f+1, p):
#     print(c)
# print('FIM')
# # se eu colocar de 1 até 100 pulando de 10 em 10 ele me dará 1, 11, 21 e assim vai

# # Exemplo:
# for c in range(0,3):
#     n = int(input('Digite um valor: '))
# print('Fim')
# # O comando que eu dei está dentro de um for, ou seja vou repetir 3x  um valor. 

# Exemplo fazendo um somátorio com os números. 
s = 0
for c in range(0,4):
    n = int(input('Digite um valor: '))
    s += n
print('O somatório de todos os valores foi {}'.format(s))
