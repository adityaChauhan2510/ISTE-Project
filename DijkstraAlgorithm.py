#Shortest Path Algorithm

def dijkstra(graph, source, destination):
    distances = {node: float('infinity') for node in graph}
    distances[source] = 0
    unvisited_nodes = set(graph)

    while unvisited_nodes:
        current_node = min(unvisited_nodes, key=lambda node: distances[node])

        if current_node == destination:
            break

        for neighbour, distance in graph[current_node].items():
            if distance + distances[current_node] < distances[neighbour]:
                distances[neighbour] = distance + distances[current_node]

        unvisited_nodes.remove(current_node)

    return distances[destination]





if __name__== "__main__":
    graph = {
        'A' : {'B':2, 'C':4},
        'B' : {'A':2, 'C':3, 'D':8},
        'C' : {'A':4, 'B':3, 'E':5, 'D':2},
        'D' : {'B':8, 'C':2, 'E':11, 'F':22},
        'E' : {'C':5, 'D':11, 'F':1},
        'F' : {'D':22, 'E':1}
    }

    source = 'A'
    destination = 'F'
    print(dijkstra(graph, source, destination))