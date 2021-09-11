from enum import Enum
import random


class Person:

    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def __repr__(self):
        return repr((self.nom, self.prenom))


class TRIE(Enum):
    TRIE_NOM = 1
    ALEATOIRE = 2


res = []

tab = [
    Person('aaa1', 'bbb1'),
    Person('aaa2', 'bbb2'),
    Person('aaa3', 'bbb3'),
    Person('aaa4', 'bbb4'),
    Person('aaa5', 'bbb5')
]

afficheListe = True
afficheListe = False

# traitement = TRIE.TRIE_NOM
traitement = TRIE.ALEATOIRE

if traitement == TRIE.TRIE_NOM:
    print("Trie par nom")
    res = sorted(tab, key=lambda person: person.nom)
elif traitement == TRIE.ALEATOIRE:
    print('Aléatoire')
    res = []
    res.extend(tab)
    random.shuffle(res)

if afficheListe:
    print(res)
else:
    i = 1
    for v in res:
        print(str(i) + ') ' + str(v))
        input("")
        i = i + 1
