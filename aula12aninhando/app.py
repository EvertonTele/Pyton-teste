# Condição Simples

# nome = str(input('Qual o seu nome? '))
# if nome == 'Everton':
#     print('Que nome bonito!')
# print('Tenha um bom dia {}!'.format(nome))





#  estrutura condicional  composta 

# nome = str(input('Qual o seu nome? '))
# if nome == 'Everton':
#     print('Que nome bonito!')
# else:
#     print('Seu nome é bem normal.')
# print('Tenha um bom dia {}!'.format(nome))
 



# # Estrutura condicional Aninhada 

# nome = str(input('Qual o seu nome? '))
# if nome == 'Everton':
#     print('Que nome bonito!')
# elif nome == 'Pedro ' or nome == 'Maria' or nome == 'Paulo':
#     print('Seu nome é bem popular no Brasil.')
# else:
#     print('Seu nome é bem normal.')
# print('Tenha um bom dia {}!'.format(nome))





# Estrutura condicional Aninhada com mais de 4 possibilidades 

nome = str(input('Qual o seu nome? '))
if nome == 'Everton':
    print('Que nome bonito!')
elif nome == 'Pedro ' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Cláudia Jessica Juliana':
    print('Belo nome feminino ')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia {}!'.format(nome))



