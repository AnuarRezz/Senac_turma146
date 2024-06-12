'''Faça um programa de calculadora simples com as seguintes operações
possíveis: adição, subtração, multiplicação e divisão. O programa inicia
apresentando ao usuário um menu de opções como mostrado abaixo:

**********************************************************************
* Calculadora. Opções possíveis:
* 1. Adição
* 2. Subtração
* 3. Multiplicação
* 4. Divisão
* 5. Sair do programa
*********************************************************************
Informe a opção desejada:


A opção informada é então analisada e o programa executa a operação apropriada,
se a opção for inválida, informe ao usuário e peça a ele para entrar com uma
opção válida.
Após a execução da operação o programa volta a apresentar o menu inicial até
que o usuário encerre o programa com a opção 5.'''
opcao = 1

def adicao (num1, num2):
    resultado1 = num1 + num2
    return resultado1

def subtracao (num1, num2):
    resultado2 = num1 - num2
    return resultado2

def multiplicacao (num1, num2):
    resultado3 = num1 * num2 
    return resultado3

def divisao (num1, num2):
   resultado4 = num1 / num2 
   return resultado4

def exponenciacao (num1, num2):
    resultado5 = num1 ** num2
    return resultado5

def raiz_quadrada (num1):
    resultado6 = num1 ** 0.5 
    return resultado6

def porcentagem (num1, num2):
    resultado7 = num1 * num2 / 100
    return resultado7 

def resto_da_divisao (num1, num2):
    resultado8 = num1 % num2 
    return resultado8 

def divisao_por_inteiro (num1, num2):
    resultado9 = num1 // num2 
    return resultado9 


def menu ():
    print ("-----Escolha Operação Matematica------")
    print ("Seleciona uma operação")
    print ("1. adição")
    print ("2. Subtração")
    print ("3. Multiplicação")
    print ("4. Divisão")
    print ("5. Exponenciação")
    print ("6. Raiz quadrada")
    print ("7. Porcentagem")
    print ("8. Resto da divisão")
    print ("9. Divisão de inteiro")
    print ("0. Sair do programa ")
    print ("-" * 30)

while opcao != 0:
    menu()
    opcao = int(input("Informe qual opção desejada: "))
    if opcao < 0 or opcao > 9: 
        print("")
        print ("Opção Invalida")
        print ("")
        break
    match opcao: 
        case 0: 
            print ("Você saiu do programa")

        case 1: 
            print ("-----Adição-----")
            num1 = int(input("Informe o primeiro numero: "))
            num2 = int(input("Informe o segundo numero a ser somado: "))
            res = adicao(num1, num2)
            print("")
            print(f"{num1} + {num2} = {res}")
            print ("")
            print ("." * 30)
        case 2: 
            print ("------Subtração-----")
            num1 = int (input("Informe o primeiro numero: "))
            num2 = int(input("Informe o segundo numero: "))
            res = subtracao (num1, num2)
            print("")
            print (f"{num1} - {num2} = {res}")
            print("")
            print ("." * 30)
           
        case 3:
            print ("------Multiplicação------")
            num1 = int(input("Informe o primeiro numero: "))
            num2 = int(input("Informe o segundo Numero: "))
            res = multiplicacao (num1, num2)
            print("")
            print(f"{num1} X {num2} = {res}")
            print ("." * 30)
                
        case 4:
            print ("-----Divisão-----")
            num1 = int (input("Informe o primeiro numero: "))
            num2 = int (input("Informe o segundo numero: "))
            res = divisao (num1, num2)
            print("")
            print (f"{num1} / {num2} = {res}")
            print("")
            print ("." * 30)

        case 5: 
            print("------Exponenciação-----")
            num1 = int(input("Informe o primeiro numero: "))
            num2 = int(input("Informe o segundo numero: "))
            res = exponenciacao (num1, num2)
            print("")
            print (f"{num1} ** {num2} = {res}")
            print("")

        case 6:
            print("-----Raiz quadrada-----")
            num1 = int(input("Informe o numero: "))
            res = raiz_quadrada (num1)
            print (f"A Raiz quadrada de {num1} é {res}")
            print("")
            print ("." * 30)

        case 7: 
            print ("-----POrcentagem-----")
            num1 = int(input("Informe o numero: "))
            num2 = int(input("Informe a pocentagem desejada: "))
            res = porcentagem (num1, num2)
            print("")
            print (f"{num2} % de {num1} é {res}")
            print("")
            print ("." * 30)

        case 8: 
            print ("-----Resto da divisão-----")
            num1 = int(input("Informe o primeiro numero: "))
            num2 = int(input("Informe o segundo numero: "))
            res = resto_da_divisao (num1, num2)
            print("")
            print(f"O Resto da divisão de {num1} e {num2} é {res}")
            print ("." * 30)

        case 9: 
            print("-----Divisão por inteiros------")
            num1 = int(input("Informe o primeiro numero: "))
            num2 = int(input("Informe o segundo numero: "))
            res = divisao_por_inteiro (num1, num2)
            print ("")
            print (f"A divisão de inteiros entre {num1} e {num2} é {res}")
            print("")