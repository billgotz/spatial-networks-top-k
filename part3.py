from part1 import create_structure
from part2 import dijkstra
import sys




def main():

    if len(sys.argv) < 3:
        print('You need to give at least two nodes to find the optimal meeting point. \nUsage python part3.py <node1> <node2> ... <nodeN>')

    nodes = []
    for node in range(1, len(sys.argv)):
        try:
            nodes.append(int(sys.argv[node]))
        except ValueError:
            print(f'[Warning] Nodes must be integers. Value {sys.argv[node]} ignored.')

    print(nodes)
    struct = create_structure()

    marked = [[0] * len(nodes)] * len(struct)
    
    for n in nodes:
        marked[n][nodes.index(n)] += 1
    
    print(marked[432][1])

if __name__ == '__main__':
    main()