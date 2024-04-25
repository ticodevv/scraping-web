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

On peux voir que le message original est "pascal" et le message crypté est "sdvfdo" avec un décalage de 3
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

On a trouvé le message original qui est "pascal" avec un décalage de 18


#### Cryptanalyse2.py

Décrypte un chiffre de César en essayant les 25 clefs possibles, et en prime, donne la meilleure solution.
Nécessite le fichier brut4g_fr.txt

Le fichier brut4g_fr.txt contient une liste de mots en français, un mot par ligne. Il est utilisé pour déterminer si un texte déchiffré est correct. Il est possible de le remplacer par un autre fichier de mots.

```bash
➜  crypto_Cesar git:(main) ✗ python3 Cryptanalyse2.py            
 1 : itlvte    score : 30.0
 2 : hskusd    score : 30.0
 3 : grjtrc    score : 30.0
 4 : fqisqb    score : 30.0
 5 : ephrpa    score : 24.93231773580408
 6 : dogqoz    score : 30.0
 7 : cnfpny    score : 30.0
 8 : bmeomx    score : 30.0
 9 : aldnlw    score : 27.022222847243476
10 : zkcmkv    score : 30.0
11 : yjblju    score : 30.0
12 : xiakit    score : 26.545101592523814
13 : whzjhs    score : 30.0
14 : vgyigr    score : 30.0
15 : ufxhfq    score : 30.0
16 : tewgep    score : 30.0
17 : sdvfdo    score : 30.0
18 : rcuecn    score : 18.204537162417395
19 : qbtdbm    score : 30.0
20 : pascal    score : 13.16467707933224
21 : ozrbzk    score : 30.0
22 : nyqayj    score : 30.0
23 : mxpzxi    score : 30.0
24 : lwoywh    score : 30.0
25 : kvnxvg    score : 30.0

20 : pascal
```

On a trouvé le message original qui est "pascal" avec un décalage de 18 et un score de 13.16. Le score est calculé en fonction du nombre de mots trouvés dans le fichier brut4g_fr.txt

#### Conclusion

Le chiffrement de César est une méthode de chiffrement très simple qui consiste à décaler les lettres d'un texte de quelques positions dans l'alphabet. Il est très facile à casser, mais il peut être utile pour des messages simples.