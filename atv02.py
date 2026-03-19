print("SOMA")
def soma(lista):
  return sum(lista)

print(soma([1,2,3,4])) # 10
print(soma([5,6,7,8])) #26
print(soma([9,10,11,12])) #42

print("PARES")
def pares(lista):
  contador = 0
  for num in lista:
    if num % 2 == 0:
      contador += 1
  return contador
    
print(pares([1,2,3,4,5,6])) # 3
print(pares([8,9,10,11,12])) # 3
print(pares([13,14,15,16,17])) # 2

print("MAIOR")
def maior(lista):
  return max(lista)

print(maior([3,7,2,9,5])) # 9
print(maior([1,2,3,4,5])) # 5
print(maior([0,1,6,2,1,10])) #10

print("MAIOR QUE X")
def x(lista, x):
  contador = 0
  for num in lista:
    if num > x:
      contador += 1
  return contador

print(x([1,5,8,2,10], 5)) # 2
print(x([0,3,5,7,0], 2)) # 3
print(x([1,3,9,10,0], 8)) # 2

print("SOMA DE PARES")
def sumPares(lista):
  soma = 0
  for num in lista:
    if num % 2 == 0:
      soma += num
  return soma

print(sumPares([1,2,3,4,5,6])) # 12
print(sumPares([7,8,9,10,11,12])) # 30
print(sumPares([13,14,15,16,17])) # 30

print("EXISTE")
def existe(lista, x):
  for num in lista:
    if num == x:
      return True
  return False

print(existe([4,7,2,9], 7)) #True
print(existe([4,7,2,9], 1)) # False
print(existe([4,7,2,9], 9)) #True

print("PRODUTO")
def produto(lista):
  resultado = 1
  for num in lista:
    resultado *= num
  return resultado

print(produto([1,2,3,4])) # 24
print(produto([4,5,2,1])) # 40
print(produto([9,4,2,1])) # 72

