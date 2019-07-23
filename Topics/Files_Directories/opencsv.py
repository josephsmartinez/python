import csv

with open("/Users/josephmartinez/Git/UNIX_Linux/Topics/TestDataFiles/CSV/Traffic/Traffic_Violations.csv", 'rt') as csv_file:
    reader = csv.reader(csv_file)
    race_count={"white":0,"black":0,"hispanic":0}
    index_set=False
    for row in reader:
      if not index_set:
        index=list(row).index('Race')
        index_set=True
      if "WHITE" in row[index]:
          race_count["white"] += 1
      elif "BLACK" in row[index]:
          race_count["black"] += 1
      elif "HISPANIC" in row[index]:
          race_count["hispanic"] += 1
print(race_count)
