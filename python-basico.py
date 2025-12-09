#Listas

#%%

minha_lista = [1, 2, 3]

type(minha_lista)

print(minha_lista[0:-1])

#Metodos básicos

#%%
l = minha_lista

l.append('4')

print(l)

lista2 = [l, minha_lista]

print(lista2[0][1])


#Dicionário

dicionario = {"nome": "Joe", "idade": 30, "filhos": ["jow", "jane"]}

print(dicionario.get("filhos"))

#%% 


for i in range(10):
    print(i)
    
world = "string"

list_worlds = [w for w in world]

print(list_worlds)