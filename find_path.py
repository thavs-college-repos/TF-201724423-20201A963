from src.data import trafico
from path import lo_siento
from collections import defaultdict

# Crear list de adjacencya en grafo y crear Graph en main() 

class Graph:
    def __init__(self, adjacency_list):
        self.adjacency_list = adjacency_list
        self.H = {k:1 for k in self.adjacency_list.keys()}

    def get_neighbors(self, v):
        return self.adjacency_list[v]

    def h(self, n):
        return self.H[n]

    def a_star_algorithm(self, start_node, stop_node):
        open_list = set([start_node])
        closed_list = set([])

        g = {}

        g[start_node] = 0

        parents = {}
        parents[start_node] = start_node

        while len(open_list) > 0:
            n = None

            for v in open_list:
                if n == None or g[v] + self.h(n) < g[n] + self.h(n):
                    n = v;

            if n == None:
                print('Path does not exist!')
                return None

            if n == stop_node:
                reconst_path = []

                while parents[n] != n:
                    reconst_path.append(n)
                    n = parents[n]

                reconst_path.append(start_node)

                reconst_path.reverse()

                print('Path found: {}'.format(reconst_path))
                return reconst_path

            for (m, weight) in self.get_neighbors(n):
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight

                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n

                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)

            open_list.remove(n)
            closed_list.add(n)

        print('Path does not exist!')
        return None
    


def find_path(a, b):
    """df = trafico()
    print (df.head())
    print( df.columns )
    print( df.dtypes )"""
    
    
    (df, paths) = lo_siento()
        
    print( a, b )
    
    # Creo lista de adjacencia de calles
    adjency_list = defaultdict(list);
    for _, row in df.iterrows():
        
        for i, p in enumerate(row["paths"]):  
            #print(row['id'], p, end="   ")  
                adjency_list[int(row['id'])].append((int(p), int((row['factor_trafico']) + 1) * (i % 5 + 1)))

        #print()

            
    g = Graph(adjency_list)
    
    streets = g.a_star_algorithm(a, b)
    street_trafico = []
    
    for street in streets:
        street_trafico.append((street, df[df['id'] == street]['factor_trafico'].values[0]))
    
    
    return (street_trafico, paths)