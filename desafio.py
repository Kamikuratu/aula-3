# Integre na solução anterior um fluxo de While 
# que repita o fluxo até que o usuário insira as 
# informações corretas

nome_valido = False
salario_valido = False
percentual_valido = False

# 1) Solicita ao usuário que digite seu nome


while nome_valido is not True:
    try:
        nome = 'Raphael'
        if nome.isdigit():
            print("Você digitou seu nome incorretamente!")
        elif len(nome.strip()) == 0:
            print("Você não digitou nada!")
        else:
            nome_valido = True
            print("Nome inputado!")
    except ValueError as e:
        print(e)

# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante

while salario_valido is not True:
    try:
        salario = 13000
        if salario == 0:
            print("Seu salário não pode ser zero!")
        else:
            salario_valido = True
            print("Salário inputado!")
    except ValueError as e:
        print(e)

# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante



while percentual_valido is not True:
    try:
        percentual = 4.5
        if percentual == 0:
            print("Seu percentual de bôuns não pode ser zero!")
        else:
            percentual_valido = True
            print("Percentual inputado!")
    except ValueError as e:
        print(e)

# 4) Calcule o valor do bônus final
bonus = 1000 + salario*percentual

# 5) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus
print(f"{nome}, seu salário é R${salario:.2f} e seu bônus final é de R${bonus:.2f}")


