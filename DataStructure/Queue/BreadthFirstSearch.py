import copy


def recursive_bfs(graph, queue, visited):
    print('---------------------')
    print(queue)
    print(visited)

    if not queue:
        return

    v = queue.pop(0)
    visited.append(v)

    for n in graph[v]:
        if n not in visited and n not in queue:
            queue.append(n)

    recursive_bfs(graph, queue, visited)


def iterative_bfs(graph, start):
    queue = [start]
    visited = []

    while queue:
        print('--------------')
        v = queue.pop(0)
        visited.append(v)
        for n in graph[v]:
            # only add neighbor to queue if not visited, and not already in queue
            if n not in visited and n not in queue:
                queue.append(n)
        print(queue)
        print(visited)


def iterative_bfs_with_dist_and_parent(graph, start):
    queue = [start]
    visited = []
    dist = {start: 0}
    parent = {start: None}
    i = 0

    while queue:
        print('--------------')
        print('level: ', i)
        print(queue)
        v = queue.pop(0)
        visited.append(v)

        for n in graph[v]:
            # only add neighbor to queue if not visited, and not already in queue
            if n not in visited and n not in queue:
                queue.append(n)
                parent[n] = v
                # dist is parent_dist + 1
                dist[n] = dist[v] + 1

        # print(visited)

    return dist, parent


def shortest_path(graph, start, goal):
    if goal == start:
        return "goal is start"

    dist, parent = iterative_bfs_with_dist_and_parent(graph, start)
    print(dist)

    if goal not in parent:
        return "no path between start and goal"

    path = [goal]
    v = copy.copy(goal)
    while parent[v] != start:
        next_p = parent[v]
        path.insert(0, next_p)
        v = next_p
    path.insert(0, start)

    print(path)
    return path


if __name__ == "__main__":
    g1 = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'D'],
        'D': ['B', 'C', 'E'],
        'E': ['B', 'D']}

    g2 = {(0, 0): [(1, 0)],
          (0, 2): [(1, 2), (0, 3)],
          (0, 3): [(0, 2)],
          (1, 0): [(0, 0), (2, 0), (1, 1)],
          (1, 1): [(1, 0), (1, 2)],
          (1, 2): [(0, 2), (2, 2), (1, 1)],
          (2, 0): [(1, 0), (3, 0)],
          (2, 2): [(1, 2), (3, 2)],
          (3, 0): [(2, 0)],
          (3, 2): [(2, 2), (3, 3)],
          (3, 3): [(3, 2)]}

    # shortest_path(g2, (0, 2), (3, 3))

    # iterative_bfs(g1, 'A')
    recursive_bfs(g1, ['A'], [])
