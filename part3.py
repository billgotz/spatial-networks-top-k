from typing import Type
from part1 import create_structure
from part2 import dijkstra as dj
import sys
from heapq import heapify, heappop, heappush
from time import time


def main():

    if len(sys.argv) < 3:
        print('You need to give at least two nodes to find the optimal meeting point. \nUsage python part3.py <node1> <node2> ... <nodeN>')

    nodes = []
    for node in range(1, len(sys.argv)):
        try:
            nodes.append(int(sys.argv[node]))
        except ValueError:
            print(f'[Warning] Node IDs must be integers. Value {sys.argv[node]} ignored.')

    # print(nodes)
    struct = create_structure()

    marked = [[None] * len(nodes) for _ in range(0, len(struct))]

    gens = []
    for d in nodes:
        gens.append(dijkstra(struct, d))

    max_g = float('inf')
    max_node = None
    min_g = 0
    max_dists = [0] * len(nodes)

    while min_g < max_g:
        for n in range(0, len(nodes)):
            spd, node = next(gens[n])
            marked[node][n] = (spd, node)

            if None not in marked[node]:
                maxdas = max(marked[node])

                if maxdas[0] < max_g:
                    max_g = maxdas[0]
                    max_node = maxdas[1]

            # print(f'marked[{node}][{n}] --> {marked[node][n]}')
            # print(f'marked[{node}] --> {marked[node]}')
            max_dists[n] = spd
        # print(max_dists)
        min_g = min(max_dists)

    else:
        print(f'Optimal meeting point: {max_node}')
        print(f'Shortest path distance: {max_g}')

    print('Paths: ')
    for n in nodes:
        spd, path, _ = dj(struct, n, max_node)
        print(f'To {n}: {[spd, path]}')


def dijkstra(nodes, s):

  # Initialize SPDs and visited nodes
  spds = [float('inf')] * len(nodes)
  path = [[]] * len(nodes)
  visited = [0] * len(nodes)
  visited_counter = 0
  
  # Initialize a priority queue -> p_q
  p_q = []
  heapify(p_q)
  # Add s to pq
  spds[s] = 0
  heappush(p_q, [spds[s], s])
  # Add s to path

#   path[t].append(s)

  while p_q:
    spd, node = heappop(p_q)
    visited[node] = 1
    visited_counter += 1
    
    yield [spd, node]

    v_neighbors = nodes[node][3]
    for neighbor in v_neighbors:
      u, weight = neighbor

      if not visited[u]:
        if spds[u] > (spd + weight):
          spds[u] = (spd + weight)

          path[u] = path[node].copy()
          path[u].append(u)

          found = 0
          for e in p_q:
            if e[1] == u:
              e[0] = spds[u]
              heapify(p_q)
              found = 1
              break

          if not found:
            heappush(p_q, [spds[u], u])


if __name__ == '__main__':
    start = time()
    main()
    end = time()
    print(f'total time: {end - start}')