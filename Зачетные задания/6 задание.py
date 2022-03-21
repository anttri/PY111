import networkx as nw


def rocket_rental(order_list):
    schedule = nw.MultiDiGraph()
    schedule.add_nodes_from(range(0, 23))

    for time in order_list:
        for i in range(time[0], time[1]):
            schedule.add_edge(i, i + 1)

    if any(n[1] > 1 for n in schedule.out_degree):
        print('Не хватит одной ракеты')
    else:
        print('Хватит одной ракеты')


if __name__ == '__main__':
    order_list = [(3, 5), (6, 7), (8, 15), (13, 16)]
    rocket_rental(order_list)
