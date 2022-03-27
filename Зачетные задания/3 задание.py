import networkx as nx

def svyazi(counter, graph):
    i = 0
    while len(new_list) < len_graph:
        start_node = list(graph.nodes)[i]
        if start_node not in new_list:
            solution(start_node, new_list, graph)
            counter += 1
        else:
            i += 1
    print(f" Число компонент связности: {counter}")


def solution(start_node, new_list, graph):
    g = graph
    list_ = list(g.neighbors(start_node))
    if len(list_) == 0:
        new_list.append(start_node)
    else:
        while list_:
            if len(list_) > 0:
                if list_[0] not in new_list:
                    new_list.append(list_[0])
                    list_ += list(g.neighbors(list_[0]))
                list_.remove(list_[0])


if __name__ == '__main__':
    counter = 0
    new_list = []
    graph = nx.Graph()
    graph.add_nodes_from("ABCDEFGHIJ")
    graph.add_edges_from([
        ('B', 'G'),
        ('F', 'G'),
        ('G', 'C'),
        ('G', 'H'),
        ('G', 'I'),
        ('C', 'H'),
        ('I', 'H'),
        ('H', 'J'),
        ('E', 'D'),
    ])
    len_graph = graph.number_of_nodes()
    svyazi(counter, graph)