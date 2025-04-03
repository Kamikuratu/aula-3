### Exercício 1: Verificação de Qualidade de Dados
# Você está analisando um conjunto de dados de vendas e precisa garantir 
# que todos os registros tenham valores positivos para `quantidade` e `preço`. 
# Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos 
# forem positivos ou "Dados inválidos" caso contrário.

#quantidade = int(input("Insira a quantidade: "))
#preço = int(input("Insira o preço: "))

#if quantidade > 0 and preço > 0:
#    print("Valores válidos")
#else:
#    print("Valores inválidos")

### Exercício 2: Classificação de Dados de Sensor
# Imagine que você está trabalhando com dados de sensores IoT. 
# Os dados incluem medições de temperatura. Você precisa classificar cada leitura 
# como 'Baixa', 'Normal' ou 'Alta'. Considerando que:

#temp = int(input("Insira uma temperatura: "))

#if temp < 18:
#    print("Temperatura baixa")
#elif temp >= 18 and temp <= 26:
#    print("Temperatura normal")
#else:
#    print("Temperatura alta")

### Exercício 3: Filtragem de Logs por Severidade
# Você está analisando logs de uma aplicação e precisa filtrar mensagens 
# com severidade 'ERROR'. Dado um registro de log em formato de dicionário 
# como `log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}`, 
# escreva um programa que imprima a mensagem se a severidade for 'ERROR'.

#log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}

#if log['level'] == "ERROR":
#    print(log['message'])

### Exercício 4: Validação de Dados de Entrada
# Antes de processar os dados de usuários em um sistema de recomendação, 
# você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha 
# fornecido um email válido. Escreva um programa que valide essas condições 
# e imprima "Dados de usuário válidos" ou o erro específico encontrado.

#idade = int(input("Insira sua idade: "))
#email = input("Insira seu e-mail: ")

#if not 18 <= idade <= 65:
#    print("Idade fora do intervalo permitido")
#elif "@" not in email and "." not in email:
#    print("Email inválido")
#else:
#    print("Dados válidos")

### Exercício 5: Detecção de Anomalias em Dados de Transações
# Você está trabalhando em um sistema de detecção de fraude e precisa identificar 
# transações suspeitas. Uma transação é considerada suspeita se o valor for superior 
# a R$ 10.000 ou se ocorrer fora do horário comercial (antes das 9h ou depois das 18h). 
# Dada uma transação como `transacao = {'valor': 12000, 'hora': 20}`, verifique se ela é suspeita.

#transacao = {'valor': 12000, 'hora': 20}

#if transacao['valor'] > 10000 or 9 < transacao['hora'] or transacao['hora'] > 18:
#    print("Transação suspeita")

### Exercício 6. Contagem de Palavras em Textos
# Objetivo:** Dado um texto, contar quantas vezes cada palavra única aparece nele.

#texto = "eu sou uma pessoa muito especial muito especial"
#palavras = texto.split(" ")
#contagem_palavras = {}

#for palavra in palavras:
#    if palavra in contagem_palavras:
#        contagem_palavras[palavra] += 1
#    else:
#        contagem_palavras[palavra] = 1

#print(contagem_palavras)

### Exercício 7. Normalização de Dados
# Objetivo:** Normalizar uma lista de números para que fiquem na escala de 0 a 1.

#lista = [2, 8, 9, 10, 27, 29, 19, 40, 42]
#lista_normalizada1 = []
#max_lista = int(max(lista))
#min_lista = int(min(lista))
#range = max_lista - min_lista

#for n in lista:
#    if n == min_lista:
#        lista_normalizada1.append(0)
#    elif n == max_lista:
#        lista_normalizada1.append(1)
#    else:
#        lista_normalizada1.append(n / range)

#print(lista_normalizada1)

#lista_normalizada2 = [(x - min_lista) / (max_lista - min_lista) for x in lista]
#print(lista_normalizada2)

### Exercício 8. Filtragem de Dados Faltantes
# Objetivo:** Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um campo específico faltando

#lista = [{'nome': 'Raphael', 'ID': 123},
#         {'nome': 'Amanda', 'ID': ''},
#         {'nome': 'Marcelo', 'ID': 125}]

#usuarios_validos = [usuario for usuario in lista if usuario['ID']]

#print(usuarios_validos)

### Exercício 9. Extração de Subconjuntos de Dados
# Objetivo:** Dada uma lista de números, extrair apenas aqueles que são pares.

#lista = [2, 3, 12, 4553, 756, 8521, 9327, 9823, 324, 245, 2421]
#pares = []
#for n in lista:
#    if n % 2 == 0:
#        pares.append(n)
#    else:
#        pass

#print(pares)

#lista2 = [2, 3, 12, 4553, 756, 8521, 9327, 9823, 324, 245, 2421]
#pares2 = [n for n in lista2 if n%2 == 0]

#print(pares2)

### Exercício 10. Agregação de Dados por Categoria
# Objetivo:** Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.

#vendas = [
#    {"categoria": "eletrônicos", "valor": 1200},
#    {"categoria": "livros", "valor": 200},
#    {"categoria": "eletrônicos", "valor": 800}
#]

#total_categoria = {}

#for venda in vendas:
#    categoria = venda["categoria"]
#    valor = venda['valor']
#    if categoria in total_categoria:
#        total_categoria[categoria] += valor
#    else:
#        total_categoria[categoria] = valor

#print(total_categoria)

### Exercícios com WHILE

### Exercício 11. Leitura de Dados até Flag
# Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.

#palavra = input("Insira a palavra secreta: ")

#while palavra != "sair":
#    if palavra == "sair":
#        print("Você saiu do programa!")
#        break
#    else:
#        print(palavra)
#        palavra = input("Tente novamente: ")
#        continue
    
#dados = []
#entrada = ""
#while entrada.lower() != "sair":
#    entrada = input("Digite um valor (ou 'sair' para terminar): ")
#    if entrada.lower() != "sair":
#        continue

### Exercício 12. Validação de Entrada
# Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida.

#idade = int(input("Insira uma idade válida: "))

#while idade < 18 or idade > 60:
#    print("Idade inválida!")
#    idade = int(input("Insira uma idade válida: "))

#print("Idade válida inserida!") 

### Exercício 13. Consumo de API Simulado
# Simular o consumo de uma API paginada, onde cada "página" de dados é processada em loop até que não haja mais páginas.

#pagina_atual = 1
#paginas_totais = 10

#while pagina_atual <= paginas_totais:
#    print(f'Página {pagina_atual} processada.')
#    pagina_atual += 1

#print(f'Todas as páginas foram processadas!')

### Exercício 14. Tentativas de Conexão
# Simular tentativas de reconexão a um serviço com um limite máximo de tentativas.

#max_tentativas = 10
#tentativa_atual = 1

#while tentativa_atual <= max_tentativas:
#    print(f'Tentativa {tentativa_atual} de {max_tentativas}, tentando novamente...')
#    tentativa_atual += 1

#print("Número máximo atingido.")

### Exercício 15. Processamento de Dados com Condição de Parada
# Processar itens de uma lista até encontrar um valor específico que indica a parada.

lista = [2, 4, 6, 8, 10, 12, 14]
valor_parada = int(input("Insira aonde deseja parar a lista (número de 2 a 14): "))
i = 2

while i < max(lista):
    if i == valor_parada:
        print("Valor de parada aitngido!")
        break
    else:
        print(i)
        i = i + 2