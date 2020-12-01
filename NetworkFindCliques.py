import community as community_louvain
import networkx as nx
import pandas as pd
import matplotlib.cm as cm
import matplotlib.pyplot as plt


# read the network
pathToNetwork=""
edgelist=pd.read_csv(pathToNetwork,sep="\t")
edgelist.columns=['Source','Target']

# Use igraph to construct a graph from an edgelist
graphG=nx.from_pandas_edgelist(edgelist, source='Source', target='Target', create_using=None)

partition = community_louvain.best_partition(graphG)
modularity1 = community_louvain.modularity(partition,graphG, weight='weight')

pos = nx.spring_layout(graphG)
# color the nodes according to their partition
cmap = cm.get_cmap('viridis', max(partition.values()) + 1)
nx.draw_networkx_nodes(graphG, pos, partition.keys(), node_size=40,
                       cmap=cmap, node_color=list(partition.values()))
nx.draw_networkx_edges(graphG, pos, alpha=0.5)
plt.show()
