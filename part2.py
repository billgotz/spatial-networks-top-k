from part1 import create_structure
import sys
import heapq



def dijkstra(nodes, s, t):
  s = int(s)
  t = int(t)
  # Initialize SPDs and visited nodes
  SPD = [float('inf')] * len(nodes)
  path = []
  distance = 0
  visited = [0] * len(nodes)
  
  # Initialize a priority queue -> p_q
  p_q = []
  heapq.heapify(p_q)
  SPD[int(s)] = 0
  heapq.heappush(p_q, [SPD[int(s)], int(s)])
  print(p_q)

  while p_q:
    v = heapq.heappop(p_q)
    spd = v[0]
    node = v[1]
    # print(p_q)

    visited[node] = 1
    # We reached the target node
    if node == t:
      print('equal')
      path.append(node)
      distance += SPD[node]
      print(distance)
      return path
    
    v_neighbors = nodes[node][1]
    for neighbor in v_neighbors:
      u = int(neighbor[0])
      weight = float(neighbor[1])

      if not visited[u]:
        if SPD[u] > spd + weight:
          SPD[u] = spd + weight
          # print(SPD[u])
          path.append(u)
          distance += SPD[u]
          
          found = 0
          for e in p_q:
            if e[1] == u:
              e[0] = SPD[u]
              heapq.heapify(p_q)
              found = 1
              break
          
          if not found:
            heapq.heappush(p_q, [SPD[u], int(u)])
  return path


def main():
  if len(sys.argv) < 3:
    print(f'You need to provide source, target nodes. \nUsage: python part1.py <source node> <target node>')
    sys.exit(1)
  
  struct = create_structure()
  print(len(struct))
  shortest_path = dijkstra(struct, sys.argv[1], sys.argv[2])
  print(len(shortest_path))
  sum = 0
  for p in shortest_path:
    print(p, end=', ')
main()