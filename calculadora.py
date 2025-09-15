def somar(x, y):
    return x + y

def subtrair(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y == 0:
        return "Erro: divisão por zero."
    return x / y

def menu():
    print("\nCalculadora Simples em Python")
    print("Selecione a operação:")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("0 - Sair")

while True:
    menu()
    escolha = input("Digite sua escolha: ")

    if escolha == "0":
        print("Encerrando a calculadora. Até mais!")
        break

    if escolha not in ("1", "2", "3", "4"):
        print("Opção inválida. Tente novamente.")
        continue

    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Erro: digite apenas números válidos.")
        continue

    if escolha == "1":
        resultado = somar(num1, num2)
        operacao = "+"
    elif escolha == "2":
        resultado = subtrair(num1, num2)
        operacao = "-"
    elif escolha == "3":
        resultado = multiplicar(num1, num2)
        operacao = "*"
    elif escolha == "4":
        resultado = dividir(num1, num2)
        operacao = "/"

    print(f"Resultado: {num1} {operacao} {num2} = {resultado}")
