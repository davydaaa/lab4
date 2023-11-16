def has_cycle(graph, v, visited, parent):
    visited[v] = True
    for neighbor in graph[v]:
        if not visited[neighbor]:
            if has_cycle(graph, neighbor, visited, v):
                return True
        elif parent != neighbor and visited[neighbor]:
            return True
    return False

def is_cyclic(graph):
    num_vertices = len(graph)
    visited = [False] * num_vertices
    for v in range(num_vertices):
        if not visited[v]:
            if has_cycle(graph, v, visited, -1):
                return True
    return False

def main():
    with open("input.txt", "r") as input_file:
        num_vertices, num_edges = map(int, input_file.readline().split())
        graph = [[] for _ in range(num_vertices)]
        for _ in range(num_edges):
            u, v = map(int, input_file.readline().split())
            graph[u - 1].append(v - 1)
            graph[v - 1].append(u - 1)

    with open("output.txt", "w") as output_file:
        if is_cyclic(graph):
            output_file.write("True\n")
        else:
            output_file.write("False\n")

if __name__ == "__main__":
    main()
