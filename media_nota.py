import time
print("Verifique sua situação")
nota1 = float(input("Digite sua 1º nota: "))
nota2 = float(input("Digite sua 2º nota: "))
nota3 = float(input("Digite sua 3º nota: "))
media = (nota1 + nota2 + nota3) / 3
print(f"Sua media foi {media:.2f}")
print("Aguarde...")
time.sleep(1.5)
if media >= 7:
    print("APROVADO")
elif media >= 5:
    print("RECUPERAÇÃO")
else:
    print("REPROVADO")

# Não tem tratamento de erro por enquanto
