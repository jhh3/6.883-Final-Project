# Read in fin data
fin_data_path = "../data/nasdaq.data"
with open(fin_data_path, 'r') as f:
    data = [float(e) for e in f.read().split(',')]

# Convert close prices to 0's and 1's
prev_value = data[0]
data01 = []
for v in data:
    data01.append(str(int(v > prev_value)))
    prev_value = v

# Write to file
fin01_data_path = "../data/sp500close01.data"
with open(fin01_data_path, 'w') as f:
    f.write(','.join(data01))
