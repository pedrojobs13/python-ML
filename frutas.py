import pandas as pd
from sklearn import tree
import matplotlib.pyplot as plt

df = pd.read_excel("dados/dados_frutas.xlsx")

print(df.head())

arvore = tree.DecisionTreeClassifier(random_state=42)

y = df['Fruta']

caracteristicas = ["Arredondada", "Suculenta", "Vermelha", "Doce"]

X = df[caracteristicas]


# Caracteristica e respostas 
arvore.fit(X.values, y)

print(arvore.predict([[0,0,0,0]]))

plt.figure(dpi=400)
tree.plot_tree(arvore, 
              feature_names=caracteristicas, 
              class_names=arvore.classes_, 
              filled=True)
plt.show()