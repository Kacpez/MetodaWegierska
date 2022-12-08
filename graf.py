import matplotlib.pyplot as plt
import networkx as nx
from networkx.algorithms import bipartite
import numpy as np

#funkcja pomocnicza dodająca wsztkie krawędzie do wierzchłków 
def dodaj_krawedz_z_waga(B,n1,n2,macierz):
    for i in range(len(n1)):
        for j in range(len(n2)):
            B.add_edge(n1[i], n2[j], weight = macierz[i][j])
    return B

#funkcja rysująca graf dwudzielny
def rysuj_graf_z_przydzialem(macierz,result):
    B = nx.Graph()
    N=len(macierz)
    #dodawanie wierzcholkow aby powstal graf dwudzielny
    lewe_wierzcholki = []
    prawe_wierzcholki = []
    for i in range(N):
        lewe_wierzcholki.append("P"+str(i+1))
        prawe_wierzcholki.append("S"+str(i+1))
    B.add_nodes_from(lewe_wierzcholki, bipartite=0)
    B.add_nodes_from(prawe_wierzcholki, bipartite=1)

    #dodawanie krawędzi
    macierz_kosztow=np.array(macierz)
    B= dodaj_krawedz_z_waga(B,lewe_wierzcholki,prawe_wierzcholki,macierz_kosztow)
    zbior = nx.bipartite.sets(B)[0]
    pozycja = nx.bipartite_layout(B, zbior)
    #kolory wierchołków
    kolor_wierzcholka=[]
    for i in range(N):
        kolor_wierzcholka.append("lightblue")
    for i in range(N):
        kolor_wierzcholka.append("yellow")
    #zaznacznie krawędzi optymalnego przypisania
    przydzielone=[]
    for i in range(N):
        for j in range(N):
            if (i,j) in result:
                przydzielone.append((lewe_wierzcholki[i],prawe_wierzcholki[j]))
    #rysowanie            
    nx.draw(B, pos=pozycja, node_size=700,with_labels=True, node_color=kolor_wierzcholka)
    nx.draw_networkx_edges(B, pozycja, edgelist=przydzielone, width=4, alpha=1, edge_color="green")
    edge_labels = nx.get_edge_attributes(B, "weight")
    nx.draw_networkx_edge_labels(B, pozycja, edge_labels,label_pos=0.85)
    plt.show()

def rysuj_graf(macierz):
    B = nx.Graph()
    N=len(macierz)
    #dodawanie wierzcholkow aby powstal graf dwudzielny
    lewe_wierzcholki = []
    prawe_wierzcholki = []
    for i in range(N):
        lewe_wierzcholki.append("P"+str(i+1))
        prawe_wierzcholki.append("S"+str(i+1))
    B.add_nodes_from(lewe_wierzcholki, bipartite=0)
    B.add_nodes_from(prawe_wierzcholki, bipartite=1)

    #dodawanie krawędzi
    macierz_kosztow=np.array(macierz)
    B= dodaj_krawedz_z_waga(B,lewe_wierzcholki,prawe_wierzcholki,macierz_kosztow)
    zbior = nx.bipartite.sets(B)[0]
    pozycja = nx.bipartite_layout(B, zbior)
    #kolory wierchołków
    kolor_wierzcholka=[]
    for i in range(N):
        kolor_wierzcholka.append("lightblue")
    for i in range(N):
        kolor_wierzcholka.append("yellow")
    #rysowanie
    nx.draw(B, pos=pozycja, node_size=700,with_labels=True, node_color=kolor_wierzcholka)
    edge_labels = nx.get_edge_attributes(B, "weight")
    nx.draw_networkx_edge_labels(B, pozycja, edge_labels,label_pos=0.85)
    plt.show()


