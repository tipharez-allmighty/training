import heapq

def dijkstra(graph, start, end):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        if current_node == end:
            return distances
        
        if current_distance > distances[current_node]:
            continue
        
        for neighbor, weight in graph[current_node].items():
            new_distance = current_distance + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heapq.heappush(priority_queue, (new_distance, neighbor))
        
    return distances 

def bellman_ford(graph, src):
    distances = {
        node: float('inf') for node in graph
    }
    predecessors = {
        node: None for node in graph
    }
    distances[src] = 0
    
    for _ in range(len(distances) - 1):
        for src in graph:
            for dest, weight in graph[src].items():
                if distances[src] != float('inf') and distances[src] + weight < distances[dest]:
                    distances[dest] = distances[src] + weight
                    predecessors[dest] = src
                    
    for src in graph:
        for dest, weight in graph[src].items():
            if distances[src] != float('inf') and distances[src] + weight < distances[dest]:
                print('Negative Cycle Detected')
                return None
    print(distances)
    return predecessors        

def getBellmanFordPath(predecessors: dict[any], start, end):
    if not predecessors:
        return None
    result = []
    current = end
    while current != start:
        result.append(current)      
        current = predecessors.get(current)
    result.append(start)
    return result[::-1]
    
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}
