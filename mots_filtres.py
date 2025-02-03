# mots_filres.py
from filtres_7 import wordlist7
from filtres_8 import wordlist8
from filtres_9 import wordlist9
from filtres_10 import wordlist10
from filtres_11 import wordlist11
from filtres_12 import wordlist12

# liste des mots est choisi en fonction de longeur de la mot chifre
def len_wordlist(len):
    if len == 7:
        return wordlist7
    if len == 8:
         return wordlist8
    if len == 9:
        return wordlist9
    if len == 10:
        return wordlist10
    if len == 11:
        return wordlist11
    if len == 12:
        return wordlist12