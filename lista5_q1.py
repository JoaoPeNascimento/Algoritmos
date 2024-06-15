def parse_input(input_string):
    lines = input_string.strip().split('\n')
    n = int(lines[0])
    u = int(lines[1])
    b = float(lines[2])
    graph = {i: set(map(int, line.split()[1:])) for i, line in enumerate(lines[3:], start=1)}
    return n, u, b, graph


def breadth_first_search(graph, start, depth):
    visited = set([start])
    frontier = [start]
    for i in range(depth):
        next_frontier = []
        for u in frontier:
            next_frontier.extend(graph[u] - visited)
            visited.update(graph[u])
        frontier = next_frontier
    return visited


def calculate_reach(n, u, b, graph):
    reach = breadth_first_search(graph, u, 1)
    if len(reach) <= b:
        return sorted(reach)
    else:
        depth = 1
        while True:
            depth += 1
            reach = breadth_first_search(graph, u, depth)
            if len(reach) <= b:
                return sorted(reach)
            cost = (len(reach) - b) * 5.25
            if cost > b:
                return sorted(breadth_first_search(graph, u, depth - 1))
            b -= cost