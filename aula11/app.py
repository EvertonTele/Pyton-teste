 #Colocando \033[m no final ele corta a pintura. 
# print('\033[4;30;45molá mundo\033[m ')



# Outra possibilidade, letra branca fundo preto 
# print('\033[37molá mundo\033[m ')



# Invertando letra branca fundo preto
# print('\033[7;30molá mundo\033[m ')


# Letra amarela fundo azul 
# print('\033[7;33;44molá, mundo\033[m ')

# Outro exemplo
# O resultado cada um tem uma cor diferente. 
# a = 3
# b = 5
# print('Os valores são \033[32m{} e \033[31m{}'.format(a, b)) 


# caso queira cancelar a cor do e conforme acima. 
# a = 3
# b = 5
# print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m!!!'.format(a, b)) 


# Outra forma de colocar cor pelo format
nome = 'Everton'
print('Oá! Muito prazer em te conhecer, {}{}{}!!!'.format('\033[4;34m', nome, '\033[m'))

