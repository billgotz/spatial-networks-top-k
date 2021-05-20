from part1 import create_structure
import sys
from heapq import heapify, heappop, heappush
import math

def dijkstra(nodes, s, t):

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

  path[t].append(s)

  while p_q:
    spd, node = heappop(p_q)
    visited[node] = 1
    visited_counter += 1
    # We reached the target node
    if node == t:
      return [spds[t], path[t], visited_counter]
    
    v_neighbors = nodes[node][3]
    for neighbor in v_neighbors:
      u = neighbor[0]
      weight = neighbor[1]
      
      if not visited[u]:
        if spds[u] > (spd + weight):
          spds[u] = (spd + weight)

          path[u] = path[node].copy()
          path[u].append(u)

          found = 0
          for e in p_q:
            if u == '55':
              print(e)
            if e[1] == u:
              e[0] = spds[u]
              heapify(p_q)
              found = 1
              break
          
          # try:
          #   p_q.index(u)
          
          if not found:
            heappush(p_q, [spds[u], u])
          
def a_star(nodes, s, t):

  # Initialize SPDs and visited nodes
  spds = [float('inf')] * len(nodes)
  lbounds = [float('inf')] * len(nodes)
  path = [[]] * len(nodes)
  visited = [0] * len(nodes)
  visited_counter = 0
  
  # Initialize a priority queue -> p_q
  p_q = []
  heapify(p_q)
  # Add s to pq
  spds[s] = 0
  lbounds[s] = dist([nodes[s][1], nodes[s][2]], [nodes[t][1], nodes[t][2]]) + spds[s]
  heappush(p_q, [lbounds[s], spds[s], s])
  # Add s to path

  path[t].append(s)

  while p_q:
    l_bound, spd, node = heappop(p_q)
    visited[node] = 1
    visited_counter += 1
    # We reached the target node
    if node == t:
      return [spds[t], path[t], visited_counter]
    
    v_neighbors = nodes[node][3]
    for neighbor in v_neighbors:
      u = neighbor[0]
      weight = neighbor[1]
      
      if not visited[u]:
        if spds[u] > (spd + weight):
          spds[u] = (spd + weight)
          lbounds[u] = dist([nodes[u][1], nodes[u][2]], [nodes[t][1], nodes[t][2]]) + spds[u]

          path[u] = path[node].copy()
          path[u].append(u)

          found = 0
          for e in p_q:

            if e[2] == u:

              e[0] = lbounds[u]
              e[1] = spds[u]
              heapify(p_q)
              found = 1
              break
          
          if not found:
            heappush(p_q, [lbounds[u], spds[u], u])

def dist(node1, node2):
    """
    TODO
    """
    dx = 0
    dy = 0

    x1, y1 = node1
    x2, y2 = node2

    if x1 < x2: 
        dx = x2 - x1
    if x1 > x2: 
        dx = x1 - x2

    if y1 < y2: 
        dy = y2 - y1
    if y1 > y2: 
        dy = y1 - y2

    return math.sqrt(dx**2 + dy**2)

def main():
  if len(sys.argv) < 3:
    print(f'You need to provide source, target nodes. \nUsage: python part1.py <source node> <target node>')
    sys.exit(1)
  
  s = int(sys.argv[1])
  t = int(sys.argv[2])

  struct = create_structure()
  # print(struct[0])
  spd, path, visited_counter = dijkstra(struct, s, t)

  print('-------- Dijkstra shortest path computation --------')
  # print(f'Shortest path is: {path}')
  print(f'Dijkstra no. of iterations: {visited_counter}')
  print(f'Dijkstra shortest path distance: {spd}')
  print(f'Shortest path: {path}')
  print('-------- End of Dijkstra --------')

  with open('out/dijkstra_{t}.txt', 'w') as p:
    p.write(f'{path}')
    


  spd_a, path_a, visited_counter_a = a_star(struct, s, t)

  print('-------- Astar shortest path computation --------')
  print(f'Dijkstra no. of iterations: {visited_counter_a}')
  print(f'Dijkstra shortest path distance: {spd_a}')
  print(f'Shortest path is: {path_a}')
  print('-------- End of Astar --------')

  with open('out/astar_{t}.txt', 'w') as a:
    a.write(f'{path_a}')


if __name__ == "__main__":
  main()
