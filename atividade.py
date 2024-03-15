"""
Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
C = 5 * ((F-32) / 9).
Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
o produto do dobro do primeiro com metade do segundo .
a soma do triplo do primeiro com o terceiro.
o terceiro elevado ao cubo.
Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58
Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7
João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.

Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
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
"""

# 6º Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

valor_raio = float(input("Digite o valor do raio d circulo: "))

pi = 3.14

area = pi * valor_raio ** 2

print("Area equivale á = ", area)






