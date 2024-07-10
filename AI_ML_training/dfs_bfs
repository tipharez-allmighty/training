import queue
import networkx as nx
import matplotlib.pyplot as plt
import time

def order_dfs(graph, start_node):
    visited = set()
    stack = [start_node]
    order = []

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            order.append(vertex)
            visited.add(vertex)
            for node in graph[vertex]:  
                if node not in visited:
                    stack.append(node)

    return order
    

def visualize_search(order, title, G, pos):
    plt.figure()
    plt.title(title)
    for i,node in enumerate(order,start=1):
        plt.clf()
        plt.title(title)
        nx.draw(G, pos, with_labels=True,node_color=['r' if n == node else 'g' for n in G.nodes])
        plt.draw()
        plt.pause(1)
    plt.show()
    time.sleep(0.5)

G = nx.Graph()
G.add_edges_from([('A','S'),
                  ('A','C'),
                  ('C','G'),
                  ('S','B'),
                  ('S','D'),
                  ('C','D'),
                  ('B','S'),
                  ('B','D'),
                  ('D','G')])
pos = nx.spring_layout(G)

visualize_search(order_dfs(G, 'S'), 'DFS Visualization', G, pos)

