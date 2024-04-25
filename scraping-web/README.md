### Scraping-Web

#### C'est quoi ?

un scraping Web est une technique informatique permettant d'extraire automatiquement des données de sites Web.

#### dans qu'elle but ?

Le but de ce projet est de scraper un site web pour en extraire des données précises. 

Exemple:
- Nom du produit
- Prix du produit

#### Le code

Nous allons utiliser les bibliothèques suivantes: 
    - pandas --> pour la manipulation des données
    - BeautifulSoup --> pour l'analyse HTML
    - Selenium --> pour l'automatisation du navigateur

```python
import pandas as pd # Importer la bibliothèque pandas pour la manipulation des données
from bs4 import BeautifulSoup # Importer la bibliothèque BeautifulSoup pour l'analyse HTML
from selenium import webdriver # Importer la bibliothèque Selenium pour l'automatisation du navigateur
```

ici nous allons lancer le navigateur et accéder à la page web que nous voulons scraper.

```python
# Lancer le navigateur
driver = webdriver.Chrome() # Lancer le navigateur Chrome
driver.get('https://sandbox.oxylabs.io/products') # Accéder à la page web
results = [] # Créer une liste pour stocker les résultats
other_results = [] # Créer une liste pour stocker les autres résultats
content = driver.page_source # Récupérer le contenu de la page web
soup = BeautifulSoup(content, 'html.parser') # Analyser le contenu de la page web
```

Récupérer les noms des produits

```python
# Récupérer les noms des produits
for a in soup.find_all(attrs={'class': 'product-card'}):
    name = a.find('h4')
    if name not in results:
        results.append(name.text)
```

Récupérer les prix des produits

```python
# Récupérer les prix
for b in soup.find_all(attrs={'class': 'product-card'}):
    name2 = b.find(attrs={'class': 'price-wrapper'})
    if name2 not in other_results:
        other_results.append(name2.text)
```

Nous allons crée une dataframe pour stocker les résultats

C'est quoi une DataFrame ?
Une DataFrame est une structure de données bidimensionnelle, mutable et hétérogène, qui peut contenir des données de type série, de type DataFrame ou de type Panel.

Pour faire simple, une DataFrame est une table de données.

```python
# Créer un DataFrame
series1 = pd.Series(results, name='Names')
series2 = pd.Series(other_results, name='Prices')
df = pd.DataFrame({'Names': series1, 'Prices': series2})
```

Nettoyer les prix et convertir en flottants
```python
# Nettoyer les prix et convertir en flottants
df['Prices'] = df['Prices'].str.replace('€', '').str.replace('.', '').str.replace(',', '.').str.strip().astype(float)
```

Trier les prix dans l'ordre croissant et ajouter le symbole euro à la fin du prix
```python
# Trier les prix dans l'ordre croissant
df = df.sort_values(by='Prices')

# Ajouter le symbole euro à la fin du prix
df['Prices'] = df['Prices'].astype(str) + '€'
```

Afficher les résultats dans un fichier CSV. 
```python
df.to_csv('products.csv', index=False, encoding='utf-8')
```

#### Conclusion

Dans ce projet, nous avons appris à scraper un site web pour en extraire des données précises. Nous avons utilisé les bibliothèques pandas, BeautifulSoup et Selenium pour manipuler les données, analyser le HTML et automatiser le navigateur. Nous avons créé une DataFrame pour stocker les résultats, nettoyé les prix et trié les prix dans l'ordre croissant. Enfin, nous avons affiché les résultats dans un fichier CSV.

Les problèmes rencontrés sont les suivants:
- Trouver les balises HTML pour extraire les données
- Nettoyer les données pour les rendre exploitables
- Automatiser le navigateur pour accéder à la page web
- Nous avons aussi eu des problèmes liés au scraping en dure car certaines pages web sont dynamiques et les données ne sont pas toujours accessibles directement dans le code source de la page web.
