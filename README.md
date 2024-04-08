# scraping-web

## Description

 un scraping Web est une technique informatique permettant d'extraire automatiquement des données de sites Web.

## Utilisation

Pour utiliser ce projet, vous devez cloner ce dépôt sur votre machine locale en utilisant la commande suivante:

```bash
git clone https://github.com/ticodevv/scraping-web.git
```

une fois le projet cloné, vous pouvez lancer le script en utilisant la commande suivante:

```bash
python3 main.py
```

### Modification 

Pour modifier le site à scraper, vous pouvez modifier la variable `url` dans le fichier `main.py`:

```python
    driver.get('https://sandbox.oxylabs.io/products')
```

Pour modifier les valeurs à scraper, vous pouvez modifier les valeurs dans le fichier `main.py`:

modifiez la valeur de la clé `name` pour changer le nom du produit:
```python
    for a in soup.find_all(attrs={'class': 'product-card'}): # Nous prenons les éléments du site ayant la classe 'product-card'
```

modifiez la valeur de la clé `price` pour changer le prix du produit:
```python
    name2 = b.find(attrs={'class': 'price-wrapper'}) # Nous prenons les éléments du site ayant la classe 'price-wrapper'
```

Nous trouvon ces elements en inspectant le site web. Ce sont des baliises HTML.
