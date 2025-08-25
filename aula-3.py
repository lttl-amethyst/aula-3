# n1 = float(input("digite o 1º valor: "))
# n2 = float(input("digite o 2º valor: "))
# print ("a soma dos valores é: ", n1 + n2)
# print ("a subtração dos valores é: ", n1 - n2)
# print ("a multiplicação dos valores é: ", n1 * n2)
# print ("a divisão dos valores é: ", n1 / n2)

# ano_nascimento = int(input("digite o ano que nasceu: "))
# ano_atual = int(input("digite o ano atual: "))
# idade = ano_atual - ano_nascimento
# print(f"você tem", idade, "anos")


# Questão 1 – Número positivo ou negativo

n = int(input("digite um valor: "))
if n >= 0:
 print("número positivo ou zero")
else:
 print("número negativo")


# Questão 2 – Login simples

senha =  int(input("digite a senha: "))
if senha == 1234:
 print("acesso permitido")
else:
 print("acesso negado")


# Questão 3 – Par ou Ímpar

n = int(input("digite um número: "))
if n %2 == 0:
    print("o número é par")
else:
    print("o número é ímpar")


# Questão 4 – Nota de aprovação

nota = int(input("digite sua nota: "))
if nota >= 6:
    print("aprovado")
else:
    print("reprovado")