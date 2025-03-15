from collections import deque

class Graph:
    def __init__(self, adj_list: dict[any, list[any]] | None = None):
        if adj_list is None:
            adj_list = {}
        self.adj_list = adj_list
    
    def __repr__(self):
        return str(self.adj_list)
    
    def addVertex(self, vertex, values: list[any] | None = None):
        self.adj_list[vertex] = []
        if values:
            for value in values:
                if value in self.adj_list:
                    self.adj_list[vertex].append(value)

    def addEdge(self, vertex, edge):
        if edge in self.adj_list and vertex in self.adj_list:
            self.adj_list[vertex].append(edge)
        
    def removeEdge(self, edge, vertex):
        if vertex in self.adj_list:
            if edge in self.adj_list[vertex]:
                self.adj_list[vertex].remove(edge)
    
    def removeVertex(self, vertex):
        if vertex in self.adj_list:
            self.adj_list.pop(vertex)
        for key in self.adj_list:
            if vertex in self.adj_list[key]:
                self.adj_list[key].remove(vertex)
    
    def bfs(self, start):
        if not start or start not in self.adj_list:
            return None
        visited = set()
        queue = deque([start])
        visited.add(start)
        while queue:
            current_vertex = queue.popleft()
            print(current_vertex)
            if current_vertex not in visited:
                visited.add(current_vertex)
            for edge in self.adj_list[current_vertex]:
                if edge not in visited:
                    queue.append(edge)
    
    def dfs(self, start):
        if not start or start not in self.adj_list:
            return None
        visited = set()
        stack = [start]
        visited.add(start)
        while stack:
            current_vertex = stack.pop()
            print(current_vertex)
            if current_vertex not in visited:
                visited.add(current_vertex)
            for edge in self.adj_list[current_vertex][::-1]:
                if edge not in visited:
                    stack.append(edge)                    
    
    def dfs_rec(self, start, visited: set | None = None):
        if not start or start not in self.adj_list:
            return None
        if visited is None:
            visited = set()
        if start not in visited:
            visited.add(start)
            print(start)
            for edge in self.adj_list[start]:
                self.dfs_rec(edge, visited)
    
    def topological_sort(self):
        topological_order = []
        visited = set()
        
        def topological_sort_util(node):
            visited.add(node)
            for edge in self.adj_list[node]:
                if edge not in visited:
                    topological_sort_util(edge)
                    
            topological_order.append(node)
            
        for vertex in self.adj_list:
            if vertex not in visited:
                topological_sort_util(vertex)
        print(topological_order)

    def bfsShortestPath(self, start, end):             
        queue = [[start]]
        while queue:
            path = queue.pop(0)
            current_vertex = path[-1]
            if current_vertex == end:
                return path
            for edge in self.adj_list.get(current_vertex, []):
                queue.append(path + [edge])
