# fonctions.py

# pour bon fonctionnement du code la dependance base58 est necessaire
# sudo pip install base58

from datetime import date
import re
import base64
import base58
from colors import *
from mots_filtres import *

author = "artur/kurza/3SI4"  # reponse question 1
date=date.today()
datejm=date.strftime("%d/%m") # reponse question 2
msg = [author , datejm ,] # liste des reponses

def q3(txt):
        textq3 = re.search(r'(\d+)\s*([\+\-\*\/])\s*(\d+)', txt) # recherche de combinaison de chiffres suivi par charactere mathematique et puis les chiffres
        if textq3:
            num1 = int(textq3.group(1))
            operator = textq3.group(2)
            num2 = int(textq3.group(3))
            print(num1, operator, num2)
            # selection de bonne reponse
            if operator == '+':
                rep = num1 + num2
            elif operator == '-':
                rep = num1 - num2
            elif operator == '*':
                rep = num1 * num2
            elif operator == '/':
                rep = num1 / num2
            else:
                print("Opérateur non reconnu")
                rep = None
            if rep is not None:
                rep3=str(rep)
                msg.append(rep3)

def q4(txt):
    txtq4 = txt.split(': ') # split de message recu pour extraire le chaine a decoder
    code4 = txtq4[2]
    if char_spec(code4) is False:   #verification si characteres speciaux dans la chaine
            if char_min(code4) is False: #verification si characteres minuscules dans la chaine
                rep4 = base64.b32decode(code4).decode('utf-8') #decodage base 32
            elif c58(code4) is False: #verification si characteres interdits dans la chaine
                rep4 = base58.b58decode(code4).decode('utf-8') #decodage base 58
            else:
                rep4 = base64.b64decode(code4).decode('utf-8')   #decodage base 64
    else:
      rep4 = base64.b85decode(code4).decode('utf-8') #decodage base 85
    print(rep4)
    msg.append(rep4)
 
def q5(txt):
    textq5 = txt.split(': ')
    decodedhex = bytes.fromhex(textq5[2]).decode() 
    morse = {' ': '/', 'E': '.', 'I': '..', 'S': '...', 'H': '....', 'V': '...-', 'U': '..-', 'F': '..-.',
'A': '.-', 'R': '.-.', 'L': '.-..', 'W': '.--', 'P': '.--.', 'J': '.---', 'T': '-', 'N': '-.', 'D': '-..',
'B': '-...', 'X': '-..-', 'K': '-.-', 'C': '-.-.', 'Y': '-.--', 'M': '--', 'G': '--.', 'Z': '--..', 
'Q': '--.-', 'O': '---'}
    
    morse_inverse = {v: k for k, v in morse.items()} # inversion des cles et valeurs dans la dictionaire
    morse_split = decodedhex.split()
    txt = [morse_inverse[char] for char in morse_split] #match de characteres de code morse et lettres lisibles
    rep5 = ''.join(txt) # consolidation de lettres vers chaine
    msg.append(rep5)

def q6(txt):
    textq6 = txt.split(': ')
    hexsplit = textq6[2].split('20')   
    #tableau de conversion de hex vers Lettres en passant par braille
    tableau = {
        'e2a081': 'A',
        'e2a083': 'B',
        'e2a089': 'C',
        'e2a099': 'D',
        'e2a091': 'E',
        'e2a08b': 'F',
        'e2a09b': 'G',
        'e2a093': 'H',
        'e2a08a': 'I',
        'e2a09a': 'J',
        'e2a085': 'K',
        'e2a087': 'L',
        'e2a08d': 'M',
        'e2a09d': 'N',
        'e2a095': 'O',
        'e2a08f': 'P',
        'e2a09f': 'Q',
        'e2a097': 'R',
        'e2a08e': 'S',
        'e2a09e': 'T',
        'e2a0a5': 'U',
        'e2a0a7': 'V',
        'e2a0ba': 'W',
        'e2a0ad': 'X',
        'e2a0bd': 'Y',
        'e2a0b5': 'Z'}
    
    txt = [tableau[char] for char in hexsplit]
    rep6 = ''.join(txt)
    msg.append(rep6)     

def q7(txt):
    textq7 = txt.split('(')
    valeurs = textq7[1].split(',')
    #nettoyage des valeurs RGB
    r = int(valeurs[0])
    g = int(valeurs[1].replace(' ', ''))
    b = int(valeurs[2].replace(') ?', ''))
    RGB = (r,g,b)
    
    for color_value, color_name in colors.items(): #recherche de nom de coleur dans dictionaire
        if color_value == RGB:
            rep7 = color_name
            print(rep7)
            break
    msg.append(rep7)

def q8(txt):
    textq8 = txt.split('question ')
    rep8 = msg[int(textq8[1]) - 1] # choix de la reponse n° x dans la liste des reponses 
    msg.append(rep8)

def q9(txt):
    textq9 = txt.split(': ')
    wordslist = textq9[2].split(' ') # liste des mots
    word = textq9[1].split(' ')
    wordnum = word[7].replace('ème','') # numero de mot
    lettres = list(wordslist[int(wordnum)-1]) # liste des lettres du n-ème mot
    rep9 = lettres[len(lettres)-1] # derniere lettre de n-ème mot
    msg.append(rep9)

def q10(msg):
    i=0
    rep10=''
    for i in range(len(msg)):
        if i == 0:
            rep10 += msg[i]  #ajout de reponse suivante
        else:
            rep10 += '_' + msg[i] # ajout de "_" entre reponses
    msg.append(rep10)

def q11(txt):
    txtq11 = txt.split(': ')
    code11 = txtq11[2]
    for decalage in range(1, 26):
        # decodage de chiffrage cesar pour tout les decalages
        decoded = ''.join(
            chr((ord(char) - 97 + decalage) % 26 + 97) 
            for char in code11.lower()
        )
        liste_decode = decoded.split() #la liste des mots a verifier dans dictionaires
        
        # recherche de mot "decrypte" dans la liste des mots 
        for mot in liste_decode:
            if mot_in_wordlist(mot):
                rep11 = mot
                msg.append(rep11)
                return rep11

def mot_in_wordlist(mot):
    longueur = len(mot) # longeur de mot
    premiere_lettre = mot[0].lower() #premiere lettre de mot 
    wordlist = len_wordlist(longueur) #choix de bon liste selon longeur de mot
    index_lettre = ord(premiere_lettre) - ord('a') #choix de bon liste de niveau inferieur par rapport premiere lettre 
    return mot.lower() in wordlist[index_lettre] # recherche de mot dans la liste et retour si mot trouvé

def char_spec(code):
    char_s = r'[!@#$%^&*()_+\-\[\]{};\':"\\|,.<>/?]'  
    if re.search(char_s, code):   #recherche des characteres spectiaux dans la chaine 
        return True
    else:
        return False

def char_min(code):
    char_m = r'[a-z]'
    if re.search(char_m, code):  #recherche des characteres minuscules dans la chaine
        return True
    else:
        return False

def c58(code):
    c_58 = r'[O0Il=]'
    if re.search(c_58, code):  #recherche des characteres interdits dans la base58 dans la chaine
        return True
    else:
        return False
    
