def pot2(x):
    return x ** 2

pot2_ = lambda x: x ** 2

print(f"Função Normal com Def: {pot2(5)}")

print(f'Função Lambda: {pot2_(3)}')

def fatorial(n):
    if (n == 0):
        return 1
    return (n * fatorial(n - 1))


def fatorialFor(n):
    fatorial = 1
    for numero in range(n, 0, -1):
        fatorial *= numero
    return fatorial

fat_ = lambda n: n * fatorial(n - 1) if n > 1 else 1

print(fatorial(5))
print(f'Fatorial com for: {fatorialFor(5)}')
print(f'Lambda: {fat_(5)}')

