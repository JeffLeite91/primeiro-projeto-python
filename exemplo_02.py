# Solução da Calculadora de Média

# Solicitar as três notas ao usuário
nota1 = float(input("Digite a primeira nota (0 a 10): "))
nota2 = float(input("Digite a segunda nota (0 a 10): "))
nota3 = float(input("Digite a terceira nota (0 a 10): "))

# Calcular a média
media = (nota1 + nota2 + nota3) / 3

# Exibir a média
print(f"\nA média é: {media:.2f}")

# Verificar o resultado e exibir a mensagem correspondente
if media >= 7:
    print("O aluno foi: Aprovado")
elif 5 <= media < 7:
    print("O aluno foi: Em Recuperação")
else:
    print("O aluno foi: Reprovado")
