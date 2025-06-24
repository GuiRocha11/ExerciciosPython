#Faça um programa para uma caixa eletrônica. O programa deverá 
#perguntar ao usuário o valor do saque e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão de 1, 5, 10, 50 e 100 reais. 
#O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.

#Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas 
#notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
#Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece 
#notas três de 100, uma nota de 50, quatro notas de 10, uma nota de 
#5 e quatro notas de 1.


valor = int(input("Digite o valor do saque (entre 10 e 600): "))

if valor < 10 or valor > 600:
        print("Valor inválido! O saque deve ser entre 10 e 600 reais.")
else:
        nota100 = valor // 100
        resto = valor % 100

        nota50 = resto // 50
        resto = resto % 50

        nota10 = resto // 10
        resto = resto % 10

        nota5 = resto // 5
        resto = resto % 5

        nota1 = resto

        print(f"Para sacar R$ {valor}, serão fornecidas:")
        
        if nota100 > 0:
            print(f"{nota100} nota(s) de R$ 100")
        if nota50 > 0:
            print(f"{nota50} nota(s) de R$ 50")
        if nota10 > 0:
            print(f"{nota10} nota(s) de R$ 10")
        if nota5 > 0:
            print(f"{nota5} nota(s) de R$ 5")
        if nota1 > 0:
            print(f"{nota1} nota(s) de R$ 1")







