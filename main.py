from enum import Enum
import random
import csv
import logging
import logging
import logging.config
from logging.handlers import RotatingFileHandler

import keyboard


class Person:

    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def __repr__(self):
        return self.prenom + ' ' + self.nom


class TRIE(Enum):
    TRIE_NOM = 1
    TRIE_PRENOM = 2
    ALEATOIRE = 3


class ExcelFr(csv.excel):
    # Séparateur de champ
    delimiter = ";"


def trim(s):
    if s == None:
        return ''
    else:
        return s.strip()


def lectureFichier():
    logger = logging.getLogger('simpleExample')

    csv.register_dialect('excel-fr', ExcelFr())

    fname = "personne.csv"
    file = open(fname, "rt", encoding='utf8')

    tab = []

    try:
        # lecture du fichier
        reader = csv.DictReader(file, dialect="excel-fr")
        # parcourt
        for row in reader:
            logger.debug('ligne:%s', row)
            nom = trim(row['nom'])
            prenom = trim(row['prenom'])
            if (nom != '' and prenom != ''):
                tab.append(Person(nom, prenom))

    finally:
        # Fermeture du fichier csv
        file.close()

    return tab


def pressKey():
    logger = logging.getLogger('simpleExample')
    if True:
        s = input("")
        logger.debug('touche:%s!', s)
        if s.strip() == 'q':
            return 1
        return 0
    else:
        while True:
            key = keyboard.read_key()
            if key == ' ' or key == 'n':
                # print("You pressed p")
                break
            elif key == 'q':
                return 1
        return 0


def initlog():
    # logging.config.fileConfig('logging.conf')
    logging.basicConfig(
        handlers=[RotatingFileHandler('./logs/app.log', maxBytes=100000, backupCount=10, encoding='utf-8')],
        level=logging.INFO,
        format="[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s",
        datefmt='%Y-%m-%dT%H:%M:%S')


def main():
    initlog()
    logger = logging.getLogger('simpleExample')
    logger.info('debut')
    res = []

    tab = lectureFichier()

    afficheListe = True
    afficheListe = False

    traitement = TRIE.TRIE_NOM
    traitement = TRIE.TRIE_PRENOM
    # traitement = TRIE.ALEATOIRE

    if traitement == TRIE.TRIE_NOM:
        print("Trie par nom")
        res = sorted(tab, key=lambda person: person.nom.lower())
    elif traitement == TRIE.TRIE_PRENOM:
        print("Trie par prenom")
        res = sorted(tab, key=lambda person: person.prenom.lower())
    elif traitement == TRIE.ALEATOIRE:
        print('Aléatoire')
        res = []
        res.extend(tab)
        random.shuffle(res)

    logger.info('liste des personnes: %s', res)

    if afficheListe:
        print(res)
    else:
        i = 1
        for v in res:
            logger.info('%s) %s', i, v)
            print(str(i) + ') ' + str(v))
            i = i + 1
            fin = pressKey()
            if fin == 1:
                break

    logger.info('fin')


if __name__ == "__main__":
    main()
