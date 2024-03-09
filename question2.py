def fibonacci(num):
    a, b = 0, 1
    while b < num:
        a, b = b, a + b
    return b == num

number = int(input("Digite um número: "))

if fibonacci(number):
    print(f"{number} pertence à sequência de Fibonacci.")
else:
    print(f"{number} não pertence à sequência de Fibonacci.")


