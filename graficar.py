import networkx as nx
import matplotlib.pyplot as plt


def agregar_arista(G, u, v, w=1, di=True):
    G.add_edge(u, v, weight=w)

    # Si el grafo no es dirigido
    if not di:
        # Agrego otra arista en sentido contrario
        G.add_edge(v, u, weight=w)

def iniciG(graf):
    G = nx.DiGraph()
    for i in graf:
        #print()
        agregar_arista(G, i[0], i[1], int(i[2]))


    # Draw the networks
    pos = nx.layout.planar_layout(G)
    nx.draw_networkx(G, pos)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.title("Grafo")
    plt.show()