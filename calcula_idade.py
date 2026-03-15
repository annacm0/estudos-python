# Programa para calcular a idade do usuário
nome = input("Qual o seu nome? ")
ano_nascimento = int(input("Em que ano você nasceu? "))
ano_atual = 2026

idade = ano_atual - ano_nascimento

print(f"Olá, {nome}! Você tem (ou fará) {idade} anos em {ano_atual}.")

