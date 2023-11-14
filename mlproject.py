from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import csv
from datetime import datetime

timevalues = []
receiptcount = []



data = pd.read_csv(r"C:\Users\Ryan\Desktop\Machine Learning project\fetchdata5.csv")

# First, I'll begin by making a simple line graph of all of the data points we have been given. As can be seen, this appears to be a linear relationship relative to the passage of time.

#plt.scatter(data['# Date'],data['Receipt_Count'])
#plt.ylabel('Receipt Counts')
#plt.xlabel('Date')
#plt.margins(0.05)
plt.xticks(np.arange(0, 365, 80))

#plt.show()

# Given the above interactions, my initial though process was that this was best solved using linear regression. In simple terms, I'm trying to find the ideal slope of a line that agreegates the variability
# day to day. My goal for this is to find a slot and an intercept point that we can use to calculate everything.

date_ordinals = []
receipt_totals = []

with open(r"C:\Users\Ryan\Desktop\Machine Learning project\fetchdata5.csv", newline='') as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        # Assuming the date is in the "Date" column
        receipt_str = row['Receipt_Count']
        receipt_totals.append(int(receipt_str))
        date_str = row["# Date"]
        # Convert the date string to a datetime object
        date_obj = datetime.strptime(date_str, "%m/%d/%Y")
        # Get the ordinal value and append to the list
        date_ordinal = date_obj.toordinal()
        date_ordinals.append(date_ordinal)



datebias = date_ordinals[0]
newdates = []
for date in date_ordinals:
    newdates.append(date - datebias)

X = np.array(newdates)
Y = np.array(receipt_totals)

# Numpy has a built in linear regression Model.

slope, intercept = np.polyfit(X, Y, 1)


# This below function will now create a line visualization that we can use to predit the future growth of receipt totals under the assumption that a linear model creates the best positive outcome.

predicted_values = slope * np.array(newdates) + intercept

# Plot the scatter plot and regression line
plt.scatter(data['# Date'], receipt_totals, label='Data Points')
plt.plot(newdates, predicted_values, color='red', label='Regression Line')
plt.xlabel('Dates')
plt.ylabel('Receipt Totals')
plt.title('Scatter Plot with Regression Line')
plt.legend()
plt.show()
