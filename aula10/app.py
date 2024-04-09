# Condição simples  
# nome = str(input('Qual o seu nome? '))
# if nome == 'Everton':
#     print('Que nome lindo você tem! ')
# print('bom dia {}'.format(nome))



# Outra forma, condição composta 
# nome = str(input('Qual o seu nome? '))
# if nome == 'Everton':
#     print('Que nome lindo você tem! ')
# else:
#     print('Seu nome é tão normal! ')
# print('bom dia {}'.format(nome))


# n1 = float(input('Digite a primeira nota: '))
# n2 = float(input('Digite a segunda nota: '))
# m = (n1 + n2)/2
# print('A sua média foi {:.1f}'.format(m))
# if m >= 6.0:
#     print('Sua média foi boa! PARABÈNS! ')
# else:
#     print('Sua média foi ruim ESTUDE MAIS! ')


# Outra forma condição Simplificada 
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('A sua média foi {:.1f}'.format(m))
print('PARABÈNS' if m >=6 else 'Estude MAIS! ')