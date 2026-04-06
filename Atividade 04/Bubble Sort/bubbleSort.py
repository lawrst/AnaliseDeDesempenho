import time

lista = [int(x) for x in open('Atividade 04/Bubble Sort/arq.txt').read().split()]
tamanho = len(lista)

print("Algoritmo: Bubble Sort")

tempos = []

for i in range(5):
  inicio = time.time()
  lista_copia = lista.copy() 

  for posicao in range(tamanho - 1):
    for comparar in range(tamanho - 1 - posicao):
      if lista_copia[comparar] > lista_copia[comparar + 1]:
        lista_copia[comparar], lista_copia[comparar + 1] = lista_copia[comparar + 1], lista_copia[comparar]
  fim = time.time()

  tempo = fim - inicio
  print(f"Execução {i + 1}: {tempo:.7f}s")
  tempos.append(tempo)

with open('Atividade 04/Bubble Sort/arq-ordenado.txt', 'w') as ordenado:
    for numero in lista_copia:
        ordenado.write(f"{numero} ")
      
media = sum(tempos) / len(tempos)

print(f"Média: {media:.7f}s")