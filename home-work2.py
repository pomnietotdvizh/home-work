#  Задание номер 2

letters = 'Who keeps company with the wolf, will learn to howl.'
template = 'w'
exclude = 'l'

for a in letters:
    if a == template:
        print (sum(len (int(a))))

for b in letters:
    if b != exclude:
        print(b)
