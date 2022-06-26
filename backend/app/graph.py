class Graph: 

    def __init__(self, edges: dict) -> None: 
        self.graph = dict
        self.add_edges(edges)
    
    def add_edges(self, edges: dict) -> None:
        self.graph = edges

    def get_edges(self) -> None:
        edges = []
        for key in self.graph.keys():
            edges.append((key, self.graph[key]))
        return edges

    def get_nodes(self) -> list:
        return list(self.graph.keys())

    def get_neighbors(self) -> dict:
        return self.graph

    def find_shortest_path(self, start: str, end: str, path=[]) -> list:
        explored = list()
        queue = list()
        queue.append([start])

        if start == end:
            return queue 
        
        while queue:
            path = queue.pop(0)
            node = path[-1]

            if node not in explored:
                neighbors = self.graph.get(node, [])
                for neighbour in neighbors:
                    new_path = list(path)
                    new_path.append(neighbour)
                    queue.append(new_path)

                    if neighbour == end:
                        return new_path 

        return False 