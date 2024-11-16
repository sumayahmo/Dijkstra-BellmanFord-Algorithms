import heapq
import networkx as nx
import matplotlib.pyplot as plt

# خوارزمية بيلمان فورد
def bellman_ford_sumayya(graph, start):
    # تعيين المسافات لجميع العقد إلى قيمة لا نهائية
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # تحديث المسافات لجميع العقد
    for _ in range(len(graph) - 1):
        for u in graph:
            for v, weight in graph[u]:
                if distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight
    return distances

# خوارزمية ديكسترا
def dijkstra_sumayya(graph, start):
    queue = [(0, start)]  # قائمة الأولويات للعقد
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_distance > distances[current_node]:
            continue

        # تحديث مسافات الجيران
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
    return distances

# تعريف الرسم البياني
graph_sumayya = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)],
}

start_node_sumayya = 'A'

# تنفيذ الخوارزميتين
bellman_ford_result = bellman_ford_sumayya(graph_sumayya, start_node_sumayya)
dijkstra_result = dijkstra_sumayya(graph_sumayya, start_node_sumayya)

print("Bellman Ford Result : ", bellman_ford_result)
print("Dijkstra Result :", dijkstra_result)

# عرض الرسم البياني باستخدام مكتبة NetworkX
G_sumayya = nx.DiGraph()
G_sumayya.add_weighted_edges_from([
    ('A', 'B', 1), ('A', 'C', 4),
    ('B', 'C', 2), ('B', 'D', 5),
    ('C', 'D', 1)
])

pos_sumayya = nx.spring_layout(G_sumayya)
nx.draw(G_sumayya, pos_sumayya, with_labels=True, node_size=2000, node_color='skyblue', font_size=16)
labels_sumayya = nx.get_edge_attributes(G_sumayya, 'weight')
nx.draw_networkx_edge_labels(G_sumayya, pos_sumayya, edge_labels=labels_sumayya)

plt.show()
