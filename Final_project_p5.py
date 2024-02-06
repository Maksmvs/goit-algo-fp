import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque
import time

class Node:
    def __init__(self, key, color="#FFFFFF"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  
        self.id = str(uuid.uuid4())  

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root, traversal_order=None):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    
    if traversal_order:
        for i in range(len(traversal_order) - 1):
            plt.plot([pos[traversal_order[i]][0], pos[traversal_order[i + 1]][0]],
                     [pos[traversal_order[i]][1], pos[traversal_order[i + 1]][1]],
                     color='red', linestyle='-', linewidth=2)
    
    plt.show()

def depth_first_traversal(node, level, max_level, traversal_order=None):
    if traversal_order is None:
        traversal_order = []
    if node is None:
        return traversal_order
    color_intensity = int(255 * ((max_level - level) / max_level))  
    color = "#{:02x}{:02x}{:02x}".format(color_intensity, color_intensity, color_intensity)
    node.color = color
    traversal_order.append(node.id)
    traversal_order = depth_first_traversal(node.left, level + 1, max_level, traversal_order)
    traversal_order = depth_first_traversal(node.right, level + 1, max_level, traversal_order)
    return traversal_order

def breadth_first_traversal(root):
    if root is None:
        return []
    traversal_order = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        traversal_order.append(node.id)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return traversal_order

root = Node(0)
root.left = Node(1)
root.left.left = Node(3)
root.left.right = Node(4)
root.right = Node(2)
root.right.left = Node(5)
root.right.right = Node(6)

print("Depth First Traversal:")
start_dfs = time.time()
dfs_order = depth_first_traversal(root, 0, 3)
end_dfs = time.time()
print("Час виконання обходу в глибину:", end_dfs - start_dfs, "секунд")

draw_tree(root, dfs_order)

print("\nBreadth First Traversal:")
start_bfs = time.time()
bfs_order = breadth_first_traversal(root)
end_bfs = time.time()
print("Час виконання обходу в ширину:", end_bfs - start_bfs, "секунд")

draw_tree(root, bfs_order)
