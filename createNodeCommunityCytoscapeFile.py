# file to import community files and create one file for Cytoscape
# text file contains Node and Community

# import libraries
import os
import pandas as pd
# Set the directory of the files
pathToCommunities=""
os.chdir(pathToCommunities)

# list the files in the directory
filesCommunity=os.listdir()

indexCom=0
# Create the data frame by reading all the files and storing them
for x in filesCommunity:
    Community_tmp=pd.read_csv(x,sep=",")
    Community_tmp=Community_tmp.assign(Community=indexCom)
    if indexCom==0:
        NodeCommunity=Community_tmp
        indexCom=indexCom+1
    else:
        NodeCommunity=pd.concat([NodeCommunity,Community_tmp])
        indexCom=indexCom+1
