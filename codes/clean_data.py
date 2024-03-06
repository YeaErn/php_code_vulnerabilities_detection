import os
import csv

# define output csv file
output_csv = "E:\MDS Notes and Assignments\Master Thesis\Code vulnerabilities dataset\cleaned_data.csv"
csv_header = ['state','code']
csv_data = []

# loop through each folder to open the sample.php file
base_dir = "E:\MDS Notes and Assignments\Master Thesis\Code vulnerabilities dataset\sampled"
for sub_folder in os.listdir(base_dir):
    inFile = base_dir + '\\' + sub_folder + '\src\sample.php'
    tmp_data = []
    concatenated_string = ''
    phpStartTagFound = False
    print(sub_folder)
    with open(inFile, "r", encoding="utf8") as f:
        lines = f.readlines()
            
        for line in lines:
        
            # get state of the sample
            if line.startswith('- State: '):
                state = line[9:]
                state = state.replace('\n','')
                tmp_data.append(state)

            # identify <? to keep only the php codes
            if line.startswith('<?'):
                phpStartTagFound = True
                
            if phpStartTagFound:
                # remove comments
                if line.startswith('#'):
                    continue

                # concatenate code lines
                line = line.replace('\n','')
                concatenated_string += line
                
        tmp_data.append(concatenated_string)

    csv_data.append(tmp_data)

# store as csv
with open(output_csv, "w", encoding='UTF8', newline='') as f:
    writer = csv.writer(f, quoting=csv.QUOTE_NONE, escapechar='\\', delimiter="|")
    writer.writerow(csv_header)
    writer.writerows(csv_data)