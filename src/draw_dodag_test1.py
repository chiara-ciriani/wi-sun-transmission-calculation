from graph import create_graph, draw_dodag

if __name__ == "__main__":

    # The weights that represent the quality of the link
    edges = [
        (11, 9, 1),
        (11, 10, 1),
        (9, 6, 1),
        (9, 7, 1),
        (10, 8, 1),
        (6, 1, 1),
        (6, 2, 1),
        (7, 3, 1),
        (8, 4, 1),
        (8, 5, 1)
    ]

    graph = create_graph(edges, 11)
    draw_dodag(graph, root=11)
