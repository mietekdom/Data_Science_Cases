# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

############ PART 1 PREPROCESING

# %% import danych z pliku .csv

df = pd.read_csv('./data_amazon/Consumer_Reviews_Amazon.csv', index_col=0)

# %% ogólne informacje

df.describe() # liczymy podstawowe statystyki dla kolumn

# %% listujemy jakie mamy kolumny

for col in df.columns:
    print(col)
    
# %% usuwamy kropki z nazw kolumn i zamieniamy na podkreslnik

df.columns = [col.replace('.', '_') for col in df.columns]

# %% wycinamy kolumny które nas interesują

df_new = df[['name', 'primaryCategories', 'reviews_rating', 'reviews_text']]

# %% zmieniamy nazwe kolumn

df_new.columns = ['name', 'category', 'rating', 'text']

df_new.info() # informacje o danych po edycji
df_new.describe() # informacje o danych po edycji

# %% export nowej ramki danych do pliku csv

df_new.to_csv('./data_amazon/review_clean.csv')


############ PART 2 ANALIZA


# %% import danych z pliku

df_review_clean = pd.read_csv('./data_amazon/review_clean.csv', index_col=0)

# %% plotowanie kategori (określamy czego mamy najwiecej w pliku)

df_review_clean['category'].value_counts().plot(kind='pie') #wykres kołowy

# %% plotowanie frekwęcji ocen 
# sortowanie od 1 do 5 (sort_index)

df_review_clean['rating'].value_counts().sort_index().plot(kind='bar', 
               legend=True, title='Frequency')

# %% typowanie trzech najlepej ocenianych produktów

tmp = df_review_clean.groupby('name').count()['rating'].rename('count').\
nlargest(3).plot(kind='bar')

# %% typowanie trzech najwyzej oceninych produktów

df_review_clean.groupby('name').agg('mean').\
rename(columns={'rating': 'avg_rating'}).nlargest(3, columns='avg_rating')

# %% typowanie trzy najgorzej ocenianych produktów

df_review_clean.groupby('name').agg('mean').\
rename(columns={'rating': 'avg_rating'}).nsmallest(3, columns='avg_rating')



