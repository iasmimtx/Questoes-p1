nota1 = float(input())
nota2 = float(input())
nota3 = float(input())
peso1 = float(input())
peso2 = float(input())

p1 = peso1 / 100
p2 = peso2 / 100
mediafinal = (nota1 * p1 + nota2 * p2 + nota3 * 0.5)/ (p1 + p2 + 0.5)

print(f'Média final: {mediafinal:.1f}')
