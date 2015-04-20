import csv
import statistics as s
import matplotlib.pyplot as plt

plt.plot(range(1088), [float(results[i][0]) - float(truth[i][0]) for i in range(1088)])
results = [row for row in csv.reader(open('results.csv', 'r'))]
truth = [row for row in csv.reader(open('groundTruth.csv', 'r'))]
plt.xlabel('Time')
plt.ylabel('Error')
plt.show()
