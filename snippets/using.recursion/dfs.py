"""This is module for dfs."""

def dfs(visited, G, n):
    """
    depth first search algorithm, which returns a list.

    :param visited ( list ) : a list of visited nodes
    :param G       ( dict ) : a dictionary of nodes, each with its list of adjacents
    :param n       ( str  ) : a particular node
    """
    if n not in visited:
        visited.add(n)
        for adj in G[n]:
            dfs(visited, G, adj)

