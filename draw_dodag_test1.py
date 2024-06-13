from graph import create_graph, draw_dodag

if __name__ == "__main__":

    # The weights that represent the quality of the link
    edges = [
        (1, 2, 1),
        (1, 3, 1),
        (1, 4, 1),
        (1, 5, 1),
        (2, 6, 1),
        (3, 7, 1),
        (4, 8, 1),
        (5, 9, 1),
        (6, 10, 1),
        (7, 11, 1),
        (8, 12, 1),
        (9, 13, 1),
    ]

    graph = create_graph(edges, 13)
    draw_dodag(graph, root=1)
