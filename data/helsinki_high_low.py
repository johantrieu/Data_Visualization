import csv

import matplotlib.pyplot as plt 

filename = 'data/helsinki.csv'
with open(filename) as f:
    reader = csv.reader(f, delimiter=";")
    header_row = next(reader)
    
    #for index, column_header in enumerate(header_row):
        #print(index, column_header)

    #Get temperatures from this file.
    years, temps = [], []
    for row in reader:
        year = int(row[0])
        temp = float(row[1])
        years.append(year)
        temps.append(temp)

#print(temps)

# Plot the temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(years, temps, c='red')

# Format plot.
plt.title("Temperature statistics from 1961 to 2020 in Helsinki", fontsize=24)
plt.xlabel('', fontsize=16)
plt.ylabel("Temperature (C)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()