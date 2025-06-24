vetor = [1,3,5,7,9,11]

frutas = ['maca', 'banana', 'pera']

print(vetor)
print(frutas)

print(vetor[4])
print(frutas[1])
#insere
vetor.append(200)
print(vetor)
frutas.append('manga')
print(frutas)
#remove
vetor.remove(vetor[1])
print(vetor)

print(len(vetor))
print(len(frutas))

for item in vetor:
    print(item)

for item in frutas:
    print(item)