from graphviz import Digraph

class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

pre_ind = 0
def get_tree(pre, inord, instart, inend):
    global pre_ind

    if instart > inend:
        return None
    root = pre[pre_ind]
    pre_ind += 1
    if instart == inend:
        return Node(root)

    in_ind = inord.find(root)

    return Node(root, left=get_tree(pre, inord, instart, in_ind-1), right=get_tree(pre, inord, in_ind + 1, inend))

def print_tree(root):
    if root is None:
        return
    print_tree(root.left)
    # print ('\t\t\t')
    print(root.data)
    print_tree(root.right)
    # print ('\n')
    print (root.data)

def post_order(root):
    if root is None:
        return
    post_order(root.left)
    post_order(root.right)
    print (root.data, end=' ')

def render_graphviz(root, parent=None, graph=None):
    if root is None:
        return graph
    if graph is None:
        graph = Digraph(comment="Tree")

    graph.node(root.data, fontcolor='blue')
    if parent is not None:
        graph.edge(parent, root.data)
    graph = render_graphviz(root.left, parent=root.data, graph=graph)
    graph = render_graphviz(root.right, parent=root.data, graph=graph)
    return graph


def main():
    global pre_ind
    pre = 'UXMZIWJEOVNHRDTKGLYAFSQPCB'
    inord = 'ZMXEJVOWINDRTHUGKFAQPSYCBL'
    pre_ind = 0
    t = get_tree(pre, inord, 0, len(pre)-1)
    post_order(t)
    print()
    g = render_graphviz(t)
    g.render('What', view=True)

if __name__ == '__main__':
    main()
