import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv(r"C:\Users\Luis Henrique\Desktop\testes-ebac\visualização-de-dados\ecommerce_preparados.csv")

#Histograma
plt.figure(figsize=(10, 6))
plt.hist(df['Nota'], bins=100, color='orange',alpha=0.8) 
plt.title('Histograma - Notas')
plt.xlabel('Nota')
plt.ylabel('Frequência')
plt.grid(True)

#Dispersão
plt.figure(figsize=(10, 6))
plt.scatter(df['Preço'], df['Preço'], color='orange', alpha=0.8, s=30)
plt.title('Dispersão - Preço')
plt.xlabel('Preço')
plt.ylabel('Preço')

#Calor
plt.figure(figsize=(10, 6))
corr = df[['Desconto', 'Nota']].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlação Desconto e Nota')

#Barra
plt.figure(figsize=(8, 8))
df['Gênero'].value_counts().plot(kind='bar', color='orange')
plt.title('Escalonamento Gênero')
plt.xlabel('Gênero')
plt.ylabel('Quantidade')


#Pizza
x= df['Temporada'].value_counts().index
y= df['Temporada'].value_counts().values
 
plt.figure(figsize=(10, 6))
plt.pie(y, labels=x, autopct='%.1f%%', startangle=90)
plt.title('Distribuição de Gênero')

#Densidade
plt.figure(figsize=(10, 6))
sns.kdeplot(df['Preço'], fill=True, color='orange')
plt.title('Desnsidade de Preços')
plt.xlabel('Preço')

#Regressão
sns.regplot(x='Preço', y='N_Avaliações', data=df, color='orange', scatter_kws={'alpha':0.5, 'color':'grey'})
plt.title('Regressão de Preço e N_Avaliações')
plt.xlabel('N_Avaliações')
plt.ylabel('Preço')

plt.show()