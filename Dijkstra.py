import math

graph = {
    "start": {"a": 6, "b": 2},
    "a": {"fin": 1},
    "b": {"a": 3, "fin": 5},
    "fin": {}
}

infinity = math.inf
costs = {
    "a": 6,
    "b": 2,
    "fin": infinity
}

parents = {
    "a": "start",
    "b": "start",
    "fin": None
}

processed = set()

def find_lowest_cost_node(costs):
    lowest_cost = math.inf
    lowest_cost_node = None
    for node, cost in costs.items():
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]

    for neighbor, distance in neighbors.items():
        new_cost = cost + distance
        if costs[neighbor] > new_cost:
            costs[neighbor] = new_cost
            parents[neighbor] = node

    processed.add(node)
    node = find_lowest_cost_node(costs)

def get_path(parents, start, end):
    path = []
    current_node = end
    while current_node is not None:
        path.append(current_node)
        current_node = parents.get(current_node)
    path.reverse()

    if path[0] == start:
        return path
    return None

print("Costs:", costs)
print("Parents:", parents)

path = get_path(parents, "start", "fin")
if path:
    print("Path:", " -> ".join(path))
else:
    print("No path found.")
