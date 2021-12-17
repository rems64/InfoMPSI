import random
import matplotlib.pyplot as plt
import numpy as np
import math

def generateGraph(n):
    vertices = [k for k in range(0, n)]
    edges = []

    xs = []
    ys = []

    for vertex in vertices:
        for target in vertices:
            if vertex==target:continue
            edges.append([vertex, target, 0])
        xs.append(random.random())
        ys.append(random.random())

    for i in range(0, len(edges)):
        a = xs[edges[i][1]]-xs[edges[i][0]]
        b = ys[edges[i][1]]-ys[edges[i][0]]
        edges[i][2] = 1-math.sqrt(a**2+b**2)/1.41

    return xs, ys, vertices, edges

def drawGraph(vertices, edges, xs, ys):
    fig, ax = plt.subplots(figsize=(3, 3))

    for edge in edges:
        ab_pairs = np.c_[[xs[edge[0]], xs[edge[1]]], [ys[edge[0]], ys[edge[1]]]]
        ab_args = ab_pairs.reshape(-1, 2, 2).swapaxes(1, 2).reshape(-1, 2)

        # Couleur de l'arrête
        lambd = edge[2]
        ax.plot(*ab_args, c=(lambd, 0.0, 1-lambd, lambd))

    # Sommets avec indices
    plt.plot(xs,ys, 'go', alpha = 0.9)
    for i in range(0, len(xs)):
        ax.text(xs[i], ys[i], str(i))

    plt.show()


xs, ys, vert, edg = generateGraph(12)
drawGraph(vert, edg, xs, ys)
