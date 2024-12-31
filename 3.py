words = ["python", "programmation", "langage", "ordinateur", "apprentissage"]
vowels = set("aeiouy")

result = [
    (word, sum(letter in vowels for letter in word.lower()))
    for word in words
]

print(result)
