nota1 = float(input("Digite a primeira nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota4 = float(input("Digite a quarta nota: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

print("Sua média é: ", media)

if media < 7: 
    print ("Aluno reprovado!")

else: 
    print ("Aluno aprovado!")


