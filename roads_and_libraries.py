import unittest


# https://www.hackerrank.com/challenges/torque-and-development

def dfs(visited, graph, node):
    if node not in visited:
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)
    return visited


def roadsAndLibraries(n, c_lib, c_road, cities):
    if c_lib <= c_road:
        return c_lib * n
    # build the graph
    graph = {}
    for i in range(1, n + 1):
        graph[i] = []

    for city in cities:
        graph[city[0]].append(city[1])
        graph[city[1]].append(city[0])

    # split graphs into components
    graph_components = set()
    for node in range(1, n + 1):
        graph_elements = dfs(set(), graph, node)
        if graph_elements not in graph_components:
            graph_components.add(frozenset(graph_elements))

    # calculate the cost
    cost_road = 0
    lib_cost = 0
    for i in graph_components:
        cost_road += c_road * (len(i) - 1)
        lib_cost += c_lib

    return cost_road + lib_cost


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(roadsAndLibraries(3, 2, 1, [[1, 2], [3, 1], [2, 3]]), 4)

    def test_b(self):
        self.assertEqual(roadsAndLibraries(5, 6, 1, [[1, 2], [1, 3], [1, 4]]), 15)


if __name__ == '__main__':
    unittest.main()
