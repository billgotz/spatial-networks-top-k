################################################
#### Onomateponimo: Vasileios Gkotzagiannis ####
#### Arithmos Mitrwou: 2672                 ####
#### Part 1                                 ####
################################################

################ IMPORTS ####################
from part1 import create_structure
from part2 import dijkstra
from heapq import heapify, heappop, heappush
from time import time
import sys
#############################################

def find_omp(struct, nodes):
  marked = [[None] * len(nodes) for _ in range(0, len(struct))]

  # Create generators for the next nearest neighbor 
  # returned from the dijkstra_next_nearest
  gens = []
  for d in nodes:
      gens.append(dijkstra_next_nearest(struct, d))

  max_g = float('inf')
  max_node = None
  min_g = 0
  max_dists = [0] * len(nodes)

  while min_g < max_g:
    for n in range(0, len(nodes)):
      # Get the next nearest from the generator 
      spd, node = next(gens[n])
      marked[node][n] = (spd, node)

      # If the node has been visited from all the initial nodes
      # take the max of the nodes and compare it with the current max
      # and update accordingly
      if None not in marked[node]:
        max_from_nodes = max(marked[node])

        if max_from_nodes[0] < max_g:
          max_g = max_from_nodes[0]
          max_node = max_from_nodes[1]

      # save the current max distances for the initial nodes
      max_dists[n] = spd
    # keep the minimum max distance of the initial nodes (max_dists)
    # in order to compare it with the max_g
    min_g = min(max_dists)

  # We found the optimal meeting point
  else:
    print(f'Optimal meeting point: {max_node}')
    print(f'Max shortest path distance: {max_g}')

  print('-------------- [Paths] -------------- ')
  for n in nodes:
    spd, path, _ = dijkstra(struct, n, max_node)
    print(f'{n} to {max_node}: {[spd, path]}')
  print('------------------------------------- ')

def dijkstra_next_nearest(nodes, s):
  # Initialize SPDs and visited nodes
  spds = [float('inf')] * len(nodes)
  visited = [0] * len(nodes)
  
  # Initialize a priority queue -> p_q
  p_q = []
  heapify(p_q)
  # Add s to pq
  spds[s] = 0
  heappush(p_q, [spds[s], s])

  while p_q:
    spd, node = heappop(p_q)
    visited[node] = 1

    # return the next nearest everytime
    yield [spd, node]

    v_neighbors = nodes[node][3]
    for neighbor in v_neighbors:
      u, weight = neighbor

      if not visited[u]:
        if spds[u] > (spd + weight):
          spds[u] = (spd + weight)

          found = 0
          for e in p_q:
            if e[1] == u:
              e[0] = spds[u]
              heapify(p_q)
              found = 1
              break

          if not found:
            heappush(p_q, [spds[u], u])

def main():
  if len(sys.argv) < 3:
    print('You need to give at least two nodes to find the optimal meeting point. \nUsage python part3.py <node1> <node2> ... <nodeN>')

  nodes = []
  for node in range(1, len(sys.argv)):
    try:
        nodes.append(int(sys.argv[node]))
    except ValueError:
        print(f'[Warning] Node IDs must be integers. Value {sys.argv[node]} ignored.')

  struct = create_structure()
  find_omp(struct, nodes)    


if __name__ == '__main__':
  start = time()
  main()
  end = time()
  print(f'Total time: {end - start}')