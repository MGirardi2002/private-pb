import random

animais = [
    "gato",
    "cachorro",
    "elefante",
    "girafa",
    "leão",
    "tigre",
    "lobo",
    "raposa",
    "formiga",
    "zebra",
    "camelo",
    "cavalo",
    "coelho",
    "peixe",
    "baleia",
    "golfinho",
    "pinguim",
    "papagaio",
    "abelha",
    "crocodilo",
]

animais_ord = sorted(animais)

for animal in animais_ord:
    print(animal)


with open("animais.csv", "w", newline="") as arquivo_csv:
    for animal in animais_ord:
        arquivo_csv.write(f"{animal}\n")
