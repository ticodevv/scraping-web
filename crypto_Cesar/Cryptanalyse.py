# chiffre et dechiffre un texte avec le chiffre de Cesar, sans le W

majuscules = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"   # pas de W
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
        while car>=len(alphabet):
            car -= len(alphabet)
        while car<0:
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
texte="sdvfdo"
texte_code = cesar(texte,15,True)
print(texte_code)

for clef in range(1,26):
    texte_decode = cesar(texte_code,clef,False)
    if clef<10:
        print(end=" ")
    print(clef,":",texte_decode)

    