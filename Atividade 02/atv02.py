print("1. Soma de elementos")
def soma(lista):
  return sum(lista)

print(soma([1,2,3,4])) # 10
print(soma([5,6,7,8])) #26
print(soma([9,10,11,12])) #42

print("---------------------------------------------")

print("2. Contar números pares")
def pares(lista):
  contador = 0
  for num in lista:
    if num % 2 == 0:
      contador += 1
  return contador

print(pares([1,2,3,4,5,6])) # 3
print(pares([8,9,10,11,12])) # 3
print(pares([13,14,15,16,17])) # 2

print("---------------------------------------------")

print("3. Maior número")
def maior(lista):
  return max(lista)

print(maior([3,7,2,9,5])) # 9
print(maior([1,2,3,4,5])) # 5
print(maior([0,1,6,2,1,10])) #10

print("---------------------------------------------")

print("4. Contar elementos maiores que um valor")
def x(lista, x):
  contador = 0
  for num in lista:
    if num > x:
      contador += 1
  return contador

print(x([1,5,8,2,10], 5)) # 2
print(x([0,3,5,7,0], 2)) # 3
print(x([1,3,9,10,0], 8)) # 2

print("---------------------------------------------")

print("5. Soma de pares")
def sumPares(lista):
  soma = 0
  for num in lista:
    if num % 2 == 0:
      soma += num
  return soma

print(sumPares([1,2,3,4,5,6])) # 12
print(sumPares([7,8,9,10,11,12])) # 30
print(sumPares([13,14,15,16,17])) # 30

print("---------------------------------------------")

print("6. Verificar a existência de elemento")
def existe(lista, x):
  for num in lista:
    if num == x:
      return True
  return False

print(existe([4,7,2,9], 7)) #True
print(existe([4,7,2,9], 1)) # False
print(existe([4,7,2,9], 9)) #True

print("---------------------------------------------")

print("7. Inverter lista")
def inverter(lista):
    nova_lista = []
    for i in range(len(lista)):
        nova_lista.append(lista[len(lista) - 1 - i])
    return nova_lista

print(inverter([1, 2, 3, 4])) # [4, 3, 2, 1]
print(inverter([5, 4, 0, 2, 10])) # [10, 2, 0, 4, 5]
print(inverter([-1, -2, -3, -4])) # [-4, -3, -2, -1]

print("---------------------------------------------")

print("8. Contar ocorrências")
def contar(lista, x):
  contador = 0
  for num in lista:
    if num == x:
      contador += 1
  return contador

print(contar([1, 2, 2, 3, 2, 4], 2)) # 3
print(contar([1, 2, 2, 3, 2, 4], 0)) # 0
print(contar([4, -2, 1, 0, 2, 4], 4)) # 2

print("---------------------------------------------")

print("9. Soma dos valores positivos")
def sumPositivos(lista):
  soma = 0
  for num in lista:
    if num > 0:
      soma += num
  return soma

print(sumPositivos([-1, 2, -3, 4, 5])) # 11
print(sumPositivos([0, -3, 4, 9, 0, -1])) # 13
print(sumPositivos([0, 0, 1, -9, -3, -1])) # 1

print("---------------------------------------------")

print("10. Produto dos elementos")
def produto(lista):
  produto = 1
  for num in lista:
    produto *= num
  return produto

print(produto([1, 2, 3, 4])) # 24
print(produto([0, -2, 3, 4])) # 0
print(produto([-1, 3, 2, 3])) # -18

print("---------------------------------------------")

print("11. Contar vogais")
def contarVogais(s):
  contador = 0
  for letra in s:
    if letra in "aeiouAEIOU":
      contador += 1
  return contador

print(contarVogais("Programacao")) # 5
print(contarVogais("Paralelepipedo")) # 7
print(contarVogais("Zebra")) # 2

print("---------------------------------------------")

print("12. Contar caracteres")
def contarCaracteres(s):
  contador = 0
  for letra in s:
    contador += 1
  return contador

print(contarCaracteres("teste")) # 5
print(contarCaracteres("Paralelepipedo")) # 14
print(contarCaracteres("Elementos")) # 9

print("---------------------------------------------")

print("13. Verificar palíndromo")
def palindromo(s):
  s = s.lower()
  
  inverter = ""
  for i in range(len(s)):
    inverter += (s[len(s) - 1 - i])
  return inverter == s

print(palindromo("Arara")) # True
print(palindromo("Casa")) # False
print(palindromo("Omississimo")) # True

print("---------------------------------------------")

print("14. Contar ocorrências de um caractere")
def ocorrencias(s, c):
  soma = 0

  for letra in s:
    if letra == c:
      soma += 1
  return soma

print(ocorrencias("banana", "a")) # 3
print(ocorrencias("omississimo", "s")) # 4
print(ocorrencias("paralelepipedo", "p")) # 3

print("---------------------------------------------")

print("15. Substituir caractere")
def substituir(s, c1, c2):
  string_nova = ""
  
  for letra in s:
    if letra == c1:
      string_nova += c2
    else:
      string_nova += letra
  return string_nova

print(substituir("banana", "a", "o")) # bonono
print(substituir("paralelepipedo", "p", "t")) # taraleletitedo
print(substituir("omississimo", "s", "r")) # omirrirrimo

print("---------------------------------------------")

print("16. Maiúsculas e minúsculas")
def maiusMinus(s):
  maiusculas = 0
  minusculas = 0

  for letra in s:
    if letra in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
      maiusculas += 1
    elif letra in "abcdefghijklmnopqrstuvwxyz":
      minusculas += 1
  return f"Maiúsculas: {maiusculas}, Minúsculas: {minusculas}"

print(maiusMinus("AbCde")) # 2, 3
print(maiusMinus("AECIOs")) # 5, 1
print(maiusMinus("oisdoDDD-1")) # 3, 5

print("---------------------------------------------")

print("17. Remover espaços")
def remover(s):
  string_nova = ""
  for letra in s:
    if letra != " ":
      string_nova += letra
  return string_nova

print(remover("ola mundo")) # olamundo
print(remover("subi no onibus")) # subinoonibus
print(remover("1 2 3 4 5")) # 12345

print("---------------------------------------------")

print("18. Primeiro caractere")
def primeiro(s):
  if s == "":
    return None
  return s[0]

print(primeiro("python")) # p
print(primeiro("Omissíssimo")) # O
print(primeiro("")) # None