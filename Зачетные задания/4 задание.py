import numpy as np
import networkx as nx


def short_path(grid_, first_x, first_y, last_x, last_y):
    new_graph = nx.Graph()
    L, H = grid_.shape
    for i in range(H):
        for j in range(L):
            new_graph.add_node((j, i))
            if j - 1 > 0:
                new_graph.add_weighted_edges_from([((j, i), (j - 1, i), grid_[j - 1, i])])
            if i - 1 > 0:
                new_graph.add_weighted_edges_from([((j, i), (j, i - 1), grid_[j, i - 1])])
            if j + 1 < L and i <= H:
                new_graph.add_weighted_edges_from([((j, i), (j + 1, i), grid_[j + 1, i])])
            if i + 1 < H and j <= L:
                new_graph.add_weighted_edges_from([((j, i), (j, i + 1), grid_[j, i + 1])])

    calculate(new_graph, stX=first_x, stY=first_y, X=last_x, Y=last_y)
    return new_graph


def calculate(g, stX, stY, X, Y):
    diction = {}
    all_ways = []
    A = (X, Y)
    B = []

    starting_node = (stX, stY)

    for i in g.nodes:
        diction[i] = float("inf")

    diction[starting_node] = 0
    len_g = len(list(g.edges))
    exit_ = True

    while exit_:
        exit_ = False
        for i in range(len_g):
            k = list(g.edges)[i][0]
            h = list(g.edges)[i][1]
            if g[k][h]["weight"] + diction[k] < diction[h]:
                diction[h] = g[k][h]["weight"] + diction[k]
                all_ways.append([k, h])
                exit_ = True
    while A != (stX, stY):
        for i in reversed(all_ways):
            if i[1] == A:
                B.append([i[0], i[1]])
                A = i[0]

    B.reverse()
    print(grid_)
    print(f"Минимальная стоимость до точки {X, Y}: {diction[(X, Y)]}")
    print(f"Минимальный путь из {A} в {X, Y}:\n{B}")


if __name__ == '__main__':
    shape = (4, 4)
    first_x = 0
    first_y = 0
    last_x = 3
    last_y = 3
    grid_ = np.random.randint(1, 10, (shape))
    short_path(grid_, first_x, first_y, last_x, last_y)
