
class Pessoa:
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    def getNome(self):
        return self.nome
    
    def getIdade(self):
        return self.idade
    
pessoa = Pessoa('Sthevan', 34)

print(pessoa.getNome())
print(f'{pessoa.getIdade()} anos')

pares = [numero for numero in range(101) if (numero % 2 == 1) ]

print(*pares)

