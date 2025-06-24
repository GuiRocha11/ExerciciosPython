n1 = int(input("Informe a primeira nota: "))
n2 = int(input("Informe a segunda nota: "))

media = (n1 + n2) / 2 

if media >= 7:
    print(f"Você está em aprovado com media: {media}")
elif media <=5:
    print(f"Você está reprovado com media: {media}")
else:
    print(f"Você está de recuperação com media {media}")