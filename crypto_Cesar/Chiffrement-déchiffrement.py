# chiffre et dechiffre un texte avec le chiffre de Cesar

majuscules = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
minuscules = majuscules.lower()

def lettre(c):
    # retourne vrai si c est une lettre non accentuee
    return c in majuscules or c in minuscules

def decalage(c,k):
    # decale une lettre. Les autres caracteres ne sont pas modifies
    if lettre(c):
        if c in majuscules :
            alphabet = majuscules
        else:
            alphabet = minuscules
        car = alphabet.find(c)
        car += k
        while car >= len(alphabet):
            car -= len(alphabet)
        while car < 0:
            car += len(alphabet)
        return alphabet[car]
    else:
        return ""

def cesar(message,d,crypte):
    # effectue le decalage d sur les caracteres de message
    chiffre=''
    for c in message:
        if lettre(c):
            if c in majuscules :
                alphabet = majuscules
            else:
                alphabet = minuscules
            if crypte:
                chiffre += decalage(c,d)
            else:
                chiffre += decalage(c,-d)
        else:
            chiffre += c
    return chiffre


# tests
texte="pascal"
texte_code = cesar(texte,3,True)
print(texte_code)
texte_decode = cesar(texte_code,3,False)
print(texte_decode)
