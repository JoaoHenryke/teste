"""


Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).


"""

#1º Faça um Programa que mostre a mensagem "Alo mundo" na tela.

#print("olá mundo")

#2º Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].
"""
num = input("Digite um numero: ")

print("O numero digitado foi:", num)
"""
# 3ºFaça um Programa que peça dois números e imprima a soma.

"""
num1 = int(input("Digite um numero: "))
num2 = int(input("Digite seu numero: "))

soma = num1 + num2

print("O resultado é = ",soma)


# 4º Faça um Programa que peça as 4 notas bimestrais e mostre a média.


nota1 = float(input("Digite uma nota: "))
nota2 = float(input("Digite uma nota: "))
nota3 = float(input("Digite uma nota: "))
nota4 = float(input("Digite uma nota: "))

soma_nota = nota1 + nota2 + nota3 + nota4
media = soma_nota / 4

print(media) # print para deterinar a quantidade de casas decimais que será impresso na saida do codigo "%.2f" % media.

# 5º Faça um Programa que converta metros para centímetros.

q_metros = float(input("Digite uma quantidade em metros para ser convertido em cenimetros: "))

converte = q_metros * 100

print(converte,"cm")


# 6º Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

valor_raio = float(input("Digite o valor do raio d circulo: "))

pi = 3.14

area = pi * valor_raio ** 2

print(f"Area equivale á = {area:.2f}")


# 7º Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

print("Lembrando que, como o quadrado tem lados iguas o valor da base será o mesmo do valor da altura.")

valor_base = float(input("Digite o valor da base do quadrado:  "))
valor_altura = float(input("Digite o valor da altura d quadrao: "))

area_quadrado = valor_base * valor_altura


print(f"A area do quadrado equivale á = {area_quadrado:.2f}")



# 8º Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
print("Para saber o valor da sua hora trabalhada, basta pegar o valor final do seu salario e dividir pela quantidade de dias trabalhado no mês e depois pegar as horas dias trabalhada e divider pela diaria de um dia de serviço")


valor_hora = float(input("Digite o valor da sua hora trabalhada no mês: "))
horas_trabalhadas = float(input("Digite a quantidade de horas trabalhadas: "))

valor_salario = valor_hora * horas_trabalhadas

print(f"Seu salario equivale a: $,{valor_salario:.2f}")

# 9º Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius, C = 5 * ((F-32) / 9).

# tc/5 = tf - 32 / 9

TF = float(input("Digite o valor da temperatuda em Fahrenheit: "))

TC1 = (TF - 32) / 9 

Tc2 = TC1 * 5

print(f"valor cº = {Tc2:.2f}")

# 10º Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit?

Tf = float(input("Digite a temperatura em celsius: "))

Tc1 = Tf * 1.8 + 32

print(f"Cº = {Tc1:.1f}")


# 11º Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:

n1= int(input("Informe um numero inteiro"))

n1 = int(input("Informe mais outro numero inteiro: "))

nr = int(input("Informe um numero real: "))

#   a) o produto do dobro do primeiro com metade do segundo .
produto_dobro = (n1 * 2) * (n2 / 2) 
print(produto_dobro)

#   b) a soma do triplo do primeiro com o terceiro.

soma = (n1 *3) + 3
print(soma)


#   c)o terceiro elevado ao cubo.

res = nr*3
print(res)


# 12º Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

altura = float(input("Informe sua altura: "))

peso = (72.7 * altura) - 58

print(f"Seu peso é igual á: {peso:.2f}")

# 13º  Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#   Para homens: (72.7*h) - 58
#   Para mulheres: (62.1*h) - 44.7

altura = float(input("Informe sua altura: "))

peso = (62.1 * altura) - 58

print(f"Seu peso é igual á: {peso:.2f}")


# 14º João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de 
# peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. 
# João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além 
# do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.

#50 dia permitido, caso exceda essa valor multa de $4,00 reais o valor.

peso_peixe = float(input("Informe a quantidade de kilos de peixe pescada: "))

q_permitido = 50 # quantdade de kilos de pexe a serem pescadas por dia.

excesso_peso = peso_peixe - 50 #variável responsavél por determina de excedu a quantidade de peso conrrespondente a 50 kilos.

valor_multa = excesso_peso * 4 #variavél responsável por calcula o valor da multa por excesso de peso

if peso_peixe <= 50:
    print("Você não pagará multa, a quantidade pescada está dentro do estabelacido.")

elif peso_peixe > 50: 
    print(f"a quantidade de peso excedido foi de {excesso_peso:.2f} kg Pagará de multa = {valor_multa:.2f}")

else:
    print("erro, tente novamente.")
"""
"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o 
total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% 
para o sindicato, faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido.
"""
hr_dia = float(input("Infome o valor da sua hora trabalhada:$ "))
hr_mes = float(input("Infome a quantidade de horas trabalhadas no mês: "))


# dados para teste: 
# hr_dia = 7.06
# hr_mes = 200
# totalizando = 1.412,19 

# Algumas resaltas do sistema. 
# - 11% de imposto de renda do salário
# - 8% para INSS
# - 5% para o sindicato
# formula para executar a funcão type, e verificar a classe do dado selecionado.
salario = hr_dia * hr_mes

impt_renda = salario * 0.11
# Representação da porcentagem em programação, 11% e a mesma coisa de 11/100.
# No caso acima coloquei entre parentese para ter prioridade , então quando o cófigo for inicia a linha, o prieiro a ser executado sera o oporação de porcentagem entre pararentese.
# Resultado com os dados do teste = 
inss = impt_renda * 0.8
# resultado com os dados teste = 1411.81
sindicato = salario * 0.5

print (f"Salario equivale á = r$ {salario:.2f}")  #Salário Bruto : R$ %.2f' %salario
print(f"Disconto do imposto de renda = R${impt_renda:.2f} ")
print ("Disconto do inss = R$ %.2f", salario) #Outra forma de apresenta saida de com controle de casas decimais.
print ("")

print("olaá João")