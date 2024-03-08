import pandas as pd 
from sklearn.model_selection import train_test_split
import csv

data_file = r"E:\MDS Notes and Assignments\Master Thesis\Code vulnerabilities dataset\cleaned_data.csv"

df = pd.read_csv(data_file,sep='|',escapechar = '\\')

X = df['code']
y = df['state']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=100)

X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.1, random_state=101)

train_output = r"E:\MDS Notes and Assignments\Master Thesis\Code vulnerabilities dataset\train_data.csv"
train_df = pd.DataFrame({
    'state': y_train,
    'code': X_train
})
train_df.to_csv(train_output, sep = "|", index = False, quoting = csv.QUOTE_NONE)

validate_output = r"E:\MDS Notes and Assignments\Master Thesis\Code vulnerabilities dataset\validate_data.csv"
validate_df = pd.DataFrame({
    'state': y_val,
    'code': X_val
})
validate_df.to_csv(validate_output, sep = "|", index = False, quoting = csv.QUOTE_NONE)

test_output = r"E:\MDS Notes and Assignments\Master Thesis\Code vulnerabilities dataset\test_data.csv"
test_df = pd.DataFrame({
    'state': y_test,
    'code': X_test
})
test_df.to_csv(test_output, sep = "|", index = False, quoting = csv.QUOTE_NONE)

