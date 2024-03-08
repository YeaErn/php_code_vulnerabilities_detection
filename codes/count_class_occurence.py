from __future__ import print_function

from phply import phplex
from phply.phpparse import make_parser
from phply.phpast import *
import phply.phpast as phpast

import pandas as pd
import csv
import ast

# Get class_list and child_nodes from the phpast files
type_list_file = r"E:\MDS Notes and Assignments\Master Thesis\Code vulnerabilities dataset\codes\type_list.py"
class_list = []
all_child_nodes = []
with open(type_list_file, 'r') as file:
    for line in file:
        # class list
        parts = line.split('=')
        if len(parts) > 1:
            class_name = parts[0].strip()
            class_list.append(class_name)
        
        # child nodes
        line = line[line.find('['):line.find(']')+1]
        all_child_nodes.append(ast.literal_eval(line))

# Flatten the list of lists and convert it to a set to remove duplicates
unique_elements = set([element for sublist in all_child_nodes for element in sublist])

# Convert the set to a list
unique_child_nodes = list(unique_elements)

# Define a function to traverse the AST and count occurrences of each class
def count_classes(ast):    
    if isinstance(ast, tuple):
        class_name, attributes = ast
        if class_name in class_list:
            class_counts[class_name] += 1
        for attr_name, attr_value in attributes.items():
            if isinstance(attr_value, tuple):
                count_classes(attr_value)
            elif isinstance(attr_value, list):
                for item in attr_value:
                    count_classes(item)
        
input_file = r"E:\MDS Notes and Assignments\Master Thesis\Code vulnerabilities dataset\cleaned_data.csv"
output_file = r"E:\MDS Notes and Assignments\Master Thesis\Code vulnerabilities dataset\count_class_occurence_data.csv"

df = pd.read_csv(input_file, sep = "|", escapechar = '\\')
output_data = []

parser = make_parser()
lexer = phplex.lexer.clone()

for idx, row in df.iterrows():
    output = parser.parse(row['code'], lexer=lexer)
    resolve_magic_constants(output)
    
    # Initialize counts for each class
    class_counts = {cls: 0 for cls in class_list}

    # Traverse the output and count the occurrences of each class
    for statement in output:
        count_classes(statement.generic())
    
    output_data.append(class_counts)
    
output_df = pd.DataFrame(output_data)

# Add 'no_' prefix to each column header
output_df.rename(columns=lambda x: 'Number_' + x, inplace=True)

output_df['State'] = df['state']

# Second cleaning: to remove columns that are all the same
df_filtered = output_df.loc[:, output_df.nunique() > 1]

# store as csv
df_filtered.to_csv(output_file, sep = ",", index = False, quoting = csv.QUOTE_NONE)