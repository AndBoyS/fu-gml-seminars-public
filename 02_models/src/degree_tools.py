import pandas as pd
import networkx as nx


def get_count(G: nx.Graph) -> pd.Series:
    counter = pd.Series(list((dict(G.degree()).values()))).value_counts()
    return counter.sort_index()

def get_empirical_cdf(G: nx.Graph) -> pd.Series:
    counter = get_count(G)
    counter /= counter.sum()
    counter = counter.cumsum()
    return counter
