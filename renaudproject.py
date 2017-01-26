import pandas as pd
import numpy as np

#Import data to be analyzed
database = pd.read_excel('Initial_Database.xlsx')

#Import mapping master list
mapping = pd.read_excel('Mapping_color.xlsx')

# Pull Color column from database

dbcolor = database['COLOR']

mapcolor = mapping['COLOR']

# Extract unique values that are not in Mapping database
# ~ means negation of isin function that finds whether values are in another Series
uniquevalues = dbcolor[~dbcolor.isin(mapcolor)]
print(uniquevalues)
# Create a new Dataframe
# This is needed so that when we append, the data is the same shape
newdf = pd.DataFrame(uniquevalues, columns=['COLOR','Number'])

# Need to fill in the NaN values with something so that when we pivot we have values.
newdf.fillna(value=9999, inplace=True)

# Append new value Dataframe to existing mapping
mapping = mapping.append(newdf)

# Merge database and mapping
# On and how are i

merged = database.merge(mapping, how='left', on='COLOR')

# Run a pivot table
pivot = pd.pivot_table(merged, index=['Name'], aggfunc=[np.sum])
