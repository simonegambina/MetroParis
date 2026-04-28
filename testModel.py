from model.model import Model

model = Model()

#print("Numero nodi: ", len(model._grafo.nodes))
print("Numero nodi: ", model.get_numnodi())
print("Numero archi: ", model.get_numarchi())

model.buildGraph()

#print("Numero nodi: ", len(model._grafo.nodes))
print("Numero nodi: ", model.get_numnodi())
print("Numero archi: ", model.get_numarchi())