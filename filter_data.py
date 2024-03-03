import json

file_name = "E:\MDS Notes and Assignments\Master Thesis\Code vulnerabilities dataset\sarifs.json"

# read the data
with open(file_name, "r") as fr:
    data = json.load(fr)
    
test_cases = data['testCases']

# Get Identifier
# print(test_cases[0]['identifier'])

# Get description
# print(test_cases[0]['sarif']['runs'][0]['properties']['description'])

# Get state
# print(test_cases[0]['sarif']['runs'][0]['properties']['state'])

xss_count, sql_count = 0, 0
good_count, bad_count = 0, 0
sql_identifiers = []
for i,v in enumerate(test_cases):

    if("Context: sql_" in test_cases[i]['sarif']['runs'][0]['properties']['description']):
        sql_count += 1
    
        sql_identifiers.append(test_cases[i]['identifier'])
        
        if (test_cases[i]['sarif']['runs'][0]['properties']['state'] == 'good'):
            good_count += 1
        else:
            bad_count += 1
            
    else:
        xss_count += 1
            
print("xss count:" + str(xss_count))
print("sql count:" + str(sql_count))
print("good count:" + str(good_count))
print("bad count:" + str(bad_count))

sql_data_compressed = "E:\MDS Notes and Assignments\Master Thesis\Code vulnerabilities dataset\sql_data_compressed.txt"
# write the data back to file
with open(sql_data_compressed, "w") as fw:
    fw.write(','.join(sql_identifiers))


sql_data_split = "E:\MDS Notes and Assignments\Master Thesis\Code vulnerabilities dataset\sql_data_split.txt"
# write the data back to file
with open(sql_data_split, "w") as fw:
    fw.write('\n'.join(sql_identifiers))
   



