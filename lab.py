"""
member1: <Iryna Denysova>
member2: <Ivan Sen>
"""
from typing import List, Dict
import queue
SEARCH_START_POINT = 0

def read_csv(file_name: str) -> Dict[int, List[int]]:
    """
    read graph represented as matrix in .csv file and return it
    as dictionary where each key represents a vertex, while the value
    represent the list of matrices adjacent to the key
    :rtype: dict(key=int, value=list(int))
    :param file_name: string
    :return: graph
    >>> read_csv("graph.csv")
    {0: [2, 5, 7], 1: [2, 6, 7], 2: [0, 1, 4, 5, 6, 7], 3: [6, 7], 4: [2, 5, 7], 5: [0, 2, 4, 7], 6: [1, 2, 3, 7], 7: [0, 1, 2, 3, 4, 5, 6]}
    """
    key = 0
    dict = {}
    num_list = []
    with open(file_name, 'r', encoding='utf-8') as csv_file:
        for line in csv_file:
            line = line.strip().split(',')
            for i, num in enumerate(line):
                if num == '1':
                    num_list.append(i)
            dict[key] = num_list
            key+=1
            num_list=[]
    return dict


def bfs(graph: Dict[int, List[int]], start_point: int = SEARCH_START_POINT) -> List[int]:
    """
    perform bfs on the graph and store its result
    in the list of vertices(integers that represent vertices)
    :rtype: list(int)
    :param graph: dict(key=int, value=list(int))
    :return: bfs-result
    >>> bfs({0: [2, 5, 7], 1: [2, 6, 7], 2: [0, 1, 4, 5, 6, 7], 3: [6, 7], 4: [2, 5, 7], 5: [0, 2, 4, 7], 6: [1, 2, 3, 7], 7: [0, 1, 2, 3, 4, 5, 6]})
    [0, 2, 5, 7, 1, 4, 6, 3]
    """
    result = []
    q = queue.Queue()
    q.put(SEARCH_START_POINT)
    visited = set()
    while not q.empty():
        vertice = q.get()
        visited.add(vertice)
        result.append(vertice)
        for neighbour in graph[vertice]:
            if neighbour not in visited:
                q.put(neighbour)
                visited.add(neighbour)
    return result


def dfs(graph: Dict[int, List[int]], result:List[int] = [], start_point:int = SEARCH_START_POINT, visited:set = set()) -> List[int]:
    """
    perform dfs on the graph and store its result
    in the list of vertices(integers that represent vertices)
    :rtype: list(int)
    :param graph:  dict(key=int, value=list(int))
    :return: dfs-result
    >>> dfs({0: [2, 5, 7], 1: [2, 6, 7], 2: [0, 1, 4, 5, 6, 7], 3: [6, 7], 4: [2, 5, 7], 5: [0, 2, 4, 7], 6: [1, 2, 3, 7], 7: [0, 1, 2, 3, 4, 5, 6]})
    [0, 2, 1, 6, 3, 7, 4, 5]
    """
    result.append(start_point)
    visited.add(start_point)
    for neighbour in graph[start_point]:
        if neighbour not in visited:
            visited.add(neighbour)
            dfs(graph, result, neighbour, visited)
    return result



def calc_pow(graph: Dict[int, List[int]]) -> Dict[int, int]:
    """
    calculate power of every vertex of your graph(i.e. number adjacent edges)
    :rtype: dict(key=int, value=int)
    :param graph: dict(key=int, value=list(int))
    :return: vertices and their powers
    >>> calc_pow({1:[2,3], 2:[1, 3], 3: [], 4: [1]})
    {1: 2, 2: 2, 3: 0, 4: 1}
    """
    dict = {}
    for key in graph:
        length = len(graph[key])
        dict[key] = length
    return dict


def find_path(n: int, edges: List[List[int]], source: int, destination: int) -> bool:
    """
    here is another way of representing a graph:
    edges - is a list of edges of a graph,
    where each edge is also a list of two integers,
    which represent 2 adjacent vertices
    find if there is a way from the source vertex to the destination one
    :rtype: bool
    :param n: int
    :param edges: list(list(int))
    :param source: int
    :param destination: int
    :return:
    >>> find_path(9, [[1, 2], [3, 4], [5, 6], [7, 8], [2, 4], [3, 5], [4, 5]], 1, 5)
    True
    >>> find_path(9, [[1, 2], [3, 4], [5, 6], [7, 8], [2, 2], [3, 5], [4, 5]], 1, 5)
    False
    """
    # Your code goes here(delete "pass" keyword)
    pass



if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
