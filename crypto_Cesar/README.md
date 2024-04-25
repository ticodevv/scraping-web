### Crypto Cesar

#### Description

Deja c'est quoi le chiffrement de César ?

Le chiffrement de César est une méthode de chiffrement très simple qui consiste à décaler les lettres d'un texte de quelques positions dans l'alphabet. Par exemple, si on décale les lettres de 3 positions, alors A devient D, B devient E, C devient F, etc.

#### Comment ça marche

Le chiffrement de César fonctionne de la manière suivante:
- On choisit un nombre de décalage (par exemple 3)
- On remplace chaque lettre du texte par la lettre décalée de 3 positions dans l'alphabet
- On obtient ainsi un texte chiffré

#### Le code

Nous avons 2 code : Chiffrement-déchiffrement.py et Cryptanalyse.py

##### Chiffrement-déchiffrement.py

Savori si une lettre en majuscule ou minuscule
```python
majuscules = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
minuscules = majuscules.lower()
```

Ici nous avons défini les majuscules et les minuscules pour pouvoir les utiliser dans les fonctions suivantes.
```python
def lettre(c):
    # retourne vrai si c est une lettre non accentuee
    return c in majuscules or c in minuscules
```

Cette fonction va nous permettre de decaler une lettre. Les autres caracteres ne sont pas modifies
```python
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
```

Cette fonction va nous permettre de crypter ou decrypter un message
```python
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
```

Ici nous avons un exemple de test
```python
# tests
texte="pascal"
texte_code = cesar(texte,3,True)
print(texte_code)
texte_decode = cesar(texte_code,3,False)
print(texte_decode)
```
Output :
```bash
➜  scraping-web git:(main) ✗ python3 crypto_Cesar/Chiffrement-déchiffrement.py 
sdvfdo
pascal
```

##### Cryptanalyse.py

Le code et et le meme que Chiffrement-déchiffrement.py mais ici on va utiliser la cryptanalyse pour trouver le message original
imaginons que nous avons un message crypté et on ne connait pas le décalage, on va utiliser la cryptanalyse pour trouver le message original sans connaitre le décalage.

il y a 1 fonctions qui sont ajoutées dans ce code
Cette fonction va nous permettre de tester tous les décalages possibles pour trouver le message original
```python
for clef in range(1,26):
    texte_decode = cesar(texte_code,clef,False)
    if clef<10:
        print(end=" ")
    print(clef,":",texte_decode)
```

Ici nous avons un exemple de test:
```bash
➜  scraping-web git:(main) ✗ python3 crypto_Cesar/Cryptanalyse.py 
hskusd
 1 : grjtrc
 2 : fqisqb
 3 : ephrpa
 4 : dogqoz
 5 : cnfpny
 6 : bmeomx
 7 : aldnlw
 8 : zkcmkv
 9 : yjblju
10 : xiakit
11 : whzjhs
12 : vgyigr
13 : ufxhfq
14 : tewgep
15 : sdvfdo
16 : rcuecn
17 : qbtdbm
18 : pascal
19 : ozrbzk
20 : nyqayj
21 : mxpzxi
22 : lwoywh
23 : kvnxvg
24 : jumwuf
25 : itlvte
```