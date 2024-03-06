from __future__ import print_function

from phply import phplex
from phply.phpparse import make_parser
from phply.phpast import *

import pprint
import pandas as pd

input_file = "E:\MDS Notes and Assignments\Master Thesis\Code vulnerabilities dataset\cleaned_data.csv";
output_file = "E:\MDS Notes and Assignments\Master Thesis\Code vulnerabilities dataset\parsed_data.csv";

df = pd.read_csv(input_file, sep = "|", escapechar = '\\')
output_data = []

parser = make_parser()
lexer = phplex.lexer.clone()

for idx, row in df.iterrows():
    output = parser.parse(row['code'], lexer=lexer)
    resolve_magic_constants(output)
    output_data.append(output)
    
output_df = pd.DataFrame({
    'state': df['state'],
    'parsed_code': output_data
})

# store as csv
output_df.to_csv(output_file, sep = "|", index = False)