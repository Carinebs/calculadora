primeiro_numero = int(input("Digite seu primeiro número: "))
segundo_numero = int(input("Digite seu segundo número: "))
print("""Se você deseja somar digite - 1 
Se você deseja subtrair digite - 2
10Se você deseja multplicar digite - 3 
Se você deseja dividir digite - 4""")
operacao = int(input())

def Soma(primeiro_numero, segundo_numero):
    return primeiro_numero + segundo_numero

def Subtracao(primeiro_numero, segundo_numero):
    return primeiro_numero - segundo_numero

def Multiplicacao(primeiro_numero, segundo_numero):
    return primeiro_numero * segundo_numero

def Divisao(primeiro_numero, segundo_numero):
    return primeiro_numero / segundo_numero

if operacao == 1 :
    print(Soma(primeiro_numero, segundo_numero))
if operacao == 2 :
    print(Subtracao(primeiro_numero, segundo_numero))
if operacao == 3 :
    print (Multiplicacao(primeiro_numero, segundo_numero))
if operacao == 4 :
    print(Divisao(primeiro_numero, segundo_numero))


    



