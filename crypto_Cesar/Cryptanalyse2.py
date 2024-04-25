# decrypte un chiffre de Cesar avec un dictionnaire de frequences 
# les frequences des 4-grammes sont stockees dans le fichier brut4g_fr.txt

from math import log10

majuscules = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" # alphabet en majuscules
minuscules = majuscules.lower() # alphabet en minuscules


def charger_tetragrammes(nom): # tetragrammes --> c'est des 4-grammes --> 4 lettres qui se suivent
    f = open(nom) # ouverture du fichier
    total = 0  # effectif total
    for line in f: # on parcourt toutes les lignes du fichier
        (w, c) = line.split(sep= ' ') # on separe le 4-gramme et son effectif
        f4g[w] = int(c) # on recupere les 4-grammes
        total += int(c) # on somme les effectifs
    for w in f4g: # on parcourt tous les 4-grammes
        f4g[w] /= total  # calcul des frequences --> les frequences sont des probabilités donc elles doivent sommer à 1
    f.close # fermeture du fichier


# score
def enlever_espaces_et_maj(s):
    res = "" # initialisation du texte sans les espaces et en majuscules
    for c in s: # on parcourt tous les caracteres du texte
        c = c.upper() # on met en majuscules
        if c in majuscules: # on ne garde que les lettres
            res += c # on ne garde que les lettres
    return res # on retourne le texte sans les espaces et en majuscules

def logscore(s):
    s = enlever_espaces_et_maj(s) # on enleve les espaces et on met en majuscules
    logsum = 0 # initialisation du score
    min_freq = 1e-10 # frequence d'un 4-gramme inexistant
    for i in range(len(s)-3): # on parcourt toutes les lettres du texte
        logsum += log10(f4g.get(s[i:i+4], min_freq)) # on prend les 4 lettres qui se suivent
    return -logsum # on retourne -logscore car on veut minimiser le score


# Cesar
def lettre(c):
    # retourne vrai si c est une lettre non accentuee
    return c in majuscules or c in minuscules # on regarde si c'est une majuscule ou une minuscule

def decalage(c,k):
    # decale une lettre. Les autres caracteres ne sont pas modifies
    if lettre(c): # si c'est une lettre
        if c in majuscules : # si c'est une majuscule
            alphabet = majuscules # on regarde si c'est une majuscule ou une minuscule
        else: # c'est une minuscule
            alphabet = minuscules # on regarde si c'est une majuscule ou une minuscule
        car = alphabet.find(c) # on cherche la lettre dans l'alphabet
        car += k # on decale
        while car>=len(alphabet): # si on depasse a droite
            car -= len(alphabet) # si on depasse a droite
        while car<0: # si on depasse a gauche
            car += len(alphabet) # on decale dans l'autre sens
        return alphabet[car] # on retourne la lettre decalee
    else: # si ce n'est pas une lettre
        return "" # on ne modifie pas les caracteres qui ne sont pas des lettres

def cesar(message,d,crypte): # crypte est un booleen qui indique si on chiffre ou dechiffre
    # effectue le decalage d sur les caracteres de message
    chiffre='' # initialisation du texte chiffre ou dechiffre
    for c in message: # on parcourt tous les caracteres du message
        if lettre(c): # si c'est une lettre
            if c in majuscules : # si c'est une majuscule
                alphabet = majuscules # on regarde si c'est une majuscule ou une minuscule
            else: # c'est une minuscule
                alphabet = minuscules # on regarde si c'est une majuscule ou une minuscule
            if crypte: # si on chiffre
                chiffre += decalage(c,d) # si on chiffre
            else: # si on dechiffre
                chiffre += decalage(c,-d) # on decale dans l'autre sens
        else: # si ce n'est pas une lettre
            chiffre += c # on ne modifie pas les caracteres qui ne sont pas des lettres
    return chiffre # on retourne le texte chiffre ou dechiffre


# tests
f4g ={}    # dico des frequences des 4-grammes 
charger_tetragrammes("brut4g_fr.txt")  # chargement des frequences des 4-grammes
texte="sdvfdo" # texte a dechiffrer
texte_code = cesar(texte,17,True) # on chiffre le texte


best_score = 10000000 # initialisation du meilleur score
best_clef = 0 # initialisation de la meilleure clef
for clef in range(1,26): # on teste toutes les cles possibles
    texte_decode = cesar(texte_code,clef,False) # on dechiffre avec la clef courante
    score = logscore(texte_decode) # on calcule le score
    if score < best_score: # si le score est meilleur que le meilleur score
        best_score = score # on met a jour le meilleur score
        best_clef = clef # on met a jour la meilleure clef
    if clef<10: # on affiche les 10 meilleures solutions
        print(end=" ") # pour l'alignement
    print(clef,":",texte_decode,"   score :",score) # on affiche le texte dechiffre et le score
print() # saut de ligne
print(best_clef,":",cesar(texte_code,best_clef,False)) # on affiche le texte dechiffre avec la meilleure clef
