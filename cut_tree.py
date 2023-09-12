import unittest


# https://www.hackerrank.com/challenges/cut-the-tree/problem


graph = {}


def build_graph(edges):
    for edge in edges:
        graph[edge[0]] = graph.get(edge[0], list())
        graph[edge[1]] = graph.get(edge[1], list())
        if edge[0] in graph and edge[0]:
            children = graph[edge[0]]
            children.append(edge[1])
            graph[edge[0]] = children
        if edge[1] in graph and edge[1]:
            children = graph[edge[1]]
            children.append(edge[0])
            graph[edge[1]] = children

    return graph


visited = set()
min_difference = 0


def dfs(visited, graph, node, data, total_sum, current_sum):  # function for dfs
    if node not in visited:
        current_sum += data[node - 1]
        global min_difference
        min_difference = abs(min(min_difference, (total_sum - 2 * current_sum)))
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour, data, total_sum, current_sum)


def cutTheTree(data, edges):
    global min_difference
    total_sum = min_difference = sum(data)
    graph = build_graph(edges)
    dfs(visited, graph, 1, data, total_sum, 0)
    return min_difference


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        self.assertEqual(
            cutTheTree([1, 2, 3, 4, 5, 6], [(1, 2), (1, 3), (2, 6), (3, 4), (3, 5)]), 3
        )

    def test_b(self):
        self.assertEqual(
            cutTheTree(
                [100, 200, 100, 500, 100, 600], [(1, 2), (2, 3), (2, 5), (4, 5), (5, 6)]
            ),
            400,
        )


if __name__ == "__main__":
    unittest.main()
