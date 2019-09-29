# exemplo lista

lista = [] #lista vazia
l1 = ["joao", "maria", 20, 1.50, 56, "Nah"]
l2 = l1 # fazendo isso se atualiza
l3 = l1.copy() # aqui não altera
l1[3]=1.51
print(l1)
print(l2)
print(l3)

l1.append("jumento")
print(l1[3:-1])

len(l1)
l1 [ len(l1)-1]
l1[-1]
l1[0:-1]

l4 = l1[:]

l4.remove("jumento")

print(l1)

l1[ 1: :2 ]
l1[ : : -2]

