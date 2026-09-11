"""
=============================
CALCULADORA SIMPLES
=============================
Primeiro programa completo - Calculadora básica
"""

print("=== CALCULADORA SIMPLES ===")
print("Operações disponíveis: +, -, *, /")
print()

# Coletando os dados do usuário
primeiro_numero = float(input("Digite o primeiro número: "))
operacao = input("Digite a operação (+, -, *, /): ")
segundo_numero = float(input("Digite o segundo número: "))

# Realizando o cálculo baseado na operação
if operacao == "+":
    resultado = primeiro_numero + segundo_numero
    print(f"{primeiro_numero} + {segundo_numero} = {resultado}")

elif operacao == "-":
    resultado = primeiro_numero - segundo_numero
    print(f"{primeiro_numero} - {segundo_numero} = {resultado}")

elif operacao == "*":
    resultado = primeiro_numero * segundo_numero
    print(f"{primeiro_numero} * {segundo_numero} = {resultado}")

elif operacao == "/":
    if segundo_numero != 0:
        resultado = primeiro_numero / segundo_numero
        print(f"{primeiro_numero} / {segundo_numero} = {resultado}")
    
    else:
        print("Erro: Divisão por zero não é permitida!")

else:
    print("Operação inválida! Use apenas +, -, * ou /")
