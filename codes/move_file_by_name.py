import shutil
import os.path

file_name = "E:\MDS Notes and Assignments\Master Thesis\Code vulnerabilities dataset\sql_data_split.txt"

# read the data
file = open(file_name, "r")
lines = file.readlines()

file_not_found = []
# move file by name
for line in lines:
    line = line.replace("\n", "")
    
    old_path = "E:/MDS Notes and Assignments/Master Thesis/Code vulnerabilities dataset/2022-05-12-php-test-suite-sqli-v1-0-0/" + line
    if os.path.isdir(old_path) == False:
        file_not_found.append(line)
        continue
    new_path = "E:/MDS Notes and Assignments/Master Thesis/Code vulnerabilities dataset/sql-only dataset/" + line
    
    shutil.move(old_path, new_path)
    
    
sql_file_not_found = "E:\MDS Notes and Assignments\Master Thesis\Code vulnerabilities dataset\sql_file_not_found.txt"
with open(sql_file_not_found, "w") as fw:
    fw.write("\n".join(file_not_found))
