################################################
#### Onomateponimo: Vasileios Gkotzagiannis ####
#### Arithmos Mitrwou: 2672                 ####
#### Part 1                                 ####
################################################

def create_structure():
  adjascency_list = {}
  with open('cal.cnode.txt', 'r') as n, open('cal.cedge.txt', 'r') as e:
    nodes = []
    for line in n.readlines():
      node = line.strip().split()
      nodes.append(node)

    initialize_adj_list(adjascency_list, len(nodes))

    for line in e.readlines():
      edge = line.strip().split()
      add_edge(adjascency_list, int(edge[1]), int(edge[2]), float(edge[3]))
  
  structure = []
  for i, k in zip(nodes, adjascency_list.items()):
    structure.append([int(i[0]), float(i[1]), float(i[2]), k[1]])
  
  return structure

def initialize_adj_list(adj_list, size):
  for i in range(0, size):
    adj_list[i] = []

def add_edge(adj_list, node0, node1, L2):
  adj_list[node0].append([node1, L2])
  adj_list[node1].append([node0, L2])

def main():
  structure = create_structure()

  # Write the structure in out.txt
  with open('out.txt', 'w') as o:
    for node in structure:
      o.write(f'{" ".join(map(str, node[:-1]))} ')
      
      for edge in node[3]:
        o.write(f'{" ".join(map(str, edge))} ')
      o.write('\n')

    print('Structure created.')

if __name__ == '__main__':
  main()
