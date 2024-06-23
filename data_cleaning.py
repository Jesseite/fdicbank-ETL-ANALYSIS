import pandas as pd
import os

#Read data
df = pd.read_csv(os.environ.get('csv_raw'), encoding="windows-1252")
print(df.head(5))

#Check data quality information
#print(df.info())
#print(df.isna().sum())
#print(df.describe())

#Add an index column
df.insert(0, 'bank_id', range(302, 302 + len(df)))
#print(df.info)

#Rename the columns
column_rename_dict = {"Bank Name": "bank_name",
                   "City": "city",
                   "State": "state",
                   "Cert": "cert",
                   "Acquiring Institution": "acquired_by",
                   "Closing Date": "closed_date",
                   "Fund": "fund"}

#Remove leading and trailing whitespaces from the column names
df.columns = df.columns.str.strip()

#Rename column names
df.rename(columns=column_rename_dict, inplace=True, errors='raise')

print(df.info)

#Store new CSV
df.to_csv(os.environ.get('csv_transform'), index=False, sep='|')