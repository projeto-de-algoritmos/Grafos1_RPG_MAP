class Graph: 

    def __init__(self, edges: dict) -> None: 
        self.graph = dict()
        self.init_graph(edges)
    
    def init_graph(self, edges: dict) -> None:
        self.graph = edges

    def get_edges(self) -> None:
        edges = list()
        for key in self.graph.keys():
            edges.append((key, self.graph.get(key)))
        return edges

    def get_nodes(self) -> list:
        return list(self.graph.keys())

    def get_graph(self) -> dict:
        return self.graph

    def find_shortest_path(self, start: str, end: str, path=[]) -> list:
        visited = dict()
        queue = list()
        parent = dict()

        if start == end:
            return [start]
        
        for node in self.get_nodes():
            visited[node] = False
            parent[node] = None

        queue.append(start) 
        visited[start] = True

        while queue:
            node = queue.pop(0)
            for neighbor in self.graph.get(node):
                if not visited[neighbor]:
                    queue.append(neighbor)
                    visited[neighbor] = True
                    parent[neighbor] = node

        path = list()

        while end:
            path.append(end)
            end = parent[end]

        path.reverse()

        return path                    
                