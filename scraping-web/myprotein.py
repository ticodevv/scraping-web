import pandas as pd # Importer la bibliothèque pandas pour la manipulation des données
from bs4 import BeautifulSoup # Importer la bibliothèque BeautifulSoup pour l'analyse HTML
from selenium import webdriver # Importer la bibliothèque Selenium pour l'automatisation du navigateur

# Lancer le navigateur
driver = webdriver.Chrome()
driver.get('https://fr.myprotein.com/nutrition/protein.list')
results = []
other_results = []
content = driver.page_source
soup = BeautifulSoup(content, 'html.parser')


# Récupérer les noms des produits
for product_list in soup.find_all(attrs={'class': 'productListProducts'}):
    for product in product_list.find_all(attrs={'class': 'productListProducts_product'}):
        name = product.find('h3', class_='productBlock_productName')
        if name and name.text.strip():  # Vérifiez si le nom existe et n'est pas vide
            results.append(name.text.strip())
        price = product.find('span', class_='productBlock_fromValue')
        if price and price.text.strip():  # Vérifiez si le nom existe et n'est pas vide
            other_results.append(price.text.strip())
        else :
            price = product.find('span', class_='productBlock_priceValue')
            if price and price.text.strip():  # Vérifiez si le nom existe et n'est pas vide
                other_results.append(price.text.strip())
            else :
                other_results.append('0.00€')

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

df.to_csv('products_myprotein.csv', index=False, encoding='utf-8')
