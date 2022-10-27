def main():
    resposta = str(input("Você deseja somar, subtrair, multiplicar ou dividir?\n"))
    if resposta == "+":
        n1 = int(input("Digite o primeiro valor: "))
        n2 = int(input("Digite o segundo valor: "))
        print(f'{somar(n1, n2)}')
    elif resposta == "-":
        n1 = int(input("Digite o primeiro valor: "))
        n2 = int(input("Digite o segundo valor: "))
        print(f'{subtrair(n1, n2)}')
    elif resposta == "/":
        n1 = int(input("Digite o primeiro valor: "))
        n2 = int(input("Digite o segundo valor: "))
        print(f'{dividir(n1, n2)}')
    elif resposta == "*":
        n1 = int(input("Digite o primeiro valor: "))
        n2 = int(input("Digite o segundo valor: "))
        print(f'{multiplicar(n1, n2)}')
    else:
        print("Utilize os símbolos (+, -, *, /) para definir o calculo.")


def somar(n1, n2):
    return n1 + n2


def subtrair(n1, n2):
    return n1 - n2


def dividir(n1, n2):
    return n1 / n2


def multiplicar(n1, n2):
    return n1 * n2


if __name__ == '__main__':
    main()
