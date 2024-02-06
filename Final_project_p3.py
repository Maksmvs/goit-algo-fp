import networkx as nx
import matplotlib.pyplot as plt
import heapq

def dijkstra(graph, start):
    distances = {city: float('infinity') for city in graph}
    distances[start] = 0
    heap = [(0, start)]

    while heap:
        current_distance, current_city = heapq.heappop(heap)
        if current_distance > distances[current_city]:
            continue
        for neighbor, distance in graph[current_city].items():
            total_distance = current_distance + distance
            if total_distance < distances[neighbor]:
                distances[neighbor] = total_distance
                heapq.heappush(heap, (total_distance, neighbor))

    return distances

def create_shortest_paths_graph(graph, start_city):
    shortest_distances = dijkstra(graph, start_city)

    shortest_paths_graph = {start_city: {}}
    for city in graph.keys():
        if city != start_city and shortest_distances[city] != float('inf'):
            shortest_paths_graph[start_city][city] = shortest_distances[city]

    return shortest_paths_graph

def visualize_graph(graph, start_city):
    G = nx.Graph()
    for city, neighbors in graph.items():
        for neighbor, distance in neighbors.items():
            G.add_edge(city, neighbor, weight=distance)

    pos = nx.spring_layout(G)
    plt.figure(figsize=(12, 10))

    nx.draw(G, pos, with_labels=True, node_size=2000, node_color='skyblue', font_size=12, font_weight='bold')
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    plt.title(f"Граф найкоротших відстаней з міста {start_city}")
    plt.show()

graph = {
    'Київ': {'Харків': 500, 'Львів': 550, 'Одеса': 450, 'Дніпро': 475, 'Чернівці': 600},
    'Харків': {'Київ': 500, 'Львів': 750, 'Одеса': 700, 'Дніпро': 400, 'Чернівці': 800},
    'Львів': {'Київ': 550, 'Харків': 750, 'Одеса': 850, 'Дніпро': 700, 'Чернівці': 400},
    'Одеса': {'Київ': 450, 'Харків': 700, 'Львів': 850, 'Дніпро': 600, 'Чернівці': 750},
    'Дніпро': {'Київ': 475, 'Харків': 400, 'Львів': 700, 'Одеса': 600, 'Чернівці': 525},
    'Чернівці': {'Київ': 600, 'Харків': 800, 'Львів': 400, 'Одеса': 750, 'Дніпро': 525}
}


start_city = input("Введіть назву початкового міста: ")

shortest_paths_graph = create_shortest_paths_graph(graph, start_city)

visualize_graph(shortest_paths_graph, start_city)
