adjascency_list = {}
def initialize_adj_list(size):
  for i in range(0, size):
    adjascency_list[i] = []


def add_edge(node0, node1, L2):
  adjascency_list[node0].append([node1, L2])
  adjascency_list[node1].append([node0, L2])

def create_structure():
  with open('node.txt', 'r') as n, open('edge.txt', 'r') as e:

    nodes = []
    for line in n.readlines():
      node = line.strip().split()
      nodes.append(node)
    
    print(nodes[0])
    print(len(nodes))
    initialize_adj_list(len(nodes))

    for line in e.readlines():
      edge = line.strip().split()
      add_edge(int(edge[1]), int(edge[2]), float(edge[3]))

  
  struct = []
  for i, k in zip(nodes, adjascency_list.items()):
    struct.append([i, k[1]])

  print(adjascency_list[0])
  print(adjascency_list[1])
  print(adjascency_list[21047])

  with open('out.txt', 'w') as o:
    for i, node in enumerate(nodes):
      st = ''
      for key, value in adjascency_list[i]:
        st += f'{key} {value} '
      o.write(f'{node} {st}\n')
  
  return struct

if __name__ == '__main__':
  struct = create_structure()
  print(struct[0])