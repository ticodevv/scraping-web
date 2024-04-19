import pandas as pd # Importer la bibliothèque pandas pour la manipulation des données
from bs4 import BeautifulSoup # Importer la bibliothèque BeautifulSoup pour l'analyse HTML
from selenium import webdriver # Importer la bibliothèque Selenium pour l'automatisation du navigateur

# Lancer le navigateur
driver = webdriver.Chrome()
driver.get('https://sandbox.oxylabs.io/products')
results = []
other_results = []
content = driver.page_source
soup = BeautifulSoup(content, 'html.parser')

# Récupérer les noms des produits
for a in soup.find_all(attrs={'class': 'product-card'}):
    name = a.find('h4')
    if name not in results:
        results.append(name.text)

# Récupérer les prix
for b in soup.find_all(attrs={'class': 'product-card'}):
    name2 = b.find(attrs={'class': 'price-wrapper'})
    if name2 not in other_results:
        other_results.append(name2.text)

# Créer un DataFrame
series1 = pd.Series(results, name='Names')
series2 = pd.Series(other_results, name='Prices')
df = pd.DataFrame({'Names': series1, 'Prices': series2})

# Nettoyer les prix et convertir en flottants
df['Prices'] = df['Prices'].str.replace('€', '').str.replace('.', '').str.replace(',', '.').str.strip().astype(float)

# Trier les prix dans l'ordre croissant
df = df.sort_values(by='Prices')

# Ajouter le symbole euro à la fin du prix
df['Prices'] = df['Prices'].astype(str) + '€'

df.to_csv('products.csv', index=False, encoding='utf-8')
