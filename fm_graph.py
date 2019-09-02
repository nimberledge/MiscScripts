from graphviz import Digraph

next_key = 0
def get_next_key():
    global next_key
    next_key += 1
    return next_key

def get_children(n, path=[]):
    if n == 0:
        return []
    if path == []:
        return [n]
    children = []
    for k in path:
        children.append(n + k)
    return children

def populate_graph(num_levels):
    graph = Digraph(comment="test")
    n = 1
    children = get_children(n, [n])
    graph.node(n, fontcolor='blue')
    for k in children:
        graph.node(k)
        graph.edge(n, k)
    print (get_children(1, [1]))

def populate_one_level(ns, paths, keys):
    for (n, path) in (ns, paths):
        children = get_children(n, path)
        for k in children:
            graph.node(get_next_key(), k)
            graph.edge(n, k)


def main():
    populate_graph(5)

if __name__ == '__main__':
    main()
