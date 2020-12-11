# file to import community files and create one file for Cytoscape
# text file contains Node and Community

# import libraries
import os
import re
import pandas as pd
# Set the directory of the files
pathToCommunities=""
os.chdir(pathToCommunities)

# function to sort the files in the directory based on their order numeric order
def sorted_alphanumeric(data):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(data, key=alphanum_key)
# list the files in the directory
filesCommunity=os.listdir()
filesCommunity=sorted_alphanumeric(filesCommunity)
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
