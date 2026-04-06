import time

lista = [int(x) for x in open('Atividade 04/Quick Sort/arq.txt').read().split()]

print("Algoritmo: Quick Sort")

def quickSort(lista):
  if len(lista) <= 1:
    return (lista)
  
  pivot = lista[-1]

  items_maiores = []
  items_menores = []

  for item in lista[:-1]:
    if item > pivot:
      items_maiores.append(item)
    else:
      items_menores.append(item)
  return quickSort(items_menores) + [pivot] + quickSort(items_maiores)

tempos = []

for i in range(5):
  inicio = time.time()
  resultado = quickSort(lista)
  fim = time.time()

  tempo = fim - inicio
  tempos.append(tempo)

  print(f"Execução: {i + 1}: {tempo:.7f}s")

with open('Atividade 04/Quick Sort/arq-ordenado.txt', 'w') as ordenado:
    for numero in resultado:
        ordenado.write(f"{numero} ")

media = sum(tempos) / len(tempos)

print(f"Média: {media:.7f}s")
