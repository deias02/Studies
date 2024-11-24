#die_visual
from die import Die

#Cria um D6 (Dado de 6)
die= Die()

# Faz alguns lançamentos e armazena os resultados em uma lista
results = [die.roll() for _ in range(1000)]  
# Usando list comprehension

#Analisa os resultados 
frequencies = [results.count(value) for value in range(1, die.num_sides + 1)]  
# Usando list comprehension

print(frequencies)