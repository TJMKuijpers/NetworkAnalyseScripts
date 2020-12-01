# Load the library igraph
library(igraph)

# Set the working directory to the graphml file
setwd("E:/Phd Thesis/Chapter 4 subsection EGM/EGM/analyse paper/Genomic interaction network/")
# Read the graphml file
graphFile=""
graph=read_graph(graphFile,format="graphml")

# Transfrom the graph to an edgelist to export as text file
compg.edges <- as.data.frame(get.edgelist(graph))
fileName=""
write.table(compg.edges,file=fileName+"txt",sep="\t")
