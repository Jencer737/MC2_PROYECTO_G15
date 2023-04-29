from graficar import iniciG

Nodo = dict()
resultado = {}
conjuntos = []
grafo={}

def Make_set(vertice):
    Nodo[vertice] = vertice

def Find_set(vertice):
    if Nodo[vertice] != vertice:
        Nodo[vertice] = Find_set(Nodo[vertice])
    return Nodo[vertice]

def Union(u, v, Ordenada):
    Dato1 = Find_set(u)
    Dato2 = Find_set(v)
    if Dato1 != Dato2:
        for Dato in Ordenada:
            Nodo[Dato1] = Dato2

def Kruskal(grafo):
    resultante = []
    cont = 0
    for vertice in grafo['A']:
        Make_set(vertice)

    Ordenada = list(grafo['B'])
    Ordenada.sort()
    Ordenada = [(a,b,c) for c,a,b in Ordenada]
    print ("==============================")
    print ("Datos Ordenados")
    print ("==============================")
    print ("Ordenados:",Ordenada)

    iniciG(Ordenada)

    Ordenada = [(c,a,b) for a,b,c in Ordenada]
    for Dato in Ordenada:
        peso, u, v = Dato
        if Find_set(u) != Find_set(v):
            resultante.append(Dato)
            print ("==============================")
            print ("Paso:",cont)
            print ("==============================")
            resultante = [(a,b,c) for c,a,b in resultante]
            print ("Resultante: ",resultante)
            resultante = [(c,a,b) for a,b,c in resultante]
            cont+=1
            Union(u, v, Ordenada)
    #iniciG(resultante)
    return resultante



def inicio(grafo2):
    for i in grafo2:
        grafo=i
        print(i)

    resultante = Kruskal(grafo)
    resultante = [(a,b,c) for c,a,b in resultante]
    iniciG(resultante)
    for origen,destino,peso in resultante:
        if origen in resultado:
            if destino in resultado:
                lista = resultado[origen]
                resultado[origen] = lista+[(destino,peso)]
                lista = resultado[destino]
                lista.append((origen,peso))
                resultado[destino] = lista
            else:
                resultado[destino] = [(origen,peso)]
                lista = resultado[origen]
                lista.append((destino,peso))
                resultado[origen] = lista
        elif destino in resultado:
            resultado[origen] = [(destino,peso)]
            lista = resultado[destino]
            lista.append((origen,peso))
            resultado[destino] = lista
        else:
            resultado[destino] = [(origen,peso)]
            resultado[origen] = [(destino,peso)]
    print ("\n=========Resultados=========")
    print ("Arbol de expansion minima:")
    for key, lista in resultado.items():
        print (key)
        print (lista)
    print ("==============================")
    #os.system("pause")