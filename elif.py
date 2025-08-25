# idade = int(input("digite sua idade: "))
# if idade >= 0 and idade < 16:
#     print("você é menor de idade") 
# elif idade > 16:
#     print ("você é menor de idade")
# elif idade > 16 and idade <= 17:
#     print("voto opcional")
# elif idade >= 18:
#     print("voto obrigatório")
# else:
#     print("error")


#     1-Você foi contratado para desenvolver um sistema simples de pagamento online. O sistema deve
# identificar o método de pagamento escolhido pelo usuário e exibir a mensagem correspondente:

pagamento = str(input("escolha a forma de pagamento: cartâo ou boleto: "))
if pagamento == 'cartão':
    print("Processando pagamento no cartão...")
elif pagamento == "boleto":
    print("Gerando boleto bancário...")
else:
    print("Método de pagamento não reconhecido.")


# 2-Crie um programa que solicita a idade de uma pessoa e classifica-a em uma das seguintes
# categorias:

idade = int(input("digite sua idade: "))
if idade > 0 and idade <= 12:
    print("criança")
elif idade >= 13 and idade <= 17:
    print("adolescente")
elif idade >= 18 and idade <= 59:
    print("adulto")
elif idade >= 60:
    print("idoso")
else:
    print("valor irreconhecido")


# 3-Uma loja online permite que seus clientes escolham entre dois tipos de entrega:

entrega = str(input("escolha o tipo de entrega: padrão ou expresso: "))
if entrega == "padrão":
    print("a entrega padrão custa R$10,00.")
elif entrega == "expresso":
    print("a entrega expresso custa R$20,00.")
else:
    print("Opção de entrega inválida")