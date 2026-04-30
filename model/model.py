from datetime import datetime

from database.DAO import DAO
import networkx as nx

class Model:
    def __init__(self):
        self._fermate = DAO.getAllFermate()
        self._grafo = nx.DiGraph()
        self._idMapFermate = {}
        for f in self._fermate:
            self._idMapFermate[f.id_fermata] = f

    def getBFSNodesFromEdges(self, source):
        archi = nx.bfs_edges(self._grafo, source)
        nodiBFS = []
        for u, v in archi:
            nodiBFS.append(v)

        return nodiBFS

    def getBFSNodesFromTree(self, source):
        tree = nx.bfs_tree(self._grafo, source)
        archi = list(tree.edges())
        nodi = list(tree.nodes())
        return nodi

    def getDFSNodesFromEdges(self, source):
        archi = nx.dfs_edges(self._grafo, source)
        nodiDFS = []
        for u, v in archi:
            nodiDFS.append(v)

        return nodiDFS

    def getDFSNodesFromTree(self, source):
        tree = nx.dfs_tree(self._grafo, source)
        archi = list(tree.edges())
        nodi = list(tree.nodes())
        return nodi







    def buildGraph(self):
        self._grafo.clear()
        self._grafo.add_nodes_from(self._fermate)

        #tic = datetime.now()
        #self.addedges()
        #toc = datetime.now()
        #print(f"Tempo impiegato da modo 1: {toc - tic}")   -- tempo: 1.57

        #tic2 = datetime.now()
        #self.addedges2()
        #toc2 = datetime.now()
        #print(f"Tempo impiegato da modo 2: {toc2 - tic2}")  -- tempo: 00.18

        tic3 = datetime.now()
        self.addedges3()
        toc3 = datetime.now()
        print(f"Tempo impiegato da modo 3: {toc3 - tic3}")  # -- tempo: 00.0047


    # questo è il metodo migliore per grafi con pochi nodi
    # ma per grafi con tanti nodi, come questo, è sconsigliato
    def addedges(self):
        self._grafo.clear_edges()
        for u in self._fermate:
            for v in self._fermate:
                if DAO.hasconn(u, v):
                    self._grafo.add_edge(u, v)

    def addedges2(self):
        self._grafo.clear_edges()
        for u in self._fermate:
            for conn in DAO.getvicini(u):
                v = self._idMapFermate[conn.id_stazA]
                self._grafo.add_edge(u, v)

    # soluzione, tipicamente difficile, consigliata per grafi con tanti nodi
    def addedges3(self):
        self._grafo.clear_edges()
        alledges = DAO.getAllEdges()
        for conn in alledges:
            u = self._idMapFermate[conn.id_stazP]
            v = self._idMapFermate[conn.id_stazA]
            self._grafo.add_edge(u, v)


    def get_numnodi(self):
        return len(self._grafo.nodes)

    def get_numarchi(self):
        return len(self._grafo.edges)


    @property
    def fermate(self):
        return self._fermate