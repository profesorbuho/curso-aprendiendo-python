from collections import Counter

# Abrir y leer archivos de texto
with open('data/example-text.txt', "r", encoding="utf-8") as text:
    text = text.read()
# print( text )

# Uso de la Counter
words_list = ["Hola", "Profesor", "mundo", "Búho", "cómo", "estas", "mundo", "Hola", "mundo"]
number_of_words = dict(Counter(words_list))
print( number_of_words )

maximo = 0
for i, j in number_of_words.items():
    if j > maximo:
        most_frequent_word = i
        maximo = j
print( most_frequent_word )

# get
mundo = number_of_words.get('mundo')
print( mundo )

programming = number_of_words.get('programacion', 0)
print( programming )

# Sorted
even = [(1, 3), (4, 1), (2, 5)]
result = sorted(even, key=lambda x: x[1], reverse=False)
print( result )

# join
join_words = ' '.join(words_list)
print( join_words )
print( type(join_words) )