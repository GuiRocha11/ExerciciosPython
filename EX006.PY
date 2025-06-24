num = int(input('Numero: '))
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))

for i in range(inicio,fim+1 ):
    print(f'Tabuada ', num, ' X ', i, '=', (num*i))